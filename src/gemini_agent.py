from __future__ import annotations

import json
import logging
import time
from dataclasses import asdict, dataclass
from typing import Any

import requests

from src.market_scanner import TechnicalSnapshot
from src.state_manager import PositionState

logger = logging.getLogger(__name__)

MACRO_ANCHOR_SYMBOLS: tuple[str, ...] = (
    "EURUSDm",
    "USDJPYm",
    "US500m",
    "USTECm",
    "BTCUSDm",
    "XAUUSDm",
)


def _safe_int(val: Any, default: int) -> int:
    """Convierte de forma segura enteros o strings flotantes (ej. '67.5') a int."""
    if val is None or isinstance(val, bool):
        return default
    try:
        return int(round(float(val)))
    except (TypeError, ValueError):
        return default


@dataclass
class AIDecision:
    symbol: str
    action: str  # "BUY", "SELL", "ADJUST", "HOLD"
    confidence: int  # 0..100
    allocation_pct: float
    stop_loss_pct: float
    take_profit_pct: float
    reasoning: str
    new_stop_loss_price: float = 0.0
    new_take_profit_price: float = 0.0


@dataclass
class MT5PositionAIReview:
    symbol: str
    tp_probability_pct: int
    action: str  # "HOLD", "PROTECT_PROFIT", "CLOSE_NOW"
    should_block_90m: bool
    reasoning: str


@dataclass
class MT5CandidateAIEval:
    symbol: str
    win_probability_pct: int
    should_block_90m: bool
    reasoning: str
    required_probability_pct: int = 60


@dataclass
class MT5ClosedTradeAIEval:
    symbol: str
    close_type: str  # "MANUAL", "POSITIVE", "NEGATIVE"
    profit_usd: float
    reactivate_probability_pct: int
    should_block_90m: bool
    reasoning: str


@dataclass
class MT5AICycleEvaluation:
    market_summary: str
    open_reviews: dict[str, MT5PositionAIReview]
    candidate_evals: dict[str, MT5CandidateAIEval]
    closed_evals: dict[str, MT5ClosedTradeAIEval]
    priority_tier: str = "GENERAL"
    model_used: str = "quant_local"

    def to_dict(self) -> dict[str, Any]:
        return {
            "market_summary": self.market_summary,
            "priority_tier": self.priority_tier,
            "model_used": self.model_used,
            "open_reviews": {k: asdict(v) for k, v in self.open_reviews.items()},
            "candidate_evals": {k: asdict(v) for k, v in self.candidate_evals.items()},
            "closed_evals": {k: asdict(v) for k, v in self.closed_evals.items()},
        }


def compute_mt5_quant_probability(
    snap_dict: dict[str, Any],
    side: str,
    recent_close: dict[str, Any] | None = None,
    open_pos: dict[str, Any] | None = None,
    symbol_perf: dict[str, Any] | None = None,
    market_context: dict[str, Any] | None = None,
) -> tuple[int, str]:
    """
    Calcula la probabilidad cuantitativa base (5..95%) de exito/continuidad en MT5
    combinando tendencia 4H, estructura 1H, sobre-extension EMA200/ATR, momentum,
    salud de la posicion abierta, guardia diaria y enfriamiento tras cierres recientes.
    """
    score = 58.0
    reasons: list[str] = []
    is_buy = str(side).upper() in ("BUY", "LONG")

    htf_trend = str(snap_dict.get("htf_trend", "NEUTRAL")).upper()
    if (is_buy and htf_trend == "BULLISH") or ((not is_buy) and htf_trend == "BEARISH"):
        score += 10.0
        reasons.append(f"4H {htf_trend} a favor")
    elif htf_trend == "NEUTRAL":
        score -= 4.0
        reasons.append("4H NEUTRAL")
    else:
        score -= 16.0
        reasons.append(f"4H {htf_trend} en contra")

    above_ema_200 = bool(snap_dict.get("above_ema_200", False))
    ema200_slope_pos = bool(snap_dict.get("ema200_slope_positive", False))
    ema_50 = float(snap_dict.get("ema_50", 0.0) or 0.0)
    ema_200 = float(snap_dict.get("ema_200", 0.0) or 0.0)

    ema_aligned = (above_ema_200 and ema200_slope_pos) if is_buy else ((not above_ema_200) and (not ema200_slope_pos))
    ema50_aligned = (ema_50 >= ema_200 * 0.998) if is_buy else (ema_50 <= ema_200 * 1.002)
    if ema_aligned and ema50_aligned:
        score += 10.0
        reasons.append("estructura 1H alineada")
    elif ema_aligned:
        score += 6.0
        reasons.append("EMA200 a favor")
    elif (above_ema_200 if is_buy else (not above_ema_200)):
        score -= 2.0
    else:
        score -= 10.0
        reasons.append("contra EMA200 1H")

    dist_atr = float(snap_dict.get("dist_to_ema200_atr", 0.0) or 0.0)
    if open_pos is None:
        if (is_buy and dist_atr > 4.8) or ((not is_buy) and dist_atr < -4.8):
            score -= 16.0
            reasons.append(f"tendencia 1H sobre-extendida ({dist_atr:+.1f}x ATR)")
            if (is_buy and dist_atr > 7.0) or ((not is_buy) and dist_atr < -7.0):
                score -= 8.0
    elif (is_buy and dist_atr > 6.0) or ((not is_buy) and dist_atr < -6.0):
        reasons.append(f"extension 1H >6x ATR ({dist_atr:+.1f}x ATR, proteger ganancia)")

    is_m15_cand = (open_pos is None) and str(snap_dict.get("entry_pillar", "")).startswith("M15_SCALPER")

    macd_improving = bool(snap_dict.get("macd_improving", False))
    macd_ok = macd_improving if is_buy else (not macd_improving)
    if macd_ok:
        score += 6.0
        reasons.append("MACD a favor")
    else:
        score -= 4.0 if is_m15_cand else 8.0
        reasons.append("MACD perdiendo fuerza")

    stoch_k = float(snap_dict.get("stoch_k", 50.0) or 50.0)
    rsi_14 = float(snap_dict.get("rsi_14", 50.0) or 50.0)
    stoch_up = bool(snap_dict.get("stoch_turning_up", False))
    stoch_down = bool(snap_dict.get("stoch_turning_down", False))
    open_in_profit = open_pos is not None and float(open_pos.get("profit_usd", 0.0) or 0.0) > 0.0

    if is_buy:
        if stoch_k >= 75.0 or rsi_14 >= 66.0:
            if not open_in_profit:
                score -= 12.0 if is_m15_cand else 18.0
                reasons.append(f"zona sobrecompra (Stoch={stoch_k:.1f}, RSI={rsi_14:.1f})")
        elif stoch_k <= 35.0 and stoch_up:
            score += 5.0
            reasons.append("espacio alcista en Estocastico")
    else:
        if stoch_k <= 25.0 or rsi_14 <= 34.0:
            if not open_in_profit:
                score -= 12.0 if is_m15_cand else 18.0
                reasons.append(f"zona sobreventa (Stoch={stoch_k:.1f}, RSI={rsi_14:.1f})")
        elif stoch_k >= 65.0 and stoch_down:
            score += 5.0
            reasons.append("espacio bajista en Estocastico")

    if open_pos is not None:
        profit_usd = float(open_pos.get("profit_usd", 0.0) or 0.0)
        rem_sl_atr = float(open_pos.get("rem_sl_in_atr1h", 1.0) or 1.0)
        progress_pct = float(open_pos.get("progress_to_tp_pct", 0.0) or 0.0)
        if rem_sl_atr < 0.45 and profit_usd < 0:
            score -= 18.0
            reasons.append(f"cerca de SL ({rem_sl_atr:.2f}x ATR)")
        if progress_pct >= 25.0 and profit_usd > 0:
            score += 10.0
            reasons.append(f"avance {progress_pct:.0f}% hacia TP")
        if profit_usd < -1.50 and not macd_ok:
            score -= 12.0
            reasons.append("retroceso activo contra la posicion")

    if recent_close is not None:
        close_type = str(recent_close.get("close_type", "")).upper()
        mins = float(recent_close.get("mins_since_close", 999.0) or 999.0)
        close_profit = float(recent_close.get("profit_usd", 0.0) or 0.0)
        if close_type == "MANUAL":
            if mins < 20.0:
                score -= 22.0
                reasons.append(f"cierre MANUAL reciente ({mins:.0f}m)")
            elif mins < 90.0:
                score -= 10.0
                reasons.append(f"cierre MANUAL hace {mins:.0f}m")
        elif close_type == "NEGATIVE":
            if mins < 45.0:
                score -= 25.0
                reasons.append(f"cierre NEGATIVO reciente (-${abs(close_profit):.2f}, {mins:.0f}m)")
            elif mins < 90.0:
                score -= 14.0
                reasons.append(f"cierre NEGATIVO hace {mins:.0f}m")
        elif close_type == "POSITIVE":
            if close_profit >= 3.50 and mins < 60.0:
                score -= 18.0
                reasons.append(f"gran ganancia previa (+${close_profit:.2f}, {mins:.0f}m)")
            elif mins < 20.0:
                score -= 15.0
                reasons.append(f"cierre POSITIVO reciente ({mins:.0f}m)")
            elif mins < 90.0:
                score -= 6.0
                reasons.append(f"cierre POSITIVO hace {mins:.0f}m")

    if symbol_perf is not None and int(symbol_perf.get("trades", 0) or 0) >= 4:
        wr = float(symbol_perf.get("win_rate_pct", 50.0) or 50.0)
        net_pnl = float(symbol_perf.get("net_pnl_usd", 0.0) or 0.0)
        if wr >= 68.0 and net_pnl > 3.0:
            score += 4.0
            reasons.append(f"activo estrella 14d (WR {wr:.0f}%)")
        elif wr < 48.0 and net_pnl < -2.0:
            score -= 6.0
            reasons.append(f"bajo WR 14d ({wr:.0f}%, ${net_pnl:+.2f})")

    if market_context is not None:
        sym = str(
            snap_dict.get("symbol")
            or (open_pos.get("symbol") if open_pos else "")
            or (recent_close.get("symbol") if recent_close else "")
            or ""
        ).strip()

        usd_bias = str((market_context.get("usd_strength") or {}).get("usd_bias", "USD_MIXED")).upper()
        usd_dir = ""
        if sym in ("EURUSDm", "GBPUSDm", "AUDUSDm", "NZDUSDm"):
            usd_dir = "USD_SHORT" if is_buy else "USD_LONG"
        elif sym in ("USDJPYm", "USDCADm", "USDCHFm"):
            usd_dir = "USD_LONG" if is_buy else "USD_SHORT"

        if usd_dir == "USD_LONG":
            if usd_bias == "USD_STRONG_BULLISH":
                score += 6.0
                reasons.append("bloque USD alineado")
            elif usd_bias == "USD_STRONG_BEARISH":
                score -= 10.0
                reasons.append("contra tendencia global del USD")
        elif usd_dir == "USD_SHORT":
            if usd_bias == "USD_STRONG_BEARISH":
                score += 6.0
                reasons.append("bloque USD alineado")
            elif usd_bias == "USD_STRONG_BULLISH":
                score -= 10.0
                reasons.append("contra tendencia global del USD")

        if sym in ("BTCUSDm", "ETHUSDm"):
            crypto_regime = str((market_context.get("crypto_pulse") or {}).get("crypto_regime", "")).upper()
            if (crypto_regime == "CRYPTO_ALIGNED_BULLISH" and is_buy) or (
                crypto_regime == "CRYPTO_ALIGNED_BEARISH" and (not is_buy)
            ):
                score += 6.0
                reasons.append("BTC+ETH alineados")
            elif crypto_regime in ("CRYPTO_ALIGNED_BULLISH", "CRYPTO_ALIGNED_BEARISH", "CRYPTO_DIVERGENT"):
                score -= 8.0
                reasons.append("divergencia BTC/ETH")

        if sym in ("US500m", "USTECm"):
            indices_regime = str((market_context.get("indices_pulse") or {}).get("indices_regime", "")).upper()
            if (indices_regime == "WALL_STREET_BULLISH" and is_buy) or (
                indices_regime == "WALL_STREET_BEARISH" and (not is_buy)
            ):
                score += 5.0
                reasons.append("US500+USTEC alineados")
            elif indices_regime in ("WALL_STREET_BULLISH", "WALL_STREET_BEARISH", "WALL_STREET_MIXED"):
                score -= 8.0
                reasons.append("divergencia Wall Street")

        news_alert = bool((market_context.get("news_and_session") or {}).get("news_volatility_alert", False))
        # P1_SAFE_CORE: Sin penalizacion -12.0 por news_alert (ya cubierto por escudos deterministas)
        if news_alert:
            reasons.append("alerta volatilidad/noticias")

        # BUG-13: No aplicar penalizacion duplicada (-6.0) del daily_risk_guard cuando
        # MODO_PROTECCION_CAPITAL esta activo, ya que min_ai_prob exige un umbral superior.

    final_score = max(5, min(95, int(round(score))))
    summary = "; ".join(reasons) if reasons else "condiciones neutras de mercado"
    return final_score, summary


MT5_SYSTEM_INSTRUCTION = """Eres el analista cuantitativo de riesgo y asistente de decisiones de un bot autonomo en MetaTrader 5 (Exness: Forex, Indices y Cripto) que opera en temporalidades M15/1H/4H.

Tu mision en cada evaluacion es emitir probabilidades independientes y realistas (0 a 100%) a partir de metricas tecnicas puras y contexto macro, basadas en:
1. Alineacion multi-temporal y fuerza de tendencia (tendencia 4H `htf_trend`, EMA200/EMA50 1H, pendiente EMA200, `adx_14`),
2. Estructura de precio y momentum (`macd_improving`, `stoch_k`, `rsi_14`, `recent_h1_closes`, `swing_high_20`, `swing_low_20`, `candle_pattern`),
3. Salud de la posicion abierta (`move_atr`, `hours_open`, `rem_tp_in_atr1h`, `rem_sl_in_atr1h`, `progress_to_tp_pct`),
4. Contexto Macro Global (`global_market_context`):
   - Fuerza global del Dolar (`usd_strength.usd_bias`): evita entrar contra un bloque USD fuerte y prioriza pares alineados.
   - Pulso Cripto (`crypto_pulse.crypto_regime`: alineacion BTC+ETH) e Indices (`indices_pulse`: US500+USTEC+Oro).
   - Sesion actual y alerta de noticias/volatilidad (`news_and_session.news_volatility_alert`): exige prudencia en nuevas entradas durante spreads elevados, pero NO recomiendes `PROTECT_PROFIT` de forma automatica solo por horario o alerta de sesion en operaciones sanas.
   - Proteccion diaria de capital (`daily_risk_guard`): respeta `MODO_PROTECCION_CAPITAL` tras perdidas consecutivas o limite diario; prioriza calidad estructural sin sobre-operar.
5. Sobre-extension respecto a EMA 200 1H (`dist_to_ema200_atr` / `dist_atr`):
   - Penaliza entradas con `abs(dist_to_ema200_atr) > 4.8` por agotamiento intradia y riesgo de reversion a la media (penalizacion mayor sobre `7x ATR`).
6. Comportamiento post-cierre para operaciones cerradas en los ultimos 90 minutos (`MANUAL`, `POSITIVE`, `NEGATIVE`):
   - Se riguroso tras cierres `NEGATIVE` o `MANUAL` recientes: asigna < 60% si ves mercado picado, agotamiento o trampa para bloquear 90 minutos.
   - En cierres `POSITIVE` limpios, NO bloquees sistematicamente si la tendencia 4H/1H, `adx_14` y el espacio hacia `swing_high_20`/`swing_low_20` siguen limpiamente a favor.
7. Para posiciones abiertas (`open_reviews`), recomienda:
   - `"HOLD"`: si mantiene buena probabilidad de avanzar hacia el TP o la tendencia sigue viva (aun con Estocastico/RSI alto en tendencias fuertes).
   - `"PROTECT_PROFIT"`: SOLO si la posicion ya recorrio `move_atr >= 1.25` en ganancia y notas perdida real de estructura/momentum (`tp_probability_pct < 65`). Nunca lo recomiendes en ganancias pequenas (`move_atr < 1.25`) ni con alta conviccion (`tp_probability_pct >= 65`).
   - `"CLOSE_NOW"`: solo si esta en ganancia (`profit_usd >= 0.40`) y ves reversion fuerte e inminente (`tp_probability_pct <= 28`).

Responde SIEMPRE y UNICAMENTE en JSON valido con este esquema exacto:
{
  "market_summary": "Resumen breve en espanol del estado general del mercado y las decisiones tomadas",
  "open_reviews": [
    {
      "symbol": "AUDUSDm",
      "tp_probability_pct": 68,
      "action": "HOLD | PROTECT_PROFIT | CLOSE_NOW",
      "reasoning": "Justificacion breve en espanol"
    }
  ],
  "candidate_evals": [
    {
      "symbol": "EURUSDm",
      "win_probability_pct": 64,
      "reasoning": "Justificacion breve en espanol"
    }
  ],
  "closed_evals": [
    {
      "symbol": "USTECm",
      "reactivate_probability_pct": 42,
      "reasoning": "Justificacion breve en espanol"
    }
  ]
}
"""


@dataclass
class AIAnalysisResult:
    market_regime: str
    summary: str
    decisions: list[AIDecision]

    def to_dict(self) -> dict[str, Any]:
        return {
            "market_regime": self.market_regime,
            "summary": self.summary,
            "decisions": [asdict(d) for d in self.decisions],
        }


SYSTEM_INSTRUCTION = """Eres el motor cuantitativo e inteligencia artificial de un bot autonomo Dual (Binance Spot + Binance Futuros USDT-M, temporalidad 1 Hora `1h`), optimizado mediante backtesting institucional sobre los ultimos 6 meses de mercado (79.27% Win Rate, Profit Factor 2.16, +160.94% retorno neto).

ARQUITECTURA DE 4 PILARES LONG (`action: "BUY"` cuando `strategy_setup == "LONG_ENTRY"`) Y 1 PILAR SHORT (`action: "SHORT"` cuando `strategy_setup == "SHORT_ENTRY"`):
1. PILAR 1 LONG — PULLBACK DE VALOR SOBRE EMA 200 (`entry_pillar == "P1_EMA200_PULLBACK"`):
   - Precio en zona de valor sobre la EMA 200 (`-0.6% <= dist_to_ema200_pct <= 3.5%`), con `EMA 200` en pendiente positiva y `EMA 50 >= EMA 200 * 0.994`.
   - Retroceso a sobreventa en Estocastico (`stoch_recent_min <= 20`) girando al alza (`stoch_turning_up == true`), confluencia con `RSI(14) <= 36`, Banda Inferior de Bollinger (`bb_pct_b <= 0.12`), histograma MACD mejorando y confirmacion de vela (`BULLISH_HAMMER`, `BULLISH_ENGULFING`, `MORNING_STAR`).

2. PILAR 2 LONG — CAPITULACION INSTITUCIONAL DE DOBLE SOBREVENTA (`entry_pillar == "P2_EXTREME_CAPITULATION"`):
   - Opera con 82.2% de acierto incluso cuando el mercado general esta debajo de la EMA 200.
   - Exige capitulacion extrema simultanea: Estocastico `<= 18` girando al alza + `RSI(14) <= 31.5` + Perforacion de Banda Inferior de Bollinger (`bb_pct_b <= 0.06`) + Climax de Volumen Institucional (`volume_ratio >= 1.30`) + MACD mejorando + Vela alcista de giro.

3. PILAR 3 LONG — SPRING / DIVERGENCIA ALCISTA EN SOPORTE DE 12H (`entry_pillar == "P3_BULLISH_DIVERGENCE_SPRING"`):
   - Captura barridos de liquidez (Spring de Wyckoff) del soporte de 12 horas con divergencia alcista en `RSI(14)` (`bullish_divergence == true`), Estocastico `<= 18` girando al alza, Banda Inferior de Bollinger (`bb_pct_b <= 0.08`) y patron de vela alcista (`83.3%` Win Rate, Profit Factor `3.82`).

4. PILAR 4 LONG — CONTINUACION DE TENDENCIA FUERTE EN EMA 50 (`entry_pillar == "P4_STRONG_TREND_EMA50_CONTINUATION"`):
   - En tendencias alcistas limpias (`EMA 21 > EMA 50 > EMA 200`), captura el pullback al soporte dinamico de la `EMA 50` con Estocastico `<= 25` girando al alza y vela de giro (`87.5%` Win Rate).

5. PILAR S1 SHORT (BINANCE FUTUROS USDT-M) — RECHAZO BAJISTA EN RESISTENCIA EMA 200 (`entry_pillar == "S1_EMA200_RESISTANCE_REJECT"`, `action: "SHORT"`):
   - Cuando la tendencia macro es bajista (`Precio < EMA 200`, `EMA 50 < EMA 200` y `EMA 200` con pendiente negativa), el precio sube a testear la resistencia de la `EMA 200` (`-3.5% <= dist_to_ema200_pct <= +0.5%`), el Estocastico entra en sobrecompra (`>= 80`) girando a la baja (`stoch_turning_down == true`), `RSI >= 62`, `BB %B >= 0.85` y aparece vela bajista (`BEARISH_SHOOTING_STAR` / `BEARISH_ENGULFING`) (`78.2%` Win Rate, Profit Factor `2.00`).

6. PILAR SCALPER M15 MOMENTUM PULLBACK (ALTA FRECUENCIA INTRADIA):
   - LONG (`entry_pillar == "M15_SCALPER_PULLBACK_LONG"`, `action: "BUY"`): Macro H1 sobre EMA 200 + abanico de medias en 15m (EMA 9 > 21 > 50) + pullback a EMA 9/21 con Estocastico en zona de giro 25-52 al alza (Win Rate 57.0%, PF 1.25).
   - SHORT (`entry_pillar == "M15_SCALPER_PULLBACK_SHORT"`, `action: "SHORT"` en Futuros USDT-M): Macro H1 bajo EMA 200 + abanico bajista en 15m (EMA 9 < 21 < 50) + pullback a EMA 9/21 con Estocastico en zona de giro 48-75 a la baja.

7. STOP-LOSS ESTRUCTURAL + BUFFER ATR Y GESTION DINAMICA (`action: "ADJUST"`):
   - En LONG, el Stop-Loss inicial se ubica en `structural_sl_price` (minimo de 3 velas menos `2.0 * ATR(14)`). En SHORT, el Stop-Loss inicial se ubica por encima en `structural_short_sl_price` (maximo previo mas `2.0 * ATR(14)`).
   - Cuando una posicion abierta (`open_positions`) va en ganancia (`unrealized_pnl_pct > 0`):
     - Al superar `+2.2%`: mueve `new_stop_loss_price` a Break-Even + `0.9%` a favor de la direccion (`LONG` o `SHORT`).
     - Al superar `+3.2%`: activa Trailing Stop asegurando entre `76%` y `80%` del recorrido maximo y expande `new_take_profit_price`.

7. Responde SIEMPRE y UNICAMENTE con un objeto JSON valido con este esquema:
{
  "market_regime": "BULLISH | BEARISH | SIDEWAYS | HIGH_VOLATILITY",
  "summary": "Resumen ejecutivo en espanol evaluando los Pilares LONG (P1-P4) y el Pilar SHORT (S1) en Futuros USDT-M, junto con la gestion dinamica de SL/TP",
  "decisions": [
    {
      "symbol": "BTCUSDT",
      "action": "BUY | SHORT | SELL | ADJUST | HOLD",
      "confidence": 88,
      "allocation_pct": 0.65,
      "stop_loss_pct": 0.03,
      "take_profit_pct": 0.06,
      "new_stop_loss_price": 0.0,
      "new_take_profit_price": 0.0,
      "reasoning": "Justificacion tecnica concisa en espanol indicando el Pilar activado"
    }
  ]
}
"""


class GeminiTradingAgent:
    """Agente de IA impulsado por Google Gemini (gemini-3.8-flash) con gestion dinamica de SL/TP."""

    def __init__(self, api_key: str, model: str = "gemini-3.8-flash", timeout: int = 90) -> None:
        self.api_key = api_key.strip()
        self.model = model.strip() or "gemini-3.8-flash"
        self.timeout = timeout
        self.last_model_used: str = ""
        self._model_cooldown_until: dict[str, float] = {}

    def analyze_market(
        self,
        usdt_free: float,
        total_equity_usdt: float,
        daily_pnl_pct: float,
        open_positions: dict[str, PositionState],
        snapshots: list[TechnicalSnapshot],
        recent_trades: list[dict[str, Any]],
        max_open_positions: int,
        max_position_pct: float,
        default_sl_pct: float,
        default_tp_pct: float,
    ) -> AIAnalysisResult:
        prices_map = {s.symbol: s.current_price for s in snapshots}
        positions_payload = []
        for sym, pos in open_positions.items():
            cur_price = prices_map.get(sym, pos.entry_price)
            positions_payload.append(
                {
                    "symbol": sym,
                    "quantity": pos.quantity,
                    "entry_price": pos.entry_price,
                    "current_price": cur_price,
                    "highest_price": pos.highest_price,
                    "unrealized_pnl_pct": round(pos.unrealized_pnl_pct(cur_price), 2),
                    "locked_profit_pct": round(pos.locked_profit_pct(), 2),
                    "r_multiple": round(pos.r_multiple(cur_price), 2),
                    "stop_loss_price": pos.stop_loss_price,
                    "initial_stop_loss_price": pos.initial_stop_loss_price,
                    "take_profit_price": pos.take_profit_price,
                    "sl_adjustments_count": pos.sl_adjustments_count,
                    "opened_at": pos.opened_at,
                }
            )

        prompt_payload = {
            "strategy_rules": {
                "timeframe": "1h",
                "trend_indicator": "EMA 200",
                "oscillator": "Stochastic (14,3,3) levels 20 / 80",
                "entry_patterns": ["BULLISH_HAMMER", "BULLISH_ENGULFING", "BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"],
                "dynamic_profit_runner": "Move Stop-Loss and Take-Profit up on winning positions (action=ADJUST) to lock profits and let winners run",
                "risk_per_trade": "1% of total equity (min $1 USD) based on previous candle low/high stop-loss",
            },
            "portfolio": {
                "usdt_free": round(usdt_free, 2),
                "total_equity_usdt": round(total_equity_usdt, 2),
                "daily_pnl_pct": round(daily_pnl_pct, 2),
                "open_positions_count": len(open_positions),
                "max_open_positions": max_open_positions,
                "open_positions": positions_payload,
            },
            "market_candidates": [s.to_dict() for s in snapshots],
            "recent_trades": recent_trades[-8:],
        }

        user_prompt = (
            "Evalua los siguientes activos en temporalidad 1H aplicando la estrategia "
            "EMA 200 + Estocastico (20/80) + Vela Martillo/Envolvente, y ajusta dinamicamente "
            "el Stop-Loss y Take-Profit en las posiciones abiertas con ganancia para dejar correr "
            "las operaciones ganadoras. Emite tu decision en JSON:\n\n"
            + json.dumps(prompt_payload, indent=2, ensure_ascii=False)
        )

        try:
            raw_text = self._call_gemini(user_prompt)
            return self._parse_response(
                raw_text=raw_text,
                max_position_pct=max_position_pct,
                default_sl_pct=default_sl_pct,
                default_tp_pct=default_tp_pct,
            )
        except Exception as exc:
            logger.warning("Usando motor cuantitativo determinista de respaldo tras demora/error en Gemini API: %s", exc)
            return self._fallback_deterministic_analysis(
                snapshots=snapshots,
                open_positions=open_positions,
                max_position_pct=max_position_pct,
                default_sl_pct=default_sl_pct,
                default_tp_pct=default_tp_pct,
            )

    def _get_models_for_priority(self, high_priority: bool = True) -> list[str]:
        if high_priority:
            raw_order = ["gemini-4-hydrogen", self.model, "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite"]
        else:
            raw_order = ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-3.5-flash", self.model]
        return list(dict.fromkeys(m for m in raw_order if m))

    def _call_gemini(
        self,
        user_prompt: str,
        system_instruction: str = SYSTEM_INSTRUCTION,
        high_priority: bool = True,
        priority_tier: str | None = None,
        trigger_reason: str = "EVENT",
    ) -> str:
        models_to_try = self._get_models_for_priority(high_priority=high_priority)
        now = time.time()
        available_models = [m for m in models_to_try if self._model_cooldown_until.get(m, 0.0) <= now]
        self.last_model_used = ""
        if not available_models:
            raise RuntimeError("Todos los modelos Gemini en cooldown activo")

        tier_label = priority_tier or ("ALTA_PRIORIDAD" if high_priority else "GENERAL")
        call_start = time.perf_counter()
        last_err: Exception | None = None
        for mdl in available_models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{mdl}:generateContent"
            payload = {
                "system_instruction": {"parts": [{"text": system_instruction}]},
                "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
                "generationConfig": {
                    "temperature": 0.1,
                    "responseMimeType": "application/json",
                },
            }
            req_timeout = 18 if mdl == "gemini-4-hydrogen" else 15
            try:
                resp = requests.post(
                    url,
                    params={"key": self.api_key},
                    json=payload,
                    timeout=req_timeout,
                )
                if resp.status_code >= 400:
                    if resp.status_code in (429, 503):
                        self._model_cooldown_until[mdl] = time.time() + 900.0
                        logger.warning("Modelo %s en cooldown 15m tras HTTP %s.", mdl, resp.status_code)
                    last_err = RuntimeError(f"Error en Gemini API ({mdl}, HTTP {resp.status_code}): {resp.text[:250]}")
                    continue
                data = resp.json()
                candidates = data.get("candidates", [])
                if not candidates:
                    last_err = RuntimeError(f"Gemini ({mdl}) no devolvio candidatos.")
                    continue
                parts = candidates[0].get("content", {}).get("parts", [])
                text = "".join(part.get("text", "") for part in parts if "text" in part)
                if text.strip():
                    self._model_cooldown_until.pop(mdl, None)
                    self.last_model_used = mdl
                    latency_ms = int(round((time.perf_counter() - call_start) * 1000.0))
                    logger.info(
                        "Gemini API OK | model_used=%s | priority_tier=%s | latency_ms=%d | trigger_reason=%s",
                        mdl,
                        tier_label,
                        latency_ms,
                        trigger_reason,
                    )
                    return text
            except Exception as exc:
                last_err = exc
                if isinstance(exc, requests.exceptions.Timeout) or "timed out" in str(exc).lower():
                    self._model_cooldown_until[mdl] = time.time() + 900.0
                    logger.warning("Modelo %s en cooldown 15m tras timeout (%ss): %s", mdl, req_timeout, exc)
                else:
                    logger.warning("Intento con modelo %s fallo/excedio tiempo: %s", mdl, exc)

        if last_err:
            raise last_err
        raise RuntimeError("No se pudo obtener respuesta de Gemini API.")

    def _fallback_deterministic_analysis(
        self,
        snapshots: list[TechnicalSnapshot],
        open_positions: dict[str, PositionState],
        max_position_pct: float,
        default_sl_pct: float,
        default_tp_pct: float,
    ) -> AIAnalysisResult:
        bullish_count = sum(1 for s in snapshots if s.above_ema_200)
        regime = "BULLISH" if bullish_count >= len(snapshots) / 2 else "BEARISH"
        decisions: list[AIDecision] = []

        for s in snapshots:
            pos = open_positions.get(s.symbol)
            if pos is not None:
                pnl = pos.unrealized_pnl_pct(s.current_price)
                if s.stoch_k >= 80.0 and s.candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"):
                    decisions.append(
                        AIDecision(
                            symbol=s.symbol,
                            action="SELL",
                            confidence=90,
                            allocation_pct=1.0,
                            stop_loss_pct=default_sl_pct,
                            take_profit_pct=default_tp_pct,
                            reasoning=f"Estocastico en sobrecompra ({s.stoch_k}) con vela bajista {s.candle_pattern}.",
                        )
                    )
                elif pnl > 1.0:
                    new_sl = max(pos.stop_loss_price, s.prev_candle_low, round(pos.entry_price + (s.current_price - pos.entry_price) * 0.65, 8))
                    new_tp = max(pos.take_profit_price, round(s.current_price * 1.04, 8))
                    decisions.append(
                        AIDecision(
                            symbol=s.symbol,
                            action="ADJUST",
                            confidence=85,
                            allocation_pct=max_position_pct,
                            stop_loss_pct=default_sl_pct,
                            take_profit_pct=default_tp_pct,
                            new_stop_loss_price=new_sl,
                            new_take_profit_price=new_tp,
                            reasoning="Posicion en ganancia: subiendo Stop-Loss y expandiendo Take-Profit para dejar correr la tendencia.",
                        )
                    )
                else:
                    decisions.append(
                        AIDecision(
                            symbol=s.symbol,
                            action="HOLD",
                            confidence=75,
                            allocation_pct=max_position_pct,
                            stop_loss_pct=default_sl_pct,
                            take_profit_pct=default_tp_pct,
                            reasoning="Manteniendo posicion abierta bajo vigilancia de SL y Estocastico.",
                        )
                    )
            elif s.strategy_setup == "LONG_ENTRY":
                pillar_label = s.entry_pillar if s.entry_pillar != "NONE" else "P1_EMA200_PULLBACK"
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="BUY",
                        confidence=89,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Pilar LONG {pillar_label} activado (Stoch %K={s.stoch_k}, RSI={s.rsi_14}, BB %B={s.bb_pct_b}, Vela={s.candle_pattern}).",
                    )
                )
            elif s.strategy_setup == "SHORT_ENTRY" and s.entry_pillar == "S1_EMA200_RESISTANCE_REJECT":
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="SHORT",
                        confidence=88,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Pilar SHORT S1_EMA200_RESISTANCE_REJECT activado para Futuros (Stoch %K={s.stoch_k}, RSI={s.rsi_14}, BB %B={s.bb_pct_b}, Vela={s.candle_pattern}).",
                    )
                )
            elif s.entry_pillar == "M15_SCALPER_PULLBACK_LONG":
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="BUY",
                        confidence=84,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Scalper M15 Pullback LONG activado (EMA 9>21>50 en 15m, Stoch %K={s.stoch_k:.1f}).",
                    )
                )
            elif s.entry_pillar == "M15_SCALPER_PULLBACK_SHORT":
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="SHORT",
                        confidence=84,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Scalper M15 Pullback SHORT activado para Futuros (EMA 9<21<50 en 15m, Stoch %K={s.stoch_k:.1f}).",
                    )
                )
            else:
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="HOLD",
                        confidence=70,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Esperando setup completo (EMA200={'Alcista' if s.above_ema_200 else 'Bajista'}, Stoch %K={s.stoch_k}, Vela={s.candle_pattern}).",
                    )
                )

        return AIAnalysisResult(
            market_regime=regime,
            summary=f"Evaluacion cuantitativa completada sobre {len(snapshots)} pares en 1H ({bullish_count} sobre EMA 200).",
            decisions=decisions,
        )

    def _parse_response(
        self,
        raw_text: str,
        max_position_pct: float,
        default_sl_pct: float,
        default_tp_pct: float,
    ) -> AIAnalysisResult:
        cleaned = raw_text.strip()
        if cleaned.startswith("```"):
            lines = cleaned.splitlines()
            lines = [ln for ln in lines if not ln.strip().startswith("```")]
            cleaned = "\n".join(lines).strip()

        parsed = json.loads(cleaned)
        regime = str(parsed.get("market_regime", "SIDEWAYS")).upper()
        summary = str(parsed.get("summary", "Sin resumen disponible."))

        decisions: list[AIDecision] = []
        for item in parsed.get("decisions", []):
            sym = str(item.get("symbol", "")).upper().strip()
            action = str(item.get("action", "HOLD")).upper().strip()
            if not sym or action not in ("BUY", "SHORT", "SELL", "ADJUST", "HOLD"):
                continue

            confidence = max(0, min(100, _safe_int(item.get("confidence", 50), 50)))
            alloc = float(item.get("allocation_pct", max_position_pct))
            alloc = max(0.01, min(max_position_pct, alloc)) if action in ("BUY", "SHORT") else 1.0

            sl_pct = float(item.get("stop_loss_pct", default_sl_pct))
            sl_pct = max(0.002, min(0.15, sl_pct))

            tp_pct = float(item.get("take_profit_pct", default_tp_pct))
            tp_pct = max(0.005, min(0.35, tp_pct))

            new_sl = float(item.get("new_stop_loss_price") or 0.0)
            new_tp = float(item.get("new_take_profit_price") or 0.0)

            reasoning = str(item.get("reasoning", "")).strip()
            decisions.append(
                AIDecision(
                    symbol=sym,
                    action=action,
                    confidence=confidence,
                    allocation_pct=alloc,
                    stop_loss_pct=sl_pct,
                    take_profit_pct=tp_pct,
                    reasoning=reasoning,
                    new_stop_loss_price=max(0.0, new_sl),
                    new_take_profit_price=max(0.0, new_tp),
                )
            )

        return AIAnalysisResult(
            market_regime=regime,
            summary=summary,
            decisions=decisions,
        )

    @staticmethod
    def _clean_json_text(raw_text: str) -> dict[str, Any]:
        cleaned = raw_text.strip()
        if cleaned.startswith("```"):
            lines = [ln for ln in cleaned.splitlines() if not ln.strip().startswith("```")]
            cleaned = "\n".join(lines).strip()
        return json.loads(cleaned)

    @staticmethod
    def _compact_llm_snapshot(
        snap: dict[str, Any] | None,
        parent_item: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        src = snap if isinstance(snap, dict) else {}
        parent = parent_item if isinstance(parent_item, dict) else {}
        keep_keys = (
            "symbol",
            "bid",
            "ask",
            "spread_points",
            "htf_trend",
            "above_ema_200",
            "ema200_slope_positive",
            "ema_200",
            "ema_50",
            "ema_21",
            "dist_to_ema200_atr",
            "adx_14",
            "stoch_k",
            "stoch_d",
            "stoch_turning_up",
            "stoch_turning_down",
            "rsi_14",
            "bb_pct_b",
            "macd_hist",
            "macd_improving",
            "atr_price",
            "atr_pct",
            "candle_pattern",
            "recent_h1_closes",
            "swing_high_20",
            "swing_low_20",
            "entry_pillar",
            "strategy_setup",
        )
        out: dict[str, Any] = {}
        for k in keep_keys:
            if k in src and src[k] is not None:
                out[k] = src[k]
            elif k in parent and parent[k] is not None:
                out[k] = parent[k]

        out.setdefault("adx_14", float(src.get("adx_14", parent.get("adx_14", 0.0)) or 0.0))
        out.setdefault(
            "dist_to_ema200_atr",
            float(src.get("dist_to_ema200_atr", parent.get("dist_to_ema200_atr", 0.0)) or 0.0),
        )
        out.setdefault(
            "recent_h1_closes",
            list(src.get("recent_h1_closes") or parent.get("recent_h1_closes") or []),
        )
        out.setdefault("swing_high_20", float(src.get("swing_high_20", parent.get("swing_high_20", 0.0)) or 0.0))
        out.setdefault("swing_low_20", float(src.get("swing_low_20", parent.get("swing_low_20", 0.0)) or 0.0))
        return out

    @staticmethod
    def _compact_market_context(
        market_context: dict[str, Any] | None,
        open_positions_data: list[dict[str, Any]],
        candidates_data: list[dict[str, Any]],
    ) -> dict[str, Any]:
        if not isinstance(market_context, dict):
            return {}
        relevant_symbols: set[str] = set(MACRO_ANCHOR_SYMBOLS)
        for item in open_positions_data:
            sym = str(item.get("symbol", "")).strip()
            if sym:
                relevant_symbols.add(sym)
        for item in candidates_data:
            sym = str(item.get("symbol", "")).strip()
            if sym:
                relevant_symbols.add(sym)

        compact_ctx = dict(market_context)
        overview = compact_ctx.get("all_assets_overview")
        if isinstance(overview, list):
            compact_ctx["all_assets_overview"] = [
                row
                for row in overview
                if isinstance(row, dict) and str(row.get("symbol", "")).strip() in relevant_symbols
            ]
        return compact_ctx

    def evaluate_mt5_market(
        self,
        open_positions_data: list[dict[str, Any]],
        candidates_data: list[dict[str, Any]],
        recent_closes_data: list[dict[str, Any]],
        high_priority: bool = True,
        market_context: dict[str, Any] | None = None,
        trigger_reason: str = "EVENT",
    ) -> MT5AICycleEvaluation:
        """
        Evalua posiciones abiertas (en positivo/negativo), candidatos de entrada y cierres recientes
        (MANUAL / POSITIVE / NEGATIVE) en MT5 usando Gemini AI (metricas tecnicas puras) + base cuantitativa + contexto macro 360°.
        Si high_priority=True prioriza el modelo principal; si False usa los modelos ligeros primero.
        """
        priority_tier = "ALTA_PRIORIDAD" if high_priority else "GENERAL"
        news_alert = bool(((market_context or {}).get("news_and_session") or {}).get("news_volatility_alert", False))
        if not open_positions_data and not candidates_data and not recent_closes_data:
            return MT5AICycleEvaluation(
                market_summary="Sin posiciones abiertas, candidatos ni cierres recientes por evaluar.",
                open_reviews={},
                candidate_evals={},
                closed_evals={},
                priority_tier=priority_tier,
                model_used="quant_local",
            )

        quant_open: dict[str, tuple[int, str]] = {}
        enriched_open: list[dict[str, Any]] = []
        llm_open: list[dict[str, Any]] = []
        for item in open_positions_data:
            sym = str(item.get("symbol", "")).strip()
            snap = item.get("snapshot") or {}
            snap_with_sym = snap if snap.get("symbol") else {**snap, "symbol": sym}
            side = str(item.get("side", "BUY")).upper()
            q_prob, q_reason = compute_mt5_quant_probability(
                snap_with_sym,
                side,
                open_pos=item,
                market_context=market_context,
            )
            quant_open[sym] = (q_prob, q_reason)
            enriched_open.append(item)

            clean_open = {
                k: v
                for k, v in item.items()
                if k not in ("quant_probability_pct", "quant_reason", "snapshot")
            }
            clean_open["move_atr"] = round(float(item.get("move_atr", snap.get("move_atr", 0.0)) or 0.0), 3)
            clean_open["hours_open"] = round(float(item.get("hours_open", snap.get("hours_open", 0.0)) or 0.0), 2)
            clean_open["snapshot"] = self._compact_llm_snapshot(snap_with_sym, item)
            llm_open.append(clean_open)

        quant_cand: dict[str, tuple[int, str]] = {}
        enriched_cands: list[dict[str, Any]] = []
        llm_cands: list[dict[str, Any]] = []
        for item in candidates_data:
            sym = str(item.get("symbol", "")).strip()
            snap = item.get("snapshot") or {}
            snap_with_sym = snap if snap.get("symbol") else {**snap, "symbol": sym}
            side = str(item.get("side", "BUY")).upper()
            recent_close = item.get("recent_close")
            symbol_perf = item.get("symbol_perf")
            q_prob, q_reason = compute_mt5_quant_probability(
                snap_with_sym,
                side,
                recent_close=recent_close,
                symbol_perf=symbol_perf,
                market_context=market_context,
            )
            quant_cand[sym] = (q_prob, q_reason)
            enriched_cands.append(item)

            clean_cand = {
                k: v
                for k, v in item.items()
                if k not in ("quant_probability_pct", "quant_reason", "snapshot", "recent_close")
            }
            if isinstance(recent_close, dict):
                clean_cand["recent_close"] = {
                    k: v
                    for k, v in recent_close.items()
                    if k not in ("quant_probability_pct", "quant_reason", "snapshot")
                }
            else:
                clean_cand["recent_close"] = recent_close
            clean_cand["snapshot"] = self._compact_llm_snapshot(snap_with_sym, item)
            llm_cands.append(clean_cand)

        quant_closed: dict[str, tuple[int, str]] = {}
        latest_closes_by_sym: dict[str, dict[str, Any]] = {}
        latest_llm_closes_by_sym: dict[str, dict[str, Any]] = {}
        for item in recent_closes_data:
            sym = str(item.get("symbol", "")).strip()
            snap = item.get("snapshot") or {}
            snap_with_sym = snap if snap.get("symbol") else {**snap, "symbol": sym}
            side = str(item.get("side", "BUY")).upper()
            q_prob, q_reason = compute_mt5_quant_probability(
                snap_with_sym,
                side,
                recent_close=item,
                market_context=market_context,
            )
            quant_closed[sym] = (q_prob, q_reason)
            latest_closes_by_sym[sym] = item

            clean_close = {
                k: v
                for k, v in item.items()
                if k not in ("quant_probability_pct", "quant_reason", "snapshot")
            }
            clean_close["snapshot"] = self._compact_llm_snapshot(snap_with_sym, item)
            latest_llm_closes_by_sym[sym] = clean_close
        enriched_closes = list(latest_closes_by_sym.values())
        llm_closes = list(latest_llm_closes_by_sym.values())

        if not self.api_key:
            return self._build_mt5_eval_result(
                parsed=None,
                enriched_open=enriched_open,
                enriched_cands=enriched_cands,
                enriched_closes=enriched_closes,
                quant_open=quant_open,
                quant_cand=quant_cand,
                quant_closed=quant_closed,
                fallback_reason="Sin API key de Gemini configurada; usando motor cuantitativo.",
                priority_tier=priority_tier,
                model_used="quant_local",
                news_alert=news_alert,
            )

        compact_context = self._compact_market_context(
            market_context=market_context,
            open_positions_data=open_positions_data,
            candidates_data=candidates_data,
        )
        payload = {
            "trigger_reason": trigger_reason,
            "global_market_context": compact_context,
            "open_positions": llm_open,
            "entry_candidates": llm_cands,
            "recent_closes_last_90m": llm_closes,
        }
        user_prompt = (
            "Evalua el mercado actual en MetaTrader 5 (Exness) usando las metricas tecnicas puras y el contexto macro. "
            "Para cada posicion abierta estima su probabilidad independiente de TP y si conviene HOLD, PROTECT_PROFIT o CLOSE_NOW. "
            "Para cada cierre reciente (MANUAL/POSITIVE/NEGATIVE) y cada candidato, estima la probabilidad real (0-100%) de reactivarlo/operarlo con exito:\n\n"
            + json.dumps(payload, ensure_ascii=False)
        )

        try:
            raw_text = self._call_gemini(
                user_prompt,
                system_instruction=MT5_SYSTEM_INSTRUCTION,
                high_priority=high_priority,
                priority_tier=priority_tier,
                trigger_reason=trigger_reason,
            )
            parsed = self._clean_json_text(raw_text)
            return self._build_mt5_eval_result(
                parsed=parsed,
                enriched_open=enriched_open,
                enriched_cands=enriched_cands,
                enriched_closes=enriched_closes,
                quant_open=quant_open,
                quant_cand=quant_cand,
                quant_closed=quant_closed,
                priority_tier=priority_tier,
                model_used=self.last_model_used or "quant_local",
                news_alert=news_alert,
            )
        except Exception as exc:
            logger.warning("Gemini MT5 API fallo o excedio tiempo (%s); usando respaldo cuantitativo determinista.", exc)
            return self._build_mt5_eval_result(
                parsed=None,
                enriched_open=enriched_open,
                enriched_cands=enriched_cands,
                enriched_closes=enriched_closes,
                quant_open=quant_open,
                quant_cand=quant_cand,
                quant_closed=quant_closed,
                fallback_reason="Respaldo cuantitativo determinista activo.",
                priority_tier=priority_tier,
                model_used="quant_local",
                news_alert=news_alert,
            )

    def _build_mt5_eval_result(
        self,
        parsed: dict[str, Any] | None,
        enriched_open: list[dict[str, Any]],
        enriched_cands: list[dict[str, Any]],
        enriched_closes: list[dict[str, Any]],
        quant_open: dict[str, tuple[int, str]],
        quant_cand: dict[str, tuple[int, str]],
        quant_closed: dict[str, tuple[int, str]],
        fallback_reason: str = "",
        priority_tier: str = "GENERAL",
        model_used: str = "quant_local",
        news_alert: bool = False,
    ) -> MT5AICycleEvaluation:
        parsed_open: dict[str, dict[str, Any]] = {}
        parsed_cands: dict[str, dict[str, Any]] = {}
        parsed_closed: dict[str, dict[str, Any]] = {}

        if parsed:
            for item in parsed.get("open_reviews", []):
                sym_key = str(item.get("symbol", "")).strip().upper()
                if sym_key:
                    parsed_open[sym_key] = item
            for item in parsed.get("candidate_evals", []):
                sym_key = str(item.get("symbol", "")).strip().upper()
                if sym_key:
                    parsed_cands[sym_key] = item
            for item in parsed.get("closed_evals", []):
                sym_key = str(item.get("symbol", "")).strip().upper()
                if sym_key:
                    parsed_closed[sym_key] = item

        open_reviews: dict[str, MT5PositionAIReview] = {}
        for item in enriched_open:
            sym = str(item.get("symbol", "")).strip()
            q_prob, q_reason = quant_open[sym]
            profit_usd = float(item.get("profit_usd", 0.0) or 0.0)
            move_atr = float(item.get("move_atr", 0.0) or 0.0)
            ai_item = parsed_open.get(sym.upper())

            if ai_item is not None:
                ai_prob = max(5, min(95, _safe_int(ai_item.get("tp_probability_pct", q_prob), q_prob)))
                final_prob = max(5, min(95, int(round(0.45 * ai_prob + 0.55 * q_prob))))
                action = str(ai_item.get("action", "HOLD")).upper().strip()
                if action not in ("HOLD", "PROTECT_PROFIT", "CLOSE_NOW"):
                    action = "HOLD"
                reasoning = str(ai_item.get("reasoning", "")).strip() or q_reason
            else:
                final_prob = q_prob
                action = "HOLD"
                reasoning = q_reason

            # BUG-02: Sin sobrescrituras forzadas por news_alert o extended_open_6x.
            # Solo permitir PROTECT_PROFIT si move_atr >= 1.25 y final_prob < 65 (nunca en ganancias pequenas ni alta conviccion).
            can_protect_profit = profit_usd > 0.0 and move_atr >= 1.25 and final_prob < 65
            if action == "CLOSE_NOW" and (profit_usd < 0.40 or final_prob > 28):
                action = "PROTECT_PROFIT" if can_protect_profit else "HOLD"
            elif profit_usd >= 0.40 and final_prob <= 28 and ai_item is None:
                action = "CLOSE_NOW"
            elif action == "HOLD" and can_protect_profit and final_prob < 50:
                action = "PROTECT_PROFIT"
            elif action == "PROTECT_PROFIT" and not can_protect_profit:
                action = "HOLD"

            open_reviews[sym] = MT5PositionAIReview(
                symbol=sym,
                tp_probability_pct=final_prob,
                action=action,
                should_block_90m=final_prob < 60,
                reasoning=reasoning,
            )

        candidate_evals: dict[str, MT5CandidateAIEval] = {}
        for item in enriched_cands:
            sym = str(item.get("symbol", "")).strip()
            q_prob, q_reason = quant_cand[sym]
            recent_close = item.get("recent_close")
            mins_since = (
                float(recent_close.get("mins_since_close", 999.0) or 999.0)
                if isinstance(recent_close, dict)
                else 999.0
            )
            recent_close_type = (
                str(recent_close.get("close_type", "")).upper()
                if isinstance(recent_close, dict)
                else ""
            )
            symbol_perf = item.get("symbol_perf")
            req_prob = _safe_int(symbol_perf.get("min_required_prob_pct", 55), 55) if isinstance(symbol_perf, dict) else 55
            ai_item = parsed_cands.get(sym.upper())

            if ai_item is not None:
                ai_prob = max(5, min(95, _safe_int(ai_item.get("win_probability_pct", q_prob), q_prob)))
                if recent_close_type in ("NEGATIVE", "MANUAL") and mins_since < 20.0:
                    blended = min(ai_prob, q_prob)
                else:
                    blended = int(round(0.45 * ai_prob + 0.55 * q_prob))
                final_prob = max(5, min(95, blended))
                reasoning = str(ai_item.get("reasoning", "")).strip() or q_reason
            else:
                final_prob = q_prob
                reasoning = q_reason

            candidate_evals[sym] = MT5CandidateAIEval(
                symbol=sym,
                win_probability_pct=final_prob,
                should_block_90m=final_prob < req_prob,
                reasoning=reasoning,
                required_probability_pct=req_prob,
            )

        closed_evals: dict[str, MT5ClosedTradeAIEval] = {}
        for item in enriched_closes:
            sym = str(item.get("symbol", "")).strip()
            q_prob, q_reason = quant_closed[sym]
            close_type = str(item.get("close_type", "NEGATIVE")).upper()
            profit_usd = float(item.get("profit_usd", 0.0) or 0.0)
            mins_since = float(item.get("mins_since_close", 999.0) or 999.0)
            ai_item = parsed_closed.get(sym.upper())

            if ai_item is not None:
                ai_prob = max(5, min(95, _safe_int(ai_item.get("reactivate_probability_pct", q_prob), q_prob)))
                if close_type in ("NEGATIVE", "MANUAL") and mins_since < 20.0:
                    blended = min(ai_prob, q_prob)
                else:
                    blended = int(round(0.45 * ai_prob + 0.55 * q_prob))
                final_prob = max(5, min(95, blended))
                reasoning = str(ai_item.get("reasoning", "")).strip() or q_reason
            else:
                final_prob = q_prob
                reasoning = q_reason

            closed_evals[sym] = MT5ClosedTradeAIEval(
                symbol=sym,
                close_type=close_type,
                profit_usd=round(profit_usd, 2),
                reactivate_probability_pct=final_prob,
                should_block_90m=final_prob < 60,
                reasoning=reasoning,
            )

        summary = (
            str(parsed.get("market_summary", "")).strip()
            if parsed
            else fallback_reason or "Evaluacion cuantitativa MT5 completada."
        )
        return MT5AICycleEvaluation(
            market_summary=summary or "Evaluacion IA/cuantitativa MT5 completada.",
            open_reviews=open_reviews,
            candidate_evals=candidate_evals,
            closed_evals=closed_evals,
            priority_tier=priority_tier,
            model_used=model_used,
        )
