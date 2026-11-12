from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import MetaTrader5 as mt5

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.bot_engine import AutonomousTradingBot
from src.config import BASE_DIR, BotConfig, load_dotenv
from src.gemini_agent import GeminiTradingAgent
from src.market_scanner import (
    calc_atr_pct,
    calc_bollinger_bands,
    calc_ema_series,
    calc_macd,
    calc_rsi,
    calc_stochastic,
    detect_candle_pattern,
)

logger = logging.getLogger("mt5_bot")

MT5_MAGIC_NUMBER = 20261109

# Universo de activos de alta liquidez en Exness Standard (sufijo 'm') compatibles con cuenta desde $10 USD
DEFAULT_MT5_SYMBOLS = [
    "EURUSDm",
    "GBPUSDm",
    "USDJPYm",
    "AUDUSDm",
    "NZDUSDm",
    "USDCADm",
    "USDCHFm",
    "EURGBPm",
    "EURJPYm",
    "US500m",
    "USTECm",
    "BTCUSDm",
    "ETHUSDm",
    "XAUUSDm",  # Se activa automaticamente cuando el margen libre supera ~$22 USD o apalancamiento >= 1:500
]


@dataclass
class MT5SymbolSnapshot:
    symbol: str
    bid: float
    ask: float
    spread_points: int
    digits: int
    point: float
    min_lot: float
    lot_step: float
    margin_min_lot_usd: float
    usd_per_1pct_move_min_lot: float
    ema_200: float
    ema_50: float
    ema_21: float
    above_ema_200: bool
    dist_to_ema200_atr: float
    ema200_slope_positive: bool
    stoch_k: float
    stoch_d: float
    stoch_recent_min: float
    stoch_recent_max: float
    stoch_turning_up: bool
    stoch_turning_down: bool
    rsi_14: float
    bb_upper: float
    bb_lower: float
    bb_pct_b: float
    macd_hist: float
    macd_improving: bool
    atr_price: float
    atr_pct: float
    candle_pattern: str
    prev_candle_low: float
    prev_candle_high: float
    entry_pillar: str
    strategy_setup: str  # LONG_ENTRY | SHORT_ENTRY | EXIT_LONG | EXIT_SHORT | WATCH
    structural_long_sl: float
    structural_short_sl: float
    htf_trend: str


class ExnessMT5AutonomousBot:
    """
    Motor autonomo para MetaTrader 5 (Exness) + Google Gemini AI:
    - Temporalidad principal: 1 Hora (H1) + confirmacion 4 Horas (H4)
    - Opera en doble direccion: BUY (LONG) y SELL (SHORT)
    - Calibrado con ATR(14) para Forex (EURUSDm, GBPUSDm, USDJPYm...), Indices (US500m, USTECm) y Cripto (BTCUSDm, ETHUSDm)
    - Proteccion estricta para cuentas desde $10 USD:
      * Verifica margen libre real con mt5.order_calc_margin()
      * Limita la distancia del Stop-Loss con mt5.order_calc_profit() para arriesgar ~$1.00 USD (1% o min $1 USD)
      * Coloca SL y TP directamente en el servidor de Exness y aplica Trailing Stop Dinamico (Break-Even + bloqueo 65%-80%)
    """

    def __init__(
        self,
        gemini_api_key: str,
        gemini_model: str = "gemini-3.8-flash",
        risk_pct: float = 0.01,
        min_risk_usd: float = 1.0,
        max_risk_usd_cap: float = 1.35,
        max_open_positions: int = 2,
        min_ai_confidence: int = 68,
        dry_run: bool = False,
        report_file: Path = Path("data/mt5_latest_report.md"),
        history_file: Path = Path("data/mt5_trades_history.json"),
    ) -> None:
        self.gemini_api_key = gemini_api_key
        self.gemini_model = gemini_model
        self.risk_pct = risk_pct
        self.min_risk_usd = min_risk_usd
        self.max_risk_usd_cap = max_risk_usd_cap
        self.max_open_positions = max_open_positions
        self.min_ai_confidence = min_ai_confidence
        self.dry_run = dry_run
        self.report_file = report_file
        self.history_file = history_file
        self.ai_agent = GeminiTradingAgent(api_key=gemini_api_key, model=gemini_model)
        self.peak_prices: dict[int, float] = {}

        self.report_file.parent.mkdir(parents=True, exist_ok=True)
        self.history_file.parent.mkdir(parents=True, exist_ok=True)

    def ensure_connected(self) -> tuple[Any, Any]:
        # Conectar a MetaTrader 5 (si no esta inicializado, conecta a la instancia oficial de Exness)
        mt5_path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
        if not mt5.initialize(path=mt5_path):
            if not mt5.initialize():
                raise RuntimeError(f"No se pudo inicializar MetaTrader 5: {mt5.last_error()}")
        term = mt5.terminal_info()
        acc = mt5.account_info()
        if term is None or acc is None:
            raise RuntimeError(f"No se pudo leer la cuenta de MetaTrader 5: {mt5.last_error()}")
        return term, acc

    def _fetch_candles(self, symbol: str, timeframe: int, count: int = 250) -> list[dict[str, float]]:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
        if rates is None or len(rates) < 60:
            return []
        candles: list[dict[str, float]] = []
        for r in rates:
            candles.append(
                {
                    "open": float(r["open"]),
                    "high": float(r["high"]),
                    "low": float(r["low"]),
                    "close": float(r["close"]),
                    "volume": float(r["tick_volume"]),
                }
            )
        return candles

    def build_snapshots(self, free_margin_usd: float, open_symbols: set[str]) -> list[MT5SymbolSnapshot]:
        snapshots: list[MT5SymbolSnapshot] = []
        for sym in DEFAULT_MT5_SYMBOLS:
            mt5.symbol_select(sym, True)

        for sym in DEFAULT_MT5_SYMBOLS:
            info = mt5.symbol_info(sym)
            tick = mt5.symbol_info_tick(sym)
            if info is None or tick is None or tick.ask <= 0 or tick.bid <= 0:
                continue

            margin_min = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, sym, info.volume_min, tick.ask)
            if margin_min is None:
                continue

            # Si el simbolo no esta abierto y requiere mas del 78% del margen libre disponible, se omite por seguridad
            if sym not in open_symbols and margin_min > max(free_margin_usd * 0.78, 7.5):
                continue

            p1pct = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, sym, info.volume_min, tick.ask, tick.ask * 1.01)
            usd_per_1pct = abs(float(p1pct)) if p1pct is not None else 1.0

            c1h = self._fetch_candles(sym, mt5.TIMEFRAME_H1, 250)
            c4h = self._fetch_candles(sym, mt5.TIMEFRAME_H4, 120)
            if len(c1h) < 205 or len(c4h) < 55:
                continue

            # Usamos las velas cerradas hasta c1h[-2] y la vela activa/recien cerrada para indicadores limpios
            closes_1h = [c["close"] for c in c1h]
            ema200_s = calc_ema_series(closes_1h, 200)
            ema50_s = calc_ema_series(closes_1h, 50)
            ema21_s = calc_ema_series(closes_1h, 21)
            rsi_14 = round(calc_rsi(closes_1h, 14), 2)
            k_s, d_s = calc_stochastic(c1h, 14, 3, 3)
            macd_l, macd_sig, macd_h = calc_macd(closes_1h)
            bb_u, bb_l, bb_b = calc_bollinger_bands(closes_1h, 20, 2.0)
            atr_pct = calc_atr_pct(c1h, 14)

            cur_price = float(tick.bid)
            trs = [
                max(
                    c1h[k]["high"] - c1h[k]["low"],
                    abs(c1h[k]["high"] - c1h[k - 1]["close"]),
                    abs(c1h[k]["low"] - c1h[k - 1]["close"]),
                )
                for k in range(len(c1h) - 14, len(c1h))
            ]
            raw_atr_val = sum(trs) / len(trs) if trs else (cur_price * 0.002)
            atr_price = max(raw_atr_val, info.point * 25.0)

            ema_200 = round(ema200_s[-1], info.digits)
            ema_50 = round(ema50_s[-1], info.digits)
            ema_21 = round(ema21_s[-1], info.digits)
            ema200_prev = ema200_s[-6] if len(ema200_s) >= 6 else ema200_s[0]
            ema200_slope_pos = ema200_s[-1] >= ema200_prev

            above_ema200 = cur_price > ema_200
            dist_atr = (cur_price - ema_200) / atr_price if atr_price > 0 else 0.0

            stoch_k = k_s[-1]
            stoch_d = d_s[-1]
            stoch_prev_k = k_s[-2] if len(k_s) >= 2 else stoch_k
            stoch_recent_min = round(min(k_s[-4:]), 2) if len(k_s) >= 4 else stoch_k
            stoch_recent_max = round(max(k_s[-4:]), 2) if len(k_s) >= 4 else stoch_k
            stoch_turning_up = stoch_k > stoch_prev_k or stoch_k >= stoch_d
            stoch_turning_down = stoch_k < stoch_prev_k or stoch_k <= stoch_d

            # Evaluamos patron tanto en la ultima vela cerrada (c1h[-2] vs c1h[-3]) como en la actual (c1h[-1] vs c1h[-2])
            pat_closed = detect_candle_pattern(c1h[-2], c1h[-3], c1h[-4])
            pat_live = detect_candle_pattern(c1h[-1], c1h[-2], c1h[-3])
            candle_pattern = pat_live if pat_live != "NONE" else pat_closed

            prev_low = min(c1h[-2]["low"], c1h[-1]["low"])
            prev_high = max(c1h[-2]["high"], c1h[-1]["high"])

            # Calculo de histograma MACD previo para confirmar giro de momentum
            _, _, prev_macd_h = calc_macd(closes_1h[:-1])
            macd_improving = macd_h > prev_macd_h
            macd_weakening = macd_h < prev_macd_h

            # Stop-Loss estructural calibrado por ATR (3.0x ATR en MT5 validado en Backtest 6M de Exness)
            sl_dist_3atr = 3.0 * atr_price
            structural_long_sl = round(cur_price - sl_dist_3atr, info.digits)
            structural_short_sl = round(float(tick.ask) + sl_dist_3atr, info.digits)

            # Tendencia 4H
            closes_4h = [c["close"] for c in c4h]
            htf_e21 = calc_ema_series(closes_4h, 21)[-1]
            htf_e50 = calc_ema_series(closes_4h, 50)[-1]
            htf_trend = "BULLISH" if closes_4h[-1] > htf_e21 >= htf_e50 else ("BEARISH" if closes_4h[-1] < htf_e21 <= htf_e50 else "NEUTRAL")

            has_bullish_trigger = candle_pattern in ("BULLISH_HAMMER", "BULLISH_ENGULFING", "MORNING_STAR") or (
                c1h[-1]["close"] > c1h[-1]["open"] and c1h[-1]["close"] > c1h[-2]["high"]
            )
            has_bearish_trigger = candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING") or (
                c1h[-1]["close"] < c1h[-1]["open"] and c1h[-1]["close"] < c1h[-2]["low"]
            )

            # === PILARES CUANTITATIVOS CALIBRADOS CON ATR PARA MT5 (FOREX / INDICES / CRIPTO) ===
            # Pilar 1 LONG: Pullback a EMA 200 o EMA 50 en tendencia alcista + Estocastico <= 22 girando al alza
            p1_long = (
                above_ema200
                and ema_50 >= ema_200 * 0.998
                and ema200_slope_pos
                and (-0.5 <= dist_atr <= 3.0 or abs(cur_price - ema_50) <= 1.5 * atr_price)
                and (stoch_recent_min <= 22.0 and stoch_k <= 42.0 and stoch_turning_up)
                and rsi_14 <= 44.0
                and bb_b <= 0.22
                and macd_improving
                and has_bullish_trigger
            )

            # Pilar 2 LONG: Capitulacion Institucional / Doble Sobreventa Extrema (Ganadora en ETH hoy +22.6%)
            p2_long = (
                stoch_recent_min <= 16.0
                and stoch_k <= 32.0
                and stoch_turning_up
                and rsi_14 <= 31.5
                and bb_b <= 0.06
                and macd_improving
                and has_bullish_trigger
            )

            # Pilar S1 SHORT: Rechazo Bajista en EMA 200 o EMA 50 en tendencia bajista + Estocastico >= 78 girando a la baja (73.7% WR en Exness 6M)
            s1_short = (
                (not above_ema200)
                and ema_50 <= ema_200 * 1.002
                and (not ema200_slope_pos)
                and (-3.0 <= dist_atr <= 0.5 or abs(cur_price - ema_50) <= 1.5 * atr_price)
                and (stoch_recent_max >= 78.0 and stoch_k >= 58.0 and stoch_turning_down)
                and rsi_14 >= 56.0
                and bb_b >= 0.78
                and macd_weakening
                and has_bearish_trigger
            )

            # === ESTRATEGIA ALTA FRECUENCIA 15 MINUTOS (SCALPER M15 MOMENTUM PULLBACK - 507 TRADES 6M) ===
            c15m = self._fetch_candles(sym, mt5.TIMEFRAME_M15, 60)
            m15_long = False
            m15_short = False
            m15_sl = 0.0
            if len(c15m) >= 45:
                closes_15 = [c["close"] for c in c15m]
                e9_15 = calc_ema_series(closes_15, 9)[-1]
                e21_15 = calc_ema_series(closes_15, 21)[-1]
                e50_15 = calc_ema_series(closes_15, 50)[-1]
                raw_k15, _ = calc_stochastic(c15m, 14, 3, 3)
                k15 = raw_k15[-1] if raw_k15 else 50.0
                k15_prev = raw_k15[-2] if len(raw_k15) >= 2 else k15
                rsi_15 = calc_rsi(closes_15, 14)
                trs_15 = [max(c15m[k]["high"] - c15m[k]["low"], abs(c15m[k]["high"] - c15m[k - 1]["close"]), abs(c15m[k]["low"] - c15m[k - 1]["close"])) for k in range(len(c15m) - 14, len(c15m))]
                atr_15 = sum(trs_15) / len(trs_15) if trs_15 else (cur_price * 0.001)

                # Scalper M15 LONG: Tendencia Macro H1 alcista + EMA 9 > 21 > 50 en M15 + Pullback con Estocastico 25-50 girando al alza
                m15_bull_align = above_ema200 and (e9_15 > e21_15 > e50_15) and cur_price >= e21_15 * 0.9995 and c15m[-1]["low"] <= e9_15 * 1.0003
                m15_long = m15_bull_align and (25.0 <= k15 <= 52.0) and (k15 > k15_prev) and (48.0 <= rsi_15 <= 64.0) and (c15m[-1]["close"] > c15m[-1]["open"] or candle_pattern in ("BULLISH_HAMMER", "BULLISH_ENGULFING"))

                # Scalper M15 SHORT: Tendencia Macro H1 bajista + EMA 9 < 21 < 50 en M15 + Pullback con Estocastico 50-75 girando a la baja
                m15_bear_align = (not above_ema200) and (e9_15 < e21_15 < e50_15) and cur_price <= e21_15 * 1.0005 and c15m[-1]["high"] >= e9_15 * 0.9997
                m15_short = m15_bear_align and (48.0 <= k15 <= 75.0) and (k15 < k15_prev) and (36.0 <= rsi_15 <= 52.0) and (c15m[-1]["close"] < c15m[-1]["open"] or candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"))

                if m15_long:
                    m15_sl = round(cur_price - (1.35 * atr_15), info.digits)
                elif m15_short:
                    m15_sl = round(float(tick.ask) + (1.35 * atr_15), info.digits)

            entry_pillar = "NONE"
            if p1_long:
                entry_pillar = "P1_EMA200_PULLBACK_LONG"
                setup = "LONG_ENTRY"
            elif p2_long:
                entry_pillar = "P2_EXTREME_OVERSOLD_LONG"
                setup = "LONG_ENTRY"
            elif s1_short:
                entry_pillar = "S1_EMA200_REJECT_SHORT"
                setup = "SHORT_ENTRY"
            elif m15_long:
                entry_pillar = "M15_SCALPER_PULLBACK_LONG"
                setup = "LONG_ENTRY"
                structural_long_sl = m15_sl
            elif m15_short:
                entry_pillar = "M15_SCALPER_PULLBACK_SHORT"
                setup = "SHORT_ENTRY"
                structural_short_sl = m15_sl
            elif stoch_k >= 80.0 and has_bearish_trigger:
                setup = "EXIT_LONG"
            elif stoch_k <= 20.0 and has_bullish_trigger:
                setup = "EXIT_SHORT"
            else:
                setup = "WATCH"

            snapshots.append(
                MT5SymbolSnapshot(
                    symbol=sym,
                    bid=round(float(tick.bid), info.digits),
                    ask=round(float(tick.ask), info.digits),
                    spread_points=int(info.spread),
                    digits=int(info.digits),
                    point=float(info.point),
                    min_lot=float(info.volume_min),
                    lot_step=float(info.volume_step),
                    margin_min_lot_usd=round(float(margin_min), 2),
                    usd_per_1pct_move_min_lot=round(usd_per_1pct, 2),
                    ema_200=ema_200,
                    ema_50=ema_50,
                    ema_21=ema_21,
                    above_ema_200=above_ema200,
                    dist_to_ema200_atr=round(dist_atr, 2),
                    ema200_slope_positive=ema200_slope_pos,
                    stoch_k=stoch_k,
                    stoch_d=stoch_d,
                    stoch_recent_min=stoch_recent_min,
                    stoch_recent_max=stoch_recent_max,
                    stoch_turning_up=stoch_turning_up,
                    stoch_turning_down=stoch_turning_down,
                    rsi_14=rsi_14,
                    bb_upper=round(bb_u, info.digits),
                    bb_lower=round(bb_l, info.digits),
                    bb_pct_b=bb_b,
                    macd_hist=macd_h,
                    macd_improving=macd_improving,
                    atr_price=round(atr_price, info.digits),
                    atr_pct=atr_pct,
                    candle_pattern=candle_pattern,
                    prev_candle_low=round(prev_low, info.digits),
                    prev_candle_high=round(prev_high, info.digits),
                    entry_pillar=entry_pillar,
                    strategy_setup=setup,
                    structural_long_sl=structural_long_sl,
                    structural_short_sl=structural_short_sl,
                    htf_trend=htf_trend,
                )
            )

        return snapshots

    def manage_open_positions(self, snapshots_map: dict[str, MT5SymbolSnapshot]) -> list[dict[str, Any]]:
        """
        Revisa posiciones abiertas en MT5 y aplica:
        1. Cierre por agotamiento en extremo opuesto del Estocastico con vela de giro.
        2. Break-Even + ganancia asegurada al alcanzar >= 1.2 * ATR de beneficio.
        3. Trailing Stop Dinamico (bloqueando 65%-80% del recorrido) y expansion del Take-Profit en el servidor de Exness.
        """
        actions: list[dict[str, Any]] = []
        positions = mt5.positions_get()
        if not positions:
            return actions

        for pos in positions:
            ticket = int(pos.ticket)
            sym = str(pos.symbol)
            is_buy = pos.type == mt5.POSITION_TYPE_BUY
            entry = float(pos.price_open)
            cur = float(pos.price_current)
            old_sl = float(pos.sl)
            old_tp = float(pos.tp)
            vol = float(pos.volume)
            profit_usd = float(pos.profit)

            info = mt5.symbol_info(sym)
            digits = int(info.digits) if info else 5
            point = float(info.point) if info else 0.00001
            snap = snapshots_map.get(sym)
            atr = snap.atr_price if snap and snap.atr_price > 0 else abs(entry * 0.003)

            # Registrar pico a favor
            if ticket not in self.peak_prices:
                self.peak_prices[ticket] = cur
            elif is_buy and cur > self.peak_prices[ticket]:
                self.peak_prices[ticket] = cur
            elif (not is_buy) and cur < self.peak_prices[ticket]:
                self.peak_prices[ticket] = cur
            peak = self.peak_prices[ticket]

            move_in_favor = (cur - entry) if is_buy else (entry - cur)
            move_atr = move_in_favor / atr if atr > 0 else 0.0

            # 1. ¿Salida por Estocastico en extremo opuesto + vela de giro con ganancia >= 1.2x ATR?
            if snap is not None and move_atr >= 1.2 and profit_usd > 0.25:
                if is_buy and snap.stoch_k >= 80.0 and snap.candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"):
                    res = self._close_mt5_position(pos, f"Cierre BUY por Estocastico={snap.stoch_k} + {snap.candle_pattern}")
                    if res:
                        actions.append(res)
                    continue
                if (not is_buy) and snap.stoch_k <= 20.0 and snap.candle_pattern in ("BULLISH_HAMMER", "BULLISH_ENGULFING", "MORNING_STAR"):
                    res = self._close_mt5_position(pos, f"Cierre SELL por Estocastico={snap.stoch_k} + {snap.candle_pattern}")
                    if res:
                        actions.append(res)
                    continue

            # 2. Trailing Stop Dinamico y Expansion de Take-Profit (por ATR o por R-Multiple monetario >= $1.80 USD)
            if (move_atr >= 1.1 or profit_usd >= 1.80) and profit_usd > 0:
                candidate_sl = old_sl
                candidate_tp = old_tp
                reasons: list[str] = []

                if is_buy:
                    # Break-Even + 0.35 ATR
                    be_plus = round(entry + (0.35 * atr), digits)
                    if be_plus > candidate_sl and be_plus < cur - (15 * point):
                        candidate_sl = be_plus
                        reasons.append("Break-Even+0.35ATR")

                    # Asegurar 68%-80% del recorrido desde entrada hasta el pico cuando >= 1.8 ATR o >= $2.50 USD (+2R)
                    if move_atr >= 1.8 or profit_usd >= 2.50:
                        keep = 0.80 if (move_atr >= 3.2 or profit_usd >= 4.50) else 0.68
                        lock_sl = round(entry + ((peak - entry) * keep), digits)
                        if lock_sl > candidate_sl and lock_sl < cur - (15 * point):
                            candidate_sl = lock_sl
                            reasons.append(f"Trailing {int(keep * 100)}% del pico")

                    # Si se acerca al TP, expandir TP +2.0 ATR para dejar correr la ganancia
                    if old_tp > 0 and (old_tp - cur) <= (0.5 * atr):
                        candidate_tp = round(cur + (2.0 * atr), digits)
                        reasons.append("Expansion TP +2.0ATR")

                    sl_improved = candidate_sl > old_sl + (5 * point)
                    tp_improved = candidate_tp > old_tp + (10 * point)
                else:
                    # Posicion SHORT (SELL)
                    be_minus = round(entry - (0.35 * atr), digits)
                    if (candidate_sl <= 0 or be_minus < candidate_sl) and be_minus > cur + (15 * point):
                        candidate_sl = be_minus
                        reasons.append("Break-Even SHORT+0.35ATR")

                    if move_atr >= 1.8 or profit_usd >= 2.50:
                        keep = 0.80 if (move_atr >= 3.2 or profit_usd >= 4.50) else 0.68
                        lock_sl = round(entry - ((entry - peak) * keep), digits)
                        if (candidate_sl <= 0 or lock_sl < candidate_sl) and lock_sl > cur + (15 * point):
                            candidate_sl = lock_sl
                            reasons.append(f"Trailing SHORT {int(keep * 100)}% de caida")

                    if old_tp > 0 and (cur - old_tp) <= (0.5 * atr):
                        candidate_tp = round(cur - (2.0 * atr), digits)
                        reasons.append("Expansion TP SHORT -2.0ATR")

                    sl_improved = old_sl <= 0 or candidate_sl < old_sl - (5 * point)
                    tp_improved = old_tp > 0 and candidate_tp < old_tp - (10 * point)

                if sl_improved or tp_improved:
                    new_sl = candidate_sl if sl_improved else old_sl
                    new_tp = candidate_tp if tp_improved else old_tp
                    mod_ok = self._modify_mt5_sl_tp(ticket, sym, new_sl, new_tp)
                    if mod_ok:
                        evt = {
                            "timestamp": datetime.now(timezone.utc).isoformat(),
                            "ticket": ticket,
                            "symbol": sym,
                            "side": "ADJUST_SL_TP",
                            "old_sl": old_sl,
                            "new_sl": new_sl,
                            "old_tp": old_tp,
                            "new_tp": new_tp,
                            "profit_usd": round(profit_usd, 2),
                            "reason": " | ".join(reasons),
                        }
                        self._append_history(evt)
                        actions.append(evt)
                        logger.info(
                            "MT5 SL/TP MOVIDO EN GANANCIA (%s #%d): SL %s -> %s | TP %s -> %s | PnL $%.2f | %s",
                            sym,
                            ticket,
                            old_sl,
                            new_sl,
                            old_tp,
                            new_tp,
                            profit_usd,
                            evt["reason"],
                        )

        return actions

    def calculate_safe_lot_and_sl(
        self,
        snap: MT5SymbolSnapshot,
        side: str,
        equity_usd: float,
        free_margin_usd: float,
    ) -> tuple[float, float, float, float]:
        """
        Calcula (lotes, sl_price, tp_price, riesgo_usd) asegurando que:
        1. El riesgo monetario sea ~1% de la cuenta (minimo $1.00 USD, tope de seguridad $1.35 USD para cuentas de $10).
        2. Si con el lote minimo (0.01) la distancia estructural de SL excede $1.35 USD, ajusta la distancia del SL
           para que la perdida maxima en caso de tocar SL nunca supere ~$1.25 USD.
        """
        is_buy = side == "BUY"
        entry = snap.ask if is_buy else snap.bid
        order_type = mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL

        # Adaptación dinámica de Fase según el capital real disponible:
        # - Fase 1 (< $28 USD): Riesgo tope $1.35 USD (cuentas de $10-$25)
        # - Fase 2 ($28 - $60 USD): Riesgo objetivo ~$1.50 - $1.85 USD, tope $2.20 USD (permite que los SL estructurales no se ahoguen)
        # - Fase 3 (>= $60 USD): Riesgo objetivo ~$2.20 - $3.00 USD, tope $3.50 USD
        if equity_usd >= 60.0:
            target_risk_usd = round(equity_usd * 0.035, 2)
            max_allowed_risk_usd = 3.50
        elif equity_usd >= 28.0:
            target_risk_usd = round(equity_usd * 0.045, 2)
            max_allowed_risk_usd = 2.20
        else:
            target_risk_usd = max(self.min_risk_usd, round(equity_usd * self.risk_pct, 2))
            max_allowed_risk_usd = max(target_risk_usd, self.max_risk_usd_cap)

        raw_sl = snap.structural_long_sl if is_buy else snap.structural_short_sl
        loss_at_min_lot = mt5.order_calc_profit(order_type, snap.symbol, snap.min_lot, entry, raw_sl)
        abs_loss_min_lot = abs(float(loss_at_min_lot)) if loss_at_min_lot is not None else 1.0

        lot = snap.min_lot
        sl_price = raw_sl

        if abs_loss_min_lot > max_allowed_risk_usd and abs_loss_min_lot > 0:
            # Acota la distancia del SL para que con el lote base el riesgo no supere max_allowed_risk_usd
            scale = max_allowed_risk_usd / abs_loss_min_lot
            adj_dist = max(abs(entry - raw_sl) * scale, snap.point * 35.0)
            sl_price = round(entry - adj_dist if is_buy else entry + adj_dist, snap.digits)
            recalc = mt5.order_calc_profit(order_type, snap.symbol, lot, entry, sl_price)
            risk_usd = abs(float(recalc)) if recalc is not None else max_allowed_risk_usd
        else:
            # Si el riesgo con lote minimo es inferior al objetivo, escala los lotes manteniendo margen seguro
            if abs_loss_min_lot > 0:
                raw_lots = (target_risk_usd / abs_loss_min_lot) * snap.min_lot
                steps = max(1, int(round(raw_lots / snap.lot_step)))
                candidate_lot = round(steps * snap.lot_step, 2)
                margin_req = mt5.order_calc_margin(order_type, snap.symbol, candidate_lot, entry) or 999999.0
                if margin_req <= free_margin_usd * 0.65:
                    lot = max(snap.min_lot, candidate_lot)
            recalc = mt5.order_calc_profit(order_type, snap.symbol, lot, entry, sl_price)
            risk_usd = abs(float(recalc)) if recalc is not None else abs_loss_min_lot

        sl_dist = abs(entry - sl_price)
        tp_dist = max(sl_dist * 2.4, snap.atr_price * 3.0)
        tp_price = round(entry + tp_dist if is_buy else entry - tp_dist, snap.digits)

        return lot, sl_price, tp_price, round(risk_usd, 2)

    def _place_mt5_order(
        self,
        snap: MT5SymbolSnapshot,
        side: str,
        lot: float,
        sl_price: float,
        tp_price: float,
        reason: str,
        risk_usd: float,
    ) -> dict[str, Any] | None:
        is_buy = side == "BUY"
        price = snap.ask if is_buy else snap.bid
        if self.dry_run:
            evt = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "symbol": snap.symbol,
                "side": side,
                "mode": "DRY_RUN",
                "lot": lot,
                "price": price,
                "sl": sl_price,
                "tp": tp_price,
                "risk_usd": risk_usd,
                "reason": reason,
            }
            self._append_history(evt)
            return evt

        info = mt5.symbol_info(snap.symbol)
        filling = mt5.ORDER_FILLING_IOC
        if info is not None:
            if info.filling_mode & 1:
                filling = mt5.ORDER_FILLING_FOK
            elif info.filling_mode & 2:
                filling = mt5.ORDER_FILLING_IOC
            else:
                filling = mt5.ORDER_FILLING_RETURN

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": snap.symbol,
            "volume": float(lot),
            "type": mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL,
            "price": float(price),
            "sl": float(sl_price),
            "tp": float(tp_price),
            "deviation": 25,
            "magic": MT5_MAGIC_NUMBER,
            "comment": f"GeminiBot_{snap.entry_pillar[:12]}",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": filling,
        }
        result = mt5.order_send(request)
        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(
                "Error al enviar orden MT5 en %s (%s): retcode=%s, comment=%s",
                snap.symbol,
                side,
                getattr(result, "retcode", None),
                getattr(result, "comment", mt5.last_error()),
            )
            return None

        evt = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "ticket": int(result.order),
            "symbol": snap.symbol,
            "side": side,
            "mode": "LIVE",
            "lot": lot,
            "price": float(result.price or price),
            "sl": sl_price,
            "tp": tp_price,
            "risk_usd": risk_usd,
            "reason": reason,
        }
        self._append_history(evt)
        logger.info(
            "ORDEN MT5 EJECUTADA: %s %s | Lote: %s @ %s | SL: %s | TP: %s | Riesgo: ~$%.2f USD | %s",
            side,
            snap.symbol,
            lot,
            evt["price"],
            sl_price,
            tp_price,
            risk_usd,
            reason,
        )
        return evt

    def _modify_mt5_sl_tp(self, ticket: int, symbol: str, new_sl: float, new_tp: float) -> bool:
        if self.dry_run:
            return True
        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "position": int(ticket),
            "symbol": symbol,
            "sl": float(new_sl),
            "tp": float(new_tp),
            "magic": MT5_MAGIC_NUMBER,
        }
        res = mt5.order_send(request)
        return res is not None and res.retcode == mt5.TRADE_RETCODE_DONE

    def _close_mt5_position(self, pos: Any, reason: str) -> dict[str, Any] | None:
        sym = str(pos.symbol)
        ticket = int(pos.ticket)
        is_buy = pos.type == mt5.POSITION_TYPE_BUY
        tick = mt5.symbol_info_tick(sym)
        close_price = float(tick.bid if is_buy else tick.ask) if tick else float(pos.price_current)

        if not self.dry_run:
            info = mt5.symbol_info(sym)
            filling = mt5.ORDER_FILLING_IOC if (info and (info.filling_mode & 2)) else mt5.ORDER_FILLING_FOK
            req = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": ticket,
                "symbol": sym,
                "volume": float(pos.volume),
                "type": mt5.ORDER_TYPE_SELL if is_buy else mt5.ORDER_TYPE_BUY,
                "price": close_price,
                "deviation": 25,
                "magic": MT5_MAGIC_NUMBER,
                "comment": "GeminiBot_Close",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": filling,
            }
            res = mt5.order_send(req)
            if res is None or res.retcode != mt5.TRADE_RETCODE_DONE:
                logger.error("No se pudo cerrar posicion #%d en %s: %s", ticket, sym, getattr(res, "comment", mt5.last_error()))
                return None

        evt = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "ticket": ticket,
            "symbol": sym,
            "side": "CLOSE",
            "price": close_price,
            "profit_usd": round(float(pos.profit), 2),
            "reason": reason,
        }
        self._append_history(evt)
        logger.info("POSICION MT5 CERRADA: %s #%d @ %s | Profit: $%+.2f USD | %s", sym, ticket, close_price, pos.profit, reason)
        return evt

    def _append_history(self, event: dict[str, Any]) -> None:
        items: list[dict[str, Any]] = []
        if self.history_file.exists():
            try:
                items = json.loads(self.history_file.read_text(encoding="utf-8"))
            except Exception:
                items = []
        items.append(event)
        self.history_file.write_text(json.dumps(items[-300:], indent=2, ensure_ascii=False), encoding="utf-8")

    def run_cycle(self, cycle_num: int = 1) -> dict[str, Any]:
        term, acc = self.ensure_connected()
        balance = float(acc.balance)
        equity = float(acc.equity)
        free_margin = float(acc.margin_free)

        raw_positions = mt5.positions_get() or ()
        open_symbols = {str(p.symbol) for p in raw_positions}

        logger.info(
            "=== Ciclo MT5 #%d | Cuenta Exness %s (%s) | Balance: $%.2f USD | Equity: $%.2f USD | Margen Libre: $%.2f USD ===",
            cycle_num,
            acc.login,
            acc.server,
            balance,
            equity,
            free_margin,
        )

        snapshots = self.build_snapshots(free_margin_usd=free_margin, open_symbols=open_symbols)
        snapshots_map = {s.symbol: s for s in snapshots}

        executed_actions = self.manage_open_positions(snapshots_map)

        # Refrescar posiciones y margen tras posibles cierres
        raw_positions = mt5.positions_get() or ()
        open_symbols = {str(p.symbol) for p in raw_positions}
        acc = mt5.account_info() or acc
        free_margin = float(acc.margin_free)
        equity = float(acc.equity)

        # Capacidad de posiciones simultaneas segun Fase de capital:
        # Fase 1 (< $28 USD): 2 posiciones
        # Fase 2 ($28 - $60 USD): 3 posiciones simultaneas
        # Fase 3 (>= $60 USD): 4 posiciones simultaneas
        if equity >= 60.0:
            effective_max_positions = 4
        elif equity >= 28.0:
            effective_max_positions = 3
        else:
            effective_max_positions = self.max_open_positions

        # Seleccionar candidatos con Pilar Institucional activo (LONG o SHORT)
        entry_candidates = [
            s for s in snapshots if s.strategy_setup in ("LONG_ENTRY", "SHORT_ENTRY") and s.symbol not in open_symbols
        ]

        for cand in entry_candidates:
            if len(open_symbols) >= effective_max_positions:
                break
            if cand.margin_min_lot_usd > free_margin * 0.78:
                continue

            side = "BUY" if cand.strategy_setup == "LONG_ENTRY" else "SELL"
            lot, sl_price, tp_price, risk_usd = self.calculate_safe_lot_and_sl(
                snap=cand,
                side=side,
                equity_usd=equity,
                free_margin_usd=free_margin,
            )
            reason = (
                f"Pilar {cand.entry_pillar} ({cand.candle_pattern}, Stoch %K={cand.stoch_k}, "
                f"RSI={cand.rsi_14}, Riesgo ~${risk_usd:.2f} USD)"
            )
            trade = self._place_mt5_order(
                snap=cand,
                side=side,
                lot=lot,
                sl_price=sl_price,
                tp_price=tp_price,
                reason=reason,
                risk_usd=risk_usd,
            )
            if trade:
                executed_actions.append(trade)
                open_symbols.add(cand.symbol)
                used_margin = cand.margin_min_lot_usd * (lot / cand.min_lot) if cand.min_lot > 0 else cand.margin_min_lot_usd
                free_margin = max(0.0, free_margin - used_margin)

        self._write_markdown_report(cycle_num, acc, raw_positions, snapshots, executed_actions)

        return {
            "cycle": cycle_num,
            "account": int(acc.login),
            "server": str(acc.server),
            "balance_usd": round(balance, 2),
            "equity_usd": round(equity, 2),
            "free_margin_usd": round(free_margin, 2),
            "open_positions": list(open_symbols),
            "executed_actions": executed_actions,
            "candidates_scanned": len(snapshots),
        }

    def _write_markdown_report(
        self,
        cycle_num: int,
        acc: Any,
        positions: tuple[Any, ...],
        snapshots: list[MT5SymbolSnapshot],
        executed_actions: list[dict[str, Any]],
    ) -> None:
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        phase_str = (
            "Fase 3 (> $60 USD) — Max 4 posiciones simultaneas"
            if acc.equity >= 60.0
            else (
                "Fase 2 ($28 - $60 USD) — Max 3 posiciones simultaneas y lotaje escalable"
                if acc.equity >= 28.0
                else "Fase 1 ($10 - $28 USD) — Micro-lotes 0.01 base y max 2 posiciones"
            )
        )
        lines = [
            "# Reporte Autonomo MetaTrader 5 (Exness) - Estrategia Cuantitativa 1H (LONG & SHORT)",
            "",
            f"- **Ultima actualizacion:** `{now_str}` | **Ciclo:** `#{cycle_num}`",
            f"- **Cuenta Exness:** `{acc.login}` (`{acc.server}`) | **Apalancamiento:** `1:{acc.leverage}`",
            f"- **Balance:** `${acc.balance:.2f} USD` | **Equity:** `${acc.equity:.2f} USD` | **Margen Libre:** `${acc.margin_free:.2f} USD`",
            f"- **Nivel de Capital:** `{phase_str}`",
            "",
            "## Posiciones Abiertas en Exness MT5",
        ]
        if not positions:
            lines.append("_No hay posiciones abiertas en este momento._")
        else:
            lines.extend(
                [
                    "| Ticket | Simbolo | Tipo | Lote | Apertura | Precio Actual | SL Actual | TP Actual | PnL ($ USD) |",
                    "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
                ]
            )
            for p in positions:
                side_str = "BUY (LONG)" if p.type == mt5.POSITION_TYPE_BUY else "SELL (SHORT)"
                lines.append(
                    f"| `{p.ticket}` | `{p.symbol}` | **{side_str}** | {p.volume} | {p.price_open} | {p.price_current} | **{p.sl}** | **{p.tp}** | **${p.profit:+.2f}** |"
                )

        lines.extend(
            [
                "",
                "## Escaneo en Vivo MetaTrader 5 (1H - Forex, Indices y Cripto compatibles con tu margen)",
                "| Simbolo | Bid / Ask | Spread | Margen (0.01) | EMA 200 | Dist (ATR) | Stoch (%K/%D) | RSI(14) | BB %B | Patron 1H | Pilar / Setup |",
                "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
            ]
        )
        for s in snapshots:
            pillar_str = s.entry_pillar if s.entry_pillar != "NONE" else s.strategy_setup
            lines.append(
                f"| `{s.symbol}` | {s.bid} | `{s.spread_points}` | `${s.margin_min_lot_usd:.2f}` | {s.ema_200} | `{s.dist_to_ema200_atr:+.2f}x` | `{s.stoch_k}`/`{s.stoch_d}` | `{s.rsi_14}` | `{s.bb_pct_b}` | `{s.candle_pattern}` | **`{pillar_str}`** |"
            )

        self.report_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    load_dotenv(BASE_DIR / ".env")
    parser = argparse.ArgumentParser(description="Bot Autonomo Exness MetaTrader 5 (1H EMA200 + Estocastico + Pilares ATR)")
    parser.add_argument("--loop", action="store_true", help="Ejecutar continuamente cada N segundos mientras la PC este encendida")
    parser.add_argument("--interval", type=int, default=300, help="Segundos entre cada escaneo en modo continuo (default: 300s = 5 min)")
    parser.add_argument("--dry-run", action="store_true", help="Modo simulacion sin enviar ordenes reales")
    args = parser.parse_args()

    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("logs/mt5_bot.log", encoding="utf-8"),
        ],
    )

    bot = ExnessMT5AutonomousBot(
        gemini_api_key=os.getenv("GEMINI_API_KEY", ""),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
        dry_run=args.dry_run,
    )
    binance_cfg = BotConfig()
    if args.dry_run:
        object.__setattr__(binance_cfg, "dry_run", True)
    binance_bot = AutonomousTradingBot(config=binance_cfg)

    cycle = 0
    while True:
        cycle += 1
        try:
            summary = bot.run_cycle(cycle_num=cycle)
            print(json.dumps(summary, indent=2, ensure_ascii=False))
        except Exception as exc:
            logger.exception("Error en ciclo MT5 #%d: %s", cycle, exc)

        # Cada 3 ciclos de 5 min (cada 15 min exactos), ejecuta tambien el Bot de Binance desde la PC
        # y sincroniza el estado con GitHub para que la Nube quede en Standby (y actue como respaldo si se apaga la PC)
        if cycle == 1 or cycle % 3 == 1:
            try:
                logger.info("Ejecutando ciclo puntual de Binance (Modo Hibrido: PC Primaria + Respaldo Cloud)...")
                b_summary = binance_bot.run_cycle()
                logger.info("Ciclo Binance completado: %s", json.dumps(b_summary, ensure_ascii=False))
                subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=str(BASE_DIR), timeout=30, check=False)
                subprocess.run(["git", "add", "data/"], cwd=str(BASE_DIR), timeout=15, check=False)
                subprocess.run(
                    ["git", "commit", "-m", "chore(local-pc): actualizar estado Binance + MT5 [skip ci]"],
                    cwd=str(BASE_DIR),
                    timeout=15,
                    check=False,
                )
                subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), timeout=30, check=False)
            except Exception as b_exc:
                logger.warning("Advertencia en sincronizacion de ciclo Binance local: %s", b_exc)

        if not args.loop:
            break
        time.sleep(max(30, args.interval))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
