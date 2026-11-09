from __future__ import annotations

import logging
from typing import Any

from src.binance_client import BinanceAPIError, BinanceSpotClient
from src.config import BotConfig
from src.gemini_agent import AIAnalysisResult, AIDecision, GeminiTradingAgent
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
    effective_sl_pct = max(sl_distance_pct, 0.0025)

    ideal_notional_usdt = risk_usd / effective_sl_pct
    max_allowed_usdt = min(available_usdt, max(total_equity_usdt * max_position_pct, min_risk_usd, 5.5))
    final_usdt = min(ideal_notional_usdt, max_allowed_usdt)
    if final_usdt < 5.5 and available_usdt >= 5.5:
        final_usdt = 5.5
    elif final_usdt < min_risk_usd and available_usdt >= min_risk_usd:
        final_usdt = min_risk_usd

    return round(final_usdt, 2), round(risk_usd, 2)


class AutonomousTradingBot:
    """
    Motor autonomo que ejecuta la estrategia:
    - Temporalidad: 1 Hora (1h)
    - Indicadores: EMA 200 + Estocastico (niveles 80 / 20)
    - Gatillo: Vela Martillo o Vela Envolvente
    - Stop-Loss inicial: Ultimo bajo/alto de la vela anterior
    - Gestion Dinamica en Ganancia (Bot + Gemini AI):
      Mueve el Stop-Loss (Break-Even / Trailing por velas) y expande el Take-Profit hacia arriba
      para dejar correr las operaciones ganadoras y maximizar beneficios.
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
        self._effective_dry_run = config.dry_run
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
        """Ejecuta un ciclo completo de la estrategia EMA 200 + Estocastico + Trailing Dinamico SL/TP."""
        self.config.validate()
        self._effective_dry_run = self.config.dry_run
        state = self.state_manager.load_state()
        state.total_cycles += 1

        logger.info(
            "=== Iniciando Ciclo #%d | Estrategia EMA %d + Estocastico (%.0f/%.0f) + SL/TP Dinamico en %s ===",
            state.total_cycles,
            self.config.ema_trend_period,
            self.config.stoch_overbought,
            self.config.stoch_oversold,
            self.config.kline_interval_primary,
        )

        # 1. Obtener precios globales (data-api.binance.vision funciona globalmente sin bloqueo)
        all_prices = self.client.get_all_prices()

        # 2. Obtener saldos reales de Binance (con fallback seguro si GitHub Actions topa con HTTP 451 sin proxy)
        if self._effective_dry_run and not self.config.binance_api_key:
            balances = self._simulated_balances_from_state(state)
        else:
            try:
                balances = self.client.get_account_balances()
                # Si la cuenta tiene saldo en USD (>= 5.0) y estamos operando contra USDT, lo convierte automaticamente
                usd_bal = float(balances.get("USD", 0.0))
                usdt_bal = float(balances.get("USDT", 0.0))
                if self.config.quote_asset == "USDT" and usd_bal >= 5.0 and not self._effective_dry_run:
                    logger.info("Detectado saldo de %.2f USD en Spot. Convirtiendo automaticamente a USDT via par USDTUSD...", usd_bal)
                    try:
                        conv_order = self.client.place_market_buy_usdt("USDTUSD", usdt_amount=usd_bal, dry_run=False)
                        logger.info("Conversion USD -> USDT completada: %s", conv_order.get("executedQty"))
                        balances = self.client.get_account_balances()
                    except Exception as conv_exc:
                        logger.warning("No se pudo convertir USD a USDT automaticamente: %s", conv_exc)
            except BinanceAPIError as exc:
                if exc.status_code == 451:
                    logger.warning(
                        "Runner en region restringida por Binance (HTTP 451 sin BINANCE_PROXY_URL). "
                        "Ejecutando analisis en vivo con datos reales de Binance + Gemini AI en modo cartera virtual."
                    )
                    self._effective_dry_run = True
                    balances = self._simulated_balances_from_state(state)
                else:
                    raise

        # 3. Reconciliar estado persistido con saldos
        usdt_free, total_equity = self._reconcile_portfolio(state, balances, all_prices)
        daily_pnl_pct = self._update_daily_metrics(state, total_equity)

        # 4. Escanear el mercado en 1H (EMA 200, Estocastico y Patrones de Velas Martillo/Envolvente)
        open_symbols = list(state.positions.keys())
        snapshots = self.scanner.build_snapshots(must_include_symbols=open_symbols)
        snapshots_map: dict[str, TechnicalSnapshot] = {s.symbol: s for s in snapshots}
        for s in snapshots:
            all_prices[s.symbol] = s.current_price

        executed_actions: list[dict[str, Any]] = []

        # 5. Gestion Dinamica de Posiciones en Ganancia y Salidas Estructurales:
        #    - Si toca Stop-Loss (inicial o ya subido en ganancia), cierra.
        #    - Si va en ganancia, sube Stop-Loss (Break-Even / Bajo de vela previa) y expande Take-Profit para dejar correr!
        #    - Si Estocastico >= 80 con vela de rechazo bajista, cobra ganancias; si sigue alcista fuerte, aprieta SL y deja correr!
        exits_and_trails = self._manage_winning_positions_and_exits(state, all_prices, snapshots_map)
        for act in exits_and_trails:
            executed_actions.append(act)
            if act.get("side") == "SELL":
                usdt_free += float(act.get("quote_qty", 0.0))

        # 6. Consultar a Gemini AI sobre los candidatos y ajustes dinamicos de SL/TP en posiciones abiertas
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

        # 7. Procesar cierres (SELL) o ajustes dinamicos de SL/TP (ADJUST / HOLD con nuevos niveles) sugeridos por Gemini AI
        for dec in ai_result.decisions:
            if dec.symbol not in state.positions:
                continue

            if dec.action == "SELL" and dec.confidence >= self.config.min_ai_confidence:
                trade = self._execute_sell(
                    state=state,
                    symbol=dec.symbol,
                    current_price=all_prices.get(dec.symbol, state.positions[dec.symbol].entry_price),
                    reason=f"Cierre IA (Confianza {dec.confidence}%): {dec.reasoning}",
                )
                if trade:
                    executed_actions.append(trade)
                    usdt_free += float(trade.get("quote_qty", 0.0))
            elif dec.action in ("ADJUST", "HOLD") and (dec.new_stop_loss_price > 0 or dec.new_take_profit_price > 0):
                adj_record = self._apply_ai_sl_tp_adjustment(
                    state=state,
                    decision=dec,
                    current_price=all_prices.get(dec.symbol, state.positions[dec.symbol].entry_price),
                )
                if adj_record:
                    executed_actions.append(adj_record)

        # 8. Ejecutar nuevas entradas que cumplan la estrategia EMA 200 + Estocastico <= 20 + Vela Martillo/Envolvente
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

                has_institutional_pillar = snap is not None and (
                    snap.entry_pillar
                    in (
                        "P1_EMA200_PULLBACK",
                        "P2_EXTREME_CAPITULATION",
                        "P3_BULLISH_DIVERGENCE_SPRING",
                        "P4_STRONG_TREND_EMA50_CONTINUATION",
                    )
                    or snap.strategy_setup == "LONG_ENTRY"
                )
                if snap is not None and (not snap.above_ema_200) and (not has_institutional_pillar):
                    logger.info(
                        "Omitiendo BUY en %s porque el precio (%.6f) esta bajo EMA 200 (%.6f) sin Pilar Institucional.",
                        dec.symbol,
                        price,
                        snap.ema_200,
                    )
                    continue

                if snap is not None and 0 < snap.structural_sl_price < price:
                    structural_sl = snap.structural_sl_price
                elif snap is not None and 0 < snap.prev_candle_low < price:
                    structural_sl = snap.prev_candle_low
                else:
                    structural_sl = round(price * (1.0 - dec.stop_loss_pct), 6)

                available_to_invest = max(0.0, usdt_free - self.config.min_usdt_reserve)
                if available_to_invest < self.config.min_order_usdt:
                    break

                # Asignacion Dinamica por Conviccion (85% en Pilares Tier-1 P2/P3/P4 con >81% WR; 65% en P1)
                conviction_cap = (
                    0.85
                    if (
                        snap is not None
                        and snap.entry_pillar
                        in (
                            "P2_EXTREME_CAPITULATION",
                            "P3_BULLISH_DIVERGENCE_SPRING",
                            "P4_STRONG_TREND_EMA50_CONTINUATION",
                        )
                    )
                    else 0.65
                )
                effective_max_pos_pct = min(self.config.max_position_pct, max(dec.allocation_pct, conviction_cap))

                order_usdt, risk_usd = calculate_position_size_1pct_risk(
                    total_equity_usdt=total_equity,
                    available_usdt=available_to_invest,
                    entry_price=price,
                    stop_loss_price=structural_sl,
                    risk_pct=self.config.risk_per_trade_pct,
                    min_risk_usd=self.config.min_risk_usd,
                    max_position_pct=effective_max_pos_pct,
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

        # 9. Guardar estado y reporte Markdown
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
                sl_init = round(cur_price * (1.0 - self.config.stop_loss_pct), 6)
                state.positions[sym] = PositionState(
                    symbol=sym,
                    base_asset=asset,
                    quantity=qty,
                    entry_price=cur_price,
                    highest_price=cur_price,
                    stop_loss_price=sl_init,
                    take_profit_price=round(cur_price * (1.0 + self.config.take_profit_pct), 6),
                    opened_at=utc_now_iso(),
                    entry_reason="Posicion preexistente sincronizada de Binance Spot",
                    initial_stop_loss_price=sl_init,
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

    def _manage_winning_positions_and_exits(
        self,
        state: BotState,
        all_prices: dict[str, float],
        snapshots_map: dict[str, TechnicalSnapshot],
    ) -> list[dict[str, Any]]:
        """
        Gestiona las operaciones abiertas para:
        1. Cerrar si el precio toca el Stop-Loss actual (en perdida controlada del 1% o en ganancia asegurada).
        2. Si la operacion va en ganancia, MOVER EL STOP-LOSS Y EL TAKE-PROFIT HACIA ARRIBA para dejar correr la operacion:
           - Al alcanzar >= 1R o >= +1.5% de ganancia: mueve el SL a Break-Even + ganancia asegurada.
           - A medida que suben las velas de 1H: sube el SL al ultimo bajo de la vela previa (`prev_candle_low`) o asegurando el 65% del pico.
           - Si el precio alcanza o se acerca al Take-Profit (o el Estocastico llega a >= 80 mientras la tendencia sigue alcista sin vela bajista):
             NO cierra prematuramente si el impulso continua; sube el SL asegurando el 75% de la ganancia y extiende el Take-Profit mas arriba!
           - Si el Estocastico llega a >= 80 Y aparece una vela bajista de rechazo (Shooting Star / Bearish Engulfing), cierra cobrando toda la ganancia.
        """
        actions: list[dict[str, Any]] = []
        for sym, pos in list(state.positions.items()):
            cur_price = float(all_prices.get(sym, pos.entry_price))
            if cur_price <= 0:
                continue

            if cur_price > pos.highest_price:
                pos.highest_price = cur_price

            pnl_pct = pos.unrealized_pnl_pct(cur_price)
            r_mult = pos.r_multiple(cur_price)
            snap = snapshots_map.get(sym)

            # 1. ¿Toco el Stop-Loss actual?
            if pos.stop_loss_price > 0 and cur_price <= pos.stop_loss_price:
                locked_tag = "GANANCIA ASEGURADA (Trailing SL)" if pos.stop_loss_price > pos.entry_price else "STOP-LOSS (Bajo de vela previa)"
                reason = f"{locked_tag} alcanzado ({cur_price} <= {pos.stop_loss_price}, PnL {pnl_pct:+.2f}%)"
                logger.warning("Ejecutando salida en %s: %s", sym, reason)
                trade = self._execute_sell(state, sym, cur_price, reason=reason)
                if trade:
                    actions.append(trade)
                continue

            # 2. ¿Estocastico >= 80 con patron de vela de rechazo bajista o perdida de EMA 200?
            is_stoch_overbought = snap is not None and (
                snap.stoch_k >= self.config.stoch_overbought or snap.stoch_d >= self.config.stoch_overbought
            )
            has_bearish_reversal = snap is not None and (
                snap.candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING") or not snap.above_ema_200
            )
            if is_stoch_overbought and has_bearish_reversal:
                reason = (
                    f"CIERRE POR ESTOCASTICO >= {self.config.stoch_overbought:.0f} + RECHAZO BAJISTA "
                    f"(%K={snap.stoch_k if snap else 0}, Patron={snap.candle_pattern if snap else 'NONE'}, PnL {pnl_pct:+.2f}%)"
                )
                logger.info("Cerrando posicion en %s: %s", sym, reason)
                trade = self._execute_sell(state, sym, cur_price, reason=reason)
                if trade:
                    actions.append(trade)
                continue

            # 2b. Cosecha por Tiempo (Time-Profit Harvest 36h del Backtest de 6 Meses):
            #     Si lleva >= 36h abierta, esta en ganancia neta (>= +0.6%) y el Estocastico ya subio a >= 72, cosecha ganancia
            if pos.hours_open() >= 36.0 and pnl_pct >= 0.6 and snap is not None and snap.stoch_k >= 72.0:
                reason = (
                    f"COSECHA CUANTITATIVA 36H (Horas={pos.hours_open():.1f}h, Stoch %K={snap.stoch_k}, PnL {pnl_pct:+.2f}%)"
                )
                logger.info("Cerrando posicion por Time-Profit Harvest en %s: %s", sym, reason)
                trade = self._execute_sell(state, sym, cur_price, reason=reason)
                if trade:
                    actions.append(trade)
                continue

            # 3. GESTION DINAMICA ("DEJAR CORRER LA GANANCIA"): Mover SL y TP hacia arriba en operaciones ganadoras
            if pnl_pct > 0:
                old_sl = pos.stop_loss_price
                old_tp = pos.take_profit_price
                candidate_sl = old_sl
                candidate_tp = old_tp
                reasons_list: list[str] = []

                # 3a. Al llegar a >= 1R o >= +1.2% de ganancia: subir SL a Break-Even + ganancia asegurada (+0.3% a +0.9%)
                if r_mult >= 1.0 or pnl_pct >= 1.2:
                    lock_pct = 0.009 if pnl_pct >= 2.2 else 0.003
                    be_plus = round(pos.entry_price * (1.0 + lock_pct), 8)
                    if be_plus > candidate_sl and be_plus < cur_price * 0.996:
                        candidate_sl = be_plus
                        reasons_list.append(f"Break-Even+{lock_pct * 100:.1f}%")

                # 3b. Trailing estructural por el bajo de la vela anterior de 1H (`prev_candle_low`)
                if snap is not None and snap.prev_candle_low > pos.entry_price:
                    if snap.prev_candle_low > candidate_sl and snap.prev_candle_low < cur_price * 0.997:
                        candidate_sl = round(snap.prev_candle_low, 8)
                        reasons_list.append(f"Bajo vela previa 1H ({snap.prev_candle_low})")

                # 3c. Si lleva >= 2.0% de ganancia o >= 1.5R: asegurar entre 60%, 76% y 80% del recorrido desde la entrada hasta el pico
                if pnl_pct >= 2.0 or r_mult >= 1.5:
                    if pnl_pct >= 5.5:
                        keep_ratio = 0.80
                    elif pnl_pct >= 3.2:
                        keep_ratio = 0.76
                    else:
                        keep_ratio = 0.60
                    profit_span = pos.highest_price - pos.entry_price
                    lock_peak_sl = round(pos.entry_price + (profit_span * keep_ratio), 8)
                    if lock_peak_sl > candidate_sl and lock_peak_sl < cur_price * 0.996:
                        candidate_sl = lock_peak_sl
                        reasons_list.append(f"Asegurar {int(keep_ratio * 100)}% del pico")

                # 3d. Si el Estocastico llega a >= 80 pero la tendencia sigue alcista (sin vela bajista),
                #     NO cerramos la operacion: apretamos el SL asegurando el 75% de la ganancia y subimos el TP para dejarla correr!
                if is_stoch_overbought:
                    profit_span = cur_price - pos.entry_price
                    tight_sl = round(pos.entry_price + (profit_span * 0.75), 8)
                    if tight_sl > candidate_sl and tight_sl < cur_price * 0.997:
                        candidate_sl = tight_sl
                        reasons_list.append(f"Estocastico en {snap.stoch_k if snap else 80} (dejar correr asegurando 75%)")
                    if candidate_tp <= cur_price * 1.02:
                        candidate_tp = round(cur_price * 1.04, 8)
                        reasons_list.append("Expansion TP +4%")

                # 3e. Si el precio alcanza o supera el Take-Profit actual (o esta a menos de 0.5% de tocarlo):
                #     En vez de cerrar y limitar la subida, subimos el SL asegurando el 80% de la ganancia y expandimos el TP!
                if old_tp > 0 and cur_price >= (old_tp * 0.995):
                    profit_span = cur_price - pos.entry_price
                    tp_lock_sl = round(pos.entry_price + (profit_span * 0.80), 8)
                    if tp_lock_sl > candidate_sl and tp_lock_sl < cur_price * 0.997:
                        candidate_sl = tp_lock_sl
                    step_pct = max(0.035, (snap.atr_pct * 2.0 / 100.0) if snap else 0.035)
                    candidate_tp = round(cur_price * (1.0 + step_pct), 8)
                    reasons_list.append(f"Meta TP alcanzada -> dejando correr con nuevo TP (+{step_pct * 100:.1f}%) y SL en ganancia")

                sl_changed = candidate_sl > old_sl * 1.0005
                tp_changed = candidate_tp > old_tp * 1.001

                if sl_changed or tp_changed:
                    pos.stop_loss_price = candidate_sl if sl_changed else old_sl
                    pos.take_profit_price = candidate_tp if tp_changed else old_tp
                    pos.sl_adjustments_count += 1
                    reason_str = " | ".join(reasons_list) or "Ajuste dinamico en ganancia"
                    pos.last_adjustment_reason = reason_str

                    adj_event = {
                        "timestamp": utc_now_iso(),
                        "symbol": sym,
                        "side": "ADJUST_SL_TP",
                        "mode": "DRY_RUN" if self._effective_dry_run else "LIVE",
                        "price": cur_price,
                        "quote_qty": round(pos.quantity * cur_price, 2),
                        "old_stop_loss": old_sl,
                        "new_stop_loss": pos.stop_loss_price,
                        "old_take_profit": old_tp,
                        "new_take_profit": pos.take_profit_price,
                        "pnl_pct": round(pnl_pct, 2),
                        "locked_profit_pct": round(pos.locked_profit_pct(), 2),
                        "reason": f"Bot Auto-Trail: {reason_str}",
                    }
                    self.state_manager.append_trade(adj_event)
                    actions.append(adj_event)
                    logger.info(
                        "SL/TP MOVIDO EN GANANCIA (%s): SL %s -> %s (Ganancia asegurada %+.2f%%) | TP %s -> %s | %s",
                        sym,
                        old_sl,
                        pos.stop_loss_price,
                        pos.locked_profit_pct(),
                        old_tp,
                        pos.take_profit_price,
                        reason_str,
                    )

        return actions

    def _apply_ai_sl_tp_adjustment(
        self,
        state: BotState,
        decision: AIDecision,
        current_price: float,
    ) -> dict[str, Any] | None:
        """
        Aplica los ajustes de Stop-Loss y Take-Profit sugeridos por Gemini AI para dejar correr ganancias.
        Regla de seguridad (Ratchet): El Stop-Loss NUNCA se baja, solo se sube a favor de la operacion.
        """
        pos = state.positions.get(decision.symbol)
        if not pos or current_price <= 0:
            return None

        old_sl = pos.stop_loss_price
        old_tp = pos.take_profit_price
        new_sl = old_sl
        new_tp = old_tp

        # Solo aceptamos subir el Stop-Loss (y debe estar por debajo del precio actual con un margen minimo de 0.25%)
        if decision.new_stop_loss_price > old_sl * 1.0005 and decision.new_stop_loss_price < current_price * 0.9975:
            new_sl = round(decision.new_stop_loss_price, 8)

        # Aceptamos subir el Take-Profit por encima del precio actual para ampliar el recorrido de ganancias
        if decision.new_take_profit_price > old_tp * 1.001 and decision.new_take_profit_price > current_price * 1.005:
            new_tp = round(decision.new_take_profit_price, 8)

        if new_sl == old_sl and new_tp == old_tp:
            return None

        pos.stop_loss_price = new_sl
        pos.take_profit_price = new_tp
        pos.sl_adjustments_count += 1
        pos.last_adjustment_reason = f"IA ({decision.confidence}%): {decision.reasoning}"
        pnl_pct = pos.unrealized_pnl_pct(current_price)

        record = {
            "timestamp": utc_now_iso(),
            "symbol": decision.symbol,
            "side": "ADJUST_SL_TP",
            "mode": "DRY_RUN" if self._effective_dry_run else "LIVE",
            "price": current_price,
            "quote_qty": round(pos.quantity * current_price, 2),
            "old_stop_loss": old_sl,
            "new_stop_loss": new_sl,
            "old_take_profit": old_tp,
            "new_take_profit": new_tp,
            "pnl_pct": round(pnl_pct, 2),
            "locked_profit_pct": round(pos.locked_profit_pct(), 2),
            "reason": f"IA ADJUST (Confianza {decision.confidence}%): {decision.reasoning}",
        }
        self.state_manager.append_trade(record)
        logger.info(
            "IA MOVIO SL/TP (%s): SL %s -> %s | TP %s -> %s | %s",
            decision.symbol,
            old_sl,
            new_sl,
            old_tp,
            new_tp,
            decision.reasoning,
        )
        return record

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
                dry_run=self._effective_dry_run,
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
                initial_stop_loss_price=sl_price,
            )

            record = {
                "timestamp": utc_now_iso(),
                "symbol": symbol,
                "side": "BUY",
                "mode": "DRY_RUN" if self._effective_dry_run else "LIVE",
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
                dry_run=self._effective_dry_run,
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
                "mode": "DRY_RUN" if self._effective_dry_run else "LIVE",
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
        mode_label = "SIMULACION / CARTERA VIRTUAL" if self._effective_dry_run else "CUENTA REAL (LIVE)"
        lines = [
            "# Reporte Autonomo - Estrategia EMA 200 + Estocastico (80/20) + SL/TP Dinamico (1H)",
            "",
            f"- **Ultima actualizacion (UTC):** `{state.updated_at}`",
            f"- **Ciclo de ejecucion:** `#{state.total_cycles}`",
            f"- **Modo:** `{mode_label}`",
            f"- **Temporalidad:** `{self.config.kline_interval_primary}` | **Riesgo Inicial:** `{self.config.risk_per_trade_pct * 100:.1f}% (min ${self.config.min_risk_usd:.2f} USD)`",
            f"- **Capital Total Estimado:** `{total_equity:.2f} {self.config.quote_asset}`",
            f"- **Liquidez Disponible:** `{usdt_free:.2f} {self.config.quote_asset}`",
            f"- **Rendimiento Diario (UTC):** `{daily_pnl_pct:+.2f}%`",
            f"- **Regimen de Mercado (Gemini 3.8 Flash):** `{ai_result.market_regime}`",
            "",
            "## Lectura de Mercado de Gemini AI",
            f"> {ai_result.summary}",
            "",
            "## Posiciones Abiertas (Con Stop-Loss y Take-Profit Dinamicos)",
        ]

        if not state.positions:
            lines.append("_No hay posiciones abiertas en este momento._")
        else:
            lines.extend(
                [
                    "| Par | Entrada | Precio Actual | PnL Actual | SL Inicial | SL Actual (Dinamico) | Ganancia Asegurada | TP Actual (Dinamico) | Ajustes |",
                    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
                ]
            )
            for sym, pos in state.positions.items():
                cur = all_prices.get(sym, pos.entry_price)
                pnl = pos.unrealized_pnl_pct(cur)
                locked = pos.locked_profit_pct()
                lines.append(
                    f"| `{sym}` | {pos.entry_price} | {cur} | **{pnl:+.2f}%** | {pos.initial_stop_loss_price} | **{pos.stop_loss_price}** | `{locked:+.2f}%` | **{pos.take_profit_price}** | {pos.sl_adjustments_count} |"
                )

        lines.extend(["", "## Operaciones y Ajustes de SL/TP en este Ciclo"])
        if not executed_actions:
            lines.append("_Ninguna orden o ajuste ejecutado en este ciclo._")
        else:
            for act in executed_actions:
                if act["side"] == "ADJUST_SL_TP":
                    lines.append(
                        f"- **AJUSTE DINAMICO SL/TP `{act['symbol']}`** (PnL `{act['pnl_pct']:+.2f}%`) | "
                        f"SL: `{act['old_stop_loss']}` → **`{act['new_stop_loss']}`** (Asegurado: `{act['locked_profit_pct']:+.2f}%`) | "
                        f"TP: `{act['old_take_profit']}` → **`{act['new_take_profit']}`** — _{act['reason']}_"
                    )
                else:
                    pnl_str = f" | PnL: `{act['pnl_pct']:+.2f}%`" if "pnl_pct" in act else ""
                    lines.append(
                        f"- **{act['side']} `{act['symbol']}`** @ `{act['price']}` ({act['quote_qty']} USDT){pnl_str} — _{act['reason']}_"
                    )

        lines.extend(
            [
                "",
                "## Escaneo Cuantitativo 1H (3 Pilares Optimizados 6M: EMA 200 Pullback + Capitulacion Extrema + Divergencia Spring)",
                "| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |",
                "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
            ]
        )
        dec_map = {d.symbol: d for d in ai_result.decisions}
        for s in snapshots:
            d = dec_map.get(s.symbol)
            act = f"**{d.action}** ({d.confidence}%)" if d else "HOLD"
            ema_pos = f"`{s.dist_to_ema200_pct:+.2f}%`"
            sl_ref = s.structural_sl_price if s.structural_sl_price > 0 else s.prev_candle_low
            pillar_str = s.entry_pillar if s.entry_pillar != "NONE" else s.strategy_setup
            lines.append(
                f"| `{s.symbol}` | {s.current_price} | {s.ema_200} | {ema_pos} | `{s.stoch_k}` / `{s.stoch_d}` | `{s.rsi_14}` | `{s.bb_pct_b}` | `{s.candle_pattern}` | {sl_ref} | `{pillar_str}` | {act} |"
            )

        return "\n".join(lines) + "\n"
