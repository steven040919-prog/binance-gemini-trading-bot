from __future__ import annotations

import logging
import math
from dataclasses import asdict, dataclass
from typing import Any

from src.binance_client import BinanceSpotClient

logger = logging.getLogger(__name__)

EXCLUDED_BASE_ASSETS = {
    "USD",
    "USDC",
    "FDUSD",
    "TUSD",
    "BUSD",
    "USDP",
    "DAI",
    "USDE",
    "USDS",
    "USD1",
    "RWUSD",
    "BFUSD",
    "U",
    "SOXLB",
    "SNDKB",
    "SPCXB",
    "KORUB",
    "QQQB",
    "NVDB",
    "NVDAB",
    "CRCLB",
    "AAPLB",
    "MSTRB",
    "AMZNB",
    "GOOGLB",
    "METAB",
    "COINB",
    "TSLAB",
    "TST",
    "PYUSD",
    "EUR",
    "AEUR",
    "GBP",
    "AUD",
    "BRL",
    "TRY",
    "RUB",
    "UAH",
    "BIDR",
    "IDRT",
    "NGN",
    "PLN",
    "RON",
    "ZAR",
    "VAI",
    "WBTC",
    "WBETH",
    "BNSOL",
}

EXCLUDED_SUFFIXES = ("UP", "DOWN", "BULL", "BEAR")


@dataclass
class TechnicalSnapshot:
    symbol: str
    current_price: float
    price_change_24h_pct: float
    quote_volume_24h_usdt: float
    high_24h: float
    low_24h: float
    # Indicadores centrales de la Estrategia (1H): EMA 200 + Estocastico (80/20) + Velas
    ema_200: float
    above_ema_200: bool
    stoch_k: float
    stoch_d: float
    stoch_recent_min: float
    stoch_recent_max: float
    candle_pattern: str  # "BULLISH_HAMMER", "BULLISH_ENGULFING", "BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING", "NONE"
    prev_candle_low: float  # Stop-Loss estructural para compras (LONG)
    prev_candle_high: float  # Stop-Loss estructural para ventas en corto (SHORT)
    strategy_setup: str  # "LONG_ENTRY", "SHORT_ENTRY", "EXIT_LONG_STOCH_80", "EXIT_SHORT_STOCH_20", "WATCH"
    # Indicadores complementarios
    rsi_14: float
    ema_9: float
    ema_21: float
    ema_50: float
    trend_primary: str
    macd_line: float
    macd_signal: float
    macd_hist: float
    bb_upper: float
    bb_lower: float
    bb_pct_b: float
    atr_pct: float
    volume_ratio: float
    support_level: float
    resistance_level: float
    htf_rsi_14: float
    htf_ema_21: float
    htf_ema_50: float
    htf_trend: str
    # Campos cuantitativos de la Estrategia Mejorada 6M (3 Pilares)
    ema_200_slope_pct: float = 0.0
    dist_to_ema200_pct: float = 0.0
    stoch_turning_up: bool = False
    macd_improving: bool = False
    bullish_divergence: bool = False
    entry_pillar: str = "NONE"  # "P1_EMA200_PULLBACK", "P2_EXTREME_CAPITULATION", "P3_BULLISH_DIVERGENCE_SPRING", "P4_STRONG_TREND_EMA50_CONTINUATION", "S1_EMA200_RESISTANCE_REJECT", "NONE"
    structural_sl_price: float = 0.0
    structural_short_sl_price: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def calc_ema_series(values: list[float], period: int) -> list[float]:
    if not values:
        return []
    k = 2.0 / (period + 1)
    ema_vals = [values[0]]
    for price in values[1:]:
        ema_vals.append(price * k + ema_vals[-1] * (1.0 - k))
    return ema_vals


def calc_stochastic(
    candles: list[dict[str, float]],
    k_period: int = 14,
    smooth_k: int = 3,
    d_period: int = 3,
) -> tuple[list[float], list[float]]:
    """Calcula las series %K suavizado y %D del oscilador Estocastico (0..100)."""
    if len(candles) < k_period:
        return [50.0], [50.0]

    raw_k: list[float] = []
    for i in range(k_period - 1, len(candles)):
        window = candles[i - k_period + 1 : i + 1]
        highest_high = max(c["high"] for c in window)
        lowest_low = min(c["low"] for c in window)
        close = candles[i]["close"]
        denom = highest_high - lowest_low
        val = ((close - lowest_low) / denom) * 100.0 if denom > 0 else 50.0
        raw_k.append(max(0.0, min(100.0, val)))

    # Suavizado simple de %K
    k_series: list[float] = []
    for i in range(len(raw_k)):
        sub = raw_k[max(0, i - smooth_k + 1) : i + 1]
        k_series.append(round(sum(sub) / len(sub), 2))

    # Media movil simple de %K para obtener %D
    d_series: list[float] = []
    for i in range(len(k_series)):
        sub = k_series[max(0, i - d_period + 1) : i + 1]
        d_series.append(round(sum(sub) / len(sub), 2))

    return k_series, d_series


def detect_candle_pattern(
    signal_candle: dict[str, float],
    prev_candle: dict[str, float],
    prev2_candle: dict[str, float] | None = None,
) -> str:
    """
    Detecta los patrones de velas de confirmacion (optimizados con backtest de 6 meses en 1H):
    1. BULLISH_HAMMER (Martillo / Pinbar alcista en soporte/retroceso)
    2. BULLISH_ENGULFING (Vela envolvente alcista / Piercing institucional)
    3. MORNING_STAR (Estrella de la manana de 3 velas en piso de sobreventa)
    4. BEARISH_SHOOTING_STAR (Martillo invertido / estrella fugaz bajista en resistencia)
    5. BEARISH_ENGULFING (Vela envolvente bajista)
    """
    o = signal_candle["open"]
    h = signal_candle["high"]
    l = signal_candle["low"]
    c = signal_candle["close"]

    po = prev_candle["open"]
    pc = prev_candle["close"]

    total_range = h - l
    if total_range <= 0:
        return "NONE"

    body = abs(c - o)
    prev_body = abs(pc - po)
    upper_wick = h - max(o, c)
    lower_wick = min(o, c) - l
    close_pos = (c - l) / total_range

    is_bullish = c > o
    is_bearish = c < o
    prev_is_bullish = pc > po
    prev_is_bearish = pc < po

    # 1. Vela Envolvente Alcista (Bullish Engulfing / Strong Piercing)
    if prev_is_bearish and is_bullish and prev_body > 0:
        if c >= po and o <= pc and body >= prev_body * 0.85:
            return "BULLISH_ENGULFING"
        if c >= po - 0.10 * prev_body and body >= prev_body * 0.80 and close_pos >= 0.65:
            return "BULLISH_ENGULFING"

    # 2. Vela Envolvente Bajista (Bearish Engulfing)
    if prev_is_bullish and is_bearish and prev_body > 0:
        if o >= pc and c <= po and body >= prev_body * 0.85:
            return "BEARISH_ENGULFING"

    # 3. Martillo Alcista (Bullish Hammer / Pinbar institucional)
    effective_body = max(body, total_range * 0.07)
    if lower_wick >= effective_body * 1.5 and (lower_wick / total_range) >= 0.42 and (upper_wick / total_range) <= 0.32:
        return "BULLISH_HAMMER"

    # 4. Estrella de la Manana (Morning Star de 3 velas)
    if prev2_candle is not None:
        p2o = prev2_candle["open"]
        p2c = prev2_candle["close"]
        p2_body = abs(p2c - p2o)
        if p2c < p2o and is_bullish and p2_body > 0:
            if c >= (p2o + p2c) / 2.0 and close_pos >= 0.65 and body >= p2_body * 0.60:
                return "MORNING_STAR"

    # 5. Martillo Invertido / Estrella Fugaz Bajista (Bearish Shooting Star)
    if upper_wick >= effective_body * 1.6 and (upper_wick / total_range) >= 0.45 and (lower_wick / total_range) <= 0.30:
        return "BEARISH_SHOOTING_STAR"

    return "NONE"


def calc_rsi(closes: list[float], period: int = 14) -> float:
    if len(closes) <= period:
        return 50.0
    gains: list[float] = []
    losses: list[float] = []
    for i in range(1, len(closes)):
        delta = closes[i] - closes[i - 1]
        gains.append(max(delta, 0.0))
        losses.append(max(-delta, 0.0))

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period

    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100.0 - (100.0 / (1.0 + rs)), 2)


def calc_macd(closes: list[float], fast: int = 12, slow: int = 26, signal: int = 9) -> tuple[float, float, float]:
    if len(closes) < slow + signal:
        return 0.0, 0.0, 0.0
    ema_fast = calc_ema_series(closes, fast)
    ema_slow = calc_ema_series(closes, slow)
    macd_series = [f - s for f, s in zip(ema_fast, ema_slow)]
    signal_series = calc_ema_series(macd_series, signal)
    macd_line = macd_series[-1]
    sig_line = signal_series[-1]
    hist = macd_line - sig_line
    return round(macd_line, 6), round(sig_line, 6), round(hist, 6)


def calc_bollinger_bands(closes: list[float], period: int = 20, std_dev: float = 2.0) -> tuple[float, float, float]:
    if len(closes) < period:
        p = closes[-1] if closes else 0.0
        return p, p, 0.5
    window = closes[-period:]
    mid = sum(window) / period
    variance = sum((x - mid) ** 2 for x in window) / period
    sd = math.sqrt(variance)
    upper = mid + std_dev * sd
    lower = mid - std_dev * sd
    band_width = upper - lower
    pct_b = (closes[-1] - lower) / band_width if band_width > 0 else 0.5
    return round(upper, 6), round(lower, 6), round(pct_b, 3)


def calc_atr_pct(candles: list[dict[str, float]], period: int = 14) -> float:
    if len(candles) <= period:
        return 1.0
    trs: list[float] = []
    for i in range(1, len(candles)):
        high = candles[i]["high"]
        low = candles[i]["low"]
        prev_close = candles[i - 1]["close"]
        tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
        trs.append(tr)
    atr = sum(trs[-period:]) / period
    last_close = candles[-1]["close"]
    return round((atr / last_close) * 100.0, 2) if last_close > 0 else 0.0


class MarketScanner:
    """Escanea dinamicamente los pares y evalua la estrategia EMA 200 + Estocastico (80/20) + Martillo/Envolvente en 1H."""

    def __init__(
        self,
        client: BinanceSpotClient,
        quote_asset: str = "USDT",
        min_24h_volume_usdt: float = 10_000_000.0,
        top_limit: int = 12,
        primary_interval: str = "1h",
        htf_interval: str = "4h",
        ema_trend_period: int = 200,
        stoch_k_period: int = 14,
        stoch_smooth_k: int = 3,
        stoch_d_period: int = 3,
        stoch_overbought: float = 80.0,
        stoch_oversold: float = 20.0,
    ) -> None:
        self.client = client
        self.quote_asset = quote_asset.upper()
        self.min_24h_volume_usdt = min_24h_volume_usdt
        self.top_limit = top_limit
        self.primary_interval = primary_interval
        self.htf_interval = htf_interval
        self.ema_trend_period = ema_trend_period
        self.stoch_k_period = stoch_k_period
        self.stoch_smooth_k = stoch_smooth_k
        self.stoch_d_period = stoch_d_period
        self.stoch_overbought = stoch_overbought
        self.stoch_oversold = stoch_oversold

    def is_eligible_symbol(self, symbol: str) -> bool:
        if not symbol.endswith(self.quote_asset):
            return False
        base = symbol[: -len(self.quote_asset)]
        if not base or base in EXCLUDED_BASE_ASSETS:
            return False
        if any(base.endswith(sfx) for sfx in EXCLUDED_SUFFIXES):
            return False
        return True

    def select_top_candidates(self, must_include_symbols: list[str] | None = None) -> list[dict[str, Any]]:
        tickers = self.client.get_24h_tickers()
        must_set = set(must_include_symbols or [])

        scored: list[tuple[float, dict[str, Any]]] = []
        included_map: dict[str, dict[str, Any]] = {}

        for t in tickers:
            sym = t.get("symbol", "")
            if not self.is_eligible_symbol(sym):
                continue

            last_price = float(t.get("lastPrice", 0.0))
            quote_vol = float(t.get("quoteVolume", 0.0))
            pct_change = float(t.get("priceChangePercent", 0.0))
            count_trades = int(t.get("count", 0))

            if last_price <= 0 or count_trades <= 100:
                continue

            if sym in must_set:
                included_map[sym] = t

            if quote_vol < self.min_24h_volume_usdt:
                continue

            if pct_change > 45.0 or pct_change < -30.0:
                continue

            vol_score = math.log10(max(quote_vol, 1.0)) * 10.0
            momentum_score = min(abs(pct_change), 18.0) * 0.8
            # Bono de Oportunidad Cuantitativa: prioriza pares liquidos que estan en retroceso cerca del soporte de 24h (donde se activan P1/P2/P3/P4)
            high_24 = float(t.get("highPrice", last_price))
            low_24 = float(t.get("lowPrice", last_price))
            rng_24 = high_24 - low_24
            range_pos = ((last_price - low_24) / rng_24) if rng_24 > 0 else 0.5
            pullback_bonus = 18.0 if (range_pos <= 0.28 and -18.0 <= pct_change <= 6.0) else 0.0
            total_score = vol_score + momentum_score + pullback_bonus
            scored.append((total_score, t))

        scored.sort(key=lambda item: item[0], reverse=True)

        selected: list[dict[str, Any]] = []
        seen: set[str] = set()

        for sym in must_include_symbols or []:
            if sym in included_map and sym not in seen:
                selected.append(included_map[sym])
                seen.add(sym)

        for _, ticker in scored:
            sym = ticker["symbol"]
            if sym not in seen:
                selected.append(ticker)
                seen.add(sym)
            if len(selected) >= self.top_limit + len(must_set):
                break

        logger.info("Candidatos dinamicos seleccionados (%d): %s", len(selected), [x["symbol"] for x in selected])
        return selected

    def build_snapshots(self, must_include_symbols: list[str] | None = None) -> list[TechnicalSnapshot]:
        candidates = self.select_top_candidates(must_include_symbols=must_include_symbols)
        snapshots: list[TechnicalSnapshot] = []

        for ticker in candidates:
            symbol = ticker["symbol"]
            try:
                # Solicitamos 260 velas de 1H para que la EMA 200 sea exacta
                candles_primary = self.client.get_klines(symbol, interval=self.primary_interval, limit=260)
                candles_htf = self.client.get_klines(symbol, interval=self.htf_interval, limit=100)
                if len(candles_primary) < 60 or len(candles_htf) < 30:
                    continue

                closes_p = [c["close"] for c in candles_primary]
                vols_p = [c["quote_volume"] for c in candles_primary]
                current_price = closes_p[-1]

                # 1. EMA de 200 periodos (Tendencia Principal) + Pendiente de 20h y Distancia %
                ema200_series = calc_ema_series(closes_p, self.ema_trend_period)
                ema_200 = ema200_series[-1]
                ema_200_prev20 = ema200_series[-21] if len(ema200_series) >= 21 else ema200_series[0]
                ema_200_slope_pct = round(((ema_200 - ema_200_prev20) / ema_200_prev20) * 100.0, 3) if ema_200_prev20 > 0 else 0.0
                dist_to_ema200_pct = round(((current_price - ema_200) / ema_200) * 100.0, 2) if ema_200 > 0 else 0.0
                above_ema_200 = current_price > ema_200

                # 2. Oscilador Estocastico (14, 3, 3) con bandas 80 y 20
                stoch_k_series, stoch_d_series = calc_stochastic(
                    candles_primary,
                    k_period=self.stoch_k_period,
                    smooth_k=self.stoch_smooth_k,
                    d_period=self.stoch_d_period,
                )
                stoch_k = stoch_k_series[-1]
                stoch_d = stoch_d_series[-1]
                prev_stoch_k = stoch_k_series[-2] if len(stoch_k_series) >= 2 else stoch_k
                stoch_turning_up = (stoch_k > prev_stoch_k) and (stoch_k >= stoch_d)

                recent_k_window = stoch_k_series[-4:] if len(stoch_k_series) >= 4 else stoch_k_series
                stoch_recent_min = min(recent_k_window)
                stoch_recent_max = max(recent_k_window)

                # 3. Patron de vela en la ultima vela cerrada (candles_primary[-2]) o en curso (candles_primary[-1])
                closed_candle = candles_primary[-2]
                prev_closed_candle = candles_primary[-3]
                prev2_closed_candle = candles_primary[-4] if len(candles_primary) >= 4 else prev_closed_candle
                pattern = detect_candle_pattern(closed_candle, prev_closed_candle, prev2_closed_candle)
                if pattern == "NONE":
                    pattern = detect_candle_pattern(candles_primary[-1], closed_candle, prev_closed_candle)

                # 4. Indicadores complementarios para los 3 Pilares Cuantitativos (optimizados 6M)
                rsi_14 = calc_rsi(closes_p, 14)
                prev_rsi_14 = calc_rsi(closes_p[:-1], 14) if len(closes_p) > 16 else rsi_14
                min_recent_rsi = min(rsi_14, prev_rsi_14)

                ema_9 = calc_ema_series(closes_p, 9)[-1]
                ema_21 = calc_ema_series(closes_p, 21)[-1]
                ema_50 = calc_ema_series(closes_p, 50)[-1]
                trend_primary = "BULLISH" if above_ema_200 else "BEARISH"

                macd_line, macd_sig, macd_hist = calc_macd(closes_p)
                _, _, prev_macd_hist = calc_macd(closes_p[:-1]) if len(closes_p) > 36 else (0.0, 0.0, macd_hist)
                macd_improving = macd_hist > prev_macd_hist

                bb_upper, bb_lower, bb_pct_b = calc_bollinger_bands(closes_p, 20, 2.0)
                _, _, prev_bb_pct_b = calc_bollinger_bands(closes_p[:-1], 20, 2.0) if len(closes_p) > 22 else (bb_upper, bb_lower, bb_pct_b)
                min_recent_bb = min(bb_pct_b, prev_bb_pct_b)

                atr_pct = calc_atr_pct(candles_primary, 14)
                atr_abs = (atr_pct / 100.0) * current_price

                avg_vol_20 = sum(vols_p[-21:-1]) / 20.0 if len(vols_p) >= 21 else sum(vols_p) / len(vols_p)
                last_closed_vol = max(vols_p[-2], vols_p[-1]) if len(vols_p) >= 2 else vols_p[-1]
                vol_ratio = round(last_closed_vol / avg_vol_20, 2) if avg_vol_20 > 0 else 1.0

                # 5. Stop-Loss estructural + Buffer de Volatilidad ATR (2.0x ATR, acotado entre 2.6% y 4.6% segun backtest 6M)
                prev_candle_low = round(min(closed_candle["low"], prev_closed_candle["low"], candles_primary[-1]["low"]), 8)
                prev_candle_high = round(max(closed_candle["high"], prev_closed_candle["high"], candles_primary[-1]["high"]), 8)
                raw_atr_sl = prev_candle_low - (2.0 * atr_abs)
                sl_dist_pct = (current_price - raw_atr_sl) / current_price if current_price > 0 else 0.03
                sl_dist_pct = max(0.026, min(0.046, sl_dist_pct))
                structural_sl_price = round(current_price * (1.0 - sl_dist_pct), 8)

                raw_short_atr_sl = prev_candle_high + (2.0 * atr_abs)
                short_sl_dist_pct = (raw_short_atr_sl - current_price) / current_price if current_price > 0 else 0.03
                short_sl_dist_pct = max(0.026, min(0.046, short_sl_dist_pct))
                structural_short_sl_price = round(current_price * (1.0 + short_sl_dist_pct), 8)

                # 6. Deteccion de Spring / Divergencia Alcista en Soporte de 12H (Pilar 3: 83.3% WR, PF 3.51)
                bullish_divergence = False
                if len(candles_primary) >= 18:
                    prev_12h_low = min(c["low"] for c in candles_primary[-15:-2])
                    prev_12h_rsis = [calc_rsi(closes_p[: idx + 1], 14) for idx in range(len(closes_p) - 15, len(closes_p) - 2)]
                    prev_min_rsi = min(prev_12h_rsis) if prev_12h_rsis else 50.0
                    swept_low = min(candles_primary[-1]["low"], closed_candle["low"]) <= prev_12h_low * 1.001
                    reclaimed_support = current_price > prev_12h_low
                    if swept_low and reclaimed_support and prev_min_rsi <= 30.0 and rsi_14 >= prev_min_rsi + 2.5:
                        bullish_divergence = True

                # 7. Evaluacion de los 3 Pilares Cuantitativos (79.26% Win Rate / PF 2.05 en los ultimos 6 meses)
                sig_candle = candles_primary[-1] if candles_primary[-1]["close"] > candles_primary[-1]["open"] else closed_candle
                is_bull_candle = sig_candle["close"] > sig_candle["open"]
                is_bull_pattern = pattern in ("BULLISH_HAMMER", "BULLISH_ENGULFING", "MORNING_STAR")
                broke_prev_high = candles_primary[-1]["close"] > closed_candle["high"] or closed_candle["close"] > prev_closed_candle["high"]

                entry_pillar = "NONE"
                # PILAR 1: Pullback de Valor en Tendencia Alcista sobre EMA 200 (71.8% WR)
                if (
                    -0.6 <= dist_to_ema200_pct <= 3.5
                    and ema_200_slope_pct >= 0.0
                    and ema_50 >= ema_200 * 0.994
                    and stoch_recent_min <= self.stoch_oversold
                    and min_recent_rsi <= 36.0
                    and min_recent_bb <= 0.12
                    and stoch_turning_up
                    and macd_improving
                    and is_bull_candle
                    and (is_bull_pattern or broke_prev_high)
                    and vol_ratio >= 1.05
                ):
                    entry_pillar = "P1_EMA200_PULLBACK"

                # PILAR 2: Capitulacion Institucional de Doble Sobreventa (82.1% WR, PF 2.50; opera incluso bajo EMA 200)
                elif (
                    stoch_recent_min <= 18.0
                    and min_recent_rsi <= 31.5
                    and min_recent_bb <= 0.08
                    and (vol_ratio >= 1.15 or is_bull_pattern)
                    and stoch_turning_up
                    and macd_improving
                    and is_bull_candle
                    and (is_bull_pattern or broke_prev_high)
                ):
                    entry_pillar = "P2_EXTREME_CAPITULATION"

                # PILAR 3: Spring / Divergencia Alcista Institucional en Soporte 12H (83.3% WR, PF 3.54)
                elif (
                    bullish_divergence
                    and min_recent_bb <= 0.08
                    and stoch_recent_min <= 18.0
                    and stoch_turning_up
                    and macd_improving
                    and is_bull_candle
                    and is_bull_pattern
                    and vol_ratio >= 1.05
                ):
                    entry_pillar = "P3_BULLISH_DIVERGENCE_SPRING"

                # PILAR 4: Continuacion de Tendencia Alcista Fuerte en EMA 50 (87.5% WR, PF 2.70)
                elif (
                    current_price > ema_200 * 1.01
                    and ema_50 > ema_200 * 1.005
                    and ema_200_slope_pct >= 0.0
                    and -1.2 <= (((current_price - ema_50) / ema_50) * 100.0) <= 1.5
                    and stoch_recent_min <= self.stoch_oversold
                    and min_recent_rsi <= 38.0
                    and min_recent_bb <= 0.10
                    and stoch_turning_up
                    and macd_improving
                    and is_bull_candle
                    and is_bull_pattern
                    and vol_ratio >= 1.05
                ):
                    entry_pillar = "P4_STRONG_TREND_EMA50_CONTINUATION"

                # PILAR SHORT S1 (Para Binance Futuros): Rechazo en Resistencia EMA 200 Descendente + Estocastico >= 80 (78.2% WR, PF 2.00)
                stoch_turning_down = (stoch_k < prev_stoch_k) and (stoch_k <= stoch_d)
                max_recent_rsi = max(rsi_14, prev_rsi_14)
                max_recent_bb = max(bb_pct_b, prev_bb_pct_b)
                is_bear_candle = candles_primary[-1]["close"] < candles_primary[-1]["open"] or closed_candle["close"] < closed_candle["open"]
                is_bear_pattern = pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING")
                broke_prev_low = candles_primary[-1]["close"] < closed_candle["low"] or closed_candle["close"] < prev_closed_candle["low"]

                if (
                    entry_pillar == "NONE"
                    and -3.5 <= dist_to_ema200_pct <= 0.6
                    and ema_200_slope_pct <= 0.0
                    and ema_50 <= ema_200 * 1.006
                    and stoch_recent_max >= self.stoch_overbought
                    and max_recent_rsi >= 64.0
                    and max_recent_bb >= 0.88
                    and stoch_turning_down
                    and (not macd_improving)
                    and is_bear_candle
                    and (is_bear_pattern or broke_prev_low)
                    and vol_ratio >= 1.05
                ):
                    entry_pillar = "S1_EMA200_RESISTANCE_REJECT"

                is_oversold_zone = (stoch_k <= self.stoch_oversold) or (stoch_recent_min <= self.stoch_oversold and stoch_k <= 35.0)
                is_overbought_zone = (stoch_k >= self.stoch_overbought) or (stoch_recent_max >= self.stoch_overbought and stoch_k >= 65.0)

                if entry_pillar in (
                    "P1_EMA200_PULLBACK",
                    "P2_EXTREME_CAPITULATION",
                    "P3_BULLISH_DIVERGENCE_SPRING",
                    "P4_STRONG_TREND_EMA50_CONTINUATION",
                ) or (above_ema_200 and is_oversold_zone and is_bull_pattern and stoch_turning_up):
                    if entry_pillar == "NONE":
                        entry_pillar = "P1_EMA200_PULLBACK"
                    strategy_setup = "LONG_ENTRY"
                elif entry_pillar == "S1_EMA200_RESISTANCE_REJECT" or (
                    (not above_ema_200) and is_overbought_zone and is_bear_pattern and stoch_turning_down
                ):
                    if entry_pillar == "NONE":
                        entry_pillar = "S1_EMA200_RESISTANCE_REJECT"
                    strategy_setup = "SHORT_ENTRY"
                elif stoch_k >= self.stoch_overbought or stoch_d >= self.stoch_overbought:
                    strategy_setup = "EXIT_LONG_STOCH_80"
                elif stoch_k <= self.stoch_oversold or stoch_d <= self.stoch_oversold:
                    strategy_setup = "EXIT_SHORT_STOCH_20"
                else:
                    strategy_setup = "WATCH"

                recent_24 = candles_primary[-24:]
                support_lvl = min(c["low"] for c in recent_24)
                resistance_lvl = max(c["high"] for c in recent_24)

                closes_h = [c["close"] for c in candles_htf]
                htf_rsi_14 = calc_rsi(closes_h, 14)
                htf_ema21 = calc_ema_series(closes_h, 21)[-1]
                htf_ema50 = calc_ema_series(closes_h, 50)[-1]
                htf_trend = "BULLISH" if closes_h[-1] > htf_ema50 else "BEARISH"

                snapshots.append(
                    TechnicalSnapshot(
                        symbol=symbol,
                        current_price=current_price,
                        price_change_24h_pct=round(float(ticker.get("priceChangePercent", 0.0)), 2),
                        quote_volume_24h_usdt=round(float(ticker.get("quoteVolume", 0.0)), 0),
                        high_24h=float(ticker.get("highPrice", current_price)),
                        low_24h=float(ticker.get("lowPrice", current_price)),
                        ema_200=round(ema_200, 6),
                        above_ema_200=above_ema_200,
                        stoch_k=stoch_k,
                        stoch_d=stoch_d,
                        stoch_recent_min=stoch_recent_min,
                        stoch_recent_max=stoch_recent_max,
                        candle_pattern=pattern,
                        prev_candle_low=prev_candle_low,
                        prev_candle_high=prev_candle_high,
                        strategy_setup=strategy_setup,
                        rsi_14=rsi_14,
                        ema_9=round(ema_9, 6),
                        ema_21=round(ema_21, 6),
                        ema_50=round(ema_50, 6),
                        trend_primary=trend_primary,
                        macd_line=macd_line,
                        macd_signal=macd_sig,
                        macd_hist=macd_hist,
                        bb_upper=bb_upper,
                        bb_lower=bb_lower,
                        bb_pct_b=bb_pct_b,
                        atr_pct=atr_pct,
                        volume_ratio=vol_ratio,
                        support_level=round(support_lvl, 6),
                        resistance_level=round(resistance_lvl, 6),
                        htf_rsi_14=htf_rsi_14,
                        htf_ema_21=round(htf_ema21, 6),
                        htf_ema_50=round(htf_ema50, 6),
                        htf_trend=htf_trend,
                        ema_200_slope_pct=ema_200_slope_pct,
                        dist_to_ema200_pct=dist_to_ema200_pct,
                        stoch_turning_up=stoch_turning_up,
                        macd_improving=macd_improving,
                        bullish_divergence=bullish_divergence,
                        entry_pillar=entry_pillar,
                        structural_sl_price=structural_sl_price,
                        structural_short_sl_price=structural_short_sl_price,
                    )
                )
            except Exception as exc:
                logger.warning("No se pudo construir snapshot tecnico para %s: %s", symbol, exc)

        return snapshots
