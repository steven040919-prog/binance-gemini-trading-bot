from __future__ import annotations

import argparse
import json
import logging
import math
import os
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import MetaTrader5 as mt5

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import BASE_DIR, load_dotenv
from src.gemini_agent import (
    GeminiTradingAgent,
    MT5AICycleEvaluation,
    MT5PositionAIReview,
)
from src.market_scanner import (
    calc_adx,
    calc_atr_pct,
    calc_atr_wilder,
    calc_bollinger_bands,
    calc_ema_series,
    calc_macd,
    calc_rsi,
    calc_stochastic,
    detect_candle_pattern,
)
from src.mt5_adaptive_scheduler import (
    AdaptiveWakeScheduler,
    WakePlan,
    WatchTarget,
    utc_iso,
)
from src.mt5_ai_brain import (
    AdaptiveCycleDecision,
    MT5AdaptiveAIBrain,
    SymbolAdaptiveDecision,
)
from src.mt5_backtester import MT5Backtester, export_strategy_priors
from src.mt5_knowledge_db import MT5KnowledgeDB
from src.mt5_strategies import (
    MT5StrategyEngine,
    RegimeSnapshot,
    StrategySignal,
    classify_session,
)

logger = logging.getLogger("mt5_bot")

MT5_MAGIC_NUMBER = 20261109

# Universo de activos de alta liquidez en Exness Standard (sufijo 'm') para contexto macro 360°
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
    "XAUUSDm",  # Se activa automaticamente cuando el margen libre y el veto de compresion SL lo permiten
]

CRYPTO_SYMBOLS = {"BTCUSDm", "ETHUSDm"}
FOREX_SYMBOLS = {
    "EURUSDm",
    "GBPUSDm",
    "USDJPYm",
    "AUDUSDm",
    "NZDUSDm",
    "USDCADm",
    "USDCHFm",
    "EURGBPm",
    "EURJPYm",
}

# Universo B_FINAL_HYBRID_ADX_0.65PCT validado IS + OOS
H1_EXCLUDED_SYMBOLS = {"ETHUSDm"}
M15_SCALPER_ALLOWED_SYMBOLS = {"US500m", "USTECm", "BTCUSDm", "XAUUSDm"}
M15_SCALPER_EXCLUDED_SYMBOLS = set(DEFAULT_MT5_SYMBOLS) - M15_SCALPER_ALLOWED_SYMBOLS
TWIN_CORRELATION_CLUSTERS = (
    {"US500m", "USTECm"},
    {"BTCUSDm", "ETHUSDm"},
    {"AUDUSDm", "NZDUSDm"},
)

# Escudo 2: Limite maximo de spread permitido para entrar (calibrado IS+OOS)
MAX_ALLOWED_SPREAD_POINTS = {
    "EURUSDm": 16,
    "GBPUSDm": 18,
    "USDJPYm": 18,
    "AUDUSDm": 16,
    "NZDUSDm": 22,
    "USDCADm": 24,
    "USDCHFm": 20,
    "EURGBPm": 22,
    "EURJPYm": 25,
    "US500m": 90,
    "USTECm": 260,
    "BTCUSDm": 1800,
    "ETHUSDm": 180,
    "XAUUSDm": 450,  # Exness cotiza Oro a 3 decimales (spread normal ~240 pts = $0.24); >450 ($0.45) bloquea latigazos de noticias
}


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
    strategy_setup: str  # LONG_ENTRY | SHORT_ENTRY | WATCH
    structural_long_sl: float
    structural_short_sl: float
    htf_trend: str
    adx_14: float = 20.0
    atr_15_price: float = 0.0
    recent_h1_closes: list[float] = field(default_factory=list)
    swing_high_20: float = 0.0
    swing_low_20: float = 0.0


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
        ai_state_file: Path = Path("data/mt5_ai_state.json"),
        adaptive_ai: bool = False,
        base_interval_minutes: int = 30,
        learning_db_path: Path | str = Path("data/mt5_learning.db"),
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
        self.ai_state_file = ai_state_file
        self.adaptive_ai = bool(adaptive_ai)
        self.base_interval_minutes = max(5, int(base_interval_minutes))
        self.learning_db_path = Path(learning_db_path) if str(learning_db_path) != ":memory:" else ":memory:"
        self.ai_agent = GeminiTradingAgent(api_key=gemini_api_key, model=gemini_model)
        self.peak_prices: dict[int, float] = {}
        self.peak_timestamps: dict[int, float] = {}
        self.profit_trail_start_ts: dict[int, float] = {}
        self.position_meta: dict[int, dict[str, Any]] = {}
        self.recent_bot_pos_ids: dict[int, float] = {}
        self.known_bot_pos_ids: set[int] = set()
        self.last_order_timestamp: float = 0.0
        self.symbol_blocked_until: dict[str, dict[str, Any]] = {}
        self.evaluated_deal_tickets: set[int] = set()
        self.recent_ai_close_decisions: list[dict[str, Any]] = []
        self.last_ai_eval: MT5AICycleEvaluation | None = None
        self.last_ai_eval_ts: float = 0.0
        self._last_ai_macro_sig: tuple[Any, ...] | None = None
        self._last_ai_atr_milestones: dict[int, int] = {}
        self._last_ai_sl_danger: dict[int, bool] = {}

        # Componentes del motor adaptativo multi-estrategia (solo activos si adaptive_ai=True)
        self.knowledge_db: MT5KnowledgeDB | None = None
        self.strategy_engine: MT5StrategyEngine | None = None
        self.wake_scheduler: AdaptiveWakeScheduler | None = None
        self.adaptive_brain: MT5AdaptiveAIBrain | None = None

        self.report_file.parent.mkdir(parents=True, exist_ok=True)
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        self.ai_state_file.parent.mkdir(parents=True, exist_ok=True)
        self._load_ai_state()

        if self.adaptive_ai:
            self._init_adaptive_components()

    def _init_adaptive_components(self) -> None:
        if self.knowledge_db is None:
            self.knowledge_db = MT5KnowledgeDB(db_path=self.learning_db_path)
        if self.strategy_engine is None:
            self.strategy_engine = MT5StrategyEngine()
        if self.wake_scheduler is None:
            self.wake_scheduler = AdaptiveWakeScheduler(
                base_interval_minutes=self.base_interval_minutes,
            )
        if self.adaptive_brain is None:
            self.adaptive_brain = MT5AdaptiveAIBrain(
                api_key=self.gemini_api_key,
                model=self.gemini_model,
            )
        # Cargar watches activos persistidos en SQLite al iniciar
        try:
            db_watches = self.knowledge_db.get_active_watches(include_postponed=True)
            if db_watches:
                loaded = self.wake_scheduler.sync_from_db_watches(db_watches)
                logger.info("AdaptiveAI: %d watches activos restaurados desde %s.", loaded, self.learning_db_path)
        except Exception as exc:
            logger.warning("AdaptiveAI: No se pudieron restaurar watches desde DB: %s", exc)

    def seed_historical_priors(
        self,
        years: float = 2.0,
        timeframe_str: str = "H1",
        only_if_empty: bool = False,
        force_synthetic: bool = False,
    ) -> dict[str, Any]:
        """Ejecuta el estudio historico de 2 anos y siembra strategy_priors en MT5KnowledgeDB."""
        self._init_adaptive_components()
        assert self.knowledge_db is not None
        assert self.strategy_engine is not None

        if only_if_empty:
            existing = self.knowledge_db.get_strategy_priors()
            if existing:
                logger.info(
                    "AdaptiveAI: strategy_priors ya poblado (%d registros); se omite re-siembra.",
                    len(existing),
                )
                return {"seeded": False, "reason": "already_populated", "priors_count": len(existing)}

        backtester = MT5Backtester(engine=self.strategy_engine)
        study_result = backtester.run_2yr_study(
            timeframe_str=timeframe_str,
            years=years,
            use_cache=True,
            force_synthetic=force_synthetic,
        )
        exported = export_strategy_priors(study_result)
        priors_list = exported.get("priors", [])
        inserted = self.knowledge_db.upsert_strategy_priors(priors_list)
        logger.info(
            "AdaptiveAI: Siembra historica completada (%s, %.1f anos, %d priors guardados en DB).",
            study_result.get("data_source", "UNKNOWN"),
            years,
            inserted,
        )
        return {
            "seeded": True,
            "data_source": study_result.get("data_source", "UNKNOWN"),
            "priors_count": inserted,
            "enabled_priors": sum(1 for p in priors_list if p.get("enabled")),
        }

    @staticmethod
    def _atomic_write_text(path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = path.with_suffix(path.suffix + f".tmp.{os.getpid()}")
        tmp_path.write_text(content, encoding="utf-8")
        os.replace(tmp_path, path)

    def ensure_connected(self) -> tuple[Any, Any]:
        """Conecta a MetaTrader 5 y verifica conexion real con el servidor del broker (internet activo)."""
        mt5_path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
        term = mt5.terminal_info()
        acc = mt5.account_info()

        # Si no hay sesion IPC activa o el terminal perdio conexion con Exness, reiniciar enlace IPC limpio
        if term is None or acc is None or not getattr(term, "connected", False):
            try:
                mt5.shutdown()
            except Exception:
                pass
            if not mt5.initialize(path=mt5_path):
                if not mt5.initialize():
                    raise ConnectionError(f"No se pudo inicializar MetaTrader 5: {mt5.last_error()}")
            term = mt5.terminal_info()
            acc = mt5.account_info()

        if term is None or acc is None:
            raise ConnectionError(f"No se pudo leer la cuenta de MetaTrader 5: {mt5.last_error()}")
        if not getattr(term, "connected", False):
            raise ConnectionError("MetaTrader 5 sin conexion a internet / servidor Exness (term.connected=False)")
        return term, acc

    def _fetch_candles(self, symbol: str, timeframe: int, count: int = 600) -> list[dict[str, float]]:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
        if rates is None or len(rates) < 55:
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

            c1h = self._fetch_candles(sym, mt5.TIMEFRAME_H1, 600)
            c4h = self._fetch_candles(sym, mt5.TIMEFRAME_H4, 200)
            if len(c1h) < 205 or len(c4h) < 55:
                continue

            # Indicadores 1H y 4H estrictamente sobre velas cerradas ([:-1]) para evitar parpadeo intra-vela (BUG-11)
            c1h_closed = c1h[:-1]
            c4h_closed = c4h[:-1]
            closes_1h = [c["close"] for c in c1h_closed]
            ema200_s = calc_ema_series(closes_1h, 200)
            ema50_s = calc_ema_series(closes_1h, 50)
            ema21_s = calc_ema_series(closes_1h, 21)
            rsi_14 = round(calc_rsi(closes_1h, 14), 2)
            k_s, d_s = calc_stochastic(c1h_closed, 14, 3, 3)
            macd_l, macd_sig, macd_h = calc_macd(closes_1h)
            bb_u, bb_l, bb_b = calc_bollinger_bands(closes_1h, 20, 2.0)

            cur_price = float(tick.bid)
            raw_atr_val = calc_atr_wilder(c1h_closed, 14)
            if raw_atr_val <= 0.0:
                raw_atr_val = cur_price * 0.002
            atr_price = max(raw_atr_val, info.point * 25.0)
            atr_pct = round((atr_price / cur_price) * 100.0, 2) if cur_price > 0 else 0.0
            adx_14 = calc_adx(c1h_closed, 14)

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

            # Patron de vela exclusivamente sobre velas cerradas con rango minimo >= 0.35 * ATR
            min_pat_range = 0.35 * atr_price
            pat_last = detect_candle_pattern(c1h_closed[-1], c1h_closed[-2], c1h_closed[-3], min_range=min_pat_range)
            pat_prev = (
                detect_candle_pattern(c1h_closed[-2], c1h_closed[-3], c1h_closed[-4], min_range=min_pat_range)
                if len(c1h_closed) >= 4
                else "NONE"
            )
            candle_pattern = pat_last if pat_last != "NONE" else pat_prev

            prev_low = min(c1h_closed[-2]["low"], c1h_closed[-1]["low"])
            prev_high = max(c1h_closed[-2]["high"], c1h_closed[-1]["high"])
            recent_h1_closes = [round(c["close"], info.digits) for c in c1h_closed[-5:]]
            swing_window = c1h_closed[-20:]
            swing_high_20 = round(max(c["high"] for c in swing_window), info.digits)
            swing_low_20 = round(min(c["low"] for c in swing_window), info.digits)

            # Calculo de histograma MACD previo sobre velas cerradas
            _, _, prev_macd_h = calc_macd(closes_1h[:-1])
            macd_improving = macd_h > prev_macd_h
            macd_weakening = macd_h < prev_macd_h

            # Stop-Loss estructural calibrado por ATR (3.0x ATR en H1)
            sl_dist_3atr = 3.0 * atr_price
            structural_long_sl = round(cur_price - sl_dist_3atr, info.digits)
            structural_short_sl = round(float(tick.ask) + sl_dist_3atr, info.digits)

            # Tendencia 4H sobre velas cerradas
            closes_4h = [c["close"] for c in c4h_closed]
            htf_e21 = calc_ema_series(closes_4h, 21)[-1]
            htf_e50 = calc_ema_series(closes_4h, 50)[-1]
            htf_trend = (
                "BULLISH"
                if closes_4h[-1] > htf_e21 >= htf_e50
                else ("BEARISH" if closes_4h[-1] < htf_e21 <= htf_e50 else "NEUTRAL")
            )

            # Triggers H1 sin veto de vela contraria (decision NO-GO validada en IS/OOS)
            has_bullish_trigger = candle_pattern in ("BULLISH_HAMMER", "BULLISH_ENGULFING", "MORNING_STAR") or (
                c1h_closed[-1]["close"] > c1h_closed[-1]["open"] and c1h_closed[-1]["close"] > c1h_closed[-2]["high"]
            )
            has_bearish_trigger = candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING") or (
                c1h_closed[-1]["close"] < c1h_closed[-1]["open"] and c1h_closed[-1]["close"] < c1h_closed[-2]["low"]
            )

            # === PILARES CUANTITATIVOS H1 (P1_SAFE_CORE: ADX 18..42, BB 0.30/0.70, RSI 48/52) ===
            h1_allowed = (sym not in H1_EXCLUDED_SYMBOLS) and (18.0 <= adx_14 < 42.0)

            # Pilar 1 LONG: Pullback a EMA 200 (sin bypass via EMA 50, abs(dist_atr) <= 4.8 y 18 <= ADX < 42)
            p1_long = (
                h1_allowed
                and above_ema200
                and ema_50 >= ema_200 * 0.998
                and ema200_slope_pos
                and abs(dist_atr) <= 4.8
                and (-0.5 <= dist_atr <= 3.0)
                and (stoch_recent_min <= 22.0 and stoch_k <= 42.0 and stoch_turning_up)
                and rsi_14 <= 48.0
                and bb_b <= 0.30
                and macd_improving
                and has_bullish_trigger
            )

            # Pilar 2 LONG desactivado permanentemente (validado muerto en auditoria)
            p2_long = False

            # Pilar S1 SHORT: Rechazo Bajista en EMA 200 (sin bypass via EMA 50, abs(dist_atr) <= 4.8 y 18 <= ADX < 42)
            s1_short = (
                h1_allowed
                and (not above_ema200)
                and ema_50 <= ema_200 * 1.002
                and (not ema200_slope_pos)
                and abs(dist_atr) <= 4.8
                and (-3.0 <= dist_atr <= 0.5)
                and (stoch_recent_max >= 78.0 and stoch_k >= 58.0 and stoch_turning_down)
                and rsi_14 >= 52.0
                and bb_b >= 0.70
                and macd_weakening
                and has_bearish_trigger
            )

            # === ESTRATEGIA ALTA FRECUENCIA M15 EXCLUSIVA CORE4 (H1_LOOSE + SL 2.0*ATR_15) ===
            m15_long = False
            m15_short = False
            m15_sl = 0.0
            atr_15_price = 0.0
            c15m = (
                self._fetch_candles(sym, mt5.TIMEFRAME_M15, 250)
                if (sym in M15_SCALPER_ALLOWED_SYMBOLS or sym in open_symbols)
                else []
            )
            if len(c15m) >= 20:
                c15m_closed = c15m[:-1]
                raw_atr_15 = calc_atr_wilder(c15m_closed, 14)
                atr_15_price = max(raw_atr_15 if raw_atr_15 > 0.0 else (cur_price * 0.001), info.point * 10.0)

            if sym in M15_SCALPER_ALLOWED_SYMBOLS and len(c15m) >= 60:
                c15m_closed = c15m[:-1]
                closes_15 = [c["close"] for c in c15m_closed]
                e9_15 = calc_ema_series(closes_15, 9)[-1]
                e21_15 = calc_ema_series(closes_15, 21)[-1]
                e50_15 = calc_ema_series(closes_15, 50)[-1]
                raw_k15, _ = calc_stochastic(c15m_closed, 14, 3, 3)
                k15 = raw_k15[-1] if raw_k15 else 50.0
                k15_prev = raw_k15[-2] if len(raw_k15) >= 2 else k15
                rsi_15 = calc_rsi(closes_15, 14)
                last_c15 = c15m_closed[-1]

                # Solo para Criptos: evitar entrar tras vela M15 ya desplomada/disparada (> 0.75 * ATR_15)
                is_crypto = sym in CRYPTO_SYMBOLS
                crypto_m15_ok = (not is_crypto) or (abs(last_c15["close"] - last_c15["open"]) <= 0.75 * atr_15_price)

                # Scalper M15 LONG (CORE4 + H1_LOOSE: stoch_k < 80 y rsi_14 < 68)
                m15_bull_align = (
                    crypto_m15_ok
                    and above_ema200
                    and (e9_15 > e21_15 > e50_15)
                    and cur_price >= e21_15 * 0.9995
                    and last_c15["low"] <= e9_15 * 1.0003
                )
                m15_long = (
                    m15_bull_align
                    and self._is_m15_scalper_context_allowed(sym, True, dist_atr, htf_trend)
                    and (stoch_k < 80.0 and rsi_14 < 68.0)
                    and (25.0 <= k15 <= 52.0)
                    and (k15 > k15_prev)
                    and (48.0 <= rsi_15 <= 64.0)
                    and (last_c15["close"] > last_c15["open"] or candle_pattern in ("BULLISH_HAMMER", "BULLISH_ENGULFING"))
                )

                # Scalper M15 SHORT (CORE4 + H1_LOOSE: stoch_k > 20 y rsi_14 > 32)
                m15_bear_align = (
                    crypto_m15_ok
                    and (not above_ema200)
                    and (e9_15 < e21_15 < e50_15)
                    and cur_price <= e21_15 * 1.0005
                    and last_c15["high"] >= e9_15 * 0.9997
                )
                m15_short = (
                    m15_bear_align
                    and self._is_m15_scalper_context_allowed(sym, False, dist_atr, htf_trend)
                    and (stoch_k > 20.0 and rsi_14 > 32.0)
                    and (48.0 <= k15 <= 75.0)
                    and (k15 < k15_prev)
                    and (36.0 <= rsi_15 <= 52.0)
                    and (last_c15["close"] < last_c15["open"] or candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"))
                )

                if m15_long:
                    m15_sl = round(cur_price - (2.0 * atr_15_price), info.digits)
                elif m15_short:
                    m15_sl = round(float(tick.ask) + (2.0 * atr_15_price), info.digits)

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
                    adx_14=adx_14,
                    atr_15_price=round(atr_15_price, info.digits),
                    recent_h1_closes=recent_h1_closes,
                    swing_high_20=swing_high_20,
                    swing_low_20=swing_low_20,
                )
            )

        return snapshots

    @staticmethod
    def _is_m15_scalper_context_allowed(
        symbol: str,
        is_long: bool,
        dist_atr: float,
        htf_trend: str,
    ) -> bool:
        """Restringe M15_SCALPER a CORE4 y filtra sobre-extension respecto a EMA 200 1H y tendencia 4H."""
        if symbol not in M15_SCALPER_ALLOWED_SYMBOLS:
            return False
        if is_long:
            return (-0.5 <= dist_atr <= 4.8) and (htf_trend != "BEARISH")
        return (-4.8 <= dist_atr <= 0.5) and (htf_trend != "BULLISH")

    @staticmethod
    def _is_pre_rollover_entry_blackout(now_utc: datetime) -> bool:
        mins = now_utc.hour * 60 + now_utc.minute
        return (20 * 60 + 30) <= mins <= (23 * 60 + 15)

    def _prune_position_meta(self, active_tickets: set[int]) -> bool:
        dirty = False
        now_ts = time.time()
        for t in list(self.position_meta.keys()):
            if t not in active_tickets:
                meta = self.position_meta.pop(t, None)
                if isinstance(meta, dict) and meta.get("is_bot", True):
                    self.recent_bot_pos_ids[t] = now_ts
                dirty = True
        for d in (
            self.peak_prices,
            self.peak_timestamps,
            self.profit_trail_start_ts,
            self._last_ai_atr_milestones,
            self._last_ai_sl_danger,
        ):
            for t in list(d.keys()):
                if t not in active_tickets:
                    d.pop(t, None)
        return dirty

    def _ensure_position_meta(
        self,
        pos: Any,
        snap: MT5SymbolSnapshot | None,
        now_ts: float,
        point: float,
    ) -> tuple[dict[str, Any], bool]:
        ticket = int(pos.ticket)
        existing = self.position_meta.get(ticket)
        if existing is not None:
            return existing, False

        is_buy = pos.type == mt5.POSITION_TYPE_BUY
        entry = float(pos.price_open)
        cur = float(pos.price_current)
        old_sl = float(pos.sl)
        comment = str(getattr(pos, "comment", "") or "")
        pos_magic = int(getattr(pos, "magic", -1))
        is_bot = (pos_magic == MT5_MAGIC_NUMBER) or comment.startswith("GeminiBot")
        is_m15 = comment.startswith("GeminiBot_M15")

        atr_1h = snap.atr_price if (snap and snap.atr_price > 0) else abs(entry * 0.003)
        atr_15 = snap.atr_15_price if (snap and snap.atr_15_price > 0) else (atr_1h * 0.5)
        sl_on_loss_side = (is_buy and old_sl > 0 and old_sl < entry) or ((not is_buy) and old_sl > entry)
        default_sl_dist = (2.0 * atr_15) if is_m15 else (3.0 * atr_1h)
        init_sl_dist = abs(entry - old_sl) if sl_on_loss_side else default_sl_dist
        init_sl_dist = max(init_sl_dist, point * 20.0)

        meta = {
            "is_bot": is_bot,
            "is_m15": is_m15,
            "init_sl_dist": init_sl_dist,
            "atr1h_at_entry": atr_1h,
            "atr15_at_entry": atr_15,
            "peak_price": cur,
            "peak_ts": now_ts,
            "trail_start_ts": None,
        }
        self.position_meta[ticket] = meta
        if is_bot:
            self.recent_bot_pos_ids[ticket] = now_ts
        self.peak_prices[ticket] = cur
        self.peak_timestamps[ticket] = now_ts
        return meta, True

    def manage_open_positions(
        self,
        snapshots_map: dict[str, MT5SymbolSnapshot],
        open_reviews: dict[str, MT5PositionAIReview] | None = None,
    ) -> list[dict[str, Any]]:
        """
        Gestion de salidas CLEAN_DIFF validada IS+OOS (B_FINAL_HYBRID_ADX_0.65PCT):
        1. Cierre Preventivo Viernes >= 21:40 UTC en activos tradicionales.
        2. Cierre Defensivo IA de emergencia solo si CLOSE_NOW + tp_prob <= 25 + profit >= $0.40 + move_atr >= 0.75.
        3. M15: BE +0.05R al alcanzar move_r >= 1.00 (SIN trailing).
        4. H1: BE +0.25*ATR al alcanzar move_atr >= 1.25; Chandelier 1.50*ATR desde move_r >= 1.50 (trail_start_ts=now_ts, nunca pos.time).
        """
        actions: list[dict[str, Any]] = []
        positions = mt5.positions_get()
        if not positions:
            if self._prune_position_meta(set()):
                self._save_ai_state()
            return actions

        now_utc = datetime.now(timezone.utc)
        now_ts = now_utc.timestamp()
        active_tickets = {int(p.ticket) for p in positions}
        state_dirty = self._prune_position_meta(active_tickets)

        # Viernes >= 21:40 UTC: Cierre preventivo obligatorio de fin de semana para activos tradicionales
        is_friday_weekend_close = (
            now_utc.weekday() == 4
            and (now_utc.hour > 21 or (now_utc.hour == 21 and now_utc.minute >= 40))
        )

        for pos in positions:
            ticket = int(pos.ticket)
            sym = str(pos.symbol)
            is_buy = pos.type == mt5.POSITION_TYPE_BUY
            entry = float(pos.price_open)
            cur = float(pos.price_current)
            old_sl = float(pos.sl)
            old_tp = float(pos.tp)
            profit_usd = float(pos.profit)
            review = open_reviews.get(sym) if open_reviews else None

            # === ESCUDO FIN DE SEMANA: CIERRE PREVENTIVO VIERNES >= 21:40 UTC (ACTIVOS TRADICIONALES) ===
            is_traditional_asset = sym not in CRYPTO_SYMBOLS
            if is_friday_weekend_close and is_traditional_asset:
                res = self._close_mt5_position(
                    pos,
                    f"Cierre Preventivo Fin de Semana (Viernes {now_utc.strftime('%H:%M')} UTC) para blindar contra gap/spread de domingo",
                )
                if res:
                    actions.append(res)
                    self.position_meta.pop(ticket, None)
                    state_dirty = True
                continue

            info = mt5.symbol_info(sym)
            digits = int(info.digits) if info else 5
            point = float(info.point) if info else 0.00001
            cur_spread_pts = float(info.spread) if info else 15.0
            stops_level = float(getattr(info, "trade_stops_level", 0) or 0) if info else 0.0
            snap = snapshots_map.get(sym)

            meta, created_meta = self._ensure_position_meta(pos, snap, now_ts, point)
            if created_meta:
                state_dirty = True

            is_m15 = bool(meta.get("is_m15", False))
            atr_1h = (
                snap.atr_price
                if (snap and snap.atr_price > 0)
                else float(meta.get("atr1h_at_entry") or abs(entry * 0.003))
            )
            atr_15 = (
                snap.atr_15_price
                if (snap and snap.atr_15_price > 0)
                else float(meta.get("atr15_at_entry") or (atr_1h * 0.5))
            )
            init_sl_dist = max(float(meta.get("init_sl_dist") or 0.0), point * 20.0)
            ref_atr = atr_15 if is_m15 else atr_1h

            min_sl_dist = max(0.35 * ref_atr, cur_spread_pts * 1.5 * point, stops_level * point)
            min_sl_improve = max(0.05 * ref_atr, 10.0 * point)

            move_in_favor = (cur - entry) if is_buy else (entry - cur)
            move_atr = move_in_favor / atr_1h if atr_1h > 0 else 0.0
            move_r = move_in_favor / init_sl_dist if init_sl_dist > 0 else 0.0

            # Actualizar pico a favor con persistencia atomica
            prev_peak = float(meta.get("peak_price", cur))
            if (is_buy and cur > prev_peak) or ((not is_buy) and cur < prev_peak):
                meta["peak_price"] = cur
                meta["peak_ts"] = now_ts
                state_dirty = True
            peak = float(meta["peak_price"])
            self.peak_prices[ticket] = peak
            self.peak_timestamps[ticket] = float(meta.get("peak_ts", now_ts))

            # === ASISTENCIA DEFENSIVA IA DE EMERGENCIA ===
            if (
                review is not None
                and review.action == "CLOSE_NOW"
                and review.tp_probability_pct <= 25
                and profit_usd >= 0.40
                and move_atr >= 0.75
            ):
                res = self._close_mt5_position(
                    pos,
                    f"Cierre Defensivo IA (Prob. TP={review.tp_probability_pct}%): {review.reasoning}",
                )
                if res:
                    actions.append(res)
                    self.position_meta.pop(ticket, None)
                    state_dirty = True
                    self.block_symbol_90m(
                        symbol=sym,
                        probability_pct=review.tp_probability_pct,
                        close_type="AI_DEFENSIVE_CLOSE",
                        profit_usd=profit_usd,
                        reason=review.reasoning,
                        duration_minutes=90.0,
                    )
                continue

            if move_in_favor <= 0.0:
                continue

            candidate_sl = old_sl
            reasons: list[str] = []
            direction = 1.0 if is_buy else -1.0

            if is_m15:
                # M15 CLEAN_DIFF: Break-Even +0.05R al alcanzar move_r >= 1.00, SIN trailing
                if move_r >= 1.00:
                    be_px = round(entry + direction * (0.05 * init_sl_dist), digits)
                    be_better = (be_px > candidate_sl) if is_buy else (candidate_sl <= 0 or be_px < candidate_sl)
                    be_valid = (be_px < cur - min_sl_dist) if is_buy else (be_px > cur + min_sl_dist)
                    if be_better and be_valid:
                        candidate_sl = be_px
                        reasons.append("M15 Break-Even +0.05R")
            else:
                # H1 CLEAN_DIFF: Break-Even +0.25*ATR @ 1.25*ATR + Chandelier 1.50*ATR desde 1.50R
                if move_atr >= 1.25:
                    be_px = round(entry + direction * (0.25 * atr_1h), digits)
                    be_better = (be_px > candidate_sl) if is_buy else (candidate_sl <= 0 or be_px < candidate_sl)
                    be_valid = (be_px < cur - min_sl_dist) if is_buy else (be_px > cur + min_sl_dist)
                    if be_better and be_valid:
                        candidate_sl = be_px
                        reasons.append("H1 Break-Even +0.25ATR")

                if move_r >= 1.50:
                    if not meta.get("trail_start_ts"):
                        # BUG-01 FIX: fijar siempre now_ts (NUNCA float(pos.time))
                        meta["trail_start_ts"] = now_ts
                        self.profit_trail_start_ts[ticket] = now_ts
                        state_dirty = True
                    ch_sl = round(peak - direction * (1.50 * atr_1h), digits)
                    ch_better = (ch_sl > candidate_sl) if is_buy else (candidate_sl <= 0 or ch_sl < candidate_sl)
                    ch_valid = (ch_sl < cur - min_sl_dist) if is_buy else (ch_sl > cur + min_sl_dist)
                    if ch_better and ch_valid:
                        candidate_sl = ch_sl
                        reasons.append("H1 Chandelier 1.50ATR")

            if is_buy:
                sl_improved = candidate_sl > old_sl + min_sl_improve
            else:
                sl_improved = old_sl <= 0 or candidate_sl < old_sl - min_sl_improve

            if sl_improved:
                mod_ok = self._modify_mt5_sl_tp(ticket, sym, candidate_sl, old_tp)
                if mod_ok:
                    evt = {
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "ticket": ticket,
                        "symbol": sym,
                        "side": "ADJUST_SL_TP",
                        "old_sl": old_sl,
                        "new_sl": candidate_sl,
                        "old_tp": old_tp,
                        "new_tp": old_tp,
                        "profit_usd": round(profit_usd, 2),
                        "reason": " | ".join(reasons),
                    }
                    self._append_history(evt)
                    actions.append(evt)
                    logger.info(
                        "MT5 SL MOVIDO CLEAN_DIFF (%s #%d): SL %s -> %s | TP %s | PnL $%.2f | %s",
                        sym,
                        ticket,
                        old_sl,
                        candidate_sl,
                        old_tp,
                        profit_usd,
                        evt["reason"],
                    )

        if state_dirty:
            self._save_ai_state()
        return actions

    def calculate_safe_lot_and_sl(
        self,
        snap: MT5SymbolSnapshot,
        side: str,
        equity_usd: float,
        free_margin_usd: float,
        ai_probability_pct: int = 70,
        risk_scale: float = 1.0,
    ) -> tuple[float, float, float, float]:
        """
        Calcula (lotes, sl_price, tp_price, riesgo_usd) con sizing proporcional (1.00% / max 1.25%),
        veto estricto de compresion SL > 20%, redondeo math.floor acotado, escalado gradual por margen
        y TP fijo 2.5R (FIXED_2.5R) tanto en H1 como en M15.
        Retorna (0.0, 0.0, 0.0, 0.0) si la orden debe vetarse o falla el calculo del broker.
        """
        is_buy = side == "BUY"
        entry = snap.ask if is_buy else snap.bid
        order_type = mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL

        # Riesgo proporcional continuo (1.00% target / 1.25% max para equity >= $250, concentrado a max 3 pos)
        if equity_usd >= 250.0:
            target_risk_usd = round(equity_usd * 0.0100, 2)
            max_allowed_risk_usd = round(equity_usd * 0.0125, 2)
        elif equity_usd >= 150.0:
            target_risk_usd = round(equity_usd * 0.015, 2)
            max_allowed_risk_usd = round(equity_usd * 0.020, 2)
        elif equity_usd >= 60.0:
            target_risk_usd = round(equity_usd * 0.035, 2)
            max_allowed_risk_usd = 3.50
        elif equity_usd >= 28.0:
            target_risk_usd = round(equity_usd * 0.045, 2)
            max_allowed_risk_usd = 2.20
        else:
            target_risk_usd = max(self.min_risk_usd, round(equity_usd * self.risk_pct, 2))
            max_allowed_risk_usd = max(target_risk_usd, self.max_risk_usd_cap)

        # Conviction Sizing suavizado: <69 -> 0.75x, 69..77 -> 0.95x, >=78 -> 1.10x
        if ai_probability_pct < 69:
            conv_scale = 0.75
        elif ai_probability_pct < 78:
            conv_scale = 0.95
        else:
            conv_scale = 1.10

        applied_risk_scale = max(0.1, float(risk_scale))
        target_risk_usd = max(1.00, round(target_risk_usd * conv_scale * applied_risk_scale, 2))
        # BUG-08 FIX: ni conv_scale < 1.0 ni risk_scale < 1.0 comprimen max_allowed_risk_usd
        max_allowed_risk_usd = max(
            1.20,
            round(max_allowed_risk_usd * max(1.0, conv_scale) * max(1.0, applied_risk_scale), 2),
        )

        raw_sl = snap.structural_long_sl if is_buy else snap.structural_short_sl
        loss_at_min_lot = mt5.order_calc_profit(order_type, snap.symbol, snap.min_lot, entry, raw_sl)
        if loss_at_min_lot is None:
            logger.warning("order_calc_profit devolvio None para %s (%s); entrada abortada.", snap.symbol, side)
            return 0.0, 0.0, 0.0, 0.0
        abs_loss_min_lot = abs(float(loss_at_min_lot))
        if abs_loss_min_lot <= 0.0:
            return 0.0, 0.0, 0.0, 0.0

        step = snap.lot_step if snap.lot_step > 0 else 0.01
        step_str = f"{step:.8f}".rstrip("0").rstrip(".")
        lot_decimals = len(step_str.split(".")[1]) if "." in step_str else 0

        lot = snap.min_lot
        sl_price = raw_sl

        if abs_loss_min_lot > max_allowed_risk_usd:
            # BUG-03 FIX: vetar si la compresion necesaria del SL estructural excede 20%
            scale = max_allowed_risk_usd / abs_loss_min_lot
            compression_ratio = 1.0 - scale
            if compression_ratio > 0.20:
                logger.info(
                    "VETO COMPRESION SL >20%% (%s): min_lot arriesga $%.2f > max $%.2f (compresion %.1f%%).",
                    snap.symbol,
                    abs_loss_min_lot,
                    max_allowed_risk_usd,
                    compression_ratio * 100.0,
                )
                return 0.0, 0.0, 0.0, 0.0
            adj_dist = max(abs(entry - raw_sl) * scale, snap.point * 35.0)
            sl_price = round(entry - adj_dist if is_buy else entry + adj_dist, snap.digits)
            recalc = mt5.order_calc_profit(order_type, snap.symbol, lot, entry, sl_price)
            if recalc is None:
                return 0.0, 0.0, 0.0, 0.0
            risk_usd = abs(float(recalc))
        else:
            raw_lots = (target_risk_usd / abs_loss_min_lot) * snap.min_lot
            steps = max(1, int(math.floor((raw_lots / step) + 1e-9)))
            candidate_lot = max(snap.min_lot, round(steps * step, lot_decimals))

            # Asegurar que el riesgo real nunca supere max_allowed_risk_usd
            while candidate_lot > snap.min_lot and ((candidate_lot / snap.min_lot) * abs_loss_min_lot) > max_allowed_risk_usd + 1e-9:
                steps = max(1, steps - 1)
                candidate_lot = max(snap.min_lot, round(steps * step, lot_decimals))

            # Escalado gradual por margen disponible <= min(free_margin * 0.35, equity * 0.15) sin caps arbitrarios
            margin_budget = min(free_margin_usd * 0.35, equity_usd * 0.15)
            margin_req = mt5.order_calc_margin(order_type, snap.symbol, candidate_lot, entry)
            if margin_req is None:
                return 0.0, 0.0, 0.0, 0.0
            if margin_req <= margin_budget:
                lot = candidate_lot
            else:
                margin_min = mt5.order_calc_margin(order_type, snap.symbol, snap.min_lot, entry)
                if margin_min is None or margin_min <= 0.0 or margin_min > free_margin_usd * 0.78:
                    return 0.0, 0.0, 0.0, 0.0
                if margin_budget >= margin_min:
                    aff_lots = (margin_budget / margin_min) * snap.min_lot
                    aff_steps = max(1, int(math.floor((aff_lots / step) + 1e-9)))
                    lot = max(snap.min_lot, min(candidate_lot, round(aff_steps * step, lot_decimals)))
                else:
                    lot = snap.min_lot

            recalc = mt5.order_calc_profit(order_type, snap.symbol, lot, entry, sl_price)
            if recalc is None:
                return 0.0, 0.0, 0.0, 0.0
            risk_usd = abs(float(recalc))
            while lot > snap.min_lot and risk_usd > max_allowed_risk_usd + 1e-9:
                cur_steps = max(1, int(math.floor((lot / step) + 1e-9)) - 1)
                lot = max(snap.min_lot, round(cur_steps * step, lot_decimals))
                recalc = mt5.order_calc_profit(order_type, snap.symbol, lot, entry, sl_price)
                if recalc is None:
                    return 0.0, 0.0, 0.0, 0.0
                risk_usd = abs(float(recalc))

        # TP fijo FIXED_2.5R tanto en H1 como en M15
        sl_dist = abs(entry - sl_price)
        tp_dist = sl_dist * 2.5
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
            self.last_order_timestamp = time.time()
            self._save_ai_state()
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

        exec_price = float(result.price or price)
        ticket = int(result.order)
        now_ts = time.time()
        self.position_meta[ticket] = {
            "is_bot": True,
            "is_m15": snap.entry_pillar.startswith("M15_SCALPER"),
            "init_sl_dist": max(abs(exec_price - sl_price), snap.point * 20.0),
            "atr1h_at_entry": snap.atr_price,
            "atr15_at_entry": snap.atr_15_price if snap.atr_15_price > 0 else (snap.atr_price * 0.5),
            "peak_price": exec_price,
            "peak_ts": now_ts,
            "trail_start_ts": None,
        }
        self.recent_bot_pos_ids[ticket] = now_ts
        self.peak_prices[ticket] = exec_price
        self.peak_timestamps[ticket] = now_ts

        evt = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "ticket": ticket,
            "symbol": snap.symbol,
            "side": side,
            "mode": "LIVE",
            "lot": lot,
            "price": exec_price,
            "sl": sl_price,
            "tp": tp_price,
            "risk_usd": risk_usd,
            "reason": reason,
        }
        self._append_history(evt)
        self.last_order_timestamp = now_ts
        self._save_ai_state()
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
        if res is None or res.retcode != mt5.TRADE_RETCODE_DONE:
            logger.warning(
                "Error al modificar SL/TP en %s #%d (SL=%s, TP=%s): retcode=%s, comment=%s",
                symbol,
                ticket,
                new_sl,
                new_tp,
                getattr(res, "retcode", None),
                getattr(res, "comment", mt5.last_error()),
            )
            return False
        return True

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
        self._atomic_write_text(self.history_file, json.dumps(items[-300:], indent=2, ensure_ascii=False))

    def _load_ai_state(self) -> None:
        if not self.ai_state_file.exists():
            return
        try:
            raw = json.loads(self.ai_state_file.read_text(encoding="utf-8"))
            now_ts = time.time()
            blocks = raw.get("symbol_blocked_until", {})
            if isinstance(blocks, dict):
                self.symbol_blocked_until = {
                    str(sym): data
                    for sym, data in blocks.items()
                    if isinstance(data, dict) and float(data.get("until_ts", 0.0)) > now_ts
                }
            tickets = raw.get("evaluated_deal_tickets", [])
            if isinstance(tickets, list):
                self.evaluated_deal_tickets = {int(t) for t in tickets[-300:]}
            decisions = raw.get("recent_ai_close_decisions", [])
            if isinstance(decisions, list):
                self.recent_ai_close_decisions = decisions[-20:]
            self.last_order_timestamp = float(raw.get("last_order_timestamp", 0.0) or 0.0)
            pos_meta_raw = raw.get("position_meta", {})
            if isinstance(pos_meta_raw, dict):
                self.position_meta = {}
                for k, v in pos_meta_raw.items():
                    if isinstance(v, dict):
                        t_id = int(k)
                        self.position_meta[t_id] = dict(v)
                        if v.get("peak_price") is not None:
                            self.peak_prices[t_id] = float(v["peak_price"])
                        if v.get("peak_ts") is not None:
                            self.peak_timestamps[t_id] = float(v["peak_ts"])
                        if v.get("trail_start_ts") is not None:
                            self.profit_trail_start_ts[t_id] = float(v["trail_start_ts"])
            recent_bot_raw = raw.get("recent_bot_pos_ids", {})
            if isinstance(recent_bot_raw, dict):
                # TTL de 48h (172800s) para reconocer cierres manuales overnight tras reinicios o _prune_position_meta
                self.recent_bot_pos_ids = {
                    int(k): float(ts)
                    for k, ts in recent_bot_raw.items()
                    if (now_ts - float(ts)) <= 172800.0
                }
        except Exception as exc:
            logger.warning("No se pudo cargar estado IA MT5 (%s): %s", self.ai_state_file, exc)

    def _save_ai_state(self) -> None:
        now_ts = time.time()
        active_blocks = {
            sym: data
            for sym, data in self.symbol_blocked_until.items()
            if float(data.get("until_ts", 0.0)) > now_ts
        }
        self.symbol_blocked_until = active_blocks
        active_recent_bot_ids = {
            pid: ts
            for pid, ts in self.recent_bot_pos_ids.items()
            if (now_ts - float(ts)) <= 172800.0
        }
        self.recent_bot_pos_ids = active_recent_bot_ids
        payload = {
            "updated_at_utc": datetime.now(timezone.utc).isoformat(),
            "last_order_timestamp": self.last_order_timestamp,
            "position_meta": {str(k): v for k, v in self.position_meta.items()},
            "recent_bot_pos_ids": {str(k): v for k, v in active_recent_bot_ids.items()},
            "symbol_blocked_until": active_blocks,
            "evaluated_deal_tickets": sorted(self.evaluated_deal_tickets)[-300:],
            "recent_ai_close_decisions": self.recent_ai_close_decisions[-20:],
        }
        self._atomic_write_text(self.ai_state_file, json.dumps(payload, indent=2, ensure_ascii=False))

    @staticmethod
    def _get_usd_direction(symbol: str, side: str) -> str:
        is_buy = str(side).upper() in ("BUY", "LONG")
        if symbol in ("EURUSDm", "GBPUSDm", "AUDUSDm", "NZDUSDm", "XAUUSDm"):
            return "USD_SHORT" if is_buy else "USD_LONG"
        if symbol in ("USDJPYm", "USDCADm", "USDCHFm"):
            return "USD_LONG" if is_buy else "USD_SHORT"
        return "NON_USD_FOREX"

    @staticmethod
    def _is_twin_conflict(symbol: str, open_symbols: set[str]) -> bool:
        for cluster in TWIN_CORRELATION_CLUSTERS:
            if symbol in cluster and any(s in open_symbols for s in cluster if s != symbol):
                return True
        return False

    def _get_open_position_ids(self) -> set[int]:
        open_pos = mt5.positions_get() or ()
        ids: set[int] = set()
        for p in open_pos:
            t = int(getattr(p, "ticket", 0) or 0)
            ident = int(getattr(p, "identifier", 0) or 0)
            if t > 0:
                ids.add(t)
            if ident > 0:
                ids.add(ident)
        return ids

    def _is_bot_position_deals(
        self,
        pos_id: int,
        deals_for_pos: list[Any],
        known_bot_pos_ids: set[int] | None = None,
    ) -> bool:
        if any(int(getattr(x, "magic", -1)) == MT5_MAGIC_NUMBER for x in deals_for_pos):
            return True
        known_ids = known_bot_pos_ids if known_bot_pos_ids is not None else self.known_bot_pos_ids
        if pos_id in known_ids:
            return True
        is_tracked_bot = (
            (pos_id in self.position_meta and bool(self.position_meta[pos_id].get("is_bot", True)))
            or (pos_id in self.recent_bot_pos_ids)
        )
        if is_tracked_bot:
            if any(
                int(getattr(x, "magic", -1)) == 0 and int(getattr(x, "reason", -1)) in (0, 1, 2)
                for x in deals_for_pos
            ):
                return True
        return False

    def _compute_symbol_performance_14d(
        self,
        now_utc: datetime | None = None,
        open_position_ids: set[int] | None = None,
        equity_usd: float = 590.0,
    ) -> dict[str, dict[str, Any]]:
        ref_utc = now_utc or datetime.now(timezone.utc)
        if ref_utc.tzinfo is None:
            ref_utc = ref_utc.replace(tzinfo=timezone.utc)
        else:
            ref_utc = ref_utc.astimezone(timezone.utc)

        deals = mt5.history_deals_get(ref_utc - timedelta(days=14), ref_utc + timedelta(minutes=60))
        if not deals:
            return {}

        open_ids = open_position_ids if open_position_ids is not None else self._get_open_position_ids()
        by_pos: dict[int, list[Any]] = {}
        discovered_bot_ids: set[int] = set()
        now_ts = ref_utc.timestamp()
        for d in deals:
            pos_id = int(getattr(d, "position_id", 0) or 0)
            if pos_id > 0:
                by_pos.setdefault(pos_id, []).append(d)
                if int(getattr(d, "magic", -1)) == MT5_MAGIC_NUMBER:
                    discovered_bot_ids.add(pos_id)
                    deal_ts = float(getattr(d, "time", 0.0) or 0.0)
                    if deal_ts > 0 and (now_ts - deal_ts) <= 172800.0:
                        self.recent_bot_pos_ids[pos_id] = max(self.recent_bot_pos_ids.get(pos_id, 0.0), deal_ts)

        if discovered_bot_ids:
            self.known_bot_pos_ids.update(discovered_bot_ids)

        stats: dict[str, dict[str, Any]] = {}
        for pos_id, dlist in by_pos.items():
            if pos_id in open_ids:
                continue
            if not self._is_bot_position_deals(pos_id, dlist, known_bot_pos_ids=self.known_bot_pos_ids):
                continue
            outs = [x for x in dlist if int(getattr(x, "entry", -1)) == mt5.DEAL_ENTRY_OUT]
            if not outs:
                continue
            sym = str(outs[-1].symbol)
            pnl = sum(
                float(getattr(x, "profit", 0.0) or 0.0)
                + float(getattr(x, "swap", 0.0) or 0.0)
                + float(getattr(x, "commission", 0.0) or 0.0)
                for x in outs
            )
            s = stats.setdefault(sym, {"trades": 0, "wins": 0, "net_pnl_usd": 0.0})
            s["trades"] += 1
            if pnl > 0:
                s["wins"] += 1
            s["net_pnl_usd"] += pnl

        eq_ref = max(1.0, float(equity_usd))
        result: dict[str, dict[str, Any]] = {}
        for sym, s in stats.items():
            trades = int(s["trades"])
            wr = round((s["wins"] / trades) * 100.0, 1) if trades > 0 else 50.0
            net_pnl = round(float(s["net_pnl_usd"]), 2)
            # P1_SAFE_CORE: escalar con equity y exigir bajo WR real (sin castigar pares con WR >= 48%)
            needs_higher_bar = trades >= 5 and wr < 48.0 and net_pnl < (-0.015 * eq_ref)
            result[sym] = {
                "trades": trades,
                "wins": int(s["wins"]),
                "win_rate_pct": wr,
                "net_pnl_usd": net_pnl,
                "min_required_prob_pct": 60 if needs_higher_bar else 55,
            }
        return result

    def _evaluate_daily_risk_guard(
        self,
        now_utc: datetime | None = None,
        equity_usd: float = 590.0,
        open_position_ids: set[int] | None = None,
        known_bot_pos_ids: set[int] | None = None,
    ) -> dict[str, Any]:
        """
        Daily Risk Guard SOFT (B_FINAL_HYBRID_ADX_0.65PCT) sobre el dia UTC actual:
        - Filtra por magic == MT5_MAGIC_NUMBER, excluye posiciones aun abiertas y suma profit + swap + commission.
        - Hard Daily Loss Stop: daily_closed_pnl_usd <= -3% equity -> pause_new_entries=True.
        - Freno de racha: 3 perdidas seguidas con mins_since_last_loss < 45m -> pause_new_entries=True (45m).
        - MODO_PROTECCION_CAPITAL: daily_closed_pnl_usd >= +4% equity o >= 2 perdidas seguidas ->
          min_ai_prob=68, risk_scale=0.75, max_positions=3 (normal: max_positions=4).
        """
        ref_utc = now_utc or datetime.now(timezone.utc)
        if ref_utc.tzinfo is None:
            ref_utc = ref_utc.replace(tzinfo=timezone.utc)
        else:
            ref_utc = ref_utc.astimezone(timezone.utc)

        utc_day_start = ref_utc.replace(hour=0, minute=0, second=0, microsecond=0)
        day_start_ts = int(utc_day_start.timestamp())
        now_ts = ref_utc.timestamp()
        eq_ref = max(1.0, float(equity_usd))

        open_ids = open_position_ids if open_position_ids is not None else self._get_open_position_ids()
        deals = mt5.history_deals_get(utc_day_start, ref_utc + timedelta(minutes=60))
        by_pos_all: dict[int, list[Any]] = {}
        by_pos_outs: dict[int, list[Any]] = {}
        if deals:
            for d in deals:
                pos_id = int(getattr(d, "position_id", 0) or 0)
                if pos_id <= 0 or pos_id in open_ids:
                    continue
                by_pos_all.setdefault(pos_id, []).append(d)
                if int(getattr(d, "entry", -1)) != mt5.DEAL_ENTRY_OUT:
                    continue
                deal_time = int(getattr(d, "time", 0) or 0)
                if deal_time < day_start_ts:
                    continue
                by_pos_outs.setdefault(pos_id, []).append(d)

        closed_positions: list[tuple[int, int, float]] = []
        for pos_id, outs in by_pos_outs.items():
            if not self._is_bot_position_deals(pos_id, by_pos_all.get(pos_id, outs), known_bot_pos_ids=known_bot_pos_ids):
                continue
            close_time = max(int(getattr(x, "time", 0) or 0) for x in outs)
            max_ticket = max(int(getattr(x, "ticket", 0) or 0) for x in outs)
            pnl = sum(
                float(getattr(x, "profit", 0.0) or 0.0)
                + float(getattr(x, "swap", 0.0) or 0.0)
                + float(getattr(x, "commission", 0.0) or 0.0)
                for x in outs
            )
            closed_positions.append((close_time, max_ticket, pnl))

        closed_positions.sort(key=lambda item: (item[0], item[1]))

        daily_closed_pnl_usd = round(sum(item[2] for item in closed_positions), 2)
        wins_today = sum(1 for item in closed_positions if item[2] > 0.0)
        losses_today = sum(1 for item in closed_positions if item[2] < 0.0)

        consecutive_losses = 0
        for _, _, pnl in reversed(closed_positions):
            if pnl < 0.0:
                consecutive_losses += 1
            else:
                break

        loss_times = [item[0] for item in closed_positions if item[2] < 0.0]
        if loss_times:
            last_loss_ts = float(max(loss_times))
            mins_since_last_loss = round(max(0.0, (now_ts - last_loss_ts) / 60.0), 1)
        else:
            mins_since_last_loss = 999.0

        hard_loss_limit_usd = round(-0.03 * eq_ref, 2)
        profit_protect_usd = round(0.04 * eq_ref, 2)
        hard_daily_loss_stop = daily_closed_pnl_usd <= (-0.03 * eq_ref)
        streak_pause = bool(consecutive_losses >= 3 and mins_since_last_loss < 45.0)
        pause_new_entries = bool(hard_daily_loss_stop or streak_pause)
        protection_triggered = bool(
            (daily_closed_pnl_usd >= (0.04 * eq_ref))
            or (consecutive_losses >= 2)
            or hard_daily_loss_stop
        )

        if streak_pause:
            pause_remaining_mins = round(max(0.0, 45.0 - mins_since_last_loss), 1)
        elif hard_daily_loss_stop:
            next_midnight = utc_day_start + timedelta(days=1)
            pause_remaining_mins = round(max(1.0, (next_midnight.timestamp() - now_ts) / 60.0), 1)
        else:
            pause_remaining_mins = 0.0

        if protection_triggered:
            protection_mode = "MODO_PROTECCION_CAPITAL"
            min_ai_prob = 62
            risk_scale = 0.75
            max_positions = 3
            triggers: list[str] = []
            if hard_daily_loss_stop:
                triggers.append(f"Hard Daily Loss Stop (${daily_closed_pnl_usd:+.2f} <= ${hard_loss_limit_usd:+.2f} = -3% equity)")
            if daily_closed_pnl_usd >= (0.04 * eq_ref):
                triggers.append(f"Ganancia diaria +${daily_closed_pnl_usd:.2f} >= +${profit_protect_usd:.2f} (+4% equity)")
            if streak_pause:
                triggers.append(f"Racha de {consecutive_losses} perdidas seguidas (pausa 45m: {pause_remaining_mins:.1f}m restantes)")
            elif consecutive_losses >= 2:
                triggers.append(f"Racha de {consecutive_losses} perdidas seguidas")
            reason = " | ".join(triggers)
        else:
            protection_mode = "NORMAL"
            min_ai_prob = 55
            risk_scale = 1.0
            max_positions = 4
            reason = "Operacion normal (sin disparadores diarios)"

        return {
            "utc_date": ref_utc.strftime("%Y-%m-%d"),
            "daily_closed_pnl_usd": daily_closed_pnl_usd,
            "closed_trades_today": len(closed_positions),
            "wins_today": wins_today,
            "losses_today": losses_today,
            "consecutive_losses": consecutive_losses,
            "mins_since_last_loss": mins_since_last_loss,
            "hard_daily_loss_stop": hard_daily_loss_stop,
            "protection_mode": protection_mode,
            "protection_active": protection_triggered,
            "pause_new_entries": pause_new_entries,
            "pause_remaining_mins": pause_remaining_mins,
            "min_ai_prob": min_ai_prob,
            "risk_scale": risk_scale,
            "max_positions": max_positions,
            "reason": reason,
        }

    def block_symbol_90m(
        self,
        symbol: str,
        probability_pct: int,
        close_type: str,
        profit_usd: float,
        reason: str,
        duration_minutes: float = 90.0,
    ) -> None:
        mins = max(1.0, float(duration_minutes))
        until_ts = time.time() + mins * 60.0
        until_utc = datetime.fromtimestamp(until_ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        self.symbol_blocked_until[symbol] = {
            "symbol": symbol,
            "until_ts": until_ts,
            "until_utc": until_utc,
            "duration_minutes": round(mins, 1),
            "probability_pct": int(probability_pct),
            "close_type": close_type,
            "profit_usd": round(float(profit_usd), 2),
            "reason": reason,
        }
        self._save_ai_state()

    def get_active_block(self, symbol: str) -> dict[str, Any] | None:
        entry = self.symbol_blocked_until.get(symbol)
        if not entry:
            return None
        remaining_sec = float(entry.get("until_ts", 0.0)) - time.time()
        if remaining_sec <= 0:
            self.symbol_blocked_until.pop(symbol, None)
            self._save_ai_state()
            return None
        return {**entry, "remaining_minutes": round(remaining_sec / 60.0, 1)}

    def _collect_recent_closed_deals(
        self,
        snapshots_map: dict[str, MT5SymbolSnapshot],
        minutes_back: int = 90,
        now_utc: datetime | None = None,
        open_position_ids: set[int] | None = None,
        known_bot_pos_ids: set[int] | None = None,
    ) -> list[dict[str, Any]]:
        ref_utc = now_utc or datetime.now(timezone.utc)
        if ref_utc.tzinfo is None:
            ref_utc = ref_utc.replace(tzinfo=timezone.utc)
        else:
            ref_utc = ref_utc.astimezone(timezone.utc)
        now_ts = ref_utc.timestamp()

        raw_deals = mt5.history_deals_get(
            ref_utc - timedelta(minutes=minutes_back + 30),
            ref_utc + timedelta(minutes=60),
        )
        if not raw_deals:
            return []

        open_ids = open_position_ids if open_position_ids is not None else self._get_open_position_ids()
        by_pos_all: dict[int, list[Any]] = {}
        by_pos_outs: dict[int, list[Any]] = {}
        for d in raw_deals:
            pos_id = int(getattr(d, "position_id", 0) or 0)
            if pos_id <= 0 or pos_id in open_ids:
                continue
            by_pos_all.setdefault(pos_id, []).append(d)
            if int(getattr(d, "entry", -1)) == mt5.DEAL_ENTRY_OUT:
                by_pos_outs.setdefault(pos_id, []).append(d)

        grouped_closes: list[tuple[int, int, int, list[Any]]] = []
        for pos_id, outs in by_pos_outs.items():
            if not self._is_bot_position_deals(pos_id, by_pos_all.get(pos_id, outs), known_bot_pos_ids=known_bot_pos_ids):
                continue
            outs_sorted = sorted(outs, key=lambda x: (int(getattr(x, "time", 0) or 0), int(getattr(x, "ticket", 0) or 0)))
            last_out = outs_sorted[-1]
            grouped_closes.append((int(last_out.time), int(last_out.ticket), pos_id, outs_sorted))

        grouped_closes.sort(key=lambda item: (item[0], item[1]))

        results: list[dict[str, Any]] = []
        for close_ts, last_ticket, pos_id, outs_sorted in grouped_closes:
            delta_sec = now_ts - float(close_ts)
            if delta_sec < -300.0:
                continue
            mins_since = max(0.0, delta_sec / 60.0)
            if mins_since >= float(minutes_back):
                continue
            last_out = outs_sorted[-1]
            sym = str(last_out.symbol)
            net_pnl = round(
                sum(
                    float(getattr(x, "profit", 0.0) or 0.0)
                    + float(getattr(x, "swap", 0.0) or 0.0)
                    + float(getattr(x, "commission", 0.0) or 0.0)
                    for x in outs_sorted
                ),
                2,
            )
            deal_reason = int(getattr(last_out, "reason", -1))
            if deal_reason in (0, 1, 2):
                close_type = "MANUAL"
            elif net_pnl >= 0.0:
                close_type = "POSITIVE"
            else:
                close_type = "NEGATIVE"

            # En MT5, un DEAL_ENTRY_OUT tipo SELL (1) cierra un BUY; tipo BUY (0) cierra un SELL.
            original_side = "BUY" if int(last_out.type) == mt5.DEAL_TYPE_SELL else "SELL"
            snap = snapshots_map.get(sym)
            closed_utc_str = datetime.fromtimestamp(close_ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            results.append(
                {
                    "ticket": last_ticket,
                    "position_id": pos_id,
                    "symbol": sym,
                    "side": original_side,
                    "close_type": close_type,
                    "profit_usd": net_pnl,
                    "mins_since_close": round(mins_since, 1),
                    "deal_reason": deal_reason,
                    "closed_at_utc": closed_utc_str,
                    "snapshot": asdict(snap) if snap is not None else {},
                }
            )
        return results

    def _build_open_positions_metrics(
        self,
        positions: tuple[Any, ...],
        snapshots_map: dict[str, MT5SymbolSnapshot],
    ) -> tuple[list[dict[str, Any]], dict[int, dict[str, Any]]]:
        payload: list[dict[str, Any]] = []
        by_ticket: dict[int, dict[str, Any]] = {}
        now_ts = datetime.now(timezone.utc).timestamp()
        for p in positions:
            ticket = int(p.ticket)
            sym = str(p.symbol)
            is_buy = p.type == mt5.POSITION_TYPE_BUY
            otype = mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL
            entry = float(p.price_open)
            cur = float(p.price_current)
            tp = float(p.tp)
            sl = float(p.sl)
            profit_usd = round(float(p.profit), 2)

            tp_calc = mt5.order_calc_profit(otype, sym, float(p.volume), entry, tp) if tp > 0 else 0.0
            tp_profit_usd = round(float(tp_calc), 2) if tp_calc is not None else 0.0
            sl_calc = mt5.order_calc_profit(otype, sym, float(p.volume), entry, sl) if sl > 0 else 0.0
            sl_profit_usd = round(float(sl_calc), 2) if sl_calc is not None else 0.0

            snap = snapshots_map.get(sym)
            atr1h = snap.atr_price if snap and snap.atr_price > 0 else max(abs(entry * 0.003), 1e-5)
            total_tp_dist = abs(tp - entry) if tp > 0 else 0.0
            cur_move = (cur - entry) if is_buy else (entry - cur)
            move_atr = round(cur_move / atr1h, 2)
            progress_pct = round((cur_move / total_tp_dist) * 100.0, 1) if total_tp_dist > 0 else 0.0
            rem_tp_dist = ((tp - cur) if is_buy else (cur - tp)) if tp > 0 else 0.0
            rem_sl_dist = ((cur - sl) if is_buy else (sl - cur)) if sl > 0 else atr1h
            pos_open_ts = float(getattr(p, "time", 0.0) or 0.0)
            hours_open = round(max(0.0, (now_ts - pos_open_ts) / 3600.0), 2) if pos_open_ts > 0 else 0.0

            metrics = {
                "ticket": ticket,
                "symbol": sym,
                "side": "BUY" if is_buy else "SELL",
                "profit_usd": profit_usd,
                "tp_profit_usd": tp_profit_usd,
                "sl_profit_usd": sl_profit_usd,
                "move_atr": move_atr,
                "hours_open": hours_open,
                "progress_to_tp_pct": progress_pct,
                "rem_tp_in_atr1h": round(rem_tp_dist / atr1h, 2),
                "rem_sl_in_atr1h": round(rem_sl_dist / atr1h, 2),
                "snapshot": asdict(snap) if snap is not None else {},
            }
            payload.append(metrics)
            by_ticket[ticket] = metrics
        return payload, by_ticket

    def _get_rotatable_stagnant_positions(
        self,
        raw_positions: tuple[Any, ...],
        open_metrics_by_ticket: dict[int, dict[str, Any]],
        snapshots_map: dict[str, MT5SymbolSnapshot],
    ) -> list[Any]:
        """
        Regla de Rotacion de Capital DESACTIVADA (P1_SAFE_CORE):
        Auditada con EV negativo (-33.60R en 67 casos historicos por bug de 'WATCH' en momentum_fading).
        Dejar correr las posiciones bajo CLEAN_DIFF (BE + Chandelier + TP 2.5R).
        """
        return []

    def build_global_market_context(
        self,
        snapshots: list[MT5SymbolSnapshot],
        daily_risk_guard: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Empaqueta en una estructura compacta el pulso macro 360° de divisas USD, criptomonedas (BTC/ETH),
        indices/oro, candado de riesgo diario y alertas de noticias/spreads para alimentar en 1 sola llamada a Gemini AI y al motor local.
        """
        snap_map = {s.symbol: s for s in snapshots}

        # 1. Fuerza global del Dolar (USD) en los 7 pares mayores
        usd_bullish = 0
        usd_bearish = 0
        for sym in ("EURUSDm", "GBPUSDm", "AUDUSDm", "NZDUSDm"):
            s = snap_map.get(sym)
            if not s:
                continue
            if (not s.above_ema_200) and s.htf_trend != "BULLISH":
                usd_bullish += 1
            elif s.above_ema_200 and s.htf_trend != "BEARISH":
                usd_bearish += 1
        for sym in ("USDJPYm", "USDCADm", "USDCHFm"):
            s = snap_map.get(sym)
            if not s:
                continue
            if s.above_ema_200 and s.htf_trend != "BEARISH":
                usd_bullish += 1
            elif (not s.above_ema_200) and s.htf_trend != "BULLISH":
                usd_bearish += 1

        if usd_bullish >= 5 and usd_bearish <= 1:
            usd_bias = "USD_STRONG_BULLISH"
        elif usd_bearish >= 5 and usd_bullish <= 1:
            usd_bias = "USD_STRONG_BEARISH"
        elif usd_bullish > usd_bearish + 1:
            usd_bias = "USD_MODERATE_BULLISH"
        elif usd_bearish > usd_bullish + 1:
            usd_bias = "USD_MODERATE_BEARISH"
        else:
            usd_bias = "USD_MIXED"

        # 2. Pulso del Mercado Cripto (BTCUSDm + ETHUSDm)
        btc = snap_map.get("BTCUSDm")
        eth = snap_map.get("ETHUSDm")
        if btc and eth:
            if (not btc.above_ema_200) and (not eth.above_ema_200) and btc.htf_trend in ("BEARISH", "NEUTRAL") and eth.htf_trend in ("BEARISH", "NEUTRAL"):
                crypto_regime = "CRYPTO_ALIGNED_BEARISH"
            elif btc.above_ema_200 and eth.above_ema_200 and btc.htf_trend in ("BULLISH", "NEUTRAL") and eth.htf_trend in ("BULLISH", "NEUTRAL"):
                crypto_regime = "CRYPTO_ALIGNED_BULLISH"
            else:
                crypto_regime = "CRYPTO_DIVERGENT"
        else:
            crypto_regime = "CRYPTO_UNAVAILABLE"

        # 3. Pulso de Indices (US500m + USTECm) y Oro (XAUUSDm)
        sp = snap_map.get("US500m")
        nq = snap_map.get("USTECm")
        gold = snap_map.get("XAUUSDm")
        if sp and nq:
            if sp.above_ema_200 and nq.above_ema_200 and sp.htf_trend != "BEARISH" and nq.htf_trend != "BEARISH":
                indices_regime = "WALL_STREET_BULLISH"
            elif (not sp.above_ema_200) and (not nq.above_ema_200) and sp.htf_trend != "BULLISH" and nq.htf_trend != "BULLISH":
                indices_regime = "WALL_STREET_BEARISH"
            else:
                indices_regime = "WALL_STREET_MIXED"
        else:
            indices_regime = "WALL_STREET_UNAVAILABLE"

        # 4. Detector de Sesion y Noticias / Volatilidad de Spreads
        now_utc = datetime.now(timezone.utc)
        utc_hour = now_utc.hour
        mins_of_day = utc_hour * 60 + now_utc.minute
        rollover_blackout_active = self._is_pre_rollover_entry_blackout(now_utc)
        if rollover_blackout_active:
            session_name = "VEDA_PRE_ROLLOVER_Y_CAMBIO_DE_DIA"
        elif 13 <= utc_hour < 17:
            session_name = "LONDRES_NY_OVERLAP"
        elif 7 <= utc_hour < 13:
            session_name = "LONDRES"
        elif 17 <= utc_hour < 21:
            session_name = "NUEVA_YORK"
        elif 0 <= utc_hour < 7:
            session_name = "ASIA_PACIFICO"
        else:
            session_name = "TRANSICION_BAJA_LIQUIDEZ"

        elevated_spreads = [
            s.symbol
            for s in snapshots
            if (s.spread_points / max(1, MAX_ALLOWED_SPREAD_POINTS.get(s.symbol, 30))) >= 0.75
        ]
        is_ny_open = (14 * 60 + 15) <= mins_of_day <= (15 * 60 + 15)
        is_london_fix = (16 * 60 + 15) <= mins_of_day <= (17 * 60 + 0)
        news_volatility_alert = (len(elevated_spreads) >= 3) or is_ny_open or is_london_fix

        overview = [
            {
                "symbol": s.symbol,
                "htf_trend": s.htf_trend,
                "above_ema_200": s.above_ema_200,
                "dist_atr": s.dist_to_ema200_atr,
                "adx_14": s.adx_14,
                "rsi_14": s.rsi_14,
                "stoch_k": s.stoch_k,
                "macd_improving": s.macd_improving,
                "candle_pattern": s.candle_pattern,
                "setup": s.strategy_setup,
                "spread": s.spread_points,
            }
            for s in snapshots
        ]

        return {
            "usd_strength": {
                "usd_bias": usd_bias,
                "usd_bullish_pairs": usd_bullish,
                "usd_bearish_pairs": usd_bearish,
            },
            "crypto_pulse": {
                "crypto_regime": crypto_regime,
                "btc_htf": btc.htf_trend if btc else "N/A",
                "btc_rsi": btc.rsi_14 if btc else 0.0,
                "eth_htf": eth.htf_trend if eth else "N/A",
                "eth_rsi": eth.rsi_14 if eth else 0.0,
            },
            "indices_pulse": {
                "indices_regime": indices_regime,
                "gold_htf": gold.htf_trend if gold else "N/A",
                "gold_rsi": gold.rsi_14 if gold else 0.0,
            },
            "news_and_session": {
                "utc_time": now_utc.strftime("%H:%M UTC"),
                "session_name": session_name,
                "rollover_blackout_active": rollover_blackout_active,
                "news_volatility_alert": news_volatility_alert,
                "elevated_spread_symbols": elevated_spreads,
            },
            "daily_risk_guard": daily_risk_guard
            or {
                "utc_date": now_utc.strftime("%Y-%m-%d"),
                "daily_closed_pnl_usd": 0.0,
                "closed_trades_today": 0,
                "wins_today": 0,
                "losses_today": 0,
                "consecutive_losses": 0,
                "mins_since_last_loss": 999.0,
                "hard_daily_loss_stop": False,
                "protection_mode": "NORMAL",
                "protection_active": False,
                "pause_new_entries": False,
                "pause_remaining_mins": 0.0,
                "min_ai_prob": 55,
                "risk_scale": 1.0,
                "max_positions": 4,
                "reason": "Operacion normal (sin disparadores diarios)",
            },
            "all_assets_overview": overview,
        }

    def _passes_deterministic_shields(
        self,
        cand: MT5SymbolSnapshot,
        side: str,
        now_utc: datetime,
        open_symbols: set[str],
        usd_dir_counts: dict[str, int],
        usd_bias: str,
        equity: float,
        free_margin: float,
        risk_scale: float,
    ) -> tuple[bool, str]:
        """
        Evalua TODOS los escudos deterministas ANTES de consultar a Gemini AI o ejecutar ESCUDO 5 (BUG-06).
        """
        if cand.margin_min_lot_usd > free_margin * 0.78:
            return False, f"MARGEN_INSUFICIENTE ({cand.margin_min_lot_usd:.2f} > {free_margin * 0.78:.2f})"

        active_block = self.get_active_block(cand.symbol)
        if active_block is not None:
            logger.info(
                "ESCUDO BLOQUEO ACTIVO: %s bloqueado %.1f min restantes (Cierre: %s, Prob. IA=%d%%). Motivo: %s",
                cand.symbol,
                active_block["remaining_minutes"],
                active_block["close_type"],
                active_block["probability_pct"],
                active_block["reason"],
            )
            return False, "ACTIVE_BLOCK"

        is_traditional = cand.symbol not in CRYPTO_SYMBOLS
        now_utc_minutes = now_utc.hour * 60 + now_utc.minute

        # Escudo Viernes >= 21:00 UTC (activos tradicionales)
        if is_traditional and now_utc.weekday() == 4 and now_utc.hour >= 21:
            logger.info("ESCUDO CIERRE VIERNES: Nueva entrada en %s omitida (Viernes >= 21:00 UTC).", cand.symbol)
            return False, "FRIDAY_CLOSE"

        # Escudo 10 Anti-Rollover 20:30 - 23:15 UTC (activos tradicionales)
        if is_traditional and self._is_pre_rollover_entry_blackout(now_utc):
            logger.info("ESCUDO 10 ANTI-ROLLOVER: Entrada en %s pausada (20:30 - 23:15 UTC).", cand.symbol)
            return False, "PRE_ROLLOVER"

        # Escudo 3 Fin de Semana Cripto
        if not is_traditional:
            wd = now_utc.weekday()
            is_weekend_crypto_block = (wd == 4 and now_utc.hour >= 21) or (wd == 5) or (wd == 6 and now_utc.hour < 22)
            if is_weekend_crypto_block:
                logger.info("ESCUDO 3 FIN DE SEMANA CRIPTO: Entrada pausada en %s hasta Domingo 22:00 UTC.", cand.symbol)
                return False, "CRYPTO_WEEKEND"

        # Escudo 2 Spread cap calibrado
        max_spread = MAX_ALLOWED_SPREAD_POINTS.get(cand.symbol, 30)
        if cand.spread_points > max_spread:
            logger.info(
                "ESCUDO 2 ANTI-NOTICIAS: Entrada pausada en %s por spread (%d > max %d).",
                cand.symbol,
                cand.spread_points,
                max_spread,
            )
            return False, "SPREAD_CAP"

        # Escudo 4 Nocturno 07:00 - 10:59 UTC (EURGBPm / NZDUSDm / AUDUSDm; libera Asia 02-06 UTC)
        if (7 <= now_utc.hour < 11) and cand.symbol in ("EURGBPm", "NZDUSDm", "AUDUSDm"):
            logger.info("ESCUDO 4 NOCTURNO (07:00-10:59 UTC): Entrada en %s pausada.", cand.symbol)
            return False, "NOCTURNAL_07_11"

        # Escudo 7 Apertura NY 14:25 - 14:55 UTC (08:25 - 08:55 CST, choque de campana Wall Street)
        if is_traditional and (14 * 60 + 25) <= now_utc_minutes <= (14 * 60 + 55):
            logger.info("ESCUDO 7 APERTURA NY (14:25-14:55 UTC): Entrada en %s pausada.", cand.symbol)
            return False, "NY_OPEN_1425_1455"

        # Escudo 8 London Fix 16:20 - 16:45 UTC (10:20 - 10:45 CST, rebalanceo EUR/GBP)
        if (16 * 60 + 20) <= now_utc_minutes <= (16 * 60 + 45) and cand.symbol in ("EURUSDm", "GBPUSDm", "EURJPYm", "EURGBPm"):
            logger.info("ESCUDO 8 LONDON FIX (16:20-16:45 UTC): Entrada en %s pausada.", cand.symbol)
            return False, "LONDON_FIX"

        # Block FX contra USD_STRONG
        cand_usd_dir = self._get_usd_direction(cand.symbol, side)
        if cand.symbol in FOREX_SYMBOLS:
            if (cand_usd_dir == "USD_LONG" and usd_bias == "USD_STRONG_BEARISH") or (
                cand_usd_dir == "USD_SHORT" and usd_bias == "USD_STRONG_BULLISH"
            ):
                logger.info(
                    "ESCUDO MACRO USD_STRONG: Entrada FX %s (%s -> %s) bloqueada contra %s.",
                    cand.symbol,
                    side,
                    cand_usd_dir,
                    usd_bias,
                )
                return False, "FX_VS_USD_STRONG"

        # Twin Cluster Cap max 1
        if self._is_twin_conflict(cand.symbol, open_symbols):
            logger.info("ESCUDO GEMELOS: Entrada en %s omitida porque su par gemelo ya esta abierto.", cand.symbol)
            return False, "TWIN_CLUSTER"

        # Correlacion USD max 2 (incluyendo XAUUSDm)
        if cand_usd_dir in usd_dir_counts and usd_dir_counts[cand_usd_dir] >= 2:
            logger.info(
                "ESCUDO CORRELACION USD: Entrada en %s (%s -> %s) omitida (%d >= 2 activas).",
                cand.symbol,
                side,
                cand_usd_dir,
                usd_dir_counts[cand_usd_dir],
            )
            return False, "USD_CORRELATION"

        # Pre-validacion calculate_safe_lot_and_sl (veto SL >20% + Spread/SL <= 12% M15 / <= 18% H1)
        pre_lot, pre_sl, _, _ = self.calculate_safe_lot_and_sl(
            snap=cand,
            side=side,
            equity_usd=equity,
            free_margin_usd=free_margin,
            ai_probability_pct=70,
            risk_scale=risk_scale,
        )
        if pre_lot <= 0.0 or pre_sl <= 0.0:
            return False, "SL_COMPRESSION_OR_SIZING_VETO"

        entry_px = cand.ask if side == "BUY" else cand.bid
        sl_dist = abs(entry_px - pre_sl)
        spread_px = cand.spread_points * cand.point if cand.point > 0 else max(0.0, cand.ask - cand.bid)
        max_sp_ratio = 0.12 if cand.entry_pillar.startswith("M15_SCALPER") else 0.18
        if sl_dist <= 0.0 or spread_px > max_sp_ratio * sl_dist:
            logger.info(
                "FILTRO SPREAD/SL: Entrada en %s omitida (spread=%.5f > %.0f%% de SL=%.5f).",
                cand.symbol,
                spread_px,
                max_sp_ratio * 100.0,
                sl_dist,
            )
            return False, "SPREAD_SL_RATIO"

        return True, "OK"

    def _process_adaptive_closed_trades(
        self,
        new_closes: list[dict[str, Any]],
        market_context: dict[str, Any],
        now_utc: datetime,
    ) -> list[dict[str, Any]]:
        """Registra cierres recientes en MT5KnowledgeDB con leccion post-mortem generada por IA."""
        assert self.knowledge_db is not None
        assert self.adaptive_brain is not None
        recorded: list[dict[str, Any]] = []
        current_session = classify_session(now_utc)

        for rc in new_closes:
            ticket = int(rc["ticket"])
            pos_id = int(rc.get("position_id") or ticket)
            sym = str(rc["symbol"])
            self.evaluated_deal_tickets.add(ticket)

            meta = self.position_meta.get(pos_id) or self.position_meta.get(ticket) or {}
            strategy_name = str(meta.get("strategy_name") or "LEGACY_H1")
            regime = str(meta.get("regime") or "ALL")
            session = str(meta.get("session") or current_session)
            entry_price = float(meta.get("entry_price") or 0.0)
            sl_price = meta.get("sl_price")
            tp_price = meta.get("tp_price")
            risk_usd = float(meta.get("risk_usd") or 0.0)
            entry_time = str(meta.get("entry_time") or "")
            profit_usd = float(rc.get("profit_usd") or 0.0)
            r_multiple = round(profit_usd / risk_usd, 3) if risk_usd > 0.0 else (1.0 if profit_usd > 0 else (-1.0 if profit_usd < 0 else 0.0))

            outcome_payload = {
                "ticket": ticket,
                "position_id": pos_id,
                "symbol": sym,
                "direction": str(rc.get("side") or "BUY"),
                "strategy_name": strategy_name,
                "regime": regime,
                "session": session,
                "entry_time": entry_time,
                "exit_time": str(rc.get("closed_at_utc") or utc_iso(now_utc) or ""),
                "entry_price": entry_price,
                "exit_price": float((rc.get("snapshot") or {}).get("bid") or 0.0),
                "sl_price": sl_price,
                "tp_price": tp_price,
                "profit_usd": profit_usd,
                "r_multiple": r_multiple,
                "close_reason": str(rc.get("close_type") or "CLOSED"),
            }

            try:
                lesson = self.adaptive_brain.generate_post_mortem_lesson(
                    trade_outcome=outcome_payload,
                    market_context=market_context,
                )
            except Exception as exc:
                logger.warning("AdaptiveAI: Error generando leccion post-mortem para %s #%d: %s", sym, ticket, exc)
                lesson = f"{sym} ({strategy_name}/{regime}) cerro {outcome_payload['close_reason']} (${profit_usd:+.2f}, {r_multiple:+.2f}R)."

            lesson_type = "WIN_PATTERN" if profit_usd > 0 else ("LOSS_AVOIDANCE" if profit_usd < 0 else "BREAKEVEN")
            row = self.knowledge_db.record_trade_outcome(
                ticket=ticket,
                symbol=sym,
                direction=outcome_payload["direction"],
                strategy_name=strategy_name,
                regime=regime,
                session=session,
                entry_time=outcome_payload["entry_time"],
                exit_time=outcome_payload["exit_time"],
                entry_price=outcome_payload["entry_price"],
                exit_price=outcome_payload["exit_price"],
                sl_price=sl_price,
                tp_price=tp_price,
                profit_usd=profit_usd,
                r_multiple=r_multiple,
                close_reason=outcome_payload["close_reason"],
                ai_lesson=lesson,
                lesson_type=lesson_type,
            )
            recorded.append(row)
            logger.info(
                "AdaptiveAI POST-MORTEM (%s #%d, %s, $%+.2f, %+.2fR): %s",
                sym,
                ticket,
                strategy_name,
                profit_usd,
                r_multiple,
                lesson,
            )

        if recorded:
            self._save_ai_state()
        return recorded

    def run_adaptive_cycle(
        self,
        cycle_num: int = 1,
        cycle_mode: str | None = None,
        due_symbols: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Ciclo adaptativo multi-estrategia + memoria SQLite + despertares exactos (SNIPER_WATCH / BASE_PATROL).
        Preserva TODOS los escudos deterministas de riesgo, spread, margen, correlacion y magic number.
        """
        self._init_adaptive_components()
        assert self.knowledge_db is not None
        assert self.strategy_engine is not None
        assert self.wake_scheduler is not None
        assert self.adaptive_brain is not None

        term, acc = self.ensure_connected()
        balance = float(acc.balance)
        equity = float(acc.equity)
        free_margin = float(acc.margin_free)

        raw_positions = mt5.positions_get() or ()
        open_symbols = {str(p.symbol) for p in raw_positions}
        open_pos_ids = {
            int(getattr(p, "ticket", 0) or 0) for p in raw_positions
        } | {
            int(getattr(p, "identifier", 0) or 0) for p in raw_positions
        }
        open_pos_ids.discard(0)

        now_utc = datetime.now(timezone.utc)
        current_session = classify_session(now_utc)

        # Podar watches expirados en scheduler y sincronizar estado EXPIRED a SQLite
        expired_watches = self.wake_scheduler.prune_expired(now_utc=now_utc)
        for ew in expired_watches:
            self.knowledge_db.update_watch_status(
                watch_id=ew.watch_id,
                status="EXPIRED",
                outcome_note=ew.outcome_note or "Watch expirado por TTL",
            )

        due_watches = self.wake_scheduler.get_due_watches(now_utc=now_utc, grace_seconds=30.0)
        resolved_mode = (cycle_mode or ("SNIPER_WATCH" if due_watches else "BASE_PATROL")).upper()
        if resolved_mode not in ("BASE_PATROL", "SNIPER_WATCH"):
            resolved_mode = "BASE_PATROL"

        sniper_symbols: list[str] = []
        if due_symbols:
            sniper_symbols.extend(due_symbols)
        for w in due_watches:
            if w.symbol not in sniper_symbols:
                sniper_symbols.append(w.symbol)

        logger.info(
            "=== Ciclo Adaptativo MT5 #%d [%s] | Cuenta %s (%s) | Balance: $%.2f | Equity: $%.2f | Margen: $%.2f ===",
            cycle_num,
            resolved_mode,
            acc.login,
            acc.server,
            balance,
            equity,
            free_margin,
        )

        snapshots = self.build_snapshots(free_margin_usd=free_margin, open_symbols=open_symbols)
        snapshots_map = {s.symbol: s for s in snapshots}
        daily_guard = self._evaluate_daily_risk_guard(
            now_utc=now_utc,
            equity_usd=equity,
            open_position_ids=open_pos_ids,
            known_bot_pos_ids=self.known_bot_pos_ids,
        )
        protection_active = daily_guard.get("protection_mode") == "MODO_PROTECCION_CAPITAL"
        market_context = self.build_global_market_context(snapshots, daily_guard)
        market_context["session"] = current_session
        market_context["cycle_mode"] = resolved_mode

        # 1. Procesar cierres recientes y actualizar aprendizaje bayesiano + lecciones
        recent_closes = self._collect_recent_closed_deals(
            snapshots_map=snapshots_map,
            minutes_back=90,
            now_utc=now_utc,
            open_position_ids=open_pos_ids,
            known_bot_pos_ids=self.known_bot_pos_ids,
        )
        new_closes = [rc for rc in recent_closes if int(rc["ticket"]) not in self.evaluated_deal_tickets]
        recorded_outcomes = self._process_adaptive_closed_trades(
            new_closes=new_closes,
            market_context=market_context,
            now_utc=now_utc,
        )

        # 2. Gestionar posiciones abiertas (Break-Even, Trailing, Chandelier, etc.)
        open_positions_data, open_metrics_by_ticket = self._build_open_positions_metrics(raw_positions, snapshots_map)
        executed_actions = self.manage_open_positions(snapshots_map, open_reviews=None)

        # Refrescar posiciones y cuenta tras gestion activa
        raw_positions = mt5.positions_get() or ()
        open_symbols = {str(p.symbol) for p in raw_positions}
        acc = mt5.account_info() or acc
        free_margin = float(acc.margin_free)
        equity = float(acc.equity)
        open_positions_data, open_metrics_by_ticket = self._build_open_positions_metrics(raw_positions, snapshots_map)

        effective_max_positions = 3 if equity >= 28.0 else self.max_open_positions
        if protection_active:
            effective_max_positions = min(effective_max_positions, int(daily_guard["max_positions"]))

        usd_dir_counts = {"USD_LONG": 0, "USD_SHORT": 0}
        for p in raw_positions:
            p_side = "BUY" if p.type == mt5.POSITION_TYPE_BUY else "SELL"
            u_dir = self._get_usd_direction(str(p.symbol), p_side)
            if u_dir in usd_dir_counts:
                usd_dir_counts[u_dir] += 1

        # 3. Evaluar universo de simbolos con MT5StrategyEngine
        if resolved_mode == "SNIPER_WATCH" and sniper_symbols:
            eval_symbols = [sym for sym in sniper_symbols if sym in snapshots_map]
        else:
            eval_symbols = [s.symbol for s in snapshots]

        strategy_signals: list[StrategySignal] = []
        regime_by_symbol: dict[str, RegimeSnapshot] = {}
        best_signal_by_symbol: dict[str, StrategySignal] = {}
        memory_context_by_symbol: dict[str, dict[str, Any]] = {}

        for sym in eval_symbols:
            snap = snapshots_map.get(sym)
            if snap is None:
                continue
            candles = self._fetch_candles(sym, mt5.TIMEFRAME_H1, count=300)
            if len(candles) < 60:
                continue
            regime_snap, signals = self.strategy_engine.evaluate_symbol(
                symbol=sym,
                candles=candles,
                digits=snap.digits,
                point=snap.point,
            )
            regime_by_symbol[sym] = regime_snap
            actionable = [sig for sig in signals if sig.setup_stage in ("READY", "FORMING") and sig.direction in ("BUY", "SELL")]
            best_sig = self.strategy_engine.select_best_signal(actionable) if actionable else self.strategy_engine.select_best_signal(signals)
            if best_sig is not None:
                best_signal_by_symbol[sym] = best_sig
            if actionable:
                strategy_signals.extend(actionable)
            elif sym in sniper_symbols and best_sig is not None:
                strategy_signals.append(best_sig)

            memory_context_by_symbol[sym] = self.knowledge_db.build_ai_memory_context(
                symbol=sym,
                regime=regime_snap.regime,
                session=current_session,
            )

        active_watches_payload = list(self.wake_scheduler.to_dict().get("active_watches", []))

        # 4. Consultar al cerebro adaptativo MT5AdaptiveAIBrain
        adaptive_decision = self.adaptive_brain.evaluate_market_cycle(
            market_context=market_context,
            strategy_signals=strategy_signals,
            memory_context=memory_context_by_symbol,
            active_watches=active_watches_payload,
            open_positions=open_positions_data,
            cycle_mode=resolved_mode,
            now_utc=now_utc,
            min_wake_minutes=1.0,
            max_wake_minutes=float(self.base_interval_minutes),
        )

        # 5. Ejecutar decisiones preservando TODOS los guardrails y actualizando SQLite + Scheduler
        usd_bias = str((market_context.get("usd_strength") or {}).get("usd_bias", "USD_MIXED"))
        risk_scale_now = float(daily_guard.get("risk_scale", 1.0)) if protection_active else 1.0

        # Ordenar entradas por mayor confianza primero
        ordered_decisions = sorted(
            adaptive_decision.decisions.items(),
            key=lambda kv: (0 if kv[1].action in ("ENTER_BUY", "ENTER_SELL") else 1, -int(kv[1].confidence_pct)),
        )

        for sym, dec in ordered_decisions:
            regime_str = regime_by_symbol[sym].regime if sym in regime_by_symbol else "ALL"
            best_sig = best_signal_by_symbol.get(sym)
            setup_stage = best_sig.setup_stage if best_sig is not None else "NONE"
            snap = snapshots_map.get(sym)

            # Registrar cada decision en decision_journal
            self.knowledge_db.record_decision(
                symbol=sym,
                regime=regime_str,
                session=current_session,
                action=dec.action,
                strategy_name=dec.strategy_name or (best_sig.strategy_name if best_sig else ""),
                confidence=float(dec.confidence_pct),
                setup_stage=setup_stage,
                next_wake_utc=dec.wake_at_utc,
                reasoning=dec.reasoning,
                snapshot=asdict(snap) if snap is not None else None,
                ts_utc=utc_iso(now_utc),
            )

            if dec.action in ("ENTER_BUY", "ENTER_SELL"):
                if snap is None or sym in open_symbols:
                    continue
                if daily_guard.get("pause_new_entries"):
                    logger.info("AdaptiveAI: Entrada %s bloqueada por PAUSA DIARIA.", sym)
                    continue
                if len(open_symbols) >= effective_max_positions:
                    logger.info("AdaptiveAI: Entrada %s omitida (max_open_positions=%d alcanzado).", sym, effective_max_positions)
                    continue
                elapsed_since_last = time.time() - self.last_order_timestamp
                if self.last_order_timestamp > 0 and elapsed_since_last < 120.0:
                    logger.info("AdaptiveAI: Entrada %s bloqueada por ESCUDO 1 de espaciado (%.1fm < 2.0m).", sym, elapsed_since_last / 60.0)
                    continue

                req_conf = max(self.min_ai_confidence, int(daily_guard.get("min_ai_prob", self.min_ai_confidence))) if protection_active else self.min_ai_confidence
                if int(dec.confidence_pct) < req_conf:
                    logger.info("AdaptiveAI: Entrada %s rechazada por confianza (%d%% < %d%%).", sym, dec.confidence_pct, req_conf)
                    continue

                side = "BUY" if dec.action == "ENTER_BUY" else "SELL"
                shields_ok, shield_reason = self._passes_deterministic_shields(
                    cand=snap,
                    side=side,
                    now_utc=now_utc,
                    open_symbols=open_symbols,
                    usd_dir_counts=usd_dir_counts,
                    usd_bias=usd_bias,
                    equity=equity,
                    free_margin=free_margin,
                    risk_scale=risk_scale_now,
                )
                if not shields_ok:
                    logger.info("AdaptiveAI: Entrada %s (%s) bloqueada por escudo determinista: %s", sym, side, shield_reason)
                    continue

                lot, sl_price, tp_price, risk_usd = self.calculate_safe_lot_and_sl(
                    snap=snap,
                    side=side,
                    equity_usd=equity,
                    free_margin_usd=free_margin,
                    ai_probability_pct=int(dec.confidence_pct),
                    risk_scale=risk_scale_now,
                )
                if lot <= 0.0 or sl_price <= 0.0:
                    continue

                # Aplicar ajuste opcional de TP/SL de la IA solo si mantiene SL seguro y RR >= 1.2
                entry_px = snap.ask if side == "BUY" else snap.bid
                if dec.tp_adjustment is not None:
                    adj_tp = round(float(dec.tp_adjustment), snap.digits)
                    sl_dist = abs(entry_px - sl_price)
                    if (side == "BUY" and adj_tp > entry_px + sl_dist * 1.2) or (side == "SELL" and adj_tp < entry_px - sl_dist * 1.2):
                        tp_price = adj_tp

                strat_label = dec.strategy_name or (best_sig.strategy_name if best_sig else "ADAPTIVE_AI")
                reason = (
                    f"AdaptiveAI [{strat_label}/{regime_str}] Conf={dec.confidence_pct}% "
                    f"(Riesgo ~${risk_usd:.2f} USD) | {dec.reasoning[:120]}"
                )
                trade = self._place_mt5_order(
                    snap=snap,
                    side=side,
                    lot=lot,
                    sl_price=sl_price,
                    tp_price=tp_price,
                    reason=reason,
                    risk_usd=risk_usd,
                )
                if trade:
                    executed_actions.append(trade)
                    open_symbols.add(sym)
                    cand_usd_dir = self._get_usd_direction(sym, side)
                    if cand_usd_dir in usd_dir_counts:
                        usd_dir_counts[cand_usd_dir] += 1
                    used_margin = snap.margin_min_lot_usd * (lot / snap.min_lot) if snap.min_lot > 0 else snap.margin_min_lot_usd
                    free_margin = max(0.0, free_margin - used_margin)

                    # Guardar metadatos de estrategia/regimen/sesion para post-mortem futuro
                    ticket = int(trade.get("ticket") or 0)
                    if ticket > 0:
                        meta = self.position_meta.setdefault(ticket, {})
                        meta.update(
                            {
                                "strategy_name": strat_label,
                                "regime": regime_str,
                                "session": current_session,
                                "entry_price": float(trade.get("price") or entry_px),
                                "sl_price": sl_price,
                                "tp_price": tp_price,
                                "risk_usd": risk_usd,
                                "entry_time": utc_iso(now_utc),
                            }
                        )
                        self._save_ai_state()

                    # Si habia un watch activo en este simbolo, marcarlo TRIGGERED
                    if self.wake_scheduler.has_active_watch(sym):
                        triggered = self.wake_scheduler.confirm_trigger(
                            sym,
                            outcome_note=f"Entrada {side} ejecutada ({strat_label})",
                            now_utc=now_utc,
                        )
                        if triggered is not None:
                            self.knowledge_db.update_watch_status(
                                watch_id=triggered.watch_id,
                                status="TRIGGERED",
                                outcome_note=triggered.outcome_note,
                            )

            elif dec.action == "WATCH_EXACT":
                watch = self.wake_scheduler.register_watch(
                    symbol=sym,
                    strategy_name=dec.strategy_name or (best_sig.strategy_name if best_sig else "ADAPTIVE_WATCH"),
                    wake_at_utc=dec.wake_at_utc,
                    wake_in_minutes=dec.wake_in_minutes,
                    hypothesis=dec.watch_hypothesis or dec.reasoning,
                    trigger_condition=dec.trigger_condition,
                    invalidation_condition=dec.invalidation_condition,
                    now_utc=now_utc,
                )
                self.knowledge_db.upsert_watch(
                    watch_id=watch.watch_id,
                    symbol=watch.symbol,
                    strategy_name=watch.strategy_name,
                    wake_at_utc=utc_iso(watch.wake_at_utc) or "",
                    hypothesis=watch.hypothesis,
                    trigger_condition=watch.trigger_condition,
                    invalidation_condition=watch.invalidation_condition,
                    postpone_count=watch.postpone_count,
                    max_postpones=watch.max_postpones,
                    status=watch.status,
                    outcome_note=watch.outcome_note,
                    created_at_utc=utc_iso(watch.created_at_utc),
                    updated_at_utc=utc_iso(watch.updated_at_utc),
                )
                logger.info(
                    "AdaptiveAI WATCH_EXACT (%s, %s): despertar exacto a %s | %s",
                    sym,
                    watch.strategy_name,
                    utc_iso(watch.wake_at_utc),
                    watch.hypothesis[:100],
                )

            elif dec.action == "POSTPONE_WATCH":
                updated = self.wake_scheduler.postpone_watch(
                    symbol=sym,
                    new_wake_at_utc=dec.wake_at_utc,
                    wake_in_minutes=dec.wake_in_minutes,
                    hypothesis=dec.watch_hypothesis or None,
                    trigger_condition=dec.trigger_condition or None,
                    invalidation_condition=dec.invalidation_condition or None,
                    note=dec.reasoning,
                    now_utc=now_utc,
                )
                if updated is not None:
                    self.knowledge_db.update_watch_status(
                        watch_id=updated.watch_id,
                        status=updated.status,
                        outcome_note=updated.outcome_note,
                        wake_at_utc=utc_iso(updated.wake_at_utc),
                        increment_postpone=True,
                    )
                    logger.info(
                        "AdaptiveAI POSTPONE_WATCH (%s): status=%s (%d/%d) -> proximo despertar %s",
                        sym,
                        updated.status,
                        updated.postpone_count,
                        updated.max_postpones,
                        utc_iso(updated.wake_at_utc),
                    )

            elif dec.action == "INVALIDATE_WATCH":
                inv = self.wake_scheduler.invalidate_watch(
                    symbol=sym,
                    reason=dec.reasoning or "Setup invalidado por IA",
                    now_utc=now_utc,
                )
                if inv is not None:
                    self.knowledge_db.update_watch_status(
                        watch_id=inv.watch_id,
                        status="INVALIDATED",
                        outcome_note=inv.outcome_note,
                    )
                lesson_text = (dec.lesson_note or dec.reasoning or "").strip()
                if lesson_text:
                    self.knowledge_db.add_lesson(
                        symbol=sym,
                        strategy_name=dec.strategy_name or (best_sig.strategy_name if best_sig else "ALL"),
                        regime=regime_str,
                        lesson_text=lesson_text,
                        lesson_type="WATCH_INVALIDATED",
                    )
                logger.info("AdaptiveAI INVALIDATE_WATCH (%s): retorno a patrulla base | %s", sym, dec.reasoning[:100])

            else:
                # HOLD
                if dec.lesson_note:
                    self.knowledge_db.add_lesson(
                        symbol=sym,
                        strategy_name=dec.strategy_name or "ALL",
                        regime=regime_str,
                        lesson_text=dec.lesson_note,
                        lesson_type="CYCLE_OBSERVATION",
                    )

        next_plan = self.wake_scheduler.next_wakeup_plan(now_utc=datetime.now(timezone.utc))

        # Construir resumen compatible para el reporte markdown
        report_ai_eval = MT5AICycleEvaluation(
            market_summary=adaptive_decision.market_summary,
            open_reviews={},
            candidate_evals={},
            closed_evals={},
            priority_tier=adaptive_decision.priority_tier,
            model_used=adaptive_decision.model_used,
        )
        self._write_markdown_report(
            cycle_num,
            acc,
            raw_positions,
            snapshots,
            executed_actions,
            ai_eval=report_ai_eval,
            open_metrics_by_ticket=open_metrics_by_ticket,
            market_context=market_context,
        )

        return {
            "cycle": cycle_num,
            "adaptive_ai": True,
            "cycle_mode": resolved_mode,
            "account": int(acc.login),
            "server": str(acc.server),
            "balance_usd": round(balance, 2),
            "equity_usd": round(equity, 2),
            "free_margin_usd": round(free_margin, 2),
            "open_positions": list(open_symbols),
            "executed_actions": executed_actions,
            "recorded_outcomes": len(recorded_outcomes),
            "candidates_scanned": len(eval_symbols),
            "signals_evaluated": len(strategy_signals),
            "daily_risk_guard": daily_guard,
            "ai_priority": adaptive_decision.priority_tier,
            "ai_model": adaptive_decision.model_used,
            "adaptive_decisions": {k: v.to_dict() for k, v in adaptive_decision.decisions.items()},
            "next_wake_plan": next_plan.to_dict(),
        }

    def run_cycle(
        self,
        cycle_num: int = 1,
        cycle_mode: str | None = None,
        due_symbols: list[str] | None = None,
    ) -> dict[str, Any]:
        if self.adaptive_ai:
            return self.run_adaptive_cycle(
                cycle_num=cycle_num,
                cycle_mode=cycle_mode,
                due_symbols=due_symbols,
            )
        term, acc = self.ensure_connected()
        balance = float(acc.balance)
        equity = float(acc.equity)
        free_margin = float(acc.margin_free)

        raw_positions = mt5.positions_get() or ()
        open_symbols = {str(p.symbol) for p in raw_positions}
        open_pos_ids = {
            int(getattr(p, "ticket", 0) or 0) for p in raw_positions
        } | {
            int(getattr(p, "identifier", 0) or 0) for p in raw_positions
        }
        open_pos_ids.discard(0)

        logger.info(
            "=== Ciclo MT5 #%d | Cuenta Exness %s (%s) | Balance: $%.2f USD | Equity: $%.2f USD | Margen Libre: $%.2f USD ===",
            cycle_num,
            acc.login,
            acc.server,
            balance,
            equity,
            free_margin,
        )

        now_utc = datetime.now(timezone.utc)
        snapshots = self.build_snapshots(free_margin_usd=free_margin, open_symbols=open_symbols)
        snapshots_map = {s.symbol: s for s in snapshots}
        sym_perf_map = self._compute_symbol_performance_14d(
            now_utc=now_utc,
            open_position_ids=open_pos_ids,
            equity_usd=equity,
        )
        daily_guard = self._evaluate_daily_risk_guard(
            now_utc=now_utc,
            equity_usd=equity,
            open_position_ids=open_pos_ids,
            known_bot_pos_ids=self.known_bot_pos_ids,
        )
        protection_active = daily_guard.get("protection_mode") == "MODO_PROTECCION_CAPITAL"
        if protection_active:
            logger.info(
                "CANDADO DIARIO ACTIVO (%s): PnL UTC $%+.2f | Racha perdidas=%d | Min IA=%d%% | Escala=%.2fx | MaxPos=%d | %s",
                daily_guard.get("protection_mode"),
                float(daily_guard.get("daily_closed_pnl_usd", 0.0)),
                int(daily_guard.get("consecutive_losses", 0)),
                int(daily_guard.get("min_ai_prob", 62)),
                float(daily_guard.get("risk_scale", 0.75)),
                int(daily_guard.get("max_positions", 3)),
                daily_guard.get("reason", ""),
            )
        market_context = self.build_global_market_context(snapshots, daily_guard)

        # Recolectar cierres COMPLETOS de los ultimos 90 minutos (excluyendo open_pos_ids)
        recent_closes = self._collect_recent_closed_deals(
            snapshots_map=snapshots_map,
            minutes_back=90,
            now_utc=now_utc,
            open_position_ids=open_pos_ids,
            known_bot_pos_ids=self.known_bot_pos_ids,
        )
        latest_close_by_sym: dict[str, dict[str, Any]] = {}
        for rc in recent_closes:
            latest_close_by_sym[rc["symbol"]] = rc

        open_positions_data, open_metrics_by_ticket = self._build_open_positions_metrics(raw_positions, snapshots_map)
        # P1_SAFE_CORE: Regla de Rotacion de Capital desactivada (evita cortar ganadoras por bug 'WATCH')
        rotatable_positions: list[Any] = []

        # Capacidad de posiciones simultaneas (concentrado a max 3 entradas de alta conviccion)
        if equity >= 28.0:
            effective_max_positions = 3
        else:
            effective_max_positions = self.max_open_positions
        if protection_active:
            effective_max_positions = min(effective_max_positions, int(daily_guard["max_positions"]))

        # Contar exposicion actual por direccion del Dolar (incluyendo XAUUSDm)
        usd_dir_counts = {"USD_LONG": 0, "USD_SHORT": 0}
        for p in raw_positions:
            p_side = "BUY" if p.type == mt5.POSITION_TYPE_BUY else "SELL"
            u_dir = self._get_usd_direction(str(p.symbol), p_side)
            if u_dir in usd_dir_counts:
                usd_dir_counts[u_dir] += 1

        # === TODOS LOS ESCUDOS DETERMINISTAS ANTES DE candidates_data / GEMINI / ESCUDO 5 ===
        usd_bias = str((market_context.get("usd_strength") or {}).get("usd_bias", "USD_MIXED"))
        risk_scale_now = float(daily_guard.get("risk_scale", 1.0)) if protection_active else 1.0
        elapsed_since_last_entry = time.time() - self.last_order_timestamp
        spacing_blocked = self.last_order_timestamp > 0 and elapsed_since_last_entry < 120.0

        eligible_candidates: list[MT5SymbolSnapshot] = []
        candidates_data: list[dict[str, Any]] = []
        if daily_guard.get("pause_new_entries"):
            logger.info(
                "PAUSA DIARIA ACTIVA: Se omiten nuevas entradas (PnL UTC: $%+.2f | Racha=%d | Restante=%.1fm).",
                float(daily_guard.get("daily_closed_pnl_usd", 0.0)),
                int(daily_guard.get("consecutive_losses", 0)),
                float(daily_guard.get("pause_remaining_mins", 0.0)),
            )
        elif spacing_blocked:
            logger.info(
                "ESCUDO 1 DE ESPACIADO: Esperando cooldown post-entrada (%.1f min < 2.0 min requeridos).",
                elapsed_since_last_entry / 60.0,
            )
        elif len(open_symbols) < effective_max_positions or len(rotatable_positions) > 0:
            pre_candidates = [
                s for s in snapshots if s.strategy_setup in ("LONG_ENTRY", "SHORT_ENTRY") and s.symbol not in open_symbols
            ]
            for cand in pre_candidates:
                cand_side = "BUY" if cand.strategy_setup == "LONG_ENTRY" else "SELL"
                ok, _ = self._passes_deterministic_shields(
                    cand=cand,
                    side=cand_side,
                    now_utc=now_utc,
                    open_symbols=open_symbols,
                    usd_dir_counts=usd_dir_counts,
                    usd_bias=usd_bias,
                    equity=equity,
                    free_margin=free_margin,
                    risk_scale=risk_scale_now,
                )
                if not ok:
                    continue
                eligible_candidates.append(cand)
                candidates_data.append(
                    {
                        "symbol": cand.symbol,
                        "side": cand_side,
                        "entry_pillar": cand.entry_pillar,
                        "snapshot": asdict(cand),
                        "recent_close": latest_close_by_sym.get(cand.symbol),
                        "symbol_perf": sym_perf_map.get(cand.symbol),
                    }
                )

        # === POLITICA EVENT-DRIVEN IA (0 llamadas API cuando no hay eventos reales) ===
        new_closes = [rc for rc in recent_closes if rc["ticket"] not in self.evaluated_deal_tickets]
        has_neg_or_manual_close = any(rc["close_type"] in ("NEGATIVE", "MANUAL") for rc in new_closes)

        if self.last_ai_eval is None:
            open_set_changed = bool(open_symbols)
        else:
            open_set_changed = set(open_symbols) != set(self.last_ai_eval.open_reviews.keys())

        atr_milestone_triggered = False
        cur_atr_buckets: dict[int, int] = {}
        cur_sl_danger: dict[int, bool] = {}
        for p_item in open_positions_data:
            t_id = int(p_item["ticket"])
            m_atr = float(p_item.get("move_atr", 0.0))
            rem_sl = float(p_item.get("rem_sl_in_atr1h", 1.0))
            p_usd = float(p_item.get("profit_usd", 0.0))
            bucket = sum(1 for thr in (0.75, 1.25, 1.75, 2.5) if m_atr >= thr)
            cur_atr_buckets[t_id] = bucket
            prev_bucket = self._last_ai_atr_milestones.get(t_id, 0)
            prev_danger = self._last_ai_sl_danger.get(t_id, False)

            if bucket > prev_bucket:
                atr_milestone_triggered = True

            # Edge-triggered con histeresis y solo en perdida (evita spam HP en BE/Chandelier o M15 con SL ajustado)
            if p_usd < 0.0 and rem_sl <= 0.45:
                if not prev_danger:
                    atr_milestone_triggered = True
                cur_sl_danger[t_id] = True
            elif prev_danger and (p_usd >= 0.0 or rem_sl > 0.55):
                cur_sl_danger[t_id] = False
            else:
                cur_sl_danger[t_id] = prev_danger

        self._last_ai_sl_danger = cur_sl_danger

        cur_macro_sig = (
            usd_bias,
            str((market_context.get("crypto_pulse") or {}).get("crypto_regime", "")),
            str((market_context.get("indices_pulse") or {}).get("indices_regime", "")),
            bool((market_context.get("news_and_session") or {}).get("news_volatility_alert", False)),
        )
        macro_regime_changed = (
            bool(open_positions_data)
            and (self._last_ai_macro_sig is not None)
            and (cur_macro_sig != self._last_ai_macro_sig)
        )
        heartbeat_triggered = bool(open_positions_data) and (time.time() - self.last_ai_eval_ts) >= 900.0

        trigger_parts: list[str] = []
        if candidates_data:
            trigger_parts.append("CANDIDATES")
        if new_closes:
            trigger_parts.append("NEW_CLOSES")
        if open_set_changed:
            trigger_parts.append("OPEN_SET_CHANGED")
        if atr_milestone_triggered:
            trigger_parts.append("ATR_MILESTONE")
        if macro_regime_changed:
            trigger_parts.append("MACRO_CHANGE")
        if heartbeat_triggered:
            trigger_parts.append("HEARTBEAT_900S")

        should_refresh_ai = bool(trigger_parts)
        trigger_reason = "+".join(trigger_parts) if trigger_parts else "IDLE"
        is_high_priority_cycle = bool(
            candidates_data
            or has_neg_or_manual_close
            or open_set_changed
            or atr_milestone_triggered
        )

        if should_refresh_ai:
            closes_for_ai = new_closes if new_closes else []
            ai_eval = self.ai_agent.evaluate_mt5_market(
                open_positions_data=open_positions_data,
                candidates_data=candidates_data,
                recent_closes_data=closes_for_ai,
                high_priority=is_high_priority_cycle,
                market_context=market_context,
                trigger_reason=trigger_reason,
            )
            self.last_ai_eval = ai_eval
            self.last_ai_eval_ts = time.time()
            self._last_ai_macro_sig = cur_macro_sig
            self._last_ai_atr_milestones = cur_atr_buckets
        elif open_symbols and self.last_ai_eval is not None:
            ai_eval = self.last_ai_eval
        else:
            ai_eval = MT5AICycleEvaluation(
                market_summary="Sin eventos relevantes en este ciclo (0 llamadas API, event-driven).",
                open_reviews={},
                candidate_evals={},
                closed_evals={},
                priority_tier="GENERAL",
                model_used="quant_local",
            )

        # Procesar cierres recientes completos evaluados por IA (P1_SAFE_CORE: POSITIVE -> 0m; NEGATIVE/MANUAL -> 45m)
        if new_closes:
            processed_syms: set[str] = set()
            for rc in new_closes:
                self.evaluated_deal_tickets.add(int(rc["ticket"]))
            for rc in reversed(new_closes):
                sym = rc["symbol"]
                if sym in processed_syms:
                    continue
                processed_syms.add(sym)
                ceval = ai_eval.closed_evals.get(sym)
                if ceval is None:
                    continue
                if rc["close_type"] == "POSITIVE":
                    logger.info(
                        "EVALUACION IA POST-CIERRE (%s #%d, POSITIVE $%+.2f): Probabilidad=%d%% -> HABILITADO (0m cooldown post-positivo) | %s",
                        sym,
                        rc["ticket"],
                        rc["profit_usd"],
                        ceval.reactivate_probability_pct,
                        ceval.reasoning,
                    )
                    decision_status = "HABILITADO (0m post-positivo)"
                elif ceval.reactivate_probability_pct < 60 or ceval.should_block_90m:
                    base_cooldown_mins = 45.0
                    remaining_mins = base_cooldown_mins - float(rc["mins_since_close"])
                    if remaining_mins > 0.5:
                        self.block_symbol_90m(
                            symbol=sym,
                            probability_pct=ceval.reactivate_probability_pct,
                            close_type=rc["close_type"],
                            profit_usd=float(rc["profit_usd"]),
                            reason=ceval.reasoning,
                            duration_minutes=remaining_mins,
                        )
                        logger.info(
                            "EVALUACION IA POST-CIERRE (%s #%d, %s $%+.2f): Probabilidad=%d%% (< 60%%) -> BLOQUEADO %.1f min | %s",
                            sym,
                            rc["ticket"],
                            rc["close_type"],
                            rc["profit_usd"],
                            ceval.reactivate_probability_pct,
                            remaining_mins,
                            ceval.reasoning,
                        )
                        decision_status = f"BLOQUEADO {int(base_cooldown_mins)}m"
                    else:
                        logger.info(
                            "EVALUACION IA POST-CIERRE (%s #%d, %s $%+.2f): Cooldown 45m ya cumplido (%.1fm) -> HABILITADO",
                            sym,
                            rc["ticket"],
                            rc["close_type"],
                            rc["profit_usd"],
                            float(rc["mins_since_close"]),
                        )
                        decision_status = "HABILITADO (45m cumplidos)"
                else:
                    logger.info(
                        "EVALUACION IA POST-CIERRE (%s #%d, %s $%+.2f): Probabilidad=%d%% (>= 60%%) -> HABILITADO para reactivacion si confirma setup | %s",
                        sym,
                        rc["ticket"],
                        rc["close_type"],
                        rc["profit_usd"],
                        ceval.reactivate_probability_pct,
                        ceval.reasoning,
                    )
                    decision_status = "HABILITADO (>=60%)"

                self.recent_ai_close_decisions.append(
                    {
                        "evaluated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                        "ticket": rc["ticket"],
                        "symbol": sym,
                        "close_type": rc["close_type"],
                        "profit_usd": rc["profit_usd"],
                        "probability_pct": ceval.reactivate_probability_pct,
                        "status": decision_status,
                        "reason": ceval.reasoning,
                    }
                )
            self._save_ai_state()

        executed_actions = self.manage_open_positions(snapshots_map, open_reviews=ai_eval.open_reviews)

        # Refrescar posiciones y margen tras posibles cierres
        raw_positions = mt5.positions_get() or ()
        open_symbols = {str(p.symbol) for p in raw_positions}
        acc = mt5.account_info() or acc
        free_margin = float(acc.margin_free)
        equity = float(acc.equity)
        _, open_metrics_by_ticket = self._build_open_positions_metrics(raw_positions, snapshots_map)

        # Recalcular exposicion USD actual
        usd_dir_counts = {"USD_LONG": 0, "USD_SHORT": 0}
        for p in raw_positions:
            p_side = "BUY" if p.type == mt5.POSITION_TYPE_BUY else "SELL"
            u_dir = self._get_usd_direction(str(p.symbol), p_side)
            if u_dir in usd_dir_counts:
                usd_dir_counts[u_dir] += 1

        # Ordenar SOLO los candidatos elegibles post-escudos por mayor probabilidad IA primero
        entry_candidates = [c for c in eligible_candidates if c.symbol not in open_symbols]
        entry_candidates.sort(
            key=lambda s: (
                ai_eval.candidate_evals[s.symbol].win_probability_pct
                if s.symbol in ai_eval.candidate_evals
                else 0
            ),
            reverse=True,
        )

        for cand in entry_candidates:
            need_rotation = len(open_symbols) >= effective_max_positions
            if need_rotation and not rotatable_positions:
                break

            # Revalidar ESCUDO 1 (2m spacing) por si ya abrimos una orden en este mismo ciclo
            elapsed_since_last_entry = time.time() - self.last_order_timestamp
            if self.last_order_timestamp > 0 and elapsed_since_last_entry < 120.0:
                logger.info(
                    "ESCUDO 1 DE ESPACIADO: Esperando cooldown post-entrada (%.1f min < 2.0 min requeridos).",
                    elapsed_since_last_entry / 60.0,
                )
                break

            side = "BUY" if cand.strategy_setup == "LONG_ENTRY" else "SELL"
            cand_usd_dir = self._get_usd_direction(cand.symbol, side)
            if not need_rotation:
                if cand.margin_min_lot_usd > free_margin * 0.78:
                    continue
                if self._is_twin_conflict(cand.symbol, open_symbols):
                    continue
                if cand_usd_dir in usd_dir_counts and usd_dir_counts[cand_usd_dir] >= 2:
                    continue

            # === ESCUDO 5 FILTRO IA (SOLO SOBRE CANDIDATOS QUE YA PASARON TODOS LOS ESCUDOS DETERMINISTAS) ===
            cand_eval = ai_eval.candidate_evals.get(cand.symbol)
            req_prob = cand_eval.required_probability_pct if cand_eval is not None else 55
            if protection_active:
                req_prob = max(req_prob, int(daily_guard["min_ai_prob"]))
            if cand_eval is not None and (cand_eval.win_probability_pct < req_prob or cand_eval.should_block_90m):
                last_close = latest_close_by_sym.get(cand.symbol)
                c_type = last_close["close_type"] if last_close else "LOW_PROB_CANDIDATE"
                c_profit = float(last_close["profit_usd"]) if last_close else 0.0
                # P1_SAFE_CORE: LOW_PROB_CANDIDATE limitado a 20m (nunca 30m/90m); NEGATIVE/MANUAL a 45m
                block_mins = 20.0 if c_type in ("LOW_PROB_CANDIDATE", "POSITIVE") else 45.0
                self.block_symbol_90m(
                    symbol=cand.symbol,
                    probability_pct=cand_eval.win_probability_pct,
                    close_type=c_type,
                    profit_usd=c_profit,
                    reason=cand_eval.reasoning,
                    duration_minutes=block_mins,
                )
                logger.info(
                    "ESCUDO 5 FILTRO IA: Entrada en %s rechazada (Prob=%d%% < umbral %d%%) -> BLOQUEADO %.0f min | %s",
                    cand.symbol,
                    cand_eval.win_probability_pct,
                    req_prob,
                    block_mins,
                    cand_eval.reasoning,
                )
                continue

            cand_prob = cand_eval.win_probability_pct if cand_eval is not None else 70
            if need_rotation:
                # Exigir alta conviccion (>= 68%) para rotar una operacion estancada en ganancia
                if cand_prob < 68:
                    continue
                rotated_pos = None
                for st_pos in rotatable_positions:
                    st_sym = str(st_pos.symbol)
                    if st_sym not in open_symbols:
                        continue
                    rem_open = open_symbols - {st_sym}
                    if self._is_twin_conflict(cand.symbol, rem_open):
                        continue
                    st_side = "BUY" if st_pos.type == mt5.POSITION_TYPE_BUY else "SELL"
                    st_u_dir = self._get_usd_direction(st_sym, st_side)
                    rem_usd_count = usd_dir_counts.get(cand_usd_dir, 0) - (1 if st_u_dir == cand_usd_dir else 0)
                    if cand_usd_dir in usd_dir_counts and rem_usd_count >= 2:
                        continue
                    rotated_pos = st_pos
                    break

                if rotated_pos is None:
                    continue

                st_sym = str(rotated_pos.symbol)
                st_hours = float(open_metrics_by_ticket.get(int(rotated_pos.ticket), {}).get("hours_open", 0.0))
                closed_evt = self._close_mt5_position(
                    rotated_pos,
                    reason=f"ROTACION DE CAPITAL por {cand.symbol} (Prob={cand_prob}%)",
                )
                if not closed_evt:
                    continue
                logger.info(
                    "ROTACION DE CAPITAL: Cerrando %s (+$%.2f tras %.1fh estancada) para abrir %s (Prob IA=%d%%).",
                    st_sym,
                    float(rotated_pos.profit),
                    st_hours,
                    cand.symbol,
                    cand_prob,
                )
                executed_actions.append(closed_evt)
                open_symbols.discard(st_sym)
                rotatable_positions = [p for p in rotatable_positions if str(p.symbol) != st_sym]
                st_side = "BUY" if rotated_pos.type == mt5.POSITION_TYPE_BUY else "SELL"
                st_u_dir = self._get_usd_direction(st_sym, st_side)
                if st_u_dir in usd_dir_counts and usd_dir_counts[st_u_dir] > 0:
                    usd_dir_counts[st_u_dir] -= 1
                acc_refresh = mt5.account_info()
                if acc_refresh is not None:
                    free_margin = float(acc_refresh.margin_free)
                    equity = float(acc_refresh.equity)

            ai_prob_for_sizing = cand_eval.win_probability_pct if cand_eval is not None else 70
            risk_scale = float(daily_guard.get("risk_scale", 1.0)) if protection_active else 1.0
            lot, sl_price, tp_price, risk_usd = self.calculate_safe_lot_and_sl(
                snap=cand,
                side=side,
                equity_usd=equity,
                free_margin_usd=free_margin,
                ai_probability_pct=ai_prob_for_sizing,
                risk_scale=risk_scale,
            )
            if lot <= 0.0 or sl_price <= 0.0:
                continue

            entry_px = cand.ask if side == "BUY" else cand.bid
            sl_dist = abs(entry_px - sl_price)
            spread_px = cand.spread_points * cand.point if cand.point > 0 else max(0.0, cand.ask - cand.bid)
            max_sp_ratio = 0.12 if cand.entry_pillar.startswith("M15_SCALPER") else 0.18
            if sl_dist <= 0.0 or spread_px > max_sp_ratio * sl_dist:
                logger.info(
                    "FILTRO SPREAD/SL: Entrada en %s omitida (spread=%.5f > %.0f%% de SL=%.5f; ratio=%.1f%%).",
                    cand.symbol,
                    spread_px,
                    max_sp_ratio * 100.0,
                    sl_dist,
                    (spread_px / max(sl_dist, 1e-9)) * 100.0,
                )
                continue

            ia_tag = f", IA={cand_eval.win_probability_pct}%" if cand_eval is not None else ""
            reason = (
                f"Pilar {cand.entry_pillar} ({cand.candle_pattern}, ADX={cand.adx_14}, Stoch %K={cand.stoch_k}, "
                f"RSI={cand.rsi_14}{ia_tag}, Riesgo ~${risk_usd:.2f} USD)"
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
                if cand_usd_dir in usd_dir_counts:
                    usd_dir_counts[cand_usd_dir] += 1
                used_margin = cand.margin_min_lot_usd * (lot / cand.min_lot) if cand.min_lot > 0 else cand.margin_min_lot_usd
                free_margin = max(0.0, free_margin - used_margin)

        self._write_markdown_report(
            cycle_num,
            acc,
            raw_positions,
            snapshots,
            executed_actions,
            ai_eval=ai_eval,
            open_metrics_by_ticket=open_metrics_by_ticket,
            market_context=market_context,
        )

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
            "daily_risk_guard": daily_guard,
            "ai_priority": ai_eval.priority_tier,
            "ai_model": ai_eval.model_used,
            "ai_trigger": trigger_reason,
            "ai_blocked_symbols": {
                sym: {
                    "remaining_minutes": round((float(data["until_ts"]) - time.time()) / 60.0, 1),
                    "probability_pct": data.get("probability_pct"),
                    "close_type": data.get("close_type"),
                }
                for sym, data in self.symbol_blocked_until.items()
                if float(data.get("until_ts", 0.0)) > time.time()
            },
        }

    @staticmethod
    def _format_macro_pulse_line(market_context: dict[str, Any] | None) -> str:
        if not market_context:
            return "- **Pulso Macro 360°:** Sin datos macro disponibles."
        usd = market_context.get("usd_strength") or {}
        crypto = market_context.get("crypto_pulse") or {}
        idx = market_context.get("indices_pulse") or {}
        ns = market_context.get("news_and_session") or {}
        alert_str = "ALERTA VOLATILIDAD/NOTICIAS" if ns.get("news_volatility_alert") else "NORMAL"
        return (
            f"- **Pulso Macro 360°:** Dolar: `{usd.get('usd_bias', 'N/A')}` (`{usd.get('usd_bullish_pairs', 0)}/{usd.get('usd_bearish_pairs', 0)}`) | "
            f"Cripto (BTC/ETH): `{crypto.get('crypto_regime', 'N/A')}` | "
            f"Wall Street: `{idx.get('indices_regime', 'N/A')}` | "
            f"Sesion/Noticias: `{ns.get('session_name', 'N/A')}` (`{alert_str}`)"
        )

    @staticmethod
    def _format_daily_risk_guard_line(market_context: dict[str, Any] | None) -> str:
        guard = (market_context or {}).get("daily_risk_guard") or {}
        if not guard:
            return "- **Candado Diario / Racha:** Sin datos disponibles."
        mode = str(guard.get("protection_mode", "NORMAL"))
        pnl = float(guard.get("daily_closed_pnl_usd", 0.0) or 0.0)
        losses = int(guard.get("consecutive_losses", 0) or 0)
        mins_loss = float(guard.get("mins_since_last_loss", 999.0) or 999.0)
        paused = bool(guard.get("pause_new_entries", False))
        hard_stop = bool(guard.get("hard_daily_loss_stop", False))
        min_prob = int(guard.get("min_ai_prob", 55) or 55)
        risk_scale = float(guard.get("risk_scale", 1.0) or 1.0)
        max_pos = int(guard.get("max_positions", 4) or 4)
        loss_age = f"{mins_loss:.1f}m" if mins_loss < 999.0 else "N/A"
        if hard_stop:
            pause_tag = " | **HARD STOP -3% ACTIVO**"
        elif paused:
            pause_tag = f" | **FRENO 45m ACTIVO** (`{float(guard.get('pause_remaining_mins', 0.0) or 0.0):.1f}m` restantes)"
        else:
            pause_tag = ""
        return (
            f"- **Candado Diario / Racha (`{guard.get('utc_date', 'UTC')}`):** `{mode}` | "
            f"PnL Cerrado Hoy: `${pnl:+.2f} USD` | Racha Perdidas: `{losses}` (ultima: `{loss_age}`) | "
            f"Umbral IA: `{min_prob}%` | Escala Riesgo: `{risk_scale:.2f}x` | Max Pos: `{max_pos}`{pause_tag}"
        )

    def _write_markdown_report(
        self,
        cycle_num: int,
        acc: Any,
        positions: tuple[Any, ...],
        snapshots: list[MT5SymbolSnapshot],
        executed_actions: list[dict[str, Any]],
        ai_eval: MT5AICycleEvaluation | None = None,
        open_metrics_by_ticket: dict[int, dict[str, Any]] | None = None,
        market_context: dict[str, Any] | None = None,
    ) -> None:
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        phase_str = (
            "Fase 5 (>= $400 USD) — B_FINAL_HYBRID_ADX (Max 3 posiciones, riesgo proporcional 1.00% / max 1.25%, veto SL >20%)"
            if acc.equity >= 400.0
            else (
                "Fase 4 ($250 - $400 USD) — Proporcional 1.00% / max 1.25% (Max 3 posiciones)"
                if acc.equity >= 250.0
                else (
                    "Fase 3 ($60 - $250 USD) — Max 3 posiciones simultaneas"
                    if acc.equity >= 60.0
                    else (
                        "Fase 2 ($28 - $60 USD) — Max 3 posiciones simultaneas y lotaje escalable"
                        if acc.equity >= 28.0
                        else "Fase 1 ($10 - $28 USD) — Micro-lotes 0.01 base y max 2 posiciones"
                    )
                )
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
            "## Lectura de Mercado y Asistencia Gemini AI",
            f"- **Modo IA del Ciclo:** `{ai_eval.priority_tier if ai_eval else 'GENERAL'}` | **Modelo utilizado:** `{ai_eval.model_used if ai_eval else 'quant_local'}`",
            self._format_macro_pulse_line(market_context),
            self._format_daily_risk_guard_line(market_context),
            f"> {ai_eval.market_summary if ai_eval else 'Evaluacion IA pendiente.'}",
            "",
            "## Posiciones Abiertas en Exness MT5",
        ]
        if not positions:
            lines.append("_No hay posiciones abiertas en este momento._")
        else:
            lines.extend(
                [
                    "| Ticket | Simbolo | Tipo | Lote | Apertura | Precio Actual | SL Actual | TP Actual | Meta TP ($ USD) | PnL ($ USD) | Prob. Profit IA | Asistencia IA |",
                    "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
                ]
            )
            for p in positions:
                side_str = "BUY (LONG)" if p.type == mt5.POSITION_TYPE_BUY else "SELL (SHORT)"
                m = (open_metrics_by_ticket or {}).get(int(p.ticket), {})
                tp_usd_str = f"${float(m.get('tp_profit_usd', 0.0)):+.2f}" if m else "—"
                rev = ai_eval.open_reviews.get(str(p.symbol)) if ai_eval else None
                prob_str = f"**{rev.tp_probability_pct}%**" if rev else "—"
                act_str = f"`{rev.action}` — {rev.reasoning}" if rev else "Vigilancia estandar"
                lines.append(
                    f"| `{p.ticket}` | `{p.symbol}` | **{side_str}** | {p.volume} | {p.price_open} | {p.price_current} | **{p.sl}** | **{p.tp}** | {tp_usd_str} | **${p.profit:+.2f}** | {prob_str} | {act_str} |"
                )

        lines.extend(
            [
                "",
                "## Evaluaciones IA Post-Cierre y Bloqueos Activos (90 Minutos)",
            ]
        )
        now_ts = time.time()
        active_blocks = [
            (sym, {**data, "remaining_minutes": round((float(data["until_ts"]) - now_ts) / 60.0, 1)})
            for sym, data in self.symbol_blocked_until.items()
            if float(data.get("until_ts", 0.0)) > now_ts
        ]
        if not active_blocks:
            lines.append("_Ningun simbolo bloqueado por IA en este momento._")
        else:
            lines.extend(
                [
                    "| Simbolo | Motivo Cierre | Prob. IA | Restante | Expira (UTC) | Diagnostico IA |",
                    "| :--- | :---: | :---: | :---: | :---: | :--- |",
                ]
            )
            for sym, b in active_blocks:
                lines.append(
                    f"| `{sym}` | `{b.get('close_type')}` (`${float(b.get('profit_usd', 0.0)):+.2f}`) | **{b.get('probability_pct')}%** | `{b['remaining_minutes']} min` | `{b.get('until_utc')}` | {b.get('reason')} |"
                )

        if self.recent_ai_close_decisions:
            lines.extend(["", "### Ultimas Evaluaciones Post-Cierre (Manual / Positivo / Negativo)"])
            for dec in reversed(self.recent_ai_close_decisions[-6:]):
                lines.append(
                    f"- `{dec['evaluated_at_utc']}` | **{dec['symbol']}** (`#{dec['ticket']}`, `{dec['close_type']}`, `${float(dec['profit_usd']):+.2f}`) -> Prob. IA: **{dec['probability_pct']}%** -> **{dec['status']}** ({dec['reason']})"
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

        self._atomic_write_text(self.report_file, "\n".join(lines) + "\n")


def main() -> int:
    load_dotenv(BASE_DIR / ".env")
    parser = argparse.ArgumentParser(description="Bot Autonomo Exness MetaTrader 5 (1H EMA200 + Estocastico + Pilares ATR + Modo Adaptativo IA)")
    parser.add_argument("--loop", action="store_true", help="Ejecutar continuamente mientras la PC/VPS este encendida")
    parser.add_argument("--interval", type=int, default=300, help="Segundos entre cada escaneo en modo clasico (default: 300s = 5 min)")
    parser.add_argument("--adaptive-ai", action="store_true", help="Activar motor adaptativo multi-estrategia + SQLite + despertares exactos (sniper wake)")
    parser.add_argument("--base-interval-minutes", type=int, default=30, help="Cadencia base en minutos para patrullaje en modo --adaptive-ai (default: 30)")
    parser.add_argument("--seed-history", action="store_true", help="Sembrar strategy_priors (estudio historico 2 anos) en SQLite si la tabla esta vacia")
    parser.add_argument("--learning-db", type=str, default="data/mt5_learning.db", help="Ruta a la base SQLite de aprendizaje (default: data/mt5_learning.db)")
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
        adaptive_ai=args.adaptive_ai,
        base_interval_minutes=args.base_interval_minutes,
        learning_db_path=args.learning_db,
    )

    if args.seed_history:
        try:
            seed_res = bot.seed_historical_priors(only_if_empty=True)
            logger.info("Resultado de siembra historica (--seed-history): %s", seed_res)
        except Exception as seed_exc:
            logger.exception("Error durante --seed-history: %s", seed_exc)

    cycle = 0
    reconnect_wait_seconds = 20
    next_cycle_mode: str | None = None
    next_due_symbols: list[str] | None = None

    while True:
        cycle += 1
        mt5_online = False
        summary: dict[str, Any] = {}
        try:
            summary = bot.run_cycle(
                cycle_num=cycle,
                cycle_mode=next_cycle_mode,
                due_symbols=next_due_symbols,
            )
            print(json.dumps(summary, indent=2, ensure_ascii=False))
            mt5_online = True
        except (ConnectionError, RuntimeError, OSError) as conn_exc:
            logger.warning(
                "Sin conexion a internet o MT5 desconectado en ciclo #%d (%s). Reintentando reconexion automatica en %ds...",
                cycle,
                conn_exc,
                reconnect_wait_seconds,
            )
            try:
                mt5.shutdown()
            except Exception:
                pass
        except Exception as exc:
            logger.exception("Error en ciclo MT5 #%d: %s", cycle, exc)

        if not args.loop:
            break

        if not mt5_online:
            next_cycle_mode = None
            next_due_symbols = None
            time.sleep(reconnect_wait_seconds)
            continue

        if args.adaptive_ai and bot.wake_scheduler is not None:
            plan = summary.get("next_wake_plan") or bot.wake_scheduler.next_wakeup_plan().to_dict()
            sleep_seconds = max(15.0, float(plan.get("sleep_seconds", args.base_interval_minutes * 60)))
            next_cycle_mode = str(plan.get("mode", "BASE_PATROL"))
            next_due_symbols = list(plan.get("due_symbols") or [])
            logger.info(
                "AdaptiveWakeScheduler: durmiendo %.1fs hasta %s | proximo modo=%s | simbolos=%s | %s",
                sleep_seconds,
                plan.get("wake_at_utc"),
                next_cycle_mode,
                next_due_symbols,
                plan.get("reason", ""),
            )
            time.sleep(sleep_seconds)
        else:
            sleep_seconds = max(30, args.interval)
            time.sleep(sleep_seconds)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
