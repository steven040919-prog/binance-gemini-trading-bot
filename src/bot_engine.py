from __future__ import annotations

import logging
from typing import Any

from src.binance_client import BinanceSpotClient
from src.config import BotConfig
from src.gemini_agent import AIAnalysisResult, GeminiTradingAgent
from src.market_scanner import MarketScanner, TechnicalSnapshot
from src.state_manager import BotState, PositionState, StateManager, utc_now_iso, utc_today_str

logger = logging.getLogger(__name__)


def calculate_position_size_1pct_risk(
    total_equity_usdt: float,
    available_usdt: float,
    entry_price: float,
    stop_loss_price: float,
    risk_pct: float = 0.01,
    min_risk_usd: float = 1.0,
    max_position_pct: float = 0.35,
) -> tuple[float, float]:
    """
    Calcula el tamano de posicion para arriesgar exactamente el 1% del capital total (minimo $1 USD)
    en funcion de la distancia entre el precio de entrada y el Stop-Loss (bajo/alto de la vela anterior).
    Retorna (monto_orden_usdt, riesgo_monetario_usd).
    """
    risk_usd = max(min_risk_usd, total_equity_usdt * risk_pct)
    if entry_price <= 0:
        return 0.0, risk_usd

    sl_distance_pct = abs(entry_price - stop_loss_price) / entry_price
    # Si el bajo de la vela anterior esta demasiado pegado (<0.25%), usamos 0.25% minimo para evitar sobredimensionar
    effective_sl_pct = max(sl_distance_pct, 0.0025)

    # Nocional ideal para que una caida de effective_sl_pct equivalga a perder `risk_usd`
    ideal_notional_usdt = risk_usd / effective_sl_pct

    # Acotamos al capital maximo permitido por posicion y a la liquidez disponible
    max_allowed_usdt = min(available_usdt, max(total_equity_usdt * max_position_pct, min_risk_usd))
    # Si la cuenta es pequena, garantizamos al menos el minimo de $1 USD o el disponible
    final_usdt = min(ideal_notional_usdt, max_allowed_usdt)
    if final_usdt < min_risk_usd and available_usdt >= min_risk_usd:
        final_usdt = min_risk_usd

    return round(final_usdt, 2), round(risk_usd, 2)


class AutonomousTradingBot:
    """
    Motor autonomo que ejecuta la estrategia:
    - Temporalidad: 1 Hora (1h)
    - Indicadores: EMA 200 + Estocastico (niveles 80 / 20)
    - Gatillo: Vela Martillo o Vela Envolvente
    - Stop-Loss: Ultimo bajo/alto de la vela anterior
    - Salida: Cuando el Estocastico alcanza el extremo opuesto (80 en compra / 20 en venta)
    - Riesgo: 1% del monto total (minimo $1 dolar)
    """

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
            ema_trend_period=config.ema_trend_period,
            stoch_k_period=config.stoch_k_period,
            stoch_smooth_k=config.stoch_smooth_k,
            stoch_d_period=config.stoch_d_period,
            stoch_overbought=config.stoch_overbought,
            stoch_oversold=config.stoch_oversold,
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
        """Ejecuta un ciclo completo de la estrategia EMA 200 + Estocastico (80/20) + Velas en 1H."""
        self.config.validate()
        state = self.state_manager.load_state()
        state.total_cycles += 1

        logger.info(
            "=== Iniciando Ciclo #%d | Estrategia EMA %d + Estocastico (%.0f/%.0f) en %s ===",
            state.total_cycles,
            self.config.ema_trend_period,
            self.config.stoch_overbought,
            self.config.stoch_oversold,
            self.config.kline_interval_primary,
        )

        # 1. Obtener precios globales y saldos reales de Binance
        all_prices = self.client.get_all_prices()
        if self.config.dry_run and not self.config.binance_api_key:
            balances = self._simulated_balances_from_state(state)
        else:
            balances = self.client.get_account_balances()

        # 2. Reconciliar estado persistido con saldos reales de Binance
        usdt_free, total_equity = self._reconcile_portfolio(state, balances, all_prices)
        daily_pnl_pct = self._update_daily_metrics(state, total_equity)

        # 3. Escanear el mercado en 1H (EMA 200, Estocastico y Patrones de Velas Martillo/Envolvente)
        open_symbols = list(state.positions.keys())
        snapshots = self.scanner.build_snapshots(must_include_symbols=open_symbols)
        snapshots_map: dict[str, TechnicalSnapshot] = {s.symbol: s for s in snapshots}
        for s in snapshots:
            all_prices[s.symbol] = s.current_price

        executed_actions: list[dict[str, Any]] = []

        # 4. Reglas Deterministas de Salida:
        #    - Stop-Loss en el ultimo bajo de la vela anterior
        #    - Cierre automatico cuando el Estocastico llega a >= 80 (sobrecompra)
        risk_exits = self._enforce_strategy_exits(state, all_prices, snapshots_map)
        for exit_trade in risk_exits:
            executed_actions.append(exit_trade)
            usdt_free += float(exit_trade.get("quote_qty", 0.0))

        # 5. Consultar a Gemini AI sobre los candidatos y setups detectados
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

        # 6. Ejecutar ventas (SELL) recomendadas por Gemini AI en posiciones abiertas
        for dec in ai_result.decisions:
            if dec.action == "SELL" and dec.symbol in state.positions:
                if dec.confidence >= self.config.min_ai_confidence:
                    trade = self._execute_sell(
                        state=state,
                        symbol=dec.symbol,
                        current_price=all_prices.get(dec.symbol, state.positions[dec.symbol].entry_price),
                        reason=f"Cierre IA (Confianza {dec.confidence}%): {dec.reasoning}",
                    )
                    if trade:
                        executed_actions.append(trade)
                        usdt_free += float(trade.get("quote_qty", 0.0))

        # 7. Ejecutar entradas que cumplan la estrategia EMA 200 + Estocastico <= 20 + Vela Martillo/Envolvente
        max_dd_limit_pct = -abs(self.config.max_daily_drawdown_pct * 100.0)
        if daily_pnl_pct <= max_dd_limit_pct:
            logger.warning(
                "CORTACIRCUITOS DIARIO ACTIVADO (PnL diario %.2f%% <= %.2f%%). Se bloquean compras nuevas hoy.",
                daily_pnl_pct,
                max_dd_limit_pct,
            )
        else:
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
                    break

                snap = snapshots_map.get(dec.symbol)
                price = all_prices.get(dec.symbol, 0.0)
                if price <= 0:
                    continue

                # Validar condicion de EMA 200 si el snapshot esta disponible
                if snap is not None and not snap.above_ema_200:
                    logger.info(
                        "Omitiendo BUY en %s porque el precio (%.6f) esta por debajo de la EMA 200 (%.6f).",
                        dec.symbol,
                        price,
                        snap.ema_200,
                    )
                    continue

                # Determinar Stop-Loss en el ultimo bajo de la vela anterior (o fallback porcentual)
                if snap is not None and 0 < snap.prev_candle_low < price:
                    structural_sl = snap.prev_candle_low
                else:
                    structural_sl = round(price * (1.0 - dec.stop_loss_pct), 6)

                available_to_invest = max(0.0, usdt_free - self.config.min_usdt_reserve)
                if available_to_invest < self.config.min_order_usdt:
                    break

                # Calcular monto exacto arriesgando solo el 1% del capital (minimo $1 USD)
                order_usdt, risk_usd = calculate_position_size_1pct_risk(
                    total_equity_usdt=total_equity,
                    available_usdt=available_to_invest,
                    entry_price=price,
                    stop_loss_price=structural_sl,
                    risk_pct=self.config.risk_per_trade_pct,
                    min_risk_usd=self.config.min_risk_usd,
                    max_position_pct=min(dec.allocation_pct, self.config.max_position_pct),
                )

                if order_usdt < self.config.min_order_usdt:
                    continue

                pattern_tag = snap.candle_pattern if snap else "IA_SIGNAL"
                stoch_tag = f"Stoch %K={snap.stoch_k}" if snap else ""
                trade = self._execute_buy(
                    state=state,
                    symbol=dec.symbol,
                    usdt_amount=order_usdt,
                    stop_loss_price=structural_sl,
                    take_profit_pct=dec.take_profit_pct,
                    reason=(
                        f"Estrategia EMA200+Stoch ({pattern_tag}, {stoch_tag}, Riesgo ~${risk_usd} USD / 1%): "
                        f"{dec.reasoning}"
                    ),
                )
                if trade:
                    executed_actions.append(trade)
                    usdt_free -= float(trade.get("quote_qty", order_usdt))

        # 8. Guardar estado y reporte Markdown
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

        to_remove: list[str] = []
        for sym, pos in list(state.positions.items()):
            live_qty = float(balances.get(pos.base_asset, 0.0))
            cur_price = float(all_prices.get(sym, pos.entry_price))
            live_val_usdt = live_qty * cur_price

            if live_val_usdt < (self.config.min_order_usdt * 0.45):
                to_remove.append(sym)
                continue

            pos.quantity = live_qty
            if cur_price > pos.highest_price:
                pos.highest_price = cur_price
            total_equity += live_val_usdt

        for sym in to_remove:
            state.positions.pop(sym, None)

        for asset, qty in balances.items():
            if asset == quote or asset == "BNB":
                if asset == "BNB":
                    bnb_price = all_prices.get("BNBUSDT", 0.0)
                    total_equity += qty * bnb_price
                continue
            sym = f"{asset}{quote}"
            if sym in state.positions or not self.scanner.is_eligible_symbol(sym):
                continue
            cur_price = float(all_prices.get(sym, 0.0))
            val_usdt = qty * cur_price
            if val_usdt >= max(self.config.min_order_usdt, 5.0):
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

    def _enforce_strategy_exits(
        self,
        state: BotState,
        all_prices: dict[str, float],
        snapshots_map: dict[str, TechnicalSnapshot],
    ) -> list[dict[str, Any]]:
        """
        Cierra automaticamente cualquier posicion abierta cuando:
        1. Toca el Stop-Loss ubicado en el ultimo bajo de la vela anterior.
        2. El oscilador Estocastico en 1H llega a >= 80 (cierre por sobrecompra de la estrategia).
        3. Toca el Take-Profit de respaldo.
        """
        exits: list[dict[str, Any]] = []
        for sym, pos in list(state.positions.items()):
            cur_price = float(all_prices.get(sym, pos.entry_price))
            if cur_price <= 0:
                continue

            if cur_price > pos.highest_price:
                pos.highest_price = cur_price

            pnl_pct = pos.unrealized_pnl_pct(cur_price)
            snap = snapshots_map.get(sym)

            trigger_reason: str | None = None
            if pos.stop_loss_price > 0 and cur_price <= pos.stop_loss_price:
                trigger_reason = (
                    f"STOP-LOSS (Bajo de vela anterior) alcanzado ({cur_price} <= {pos.stop_loss_price}, PnL {pnl_pct:+.2f}%)"
                )
            elif snap is not None and (
                snap.stoch_k >= self.config.stoch_overbought or snap.stoch_d >= self.config.stoch_overbought
            ):
                trigger_reason = (
                    f"CIERRE POR ESTOCASTICO >= {self.config.stoch_overbought:.0f} "
                    f"(%K={snap.stoch_k}, %D={snap.stoch_d}, PnL {pnl_pct:+.2f}%)"
                )
            elif pos.take_profit_price > 0 and cur_price >= pos.take_profit_price:
                trigger_reason = f"TAKE-PROFIT alcanzado ({cur_price} >= {pos.take_profit_price}, PnL {pnl_pct:+.2f}%)"

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
        stop_loss_price: float,
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

            sl_price = round(stop_loss_price, 8) if stop_loss_price > 0 else round(avg_price * (1.0 - self.config.stop_loss_pct), 8)
            tp_price = round(avg_price * (1.0 + take_profit_pct), 8)
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
            logger.info("COMPRA ejecutada: %s | Cantidad: %s @ %s | Total: %.2f USDT | SL: %s", symbol, exec_qty, avg_price, quote_qty, sl_price)
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
            "# Reporte Autonomo - Estrategia EMA 200 + Estocastico (80/20) + Velas (1H)",
            "",
            f"- **Ultima actualizacion (UTC):** `{state.updated_at}`",
            f"- **Ciclo de ejecucion:** `#{state.total_cycles}`",
            f"- **Modo:** `{mode_label}`",
            f"- **Temporalidad:** `{self.config.kline_interval_primary}` | **Riesgo por Operacion:** `{self.config.risk_per_trade_pct * 100:.1f}% (min ${self.config.min_risk_usd:.2f} USD)`",
            f"- **Capital Total Estimado:** `{total_equity:.2f} {self.config.quote_asset}`",
            f"- **Liquidez Disponible:** `{usdt_free:.2f} {self.config.quote_asset}`",
            f"- **Rendimiento Diario (UTC):** `{daily_pnl_pct:+.2f}%`",
            f"- **Regimen de Mercado (Gemini 3.8 Flash):** `{ai_result.market_regime}`",
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
                    "| Par | Cantidad | Entrada | Precio Actual | PnL (%) | Stop-Loss (Bajo Vela Previa) | Salida Estocastico |",
                    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
                ]
            )
            for sym, pos in state.positions.items():
                cur = all_prices.get(sym, pos.entry_price)
                pnl = pos.unrealized_pnl_pct(cur)
                lines.append(
                    f"| `{sym}` | {pos.quantity} | {pos.entry_price} | {cur} | **{pnl:+.2f}%** | {pos.stop_loss_price} | `Stoch >= {self.config.stoch_overbought:.0f}` |"
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
                "## Escaneo 1H: EMA 200 + Estocastico (20/80) + Patrones de Vela",
                "| Par | Precio | EMA 200 | Posicion EMA | Estocastico (%K / %D) | Patron de Vela (1H) | SL Vela Previa | Setup | Decision IA |",
                "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
            ]
        )
        dec_map = {d.symbol: d for d in ai_result.decisions}
        for s in snapshots:
            d = dec_map.get(s.symbol)
            act = f"**{d.action}** ({d.confidence}%)" if d else "HOLD"
            ema_pos = "SOBRE EMA 200 (Alza)" if s.above_ema_200 else "BAJO EMA 200 (Baja)"
            sl_ref = s.prev_candle_low if s.above_ema_200 else s.prev_candle_high
            lines.append(
                f"| `{s.symbol}` | {s.current_price} | {s.ema_200} | {ema_pos} | `{s.stoch_k}` / `{s.stoch_d}` | `{s.candle_pattern}` | {sl_ref} | `{s.strategy_setup}` | {act} |"
            )

        return "\n".join(lines) + "\n"
