from __future__ import annotations

import math
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Sequence

import numpy as np

from src.market_scanner import detect_candle_pattern

# Canonical market regimes
REGIME_TREND_UP = "TREND_UP"
REGIME_TREND_DOWN = "TREND_DOWN"
REGIME_RANGE = "RANGE"
REGIME_HIGH_VOL_CHOP = "HIGH_VOL_CHOP"
ALL_REGIMES = (
    REGIME_TREND_UP,
    REGIME_TREND_DOWN,
    REGIME_RANGE,
    REGIME_HIGH_VOL_CHOP,
)

# Canonical trading sessions (UTC)
SESSION_ASIA = "ASIA"
SESSION_LONDON = "LONDON"
SESSION_NY_OVERLAP = "NY_OVERLAP"
SESSION_NEW_YORK = "NEW_YORK"
SESSION_ROLLOVER = "ROLLOVER"
ALL_SESSIONS = (
    SESSION_ASIA,
    SESSION_LONDON,
    SESSION_NY_OVERLAP,
    SESSION_NEW_YORK,
    SESSION_ROLLOVER,
)

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
METALS_SYMBOLS = {"XAUUSDm", "XAGUSDm"}
INDICES_SYMBOLS = {"US500m", "USTECm", "US30m"}
CRYPTO_SYMBOLS = {"BTCUSDm", "ETHUSDm"}


def get_asset_class(symbol: str) -> str:
    if symbol in CRYPTO_SYMBOLS:
        return "CRYPTO"
    if symbol in METALS_SYMBOLS:
        return "METALS"
    if symbol in INDICES_SYMBOLS:
        return "INDICES"
    if symbol in FOREX_SYMBOLS:
        return "FOREX"
    return "OTHER"


def classify_session(ts: datetime | int | float | None) -> str:
    """Classify UTC timestamp into market session consistent with mt5_bot.py blackout."""
    if ts is None:
        dt = datetime.now(timezone.utc)
    elif isinstance(ts, (int, float)):
        dt = datetime.fromtimestamp(float(ts), tz=timezone.utc)
    else:
        dt = ts.astimezone(timezone.utc) if ts.tzinfo else ts.replace(tzinfo=timezone.utc)

    mins = dt.hour * 60 + dt.minute
    if (20 * 60 + 30) <= mins <= (23 * 60 + 59):
        return SESSION_ROLLOVER
    if 0 <= mins < (7 * 60):
        return SESSION_ASIA
    if (7 * 60) <= mins < (12 * 60):
        return SESSION_LONDON
    if (12 * 60) <= mins < (16 * 60):
        return SESSION_NY_OVERLAP
    return SESSION_NEW_YORK


@dataclass
class RegimeSnapshot:
    regime: str  # TREND_UP | TREND_DOWN | RANGE | HIGH_VOL_CHOP
    adx_14: float
    ema200_slope_atr: float
    dist_ema200_atr: float
    atr_percentile: float
    bb_width: float
    bb_width_percentile: float
    confidence: float
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class StrategySignal:
    symbol: str
    strategy_name: str
    direction: str  # BUY | SELL | NONE
    score: float  # 0..100
    entry_price: float
    sl_price: float
    tp_price: float
    rr_ratio: float
    regime: str
    setup_stage: str  # READY | FORMING | NONE
    forming_hint: str
    invalidation_level: float
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class IndicatorArrays:
    """Precomputed numpy indicator arrays for fast O(1)-per-bar evaluation."""

    n: int
    times: np.ndarray
    opens: np.ndarray
    highs: np.ndarray
    lows: np.ndarray
    closes: np.ndarray
    volumes: np.ndarray
    ema_9: np.ndarray
    ema_21: np.ndarray
    ema_50: np.ndarray
    ema_200: np.ndarray
    atr_14: np.ndarray
    adx_14: np.ndarray
    plus_di: np.ndarray
    minus_di: np.ndarray
    rsi_14: np.ndarray
    stoch_k: np.ndarray
    stoch_d: np.ndarray
    bb_mid: np.ndarray
    bb_upper: np.ndarray
    bb_lower: np.ndarray
    bb_pct_b: np.ndarray
    bb_width: np.ndarray
    macd_line: np.ndarray
    macd_signal: np.ndarray
    macd_hist: np.ndarray
    atr_pctile: np.ndarray
    bb_width_pctile: np.ndarray
    ema200_slope_atr: np.ndarray
    dist_ema200_atr: np.ndarray
    swing_high_20: np.ndarray
    swing_low_20: np.ndarray


def _ema_np(values: np.ndarray, period: int) -> np.ndarray:
    n = len(values)
    out = np.empty(n, dtype=np.float64)
    if n == 0:
        return out
    if period <= 1:
        return values.astype(np.float64, copy=True)
    k = 2.0 / (period + 1.0)
    omk = 1.0 - k
    if n < period:
        out[0] = values[0]
        for i in range(1, n):
            out[i] = values[i] * k + out[i - 1] * omk
        return out
    running = 0.0
    for i in range(period):
        running += values[i]
        out[i] = running / (i + 1)
    prev = out[period - 1]
    for i in range(period, n):
        prev = values[i] * k + prev * omk
        out[i] = prev
    return out


def _rsi_np(closes: np.ndarray, period: int = 14) -> np.ndarray:
    n = len(closes)
    out = np.full(n, 50.0, dtype=np.float64)
    if n <= period:
        return out
    diffs = np.diff(closes)
    gains = np.maximum(diffs, 0.0)
    losses = np.maximum(-diffs, 0.0)
    avg_gain = float(np.mean(gains[:period]))
    avg_loss = float(np.mean(losses[:period]))
    out[period] = 100.0 if avg_loss == 0.0 else 100.0 - (100.0 / (1.0 + avg_gain / avg_loss))
    pm1 = period - 1.0
    for i in range(period, len(diffs)):
        avg_gain = (avg_gain * pm1 + gains[i]) / period
        avg_loss = (avg_loss * pm1 + losses[i]) / period
        if avg_loss == 0.0:
            out[i + 1] = 100.0
        else:
            out[i + 1] = 100.0 - (100.0 / (1.0 + avg_gain / avg_loss))
    return out


def _atr_adx_np(
    highs: np.ndarray,
    lows: np.ndarray,
    closes: np.ndarray,
    period: int = 14,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    n = len(closes)
    atr = np.zeros(n, dtype=np.float64)
    adx = np.full(n, 20.0, dtype=np.float64)
    plus_di = np.full(n, 20.0, dtype=np.float64)
    minus_di = np.full(n, 20.0, dtype=np.float64)
    if n == 0:
        return atr, adx, plus_di, minus_di
    atr[0] = max(0.0, highs[0] - lows[0])
    if n == 1:
        return atr, adx, plus_di, minus_di

    tr = np.empty(n, dtype=np.float64)
    pdm = np.zeros(n, dtype=np.float64)
    mdm = np.zeros(n, dtype=np.float64)
    tr[0] = highs[0] - lows[0]
    for i in range(1, n):
        hi = highs[i]
        lo = lows[i]
        pc = closes[i - 1]
        tr[i] = max(hi - lo, abs(hi - pc), abs(lo - pc))
        up = hi - highs[i - 1]
        dn = lows[i - 1] - lo
        if up > dn and up > 0.0:
            pdm[i] = up
        elif dn > up and dn > 0.0:
            mdm[i] = dn

    # Wilder ATR
    if n <= period:
        for i in range(1, n):
            atr[i] = float(np.mean(tr[1 : i + 1]))
        return atr, adx, plus_di, minus_di

    for i in range(1, period):
        atr[i] = float(np.mean(tr[1 : i + 1]))
    atr_val = float(np.mean(tr[1 : period + 1]))
    atr[period] = atr_val
    pm1 = period - 1.0
    for i in range(period + 1, n):
        atr_val = (atr_val * pm1 + tr[i]) / period
        atr[i] = atr_val

    # Wilder ADX / +DI / -DI
    if n < period * 2 + 2:
        return atr, adx, plus_di, minus_di

    atr_s = float(np.sum(tr[1 : period + 1]))
    p_s = float(np.sum(pdm[1 : period + 1]))
    m_s = float(np.sum(mdm[1 : period + 1]))
    dx = np.zeros(n, dtype=np.float64)
    for i in range(period, n):
        if i > period:
            atr_s = atr_s - (atr_s / period) + tr[i]
            p_s = p_s - (p_s / period) + pdm[i]
            m_s = m_s - (m_s / period) + mdm[i]
        if atr_s > 0.0:
            pdi = 100.0 * p_s / atr_s
            mdi = 100.0 * m_s / atr_s
            plus_di[i] = pdi
            minus_di[i] = mdi
            s = pdi + mdi
            dx[i] = 100.0 * abs(pdi - mdi) / s if s > 0.0 else 0.0

    start_adx = period * 2 - 1
    adx_val = float(np.mean(dx[period : start_adx + 1]))
    adx[start_adx] = adx_val
    for i in range(start_adx + 1, n):
        adx_val = (adx_val * pm1 + dx[i]) / period
        adx[i] = adx_val
    return atr, adx, plus_di, minus_di


def _stoch_np(
    highs: np.ndarray,
    lows: np.ndarray,
    closes: np.ndarray,
    k_period: int = 14,
    smooth_k: int = 3,
    d_period: int = 3,
) -> tuple[np.ndarray, np.ndarray]:
    n = len(closes)
    k_out = np.full(n, 50.0, dtype=np.float64)
    d_out = np.full(n, 50.0, dtype=np.float64)
    if n < k_period:
        return k_out, d_out

    raw_k = np.full(n, 50.0, dtype=np.float64)
    for i in range(k_period - 1, n):
        hh = float(np.max(highs[i - k_period + 1 : i + 1]))
        ll = float(np.min(lows[i - k_period + 1 : i + 1]))
        denom = hh - ll
        val = ((closes[i] - ll) / denom) * 100.0 if denom > 0.0 else 50.0
        raw_k[i] = max(0.0, min(100.0, val))

    for i in range(k_period - 1, n):
        start = max(k_period - 1, i - smooth_k + 1)
        k_out[i] = float(np.mean(raw_k[start : i + 1]))
    for i in range(k_period - 1, n):
        start = max(k_period - 1, i - d_period + 1)
        d_out[i] = float(np.mean(k_out[start : i + 1]))
    return k_out, d_out


def _bollinger_np(
    closes: np.ndarray, period: int = 20, std_dev: float = 2.0
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    n = len(closes)
    mid = closes.astype(np.float64, copy=True)
    upper = closes.astype(np.float64, copy=True)
    lower = closes.astype(np.float64, copy=True)
    pct_b = np.full(n, 0.5, dtype=np.float64)
    width = np.zeros(n, dtype=np.float64)
    if n < period:
        return mid, upper, lower, pct_b, width

    csum = np.cumsum(np.insert(closes, 0, 0.0))
    csum2 = np.cumsum(np.insert(closes * closes, 0, 0.0))
    m_vals = (csum[period:] - csum[:-period]) / period
    var_vals = np.maximum(0.0, (csum2[period:] - csum2[:-period]) / period - m_vals * m_vals)
    sd_vals = np.sqrt(var_vals)

    mid[period - 1 :] = m_vals
    upper[period - 1 :] = m_vals + std_dev * sd_vals
    lower[period - 1 :] = m_vals - std_dev * sd_vals

    bw = upper[period - 1 :] - lower[period - 1 :]
    safe_bw = np.where(bw > 0.0, bw, 1.0)
    pct_b[period - 1 :] = np.where(bw > 0.0, (closes[period - 1 :] - lower[period - 1 :]) / safe_bw, 0.5)
    safe_mid = np.where(m_vals > 0.0, m_vals, 1.0)
    width[period - 1 :] = np.where(m_vals > 0.0, bw / safe_mid, 0.0)
    return mid, upper, lower, pct_b, width


def _rolling_percentile_np(values: np.ndarray, window: int = 100) -> np.ndarray:
    n = len(values)
    out = np.full(n, 50.0, dtype=np.float64)
    if n < 5:
        return out
    for i in range(n):
        start = max(0, i - window + 1)
        w = values[start : i + 1]
        if len(w) < 5:
            out[i] = 50.0
        else:
            cur = values[i]
            out[i] = float(np.sum(w <= cur)) / len(w) * 100.0
    return out


def compute_indicators(candles: Sequence[dict[str, Any]]) -> IndicatorArrays:
    """Compute all technical indicators for a candle series (closed bars)."""
    n = len(candles)
    times = np.array([float(c.get("time", i)) for i, c in enumerate(candles)], dtype=np.float64)
    opens = np.array([float(c["open"]) for c in candles], dtype=np.float64)
    highs = np.array([float(c["high"]) for c in candles], dtype=np.float64)
    lows = np.array([float(c["low"]) for c in candles], dtype=np.float64)
    closes = np.array([float(c["close"]) for c in candles], dtype=np.float64)
    volumes = np.array([float(c.get("volume", c.get("tick_volume", 0.0))) for c in candles], dtype=np.float64)

    ema_9 = _ema_np(closes, 9)
    ema_21 = _ema_np(closes, 21)
    ema_50 = _ema_np(closes, 50)
    ema_200 = _ema_np(closes, 200)
    atr_14, adx_14, plus_di, minus_di = _atr_adx_np(highs, lows, closes, 14)
    rsi_14 = _rsi_np(closes, 14)
    stoch_k, stoch_d = _stoch_np(highs, lows, closes, 14, 3, 3)
    bb_mid, bb_upper, bb_lower, bb_pct_b, bb_width = _bollinger_np(closes, 20, 2.0)

    ema_12 = _ema_np(closes, 12)
    ema_26 = _ema_np(closes, 26)
    macd_line = ema_12 - ema_26
    macd_signal = _ema_np(macd_line, 9)
    macd_hist = macd_line - macd_signal

    atr_pctile = _rolling_percentile_np(atr_14, 100)
    bb_width_pctile = _rolling_percentile_np(bb_width, 100)

    ema200_slope_atr = np.zeros(n, dtype=np.float64)
    dist_ema200_atr = np.zeros(n, dtype=np.float64)
    for i in range(n):
        a = atr_14[i] if atr_14[i] > 0.0 else max(closes[i] * 0.002, 1e-8)
        prev_i = max(0, i - 6)
        ema200_slope_atr[i] = (ema_200[i] - ema_200[prev_i]) / a
        dist_ema200_atr[i] = (closes[i] - ema_200[i]) / a

    # Prior 20-bar swing high/low EXCLUDING current bar i (strictly no lookahead)
    swing_high_20 = np.copy(highs)
    swing_low_20 = np.copy(lows)
    for i in range(1, n):
        start = max(0, i - 20)
        swing_high_20[i] = float(np.max(highs[start:i]))
        swing_low_20[i] = float(np.min(lows[start:i]))

    return IndicatorArrays(
        n=n,
        times=times,
        opens=opens,
        highs=highs,
        lows=lows,
        closes=closes,
        volumes=volumes,
        ema_9=ema_9,
        ema_21=ema_21,
        ema_50=ema_50,
        ema_200=ema_200,
        atr_14=atr_14,
        adx_14=adx_14,
        plus_di=plus_di,
        minus_di=minus_di,
        rsi_14=rsi_14,
        stoch_k=stoch_k,
        stoch_d=stoch_d,
        bb_mid=bb_mid,
        bb_upper=bb_upper,
        bb_lower=bb_lower,
        bb_pct_b=bb_pct_b,
        bb_width=bb_width,
        macd_line=macd_line,
        macd_signal=macd_signal,
        macd_hist=macd_hist,
        atr_pctile=atr_pctile,
        bb_width_pctile=bb_width_pctile,
        ema200_slope_atr=ema200_slope_atr,
        dist_ema200_atr=dist_ema200_atr,
        swing_high_20=swing_high_20,
        swing_low_20=swing_low_20,
    )


class MarketRegimeClassifier:
    """Objective regime classifier using ADX, EMA200 slope/distance, ATR percentile, and BB width."""

    def __init__(
        self,
        adx_trend_threshold: float = 20.0,
        high_vol_atr_pctile: float = 88.0,
        extreme_vol_atr_pctile: float = 95.0,
    ) -> None:
        self.adx_trend_threshold = adx_trend_threshold
        self.high_vol_atr_pctile = high_vol_atr_pctile
        self.extreme_vol_atr_pctile = extreme_vol_atr_pctile

    def classify_at(self, ind: IndicatorArrays, idx: int = -1) -> RegimeSnapshot:
        if idx < 0:
            idx = ind.n + idx
        adx = float(ind.adx_14[idx])
        pdi = float(ind.plus_di[idx])
        mdi = float(ind.minus_di[idx])
        slope = float(ind.ema200_slope_atr[idx])
        dist = float(ind.dist_ema200_atr[idx])
        atr_p = float(ind.atr_pctile[idx])
        bb_w = float(ind.bb_width[idx])
        bb_wp = float(ind.bb_width_pctile[idx])
        close = float(ind.closes[idx])
        e21 = float(ind.ema_21[idx])
        e50 = float(ind.ema_50[idx])
        e200 = float(ind.ema_200[idx])

        # 1. HIGH_VOL_CHOP: volatility spike without clean directional trend
        if (atr_p >= self.extreme_vol_atr_pctile and adx < 26.0) or (
            atr_p >= self.high_vol_atr_pctile
            and bb_wp >= 82.0
            and (adx < 22.0 or abs(dist) < 1.0)
        ):
            conf = min(98.0, 60.0 + (atr_p - 80.0) * 1.5)
            return RegimeSnapshot(
                regime=REGIME_HIGH_VOL_CHOP,
                adx_14=round(adx, 2),
                ema200_slope_atr=round(slope, 3),
                dist_ema200_atr=round(dist, 2),
                atr_percentile=round(atr_p, 1),
                bb_width=round(bb_w, 5),
                bb_width_percentile=round(bb_wp, 1),
                confidence=round(conf, 1),
                reason=f"ATR pctile {atr_p:.0f}% & BBw pctile {bb_wp:.0f}% with weak/whipsaw ADX {adx:.1f}",
            )

        # 2. TREND_UP
        bull_align = close > e200 and (e50 >= e200 * 0.998 or e21 > e50) and slope >= -0.05
        if adx >= self.adx_trend_threshold and bull_align and (pdi >= mdi - 2.0 or dist >= 0.4):
            conf = min(98.0, 52.0 + (adx - self.adx_trend_threshold) * 1.5 + max(0.0, slope) * 18.0)
            return RegimeSnapshot(
                regime=REGIME_TREND_UP,
                adx_14=round(adx, 2),
                ema200_slope_atr=round(slope, 3),
                dist_ema200_atr=round(dist, 2),
                atr_percentile=round(atr_p, 1),
                bb_width=round(bb_w, 5),
                bb_width_percentile=round(bb_wp, 1),
                confidence=round(conf, 1),
                reason=f"ADX {adx:.1f}, price +{dist:.2f} ATR above EMA200 (slope {slope:+.2f})",
            )

        # 3. TREND_DOWN
        bear_align = close < e200 and (e50 <= e200 * 1.002 or e21 < e50) and slope <= 0.05
        if adx >= self.adx_trend_threshold and bear_align and (mdi >= pdi - 2.0 or dist <= -0.4):
            conf = min(98.0, 52.0 + (adx - self.adx_trend_threshold) * 1.5 + max(0.0, -slope) * 18.0)
            return RegimeSnapshot(
                regime=REGIME_TREND_DOWN,
                adx_14=round(adx, 2),
                ema200_slope_atr=round(slope, 3),
                dist_ema200_atr=round(dist, 2),
                atr_percentile=round(atr_p, 1),
                bb_width=round(bb_w, 5),
                bb_width_percentile=round(bb_wp, 1),
                confidence=round(conf, 1),
                reason=f"ADX {adx:.1f}, price {dist:.2f} ATR below EMA200 (slope {slope:+.2f})",
            )

        # 4. RANGE
        conf = min(95.0, 55.0 + max(0.0, self.adx_trend_threshold - adx) * 2.0)
        return RegimeSnapshot(
            regime=REGIME_RANGE,
            adx_14=round(adx, 2),
            ema200_slope_atr=round(slope, 3),
            dist_ema200_atr=round(dist, 2),
            atr_percentile=round(atr_p, 1),
            bb_width=round(bb_w, 5),
            bb_width_percentile=round(bb_wp, 1),
            confidence=round(conf, 1),
            reason=f"ADX {adx:.1f} / mixed EMA alignment (dist {dist:+.2f} ATR)",
        )

    def classify(self, candles: Sequence[dict[str, Any]]) -> RegimeSnapshot:
        ind = compute_indicators(candles)
        return self.classify_at(ind, -1)


def _candle_dict(ind: IndicatorArrays, idx: int) -> dict[str, float]:
    return {
        "open": float(ind.opens[idx]),
        "high": float(ind.highs[idx]),
        "low": float(ind.lows[idx]),
        "close": float(ind.closes[idx]),
    }


def _detect_pattern_at(ind: IndicatorArrays, idx: int, min_range: float) -> str:
    if idx < 2:
        return "NONE"
    c0 = _candle_dict(ind, idx)
    c1 = _candle_dict(ind, idx - 1)
    c2 = _candle_dict(ind, idx - 2) if idx >= 2 else None
    pat = detect_candle_pattern(c0, c1, c2, min_range=min_range)
    if pat != "NONE" or idx < 3:
        return pat
    return detect_candle_pattern(c1, c2, _candle_dict(ind, idx - 3), min_range=min_range)


def _none_signal(symbol: str, strategy_name: str, regime: str) -> StrategySignal:
    return StrategySignal(
        symbol=symbol,
        strategy_name=strategy_name,
        direction="NONE",
        score=0.0,
        entry_price=0.0,
        sl_price=0.0,
        tp_price=0.0,
        rr_ratio=0.0,
        regime=regime,
        setup_stage="NONE",
        forming_hint="",
        invalidation_level=0.0,
        metadata={},
    )


def _round_px(val: float, digits: int) -> float:
    return round(float(val), max(0, int(digits)))


class BaseMT5Strategy:
    name: str = "base_strategy"
    allowed_regimes: tuple[str, ...] = ALL_REGIMES

    def evaluate_at(
        self,
        symbol: str,
        ind: IndicatorArrays,
        idx: int,
        regime_snap: RegimeSnapshot,
        digits: int = 5,
        point: float = 1e-5,
    ) -> StrategySignal:
        raise NotImplementedError


class TrendPullbackEMAStochStrategy(BaseMT5Strategy):
    """Strategy 1: Trend Pullback using EMA200/EMA50/EMA21 + Stochastic + RSI + Candle Confirmation."""

    name = "trend_pullback_ema_stoch"
    allowed_regimes = (REGIME_TREND_UP, REGIME_TREND_DOWN)

    def evaluate_at(
        self,
        symbol: str,
        ind: IndicatorArrays,
        idx: int,
        regime_snap: RegimeSnapshot,
        digits: int = 5,
        point: float = 1e-5,
    ) -> StrategySignal:
        regime = regime_snap.regime
        if idx < 205 or regime not in self.allowed_regimes:
            return _none_signal(symbol, self.name, regime)

        close = float(ind.closes[idx])
        open_px = float(ind.opens[idx])
        high = float(ind.highs[idx])
        low = float(ind.lows[idx])
        atr = max(float(ind.atr_14[idx]), point * 20.0)
        adx = float(ind.adx_14[idx])
        if adx < 19.0 or adx > 46.0:
            return _none_signal(symbol, self.name, regime)

        e21 = float(ind.ema_21[idx])
        e50 = float(ind.ema_50[idx])
        e200 = float(ind.ema_200[idx])
        dist_atr = float(ind.dist_ema200_atr[idx])
        rsi = float(ind.rsi_14[idx])
        k = float(ind.stoch_k[idx])
        d = float(ind.stoch_d[idx])
        prev_k = float(ind.stoch_k[idx - 1])
        k_min4 = float(np.min(ind.stoch_k[max(0, idx - 3) : idx + 1]))
        k_max4 = float(np.max(ind.stoch_k[max(0, idx - 3) : idx + 1]))
        macd_improving = float(ind.macd_hist[idx]) > float(ind.macd_hist[idx - 1])
        macd_weakening = float(ind.macd_hist[idx]) < float(ind.macd_hist[idx - 1])
        pat = _detect_pattern_at(ind, idx, min_range=0.35 * atr)

        if regime == REGIME_TREND_UP and -0.5 <= dist_atr <= 4.5 and e50 >= e200 * 0.998:
            turning_up = k > prev_k or k >= d
            bull_candle = (
                pat in ("BULLISH_HAMMER", "BULLISH_ENGULFING", "MORNING_STAR")
                or (close > open_px and close > float(ind.highs[idx - 1]) * 0.9998)
            )
            near_value = (low <= e21 + 0.35 * atr) or (low <= e50 + 0.5 * atr) or (ind.bb_pct_b[idx] <= 0.38)
            if k_min4 <= 28.0 and k <= 48.0 and turning_up and rsi <= 54.0 and near_value and bull_candle:
                recent_low = float(np.min(ind.lows[max(0, idx - 2) : idx + 1]))
                sl_dist = max(1.3 * atr, min(2.6 * atr, close - recent_low + 0.45 * atr))
                sl = _round_px(close - sl_dist, digits)
                rr = 2.2
                tp = _round_px(close + sl_dist * rr, digits)
                score = 68.0
                if pat in ("BULLISH_HAMMER", "BULLISH_ENGULFING", "MORNING_STAR"):
                    score += 10.0
                if macd_improving:
                    score += 7.0
                if k_min4 <= 20.0:
                    score += 6.0
                if 22.0 <= adx <= 35.0:
                    score += 5.0
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="BUY",
                    score=round(min(98.0, score), 1),
                    entry_price=_round_px(close, digits),
                    sl_price=sl,
                    tp_price=tp,
                    rr_ratio=rr,
                    regime=regime,
                    setup_stage="READY",
                    forming_hint="",
                    invalidation_level=sl,
                    metadata={"pattern": pat, "stoch_k": round(k, 1), "rsi": round(rsi, 1), "adx": round(adx, 1)},
                )

            # FORMING BUY: pullback in progress, waiting for stoch turn / bullish candle
            if near_value and k <= 34.0 and rsi <= 48.0:
                inv = _round_px(min(e200 - 0.8 * atr, low - 1.5 * atr), digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="BUY",
                    score=54.0,
                    entry_price=_round_px(close, digits),
                    sl_price=inv,
                    tp_price=_round_px(close + 2.2 * max(atr, close - inv), digits),
                    rr_ratio=2.2,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"TREND_UP pullback near EMA21/50 (Stoch {k:.1f}, RSI {rsi:.1f}); wait for bullish trigger close",
                    invalidation_level=inv,
                    metadata={"stoch_k": round(k, 1), "rsi": round(rsi, 1), "adx": round(adx, 1)},
                )

        if regime == REGIME_TREND_DOWN and -4.5 <= dist_atr <= 0.5 and e50 <= e200 * 1.002:
            turning_down = k < prev_k or k <= d
            bear_candle = (
                pat in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING")
                or (close < open_px and close < float(ind.lows[idx - 1]) * 1.0002)
            )
            near_value = (high >= e21 - 0.35 * atr) or (high >= e50 - 0.5 * atr) or (ind.bb_pct_b[idx] >= 0.62)
            if k_max4 >= 72.0 and k >= 52.0 and turning_down and rsi >= 46.0 and near_value and bear_candle:
                recent_high = float(np.max(ind.highs[max(0, idx - 2) : idx + 1]))
                sl_dist = max(1.3 * atr, min(2.6 * atr, recent_high - close + 0.45 * atr))
                sl = _round_px(close + sl_dist, digits)
                rr = 2.2
                tp = _round_px(close - sl_dist * rr, digits)
                score = 68.0
                if pat in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"):
                    score += 10.0
                if macd_weakening:
                    score += 7.0
                if k_max4 >= 80.0:
                    score += 6.0
                if 22.0 <= adx <= 35.0:
                    score += 5.0
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="SELL",
                    score=round(min(98.0, score), 1),
                    entry_price=_round_px(close, digits),
                    sl_price=sl,
                    tp_price=tp,
                    rr_ratio=rr,
                    regime=regime,
                    setup_stage="READY",
                    forming_hint="",
                    invalidation_level=sl,
                    metadata={"pattern": pat, "stoch_k": round(k, 1), "rsi": round(rsi, 1), "adx": round(adx, 1)},
                )

            if near_value and k >= 66.0 and rsi >= 52.0:
                inv = _round_px(max(e200 + 0.8 * atr, high + 1.5 * atr), digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="SELL",
                    score=54.0,
                    entry_price=_round_px(close, digits),
                    sl_price=inv,
                    tp_price=_round_px(close - 2.2 * max(atr, inv - close), digits),
                    rr_ratio=2.2,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"TREND_DOWN pullback near EMA21/50 (Stoch {k:.1f}, RSI {rsi:.1f}); wait for bearish trigger close",
                    invalidation_level=inv,
                    metadata={"stoch_k": round(k, 1), "rsi": round(rsi, 1), "adx": round(adx, 1)},
                )

        return _none_signal(symbol, self.name, regime)


class VolatilitySqueezeBreakoutStrategy(BaseMT5Strategy):
    """Strategy 2: Bollinger Band Squeeze followed by expansion breakout."""

    name = "volatility_squeeze_breakout"
    allowed_regimes = (REGIME_RANGE, REGIME_TREND_UP, REGIME_TREND_DOWN)

    def evaluate_at(
        self,
        symbol: str,
        ind: IndicatorArrays,
        idx: int,
        regime_snap: RegimeSnapshot,
        digits: int = 5,
        point: float = 1e-5,
    ) -> StrategySignal:
        regime = regime_snap.regime
        if idx < 110 or regime not in self.allowed_regimes:
            return _none_signal(symbol, self.name, regime)

        close = float(ind.closes[idx])
        open_px = float(ind.opens[idx])
        high = float(ind.highs[idx])
        low = float(ind.lows[idx])
        atr = max(float(ind.atr_14[idx]), point * 20.0)
        bar_range = high - low
        bb_u = float(ind.bb_upper[idx])
        bb_l = float(ind.bb_lower[idx])
        bb_m = float(ind.bb_mid[idx])
        bb_b = float(ind.bb_pct_b[idx])
        bb_wp = float(ind.bb_width_pctile[idx])
        recent_squeeze = float(np.min(ind.bb_width_pctile[max(0, idx - 6) : idx]))
        adx = float(ind.adx_14[idx])
        adx_rising = adx >= float(ind.adx_14[idx - 1])
        e21 = float(ind.ema_21[idx])
        e50 = float(ind.ema_50[idx])
        rsi = float(ind.rsi_14[idx])

        # READY BUY breakout from squeeze
        if (
            recent_squeeze <= 25.0
            and close > bb_u
            and close > open_px
            and bar_range >= 0.85 * atr
            and e21 >= e50 * 0.999
            and 52.0 <= rsi <= 76.0
        ):
            sl_dist = max(1.4 * atr, min(2.4 * atr, close - bb_m + 0.35 * atr))
            sl = _round_px(close - sl_dist, digits)
            rr = 2.4
            tp = _round_px(close + sl_dist * rr, digits)
            score = 67.0 + (8.0 if recent_squeeze <= 15.0 else 0.0) + (7.0 if adx_rising else 0.0) + (6.0 if regime == REGIME_TREND_UP else 0.0)
            return StrategySignal(
                symbol=symbol,
                strategy_name=self.name,
                direction="BUY",
                score=round(min(96.0, score), 1),
                entry_price=_round_px(close, digits),
                sl_price=sl,
                tp_price=tp,
                rr_ratio=rr,
                regime=regime,
                setup_stage="READY",
                forming_hint="",
                invalidation_level=sl,
                metadata={"squeeze_pctile": round(recent_squeeze, 1), "bb_pct_b": round(bb_b, 2), "adx": round(adx, 1)},
            )

        # READY SELL breakout from squeeze
        if (
            recent_squeeze <= 25.0
            and close < bb_l
            and close < open_px
            and bar_range >= 0.85 * atr
            and e21 <= e50 * 1.001
            and 24.0 <= rsi <= 48.0
        ):
            sl_dist = max(1.4 * atr, min(2.4 * atr, bb_m - close + 0.35 * atr))
            sl = _round_px(close + sl_dist, digits)
            rr = 2.4
            tp = _round_px(close - sl_dist * rr, digits)
            score = 67.0 + (8.0 if recent_squeeze <= 15.0 else 0.0) + (7.0 if adx_rising else 0.0) + (6.0 if regime == REGIME_TREND_DOWN else 0.0)
            return StrategySignal(
                symbol=symbol,
                strategy_name=self.name,
                direction="SELL",
                score=round(min(96.0, score), 1),
                entry_price=_round_px(close, digits),
                sl_price=sl,
                tp_price=tp,
                rr_ratio=rr,
                regime=regime,
                setup_stage="READY",
                forming_hint="",
                invalidation_level=sl,
                metadata={"squeeze_pctile": round(recent_squeeze, 1), "bb_pct_b": round(bb_b, 2), "adx": round(adx, 1)},
            )

        # FORMING: tight squeeze coiled near upper or lower band
        if bb_wp <= 20.0:
            if bb_b >= 0.78 and e21 >= e50 * 0.999:
                inv = _round_px(bb_l, digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="BUY",
                    score=53.0,
                    entry_price=_round_px(bb_u, digits),
                    sl_price=inv,
                    tp_price=_round_px(bb_u + 2.4 * max(atr, bb_u - bb_m), digits),
                    rr_ratio=2.4,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"BB squeeze (width pctile {bb_wp:.0f}%) pressing upper band ({bb_u:.{digits}f}); watch for breakout close",
                    invalidation_level=inv,
                    metadata={"squeeze_pctile": round(bb_wp, 1), "bb_pct_b": round(bb_b, 2)},
                )
            if bb_b <= 0.22 and e21 <= e50 * 1.001:
                inv = _round_px(bb_u, digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="SELL",
                    score=53.0,
                    entry_price=_round_px(bb_l, digits),
                    sl_price=inv,
                    tp_price=_round_px(bb_l - 2.4 * max(atr, bb_m - bb_l), digits),
                    rr_ratio=2.4,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"BB squeeze (width pctile {bb_wp:.0f}%) pressing lower band ({bb_l:.{digits}f}); watch for breakdown close",
                    invalidation_level=inv,
                    metadata={"squeeze_pctile": round(bb_wp, 1), "bb_pct_b": round(bb_b, 2)},
                )

        return _none_signal(symbol, self.name, regime)


class MeanReversionBBRSIStrategy(BaseMT5Strategy):
    """Strategy 3: Mean Reversion using Bollinger Bands + RSI strictly in RANGE regime."""

    name = "mean_reversion_bb_rsi"
    allowed_regimes = (REGIME_RANGE,)

    def evaluate_at(
        self,
        symbol: str,
        ind: IndicatorArrays,
        idx: int,
        regime_snap: RegimeSnapshot,
        digits: int = 5,
        point: float = 1e-5,
    ) -> StrategySignal:
        regime = regime_snap.regime
        if idx < 60 or regime != REGIME_RANGE:
            return _none_signal(symbol, self.name, regime)

        adx = float(ind.adx_14[idx])
        if adx >= 22.0 or float(ind.atr_pctile[idx]) >= 85.0:
            return _none_signal(symbol, self.name, regime)

        close = float(ind.closes[idx])
        open_px = float(ind.opens[idx])
        high = float(ind.highs[idx])
        low = float(ind.lows[idx])
        bar_range = max(high - low, point)
        atr = max(float(ind.atr_14[idx]), point * 20.0)
        bb_m = float(ind.bb_mid[idx])
        bb_b = float(ind.bb_pct_b[idx])
        prev_bb_b = float(ind.bb_pct_b[idx - 1])
        rsi = float(ind.rsi_14[idx])
        prev_rsi = float(ind.rsi_14[idx - 1])
        pat = _detect_pattern_at(ind, idx, min_range=0.3 * atr)

        # READY BUY: oversold at lower BB + reversal candle
        oversold = (bb_b <= 0.10 or prev_bb_b <= 0.05) and (rsi <= 35.0 or prev_rsi <= 32.0)
        bull_rev = (
            pat in ("BULLISH_HAMMER", "BULLISH_ENGULFING", "MORNING_STAR")
            or (close > open_px and (close - low) / bar_range >= 0.55 and rsi > prev_rsi)
        )
        if oversold and bull_rev:
            sl_dist = max(1.1 * atr, min(1.9 * atr, close - min(low, float(ind.lows[idx - 1])) + 0.5 * atr))
            sl = _round_px(close - sl_dist, digits)
            target_mid = bb_m - close
            tp_dist = max(sl_dist * 1.5, target_mid)
            tp = _round_px(close + tp_dist, digits)
            rr = round(tp_dist / sl_dist, 2)
            score = 66.0 + (8.0 if rsi <= 30.0 else 0.0) + (8.0 if pat != "NONE" else 0.0) + (6.0 if adx < 16.0 else 0.0)
            return StrategySignal(
                symbol=symbol,
                strategy_name=self.name,
                direction="BUY",
                score=round(min(94.0, score), 1),
                entry_price=_round_px(close, digits),
                sl_price=sl,
                tp_price=tp,
                rr_ratio=rr,
                regime=regime,
                setup_stage="READY",
                forming_hint="",
                invalidation_level=sl,
                metadata={"bb_pct_b": round(bb_b, 2), "rsi": round(rsi, 1), "adx": round(adx, 1), "pattern": pat},
            )

        # READY SELL: overbought at upper BB + reversal candle
        overbought = (bb_b >= 0.90 or prev_bb_b >= 0.95) and (rsi >= 65.0 or prev_rsi >= 68.0)
        bear_rev = (
            pat in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING")
            or (close < open_px and (high - close) / bar_range >= 0.55 and rsi < prev_rsi)
        )
        if overbought and bear_rev:
            sl_dist = max(1.1 * atr, min(1.9 * atr, max(high, float(ind.highs[idx - 1])) - close + 0.5 * atr))
            sl = _round_px(close + sl_dist, digits)
            target_mid = close - bb_m
            tp_dist = max(sl_dist * 1.5, target_mid)
            tp = _round_px(close - tp_dist, digits)
            rr = round(tp_dist / sl_dist, 2)
            score = 66.0 + (8.0 if rsi >= 70.0 else 0.0) + (8.0 if pat != "NONE" else 0.0) + (6.0 if adx < 16.0 else 0.0)
            return StrategySignal(
                symbol=symbol,
                strategy_name=self.name,
                direction="SELL",
                score=round(min(94.0, score), 1),
                entry_price=_round_px(close, digits),
                sl_price=sl,
                tp_price=tp,
                rr_ratio=rr,
                regime=regime,
                setup_stage="READY",
                forming_hint="",
                invalidation_level=sl,
                metadata={"bb_pct_b": round(bb_b, 2), "rsi": round(rsi, 1), "adx": round(adx, 1), "pattern": pat},
            )

        # FORMING mean reversion
        if bb_b <= 0.14 and rsi <= 38.0:
            inv = _round_px(low - 1.2 * atr, digits)
            return StrategySignal(
                symbol=symbol,
                strategy_name=self.name,
                direction="BUY",
                score=52.0,
                entry_price=_round_px(close, digits),
                sl_price=inv,
                tp_price=_round_px(bb_m, digits),
                rr_ratio=1.6,
                regime=regime,
                setup_stage="FORMING",
                forming_hint=f"RANGE lower BB test (pctB {bb_b:.2f}, RSI {rsi:.1f}); wait for bullish rejection close",
                invalidation_level=inv,
                metadata={"bb_pct_b": round(bb_b, 2), "rsi": round(rsi, 1)},
            )
        if bb_b >= 0.86 and rsi >= 62.0:
            inv = _round_px(high + 1.2 * atr, digits)
            return StrategySignal(
                symbol=symbol,
                strategy_name=self.name,
                direction="SELL",
                score=52.0,
                entry_price=_round_px(close, digits),
                sl_price=inv,
                tp_price=_round_px(bb_m, digits),
                rr_ratio=1.6,
                regime=regime,
                setup_stage="FORMING",
                forming_hint=f"RANGE upper BB test (pctB {bb_b:.2f}, RSI {rsi:.1f}); wait for bearish rejection close",
                invalidation_level=inv,
                metadata={"bb_pct_b": round(bb_b, 2), "rsi": round(rsi, 1)},
            )

        return _none_signal(symbol, self.name, regime)


class StructureSwingSRRejectionStrategy(BaseMT5Strategy):
    """Strategy 4: Liquidity sweep / rejection at prior 20-bar Swing Support or Resistance."""

    name = "structure_swing_sr_rejection"
    allowed_regimes = (REGIME_TREND_UP, REGIME_TREND_DOWN, REGIME_RANGE)

    def evaluate_at(
        self,
        symbol: str,
        ind: IndicatorArrays,
        idx: int,
        regime_snap: RegimeSnapshot,
        digits: int = 5,
        point: float = 1e-5,
    ) -> StrategySignal:
        regime = regime_snap.regime
        if idx < 30 or regime not in self.allowed_regimes:
            return _none_signal(symbol, self.name, regime)

        close = float(ind.closes[idx])
        open_px = float(ind.opens[idx])
        high = float(ind.highs[idx])
        low = float(ind.lows[idx])
        bar_range = max(high - low, point)
        atr = max(float(ind.atr_14[idx]), point * 20.0)
        adx = float(ind.adx_14[idx])

        prior_low = float(ind.swing_low_20[idx])
        prior_high = float(ind.swing_high_20[idx])
        lower_wick = min(open_px, close) - low
        upper_wick = high - max(open_px, close)
        pat = _detect_pattern_at(ind, idx, min_range=0.35 * atr)

        # Support test & bullish rejection (avoid fighting strong TREND_DOWN)
        if not (regime == REGIME_TREND_DOWN and adx >= 26.0):
            tested_support = low <= prior_low + 0.25 * atr
            reclaimed = close > prior_low
            wick_reject = (lower_wick / bar_range >= 0.40 and close >= low + 0.55 * bar_range) or pat in (
                "BULLISH_HAMMER",
                "BULLISH_ENGULFING",
                "MORNING_STAR",
            )
            if tested_support and reclaimed and wick_reject and bar_range >= 0.45 * atr:
                sl_dist = max(1.2 * atr, min(2.3 * atr, close - low + 0.45 * atr))
                sl = _round_px(close - sl_dist, digits)
                rr = 2.0
                tp = _round_px(close + sl_dist * rr, digits)
                score = 67.0 + (8.0 if low < prior_low else 0.0) + (8.0 if regime == REGIME_TREND_UP else 0.0) + (6.0 if pat != "NONE" else 0.0)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="BUY",
                    score=round(min(96.0, score), 1),
                    entry_price=_round_px(close, digits),
                    sl_price=sl,
                    tp_price=tp,
                    rr_ratio=rr,
                    regime=regime,
                    setup_stage="READY",
                    forming_hint="",
                    invalidation_level=sl,
                    metadata={"support": _round_px(prior_low, digits), "swept": low < prior_low, "pattern": pat},
                )

            if 0.0 <= (close - prior_low) <= 0.45 * atr and close <= open_px:
                inv = _round_px(prior_low - 0.8 * atr, digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="BUY",
                    score=52.0,
                    entry_price=_round_px(prior_low, digits),
                    sl_price=inv,
                    tp_price=_round_px(prior_low + 2.0 * max(atr, prior_low - inv), digits),
                    rr_ratio=2.0,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"Approaching 20-bar support {prior_low:.{digits}f}; watch for sweep + bullish rejection",
                    invalidation_level=inv,
                    metadata={"support": _round_px(prior_low, digits)},
                )

        # Resistance test & bearish rejection (avoid fighting strong TREND_UP)
        if not (regime == REGIME_TREND_UP and adx >= 26.0):
            tested_res = high >= prior_high - 0.25 * atr
            reclaimed_down = close < prior_high
            wick_reject_dn = (upper_wick / bar_range >= 0.40 and close <= high - 0.55 * bar_range) or pat in (
                "BEARISH_SHOOTING_STAR",
                "BEARISH_ENGULFING",
            )
            if tested_res and reclaimed_down and wick_reject_dn and bar_range >= 0.45 * atr:
                sl_dist = max(1.2 * atr, min(2.3 * atr, high - close + 0.45 * atr))
                sl = _round_px(close + sl_dist, digits)
                rr = 2.0
                tp = _round_px(close - sl_dist * rr, digits)
                score = 67.0 + (8.0 if high > prior_high else 0.0) + (8.0 if regime == REGIME_TREND_DOWN else 0.0) + (6.0 if pat != "NONE" else 0.0)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="SELL",
                    score=round(min(96.0, score), 1),
                    entry_price=_round_px(close, digits),
                    sl_price=sl,
                    tp_price=tp,
                    rr_ratio=rr,
                    regime=regime,
                    setup_stage="READY",
                    forming_hint="",
                    invalidation_level=sl,
                    metadata={"resistance": _round_px(prior_high, digits), "swept": high > prior_high, "pattern": pat},
                )

            if 0.0 <= (prior_high - close) <= 0.45 * atr and close >= open_px:
                inv = _round_px(prior_high + 0.8 * atr, digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="SELL",
                    score=52.0,
                    entry_price=_round_px(prior_high, digits),
                    sl_price=inv,
                    tp_price=_round_px(prior_high - 2.0 * max(atr, inv - prior_high), digits),
                    rr_ratio=2.0,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"Approaching 20-bar resistance {prior_high:.{digits}f}; watch for sweep + bearish rejection",
                    invalidation_level=inv,
                    metadata={"resistance": _round_px(prior_high, digits)},
                )

        return _none_signal(symbol, self.name, regime)


class MomentumADXContinuationStrategy(BaseMT5Strategy):
    """Strategy 5: Strong Trend Momentum Continuation using ADX + DI spread + EMA stack + MACD."""

    name = "momentum_adx_continuation"
    allowed_regimes = (REGIME_TREND_UP, REGIME_TREND_DOWN)

    def evaluate_at(
        self,
        symbol: str,
        ind: IndicatorArrays,
        idx: int,
        regime_snap: RegimeSnapshot,
        digits: int = 5,
        point: float = 1e-5,
    ) -> StrategySignal:
        regime = regime_snap.regime
        if idx < 205 or regime not in self.allowed_regimes:
            return _none_signal(symbol, self.name, regime)

        close = float(ind.closes[idx])
        open_px = float(ind.opens[idx])
        high = float(ind.highs[idx])
        low = float(ind.lows[idx])
        atr = max(float(ind.atr_14[idx]), point * 20.0)
        adx = float(ind.adx_14[idx])
        prev_adx = float(ind.adx_14[idx - 1])
        pdi = float(ind.plus_di[idx])
        mdi = float(ind.minus_di[idx])
        e9 = float(ind.ema_9[idx])
        e21 = float(ind.ema_21[idx])
        e50 = float(ind.ema_50[idx])
        e200 = float(ind.ema_200[idx])
        rsi = float(ind.rsi_14[idx])
        macd_h = float(ind.macd_hist[idx])
        prev_macd_h = float(ind.macd_hist[idx - 1])

        if adx < 25.0:
            return _none_signal(symbol, self.name, regime)

        if regime == REGIME_TREND_UP and e9 > e21 > e50 > e200 and pdi > mdi + 4.0:
            dist_e21 = (close - e21) / atr
            # Ready: continuation breakout after brief touch near EMA9/21
            touched_ema = min(low, float(ind.lows[idx - 1])) <= e9 + 0.25 * atr
            if (
                adx >= prev_adx
                and macd_h > 0.0
                and macd_h >= prev_macd_h
                and 52.0 <= rsi <= 72.0
                and 0.0 <= dist_e21 <= 1.8
                and touched_ema
                and close > open_px
                and close > float(ind.highs[idx - 1])
            ):
                sl_dist = max(1.5 * atr, min(2.4 * atr, close - e21 + 0.8 * atr))
                sl = _round_px(close - sl_dist, digits)
                rr = 2.3
                tp = _round_px(close + sl_dist * rr, digits)
                score = 68.0 + (8.0 if adx >= 30.0 else 0.0) + (7.0 if pdi - mdi >= 10.0 else 0.0) + (5.0 if rsi <= 66.0 else 0.0)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="BUY",
                    score=round(min(96.0, score), 1),
                    entry_price=_round_px(close, digits),
                    sl_price=sl,
                    tp_price=tp,
                    rr_ratio=rr,
                    regime=regime,
                    setup_stage="READY",
                    forming_hint="",
                    invalidation_level=sl,
                    metadata={"adx": round(adx, 1), "di_spread": round(pdi - mdi, 1), "rsi": round(rsi, 1)},
                )

            if -0.3 <= dist_e21 <= 0.7 and 48.0 <= rsi <= 65.0:
                inv = _round_px(e50 - 0.5 * atr, digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="BUY",
                    score=55.0,
                    entry_price=_round_px(high, digits),
                    sl_price=inv,
                    tp_price=_round_px(close + 2.3 * max(atr, close - inv), digits),
                    rr_ratio=2.3,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"Strong ADX ({adx:.1f}) uptrend pausing at EMA9/21; watch for break above {high:.{digits}f}",
                    invalidation_level=inv,
                    metadata={"adx": round(adx, 1), "di_spread": round(pdi - mdi, 1)},
                )

        if regime == REGIME_TREND_DOWN and e9 < e21 < e50 < e200 and mdi > pdi + 4.0:
            dist_e21 = (e21 - close) / atr
            touched_ema = max(high, float(ind.highs[idx - 1])) >= e9 - 0.25 * atr
            if (
                adx >= prev_adx
                and macd_h < 0.0
                and macd_h <= prev_macd_h
                and 28.0 <= rsi <= 48.0
                and 0.0 <= dist_e21 <= 1.8
                and touched_ema
                and close < open_px
                and close < float(ind.lows[idx - 1])
            ):
                sl_dist = max(1.5 * atr, min(2.4 * atr, e21 - close + 0.8 * atr))
                sl = _round_px(close + sl_dist, digits)
                rr = 2.3
                tp = _round_px(close - sl_dist * rr, digits)
                score = 68.0 + (8.0 if adx >= 30.0 else 0.0) + (7.0 if mdi - pdi >= 10.0 else 0.0) + (5.0 if rsi >= 34.0 else 0.0)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="SELL",
                    score=round(min(96.0, score), 1),
                    entry_price=_round_px(close, digits),
                    sl_price=sl,
                    tp_price=tp,
                    rr_ratio=rr,
                    regime=regime,
                    setup_stage="READY",
                    forming_hint="",
                    invalidation_level=sl,
                    metadata={"adx": round(adx, 1), "di_spread": round(mdi - pdi, 1), "rsi": round(rsi, 1)},
                )

            if -0.3 <= dist_e21 <= 0.7 and 35.0 <= rsi <= 52.0:
                inv = _round_px(e50 + 0.5 * atr, digits)
                return StrategySignal(
                    symbol=symbol,
                    strategy_name=self.name,
                    direction="SELL",
                    score=55.0,
                    entry_price=_round_px(low, digits),
                    sl_price=inv,
                    tp_price=_round_px(close - 2.3 * max(atr, inv - close), digits),
                    rr_ratio=2.3,
                    regime=regime,
                    setup_stage="FORMING",
                    forming_hint=f"Strong ADX ({adx:.1f}) downtrend pausing at EMA9/21; watch for break below {low:.{digits}f}",
                    invalidation_level=inv,
                    metadata={"adx": round(adx, 1), "di_spread": round(mdi - pdi, 1)},
                )

        return _none_signal(symbol, self.name, regime)


DEFAULT_STRATEGIES: tuple[BaseMT5Strategy, ...] = (
    TrendPullbackEMAStochStrategy(),
    VolatilitySqueezeBreakoutStrategy(),
    MeanReversionBBRSIStrategy(),
    StructureSwingSRRejectionStrategy(),
    MomentumADXContinuationStrategy(),
)


class MT5StrategyEngine:
    """Multi-strategy orchestrator combining MarketRegimeClassifier with all 5 MT5 strategies."""

    def __init__(
        self,
        strategies: Sequence[BaseMT5Strategy] | None = None,
        regime_classifier: MarketRegimeClassifier | None = None,
    ) -> None:
        self.strategies: list[BaseMT5Strategy] = list(strategies) if strategies is not None else list(DEFAULT_STRATEGIES)
        self.regime_classifier = regime_classifier or MarketRegimeClassifier()

    @property
    def strategy_names(self) -> list[str]:
        return [s.name for s in self.strategies]

    def evaluate_at_index(
        self,
        symbol: str,
        ind: IndicatorArrays,
        idx: int = -1,
        digits: int = 5,
        point: float = 1e-5,
    ) -> tuple[RegimeSnapshot, list[StrategySignal]]:
        if idx < 0:
            idx = ind.n + idx
        regime_snap = self.regime_classifier.classify_at(ind, idx)
        signals: list[StrategySignal] = []
        for strat in self.strategies:
            sig = strat.evaluate_at(symbol, ind, idx, regime_snap, digits=digits, point=point)
            if sig.setup_stage != "NONE":
                signals.append(sig)
        signals.sort(key=lambda s: (1 if s.setup_stage == "READY" else 0, s.score), reverse=True)
        return regime_snap, signals

    def evaluate_symbol(
        self,
        symbol: str,
        candles: Sequence[dict[str, Any]],
        digits: int = 5,
        point: float = 1e-5,
    ) -> tuple[RegimeSnapshot, list[StrategySignal]]:
        """Evaluate closed candles for a single symbol and return (RegimeSnapshot, active signals)."""
        ind = compute_indicators(candles)
        return self.evaluate_at_index(symbol, ind, idx=-1, digits=digits, point=point)

    @staticmethod
    def select_best_signal(signals: Sequence[StrategySignal]) -> StrategySignal | None:
        active = [s for s in signals if s.setup_stage in ("READY", "FORMING")]
        if not active:
            return None
        active.sort(key=lambda s: (1 if s.setup_stage == "READY" else 0, s.score), reverse=True)
        return active[0]
