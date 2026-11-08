from __future__ import annotations

import logging
import math
from dataclasses import asdict, dataclass
from typing import Any

from src.binance_client import BinanceSpotClient

logger = logging.getLogger(__name__)

EXCLUDED_BASE_ASSETS = {
    "USDC",
    "FDUSD",
    "TUSD",
    "BUSD",
    "USDP",
    "DAI",
    "USDE",
    "USDS",
    "USD1",
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
    # Indicadores Timeframe Primario (ej. 15m)
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
    # Indicadores Timeframe Superior (ej. 1h)
    htf_rsi_14: float
    htf_ema_21: float
    htf_ema_50: float
    htf_trend: str

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
    """Escanea dinamicamente los pares con mayor liquidez y movimiento en Binance Spot."""

    def __init__(
        self,
        client: BinanceSpotClient,
        quote_asset: str = "USDT",
        min_24h_volume_usdt: float = 15_000_000.0,
        top_limit: int = 8,
        primary_interval: str = "15m",
        htf_interval: str = "1h",
    ) -> None:
        self.client = client
        self.quote_asset = quote_asset.upper()
        self.min_24h_volume_usdt = min_24h_volume_usdt
        self.top_limit = top_limit
        self.primary_interval = primary_interval
        self.htf_interval = htf_interval

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

            # Descartamos pares con pumps extremos (>40% en 24h) o colapsos libres (<-25%) para evitar trampas
            if pct_change > 40.0 or pct_change < -25.0:
                continue

            # Puntaje compuesto: Liquidez (log10 volumen) + Actividad/Momentum moderado
            vol_score = math.log10(max(quote_vol, 1.0)) * 10.0
            momentum_score = min(abs(pct_change), 18.0) * 1.4
            total_score = vol_score + momentum_score
            scored.append((total_score, t))

        scored.sort(key=lambda item: item[0], reverse=True)

        selected: list[dict[str, Any]] = []
        seen: set[str] = set()

        # Primero garantizamos las posiciones abiertas actuales
        for sym in must_include_symbols or []:
            if sym in included_map and sym not in seen:
                selected.append(included_map[sym])
                seen.add(sym)

        # Luego agregamos los mejores candidatos dinamicos hasta alcanzar el limite
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
                candles_primary = self.client.get_klines(symbol, interval=self.primary_interval, limit=100)
                candles_htf = self.client.get_klines(symbol, interval=self.htf_interval, limit=80)
                if len(candles_primary) < 35 or len(candles_htf) < 35:
                    continue

                closes_p = [c["close"] for c in candles_primary]
                vols_p = [c["quote_volume"] for c in candles_primary]
                current_price = closes_p[-1]

                rsi_14 = calc_rsi(closes_p, 14)
                ema9_s = calc_ema_series(closes_p, 9)
                ema21_s = calc_ema_series(closes_p, 21)
                ema50_s = calc_ema_series(closes_p, 50)
                ema_9, ema_21, ema_50 = ema9_s[-1], ema21_s[-1], ema50_s[-1]

                if ema_9 > ema_21 > ema_50:
                    trend_primary = "BULLISH"
                elif ema_9 < ema_21 < ema_50:
                    trend_primary = "BEARISH"
                else:
                    trend_primary = "NEUTRAL"

                macd_line, macd_sig, macd_hist = calc_macd(closes_p)
                bb_upper, bb_lower, bb_pct_b = calc_bollinger_bands(closes_p, 20, 2.0)
                atr_pct = calc_atr_pct(candles_primary, 14)

                # Ratio de volumen de la ultima vela cerrada respecto al promedio de 20 velas
                avg_vol_20 = sum(vols_p[-21:-1]) / 20.0 if len(vols_p) >= 21 else sum(vols_p) / len(vols_p)
                last_closed_vol = vols_p[-2] if len(vols_p) >= 2 else vols_p[-1]
                vol_ratio = round(last_closed_vol / avg_vol_20, 2) if avg_vol_20 > 0 else 1.0

                recent_24 = candles_primary[-24:]
                support_lvl = min(c["low"] for c in recent_24)
                resistance_lvl = max(c["high"] for c in recent_24)

                # Timeframe superior (1h)
                closes_h = [c["close"] for c in candles_htf]
                htf_rsi_14 = calc_rsi(closes_h, 14)
                htf_ema21 = calc_ema_series(closes_h, 21)[-1]
                htf_ema50 = calc_ema_series(closes_h, 50)[-1]
                if closes_h[-1] > htf_ema21 > htf_ema50:
                    htf_trend = "BULLISH"
                elif closes_h[-1] < htf_ema21 < htf_ema50:
                    htf_trend = "BEARISH"
                else:
                    htf_trend = "NEUTRAL"

                snapshots.append(
                    TechnicalSnapshot(
                        symbol=symbol,
                        current_price=current_price,
                        price_change_24h_pct=round(float(ticker.get("priceChangePercent", 0.0)), 2),
                        quote_volume_24h_usdt=round(float(ticker.get("quoteVolume", 0.0)), 0),
                        high_24h=float(ticker.get("highPrice", current_price)),
                        low_24h=float(ticker.get("lowPrice", current_price)),
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
                    )
                )
            except Exception as exc:
                logger.warning("No se pudo construir snapshot tecnico para %s: %s", symbol, exc)

        return snapshots
