from __future__ import annotations

import logging
from typing import Any

from src.binance_client import BinanceSpotClient
from src.config import BotConfig
from src.gemini_agent import AIAnalysisResult, GeminiTradingAgent
from src.market_scanner import MarketScanner, TechnicalSnapshot
from src.state_manager import BotState, PositionState, StateManager, utc_now_iso, utc_today_str

logger = logging.getLogger(__name__)


class AutonomousTradingBot:
    """Motor principal que coordina Binance Spot, Gestion de Riesgo Estricta y Gemini AI."""

    def __init__(
        self,
        config: BotConfig,
        binance_client: BinanceSpotClient | None = None,
        scanner: MarketScanner | None = None,
        ai_agent: GeminiTradingAgent | None = None,
        state_manager: StateManager | None = None,
    ) -> None:
        self.config = config
        self.client = binance_client or BinanceSpotClient(
            api_key=config.binance_api_key,
            api_secret=config.binance_api_secret,
            proxy_url=config.binance_proxy_url,
        )
        self.scanner = scanner or MarketScanner(
            client=self.client,
            quote_asset=config.quote_asset,
            min_24h_volume_usdt=config.min_24h_volume_usdt,
            top_limit=config.top_candidates_limit,
            primary_interval=config.kline_interval_primary,
            htf_interval=config.kline_interval_htf,
        )
        self.ai_agent = ai_agent or GeminiTradingAgent(
            api_key=config.gemini_api_key,
            model=config.gemini_model,
        )
        self.state_manager = state_manager or StateManager(
            state_file=config.state_file,
            history_file=config.history_file,
            report_file=config.report_file,
        )

    def run_cycle(self) -> dict[str, Any]:
        """Ejecuta un ciclo completo de auditoria de riesgo, escaneo, IA y trading."""
        self.config.validate()
        state = self.state_manager.load_state()
        state.total_cycles += 1

        logger.info("=== Iniciando Ciclo #%d (Modo: %s) ===", state.total_cycles, "DRY_RUN" if self.config.dry_run else "LIVE REAL")

        # 1. Obtener precios globales y saldos reales de Binance
        all_prices = self.client.get_all_prices()
        if self.config.dry_run and not self.config.binance_api_key:
            balances = self._simulated_balances_from_state(state)
        else:
            balances = self.client.get_account_balances()

        # 2. Reconciliar estado persistido con saldos reales de Binance
        usdt_free, total_equity = self._reconcile_portfolio(state, balances, all_prices)
        daily_pnl_pct = self._update_daily_metrics(state, total_equity)

        logger.info(
            "Capital Total: %.2f %s | Liquidez Libre: %.2f %s | PnL Diario: %+.2f%% | Posiciones Abiertas: %d/%d",
            total_equity,
            self.config.quote_asset,
            usdt_free,
            self.config.quote_asset,
            daily_pnl_pct,
            len(state.positions),
            self.config.max_open_positions,
        )

        executed_actions: list[dict[str, Any]] = []

        # 3. Verificacion determinista de Stop-Loss, Take-Profit y Trailing Stop (antes de consultar a la IA)
        risk_exits = self._enforce_hard_position_limits(state, all_prices)
        for exit_trade in risk_exits:
            executed_actions.append(exit_trade)
            usdt_free += float(exit_trade.get("quote_qty", 0.0))

        # 4. Escanear los pares con mayor volumen/movimiento + posiciones actuales
        open_symbols = list(state.positions.keys())
        snapshots = self.scanner.build_snapshots(must_include_symbols=open_symbols)
        snapshot_prices = {s.symbol: s.current_price for s in snapshots}
        all_prices.update(snapshot_prices)

        # 5. Consultar a Gemini AI para decisiones estrategicas
        recent_trades = self.state_manager.load_history()[-10:]
        ai_result = self.ai_agent.analyze_market(
            usdt_free=usdt_free,
            total_equity_usdt=total_equity,
            daily_pnl_pct=daily_pnl_pct,
            open_positions=state.positions,
            snapshots=snapshots,
            recent_trades=recent_trades,
            max_open_positions=self.config.max_open_positions,
            max_position_pct=self.config.max_position_pct,
            default_sl_pct=self.config.stop_loss_pct,
            default_tp_pct=self.config.take_profit_pct,
        )
        logger.info("Regimen IA: %s | %s", ai_result.market_regime, ai_result.summary)

        # 6. Ejecutar primero las ventas (SELL) recomendadas por Gemini AI
        for dec in ai_result.decisions:
            if dec.action == "SELL" and dec.symbol in state.positions:
                if dec.confidence >= self.config.min_ai_confidence:
                    trade = self._execute_sell(
                        state=state,
                        symbol=dec.symbol,
                        current_price=all_prices.get(dec.symbol, state.positions[dec.symbol].entry_price),
                        reason=f"IA SELL (Confianza {dec.confidence}%): {dec.reasoning}",
                    )
                    if trade:
                        executed_actions.append(trade)
                        usdt_free += float(trade.get("quote_qty", 0.0))

        # 7. Verificar Cortacircuitos Diario antes de permitir nuevas compras (BUY)
        max_dd_limit_pct = -abs(self.config.max_daily_drawdown_pct * 100.0)
        if daily_pnl_pct <= max_dd_limit_pct:
            logger.warning(
                "CORTACIRCUITOS DIARIO ACTIVADO (PnL diario %.2f%% <= %.2f%%). Se bloquean compras nuevas hoy.",
                daily_pnl_pct,
                max_dd_limit_pct,
            )
        else:
            # Ordenar compras de mayor a menor confianza
            buy_decisions = [
                d
                for d in ai_result.decisions
                if d.action == "BUY"
                and d.confidence >= self.config.min_ai_confidence
                and d.symbol not in state.positions
            ]
            buy_decisions.sort(key=lambda x: x.confidence, reverse=True)

            for dec in buy_decisions:
                if len(state.positions) >= self.config.max_open_positions:
                    logger.info("Maximo de posiciones abiertas alcanzado (%d).", self.config.max_open_positions)
                    break

                available_to_invest = usdt_free - self.config.min_usdt_reserve
                if available_to_invest < self.config.min_order_usdt:
                    logger.info(
                        "USDT disponible tras reserva (%.2f USDT) menor al minimo por orden (%.2f USDT).",
                        available_to_invest,
                        self.config.min_order_usdt,
                    )
                    break

                # Calcular tamano de posicion respetando MAX_POSITION_PCT
                capped_alloc_pct = min(dec.allocation_pct, self.config.max_position_pct)
                target_usdt = min(total_equity * capped_alloc_pct, available_to_invest)
                if target_usdt < self.config.min_order_usdt:
                    continue

                price = all_prices.get(dec.symbol, 0.0)
                if price <= 0:
                    continue

                trade = self._execute_buy(
                    state=state,
                    symbol=dec.symbol,
                    usdt_amount=target_usdt,
                    stop_loss_pct=dec.stop_loss_pct,
                    take_profit_pct=dec.take_profit_pct,
                    reason=f"IA BUY (Confianza {dec.confidence}%): {dec.reasoning}",
                )
                if trade:
                    executed_actions.append(trade)
                    usdt_free -= float(trade.get("quote_qty", target_usdt))

        # 8. Guardar estado actualizado y reporte Markdown para el repositorio
        state.last_equity_usdt = total_equity
        self.state_manager.save_state(state)
        report_md = self._build_markdown_report(
            state=state,
            usdt_free=usdt_free,
            total_equity=total_equity,
            daily_pnl_pct=daily_pnl_pct,
            ai_result=ai_result,
            snapshots=snapshots,
            executed_actions=executed_actions,
            all_prices=all_prices,
        )
        self.state_manager.write_report(report_md)

        return {
            "cycle": state.total_cycles,
            "total_equity_usdt": round(total_equity, 2),
            "usdt_free": round(usdt_free, 2),
            "daily_pnl_pct": round(daily_pnl_pct, 2),
            "market_regime": ai_result.market_regime,
            "executed_actions": executed_actions,
            "open_positions": list(state.positions.keys()),
        }

    def _simulated_balances_from_state(self, state: BotState) -> dict[str, float]:
        balances: dict[str, float] = {}
        start_eq = state.last_equity_usdt if state.last_equity_usdt > 0 else 1000.0
        invested = sum(p.quantity * p.entry_price for p in state.positions.values())
        balances[self.config.quote_asset] = max(0.0, start_eq - invested)
        for pos in state.positions.values():
            balances[pos.base_asset] = pos.quantity
        return balances

    def _reconcile_portfolio(
        self,
        state: BotState,
        balances: dict[str, float],
        all_prices: dict[str, float],
    ) -> tuple[float, float]:
        quote = self.config.quote_asset
        usdt_free = float(balances.get(quote, 0.0))
        total_equity = usdt_free

        # Sincronizar posiciones registradas con el balance real en Binance
        to_remove: list[str] = []
        for sym, pos in list(state.positions.items()):
            live_qty = float(balances.get(pos.base_asset, 0.0))
            cur_price = float(all_prices.get(sym, pos.entry_price))
            live_val_usdt = live_qty * cur_price

            if live_val_usdt < (self.config.min_order_usdt * 0.45):
                logger.info(
                    "Removiendo posicion %s del estado (valor actual %.2f USDT es polvo/cerrada).",
                    sym,
                    live_val_usdt,
                )
                to_remove.append(sym)
                continue

            pos.quantity = live_qty
            if cur_price > pos.highest_price:
                pos.highest_price = cur_price
            total_equity += live_val_usdt

        for sym in to_remove:
            state.positions.pop(sym, None)

        # Detectar activos Spot elegibles en la cuenta que no esten registrados aun
        for asset, qty in balances.items():
            if asset == quote or asset == "BNB":
                # BNB suele reservarse para comisiones si es monto pequeno
                if asset == "BNB":
                    bnb_price = all_prices.get("BNBUSDT", 0.0)
                    total_equity += qty * bnb_price
                continue
            sym = f"{asset}{quote}"
            if sym in state.positions or not self.scanner.is_eligible_symbol(sym):
                continue
            cur_price = float(all_prices.get(sym, 0.0))
            val_usdt = qty * cur_price
            if val_usdt >= self.config.min_order_usdt:
                logger.info("Adoptando posicion existente en cuenta Spot: %s (%.4f unidades ~ %.2f USDT)", sym, qty, val_usdt)
                state.positions[sym] = PositionState(
                    symbol=sym,
                    base_asset=asset,
                    quantity=qty,
                    entry_price=cur_price,
                    highest_price=cur_price,
                    stop_loss_price=round(cur_price * (1.0 - self.config.stop_loss_pct), 6),
                    take_profit_price=round(cur_price * (1.0 + self.config.take_profit_pct), 6),
                    opened_at=utc_now_iso(),
                    entry_reason="Posicion preexistente sincronizada de Binance Spot",
                )
                total_equity += val_usdt

        return usdt_free, total_equity

    def _update_daily_metrics(self, state: BotState, total_equity: float) -> float:
        today = utc_today_str()
        if state.daily_date != today or state.daily_start_equity_usdt <= 0:
            state.daily_date = today
            state.daily_start_equity_usdt = total_equity
        if state.daily_start_equity_usdt <= 0:
            return 0.0
        return ((total_equity - state.daily_start_equity_usdt) / state.daily_start_equity_usdt) * 100.0

    def _enforce_hard_position_limits(
        self,
        state: BotState,
        all_prices: dict[str, float],
    ) -> list[dict[str, Any]]:
        exits: list[dict[str, Any]] = []
        for sym, pos in list(state.positions.items()):
            cur_price = float(all_prices.get(sym, pos.entry_price))
            if cur_price <= 0:
                continue

            if cur_price > pos.highest_price:
                pos.highest_price = cur_price

            pnl_pct = pos.unrealized_pnl_pct(cur_price)
            peak_gain_pct = ((pos.highest_price - pos.entry_price) / pos.entry_price) * 100.0 if pos.entry_price > 0 else 0.0
            drop_from_peak_pct = pos.drawdown_from_peak_pct(cur_price)

            trigger_reason: str | None = None
            if pos.stop_loss_price > 0 and cur_price <= pos.stop_loss_price:
                trigger_reason = f"STOP-LOSS ESTRICTO alcanzado ({cur_price} <= {pos.stop_loss_price}, PnL {pnl_pct:+.2f}%)"
            elif pos.take_profit_price > 0 and cur_price >= pos.take_profit_price:
                trigger_reason = f"TAKE-PROFIT alcanzado ({cur_price} >= {pos.take_profit_price}, PnL {pnl_pct:+.2f}%)"
            elif (
                peak_gain_pct >= (self.config.trailing_activation_pct * 100.0)
                and drop_from_peak_pct >= (self.config.trailing_stop_pct * 100.0)
            ):
                trigger_reason = (
                    f"TRAILING STOP activado (Pico {pos.highest_price}, retroceso -{drop_from_peak_pct:.2f}%, "
                    f"ganancia asegurada {pnl_pct:+.2f}%)"
                )

            if trigger_reason:
                logger.warning("Ejecutando salida automatica en %s: %s", sym, trigger_reason)
                trade = self._execute_sell(state, sym, cur_price, reason=trigger_reason)
                if trade:
                    exits.append(trade)

        return exits

    def _execute_buy(
        self,
        state: BotState,
        symbol: str,
        usdt_amount: float,
        stop_loss_pct: float,
        take_profit_pct: float,
        reason: str,
    ) -> dict[str, Any] | None:
        try:
            order = self.client.place_market_buy_usdt(
                symbol=symbol,
                usdt_amount=usdt_amount,
                dry_run=self.config.dry_run,
            )
            exec_qty = float(order.get("executedQty", 0.0))
            quote_qty = float(order.get("cummulativeQuoteQty", usdt_amount))
            avg_price = float(order.get("avgPrice", 0.0))
            if exec_qty <= 0 or avg_price <= 0:
                return None

            sl_price = round(avg_price * (1.0 - stop_loss_pct), 6)
            tp_price = round(avg_price * (1.0 + take_profit_pct), 6)
            base_asset = symbol[: -len(self.config.quote_asset)]

            state.positions[symbol] = PositionState(
                symbol=symbol,
                base_asset=base_asset,
                quantity=exec_qty,
                entry_price=avg_price,
                highest_price=avg_price,
                stop_loss_price=sl_price,
                take_profit_price=tp_price,
                opened_at=utc_now_iso(),
                entry_reason=reason,
            )

            record = {
                "timestamp": utc_now_iso(),
                "symbol": symbol,
                "side": "BUY",
                "mode": "DRY_RUN" if self.config.dry_run else "LIVE",
                "quantity": exec_qty,
                "price": avg_price,
                "quote_qty": round(quote_qty, 2),
                "stop_loss_price": sl_price,
                "take_profit_price": tp_price,
                "reason": reason,
            }
            self.state_manager.append_trade(record)
            logger.info("COMPRA ejecutada: %s | Cantidad: %s @ %s | Total: %.2f USDT", symbol, exec_qty, avg_price, quote_qty)
            return record
        except Exception as exc:
            logger.error("Error al ejecutar COMPRA de %s: %s", symbol, exc)
            return None

    def _execute_sell(
        self,
        state: BotState,
        symbol: str,
        current_price: float,
        reason: str,
    ) -> dict[str, Any] | None:
        pos = state.positions.get(symbol)
        if not pos:
            return None

        try:
            order = self.client.place_market_sell_quantity(
                symbol=symbol,
                quantity=pos.quantity,
                dry_run=self.config.dry_run,
            )
            exec_qty = float(order.get("executedQty", pos.quantity))
            quote_qty = float(order.get("cummulativeQuoteQty", exec_qty * current_price))
            avg_price = float(order.get("avgPrice", current_price))
            pnl_pct = pos.unrealized_pnl_pct(avg_price)
            pnl_usdt = quote_qty - (exec_qty * pos.entry_price)

            state.positions.pop(symbol, None)

            record = {
                "timestamp": utc_now_iso(),
                "symbol": symbol,
                "side": "SELL",
                "mode": "DRY_RUN" if self.config.dry_run else "LIVE",
                "quantity": exec_qty,
                "entry_price": pos.entry_price,
                "price": avg_price,
                "quote_qty": round(quote_qty, 2),
                "pnl_usdt": round(pnl_usdt, 2),
                "pnl_pct": round(pnl_pct, 2),
                "reason": reason,
            }
            self.state_manager.append_trade(record)
            logger.info(
                "VENTA ejecutada: %s | Cantidad: %s @ %s | PnL: %+.2f USDT (%+.2f%%)",
                symbol,
                exec_qty,
                avg_price,
                pnl_usdt,
                pnl_pct,
            )
            return record
        except Exception as exc:
            logger.error("Error al ejecutar VENTA de %s: %s", symbol, exc)
            return None

    def _build_markdown_report(
        self,
        state: BotState,
        usdt_free: float,
        total_equity: float,
        daily_pnl_pct: float,
        ai_result: AIAnalysisResult,
        snapshots: list[TechnicalSnapshot],
        executed_actions: list[dict[str, Any]],
        all_prices: dict[str, float],
    ) -> str:
        mode_label = "SIMULACION (DRY_RUN)" if self.config.dry_run else "CUENTA REAL (LIVE)"
        lines = [
            "# Reporte Autonomo de Trading - Binance + Gemini AI",
            "",
            f"- **Ultima actualizacion (UTC):** `{state.updated_at}`",
            f"- **Ciclo de ejecucion:** `#{state.total_cycles}`",
            f"- **Modo:** `{mode_label}`",
            f"- **Capital Total Estimado:** `{total_equity:.2f} {self.config.quote_asset}`",
            f"- **Liquidez Disponible:** `{usdt_free:.2f} {self.config.quote_asset}`",
            f"- **Rendimiento Diario (UTC):** `{daily_pnl_pct:+.2f}%`",
            f"- **Regimen de Mercado (Gemini):** `{ai_result.market_regime}`",
            "",
            "## Lectura de Mercado de Gemini AI",
            f"> {ai_result.summary}",
            "",
            "## Posiciones Abiertas Actuales",
        ]

        if not state.positions:
            lines.append("_No hay posiciones abiertas en este momento._")
        else:
            lines.extend(
                [
                    "| Par | Cantidad | Entrada | Precio Actual | PnL (%) | Stop-Loss | Take-Profit |",
                    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
                ]
            )
            for sym, pos in state.positions.items():
                cur = all_prices.get(sym, pos.entry_price)
                pnl = pos.unrealized_pnl_pct(cur)
                lines.append(
                    f"| `{sym}` | {pos.quantity} | {pos.entry_price} | {cur} | **{pnl:+.2f}%** | {pos.stop_loss_price} | {pos.take_profit_price} |"
                )

        lines.extend(["", "## Operaciones Ejecutadas en este Ciclo"])
        if not executed_actions:
            lines.append("_Ninguna orden ejecutada en este ciclo._")
        else:
            for act in executed_actions:
                pnl_str = f" | PnL: `{act['pnl_pct']:+.2f}%`" if "pnl_pct" in act else ""
                lines.append(
                    f"- **{act['side']} `{act['symbol']}`** @ `{act['price']}` ({act['quote_qty']} USDT){pnl_str} — _{act['reason']}_"
                )

        lines.extend(
            [
                "",
                "## Escaneo Dinamico y Decisiones IA",
                "| Par | Precio | Cambio 24h | RSI (15m) | Tendencia (15m/1h) | Decision IA | Confianza | Motivo |",
                "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
            ]
        )
        dec_map = {d.symbol: d for d in ai_result.decisions}
        for s in snapshots:
            d = dec_map.get(s.symbol)
            act = d.action if d else "HOLD"
            conf = f"{d.confidence}%" if d else "-"
            reason = d.reasoning if d else "-"
            lines.append(
                f"| `{s.symbol}` | {s.current_price} | {s.price_change_24h_pct:+.2f}% | {s.rsi_14} | `{s.trend_primary}` / `{s.htf_trend}` | **{act}** | {conf} | {reason} |"
            )

        return "\n".join(lines) + "\n"
