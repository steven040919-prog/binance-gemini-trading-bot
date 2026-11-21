from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Sequence

import numpy as np

from src.mt5_strategies import (
    ALL_REGIMES,
    CRYPTO_SYMBOLS,
    MT5StrategyEngine,
    SESSION_ROLLOVER,
    StrategySignal,
    classify_session,
    compute_indicators,
    get_asset_class,
)

# Default universe & spread limits mirrored from src/mt5_bot.py (kept self-contained if MT5 is offline)
DEFAULT_MT5_SYMBOLS: list[str] = [
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
    "XAUUSDm",
]

MAX_ALLOWED_SPREAD_POINTS: dict[str, int] = {
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
    "XAUUSDm": 450,
}

DEFAULT_SYMBOL_SPECS: dict[str, tuple[int, float, float]] = {
    # symbol: (digits, point, typical_base_price)
    "EURUSDm": (5, 1e-5, 1.08500),
    "GBPUSDm": (5, 1e-5, 1.27000),
    "USDJPYm": (3, 1e-3, 152.000),
    "AUDUSDm": (5, 1e-5, 0.65500),
    "NZDUSDm": (5, 1e-5, 0.60500),
    "USDCADm": (5, 1e-5, 1.37500),
    "USDCHFm": (5, 1e-5, 0.88500),
    "EURGBPm": (5, 1e-5, 0.85200),
    "EURJPYm": (3, 1e-3, 165.000),
    "US500m": (2, 0.01, 5600.00),
    "USTECm": (2, 0.01, 19500.00),
    "BTCUSDm": (2, 0.01, 75000.00),
    "ETHUSDm": (2, 0.01, 3000.00),
    "XAUUSDm": (3, 0.001, 2450.000),
}

TIMEFRAME_MINUTES: dict[str, int] = {
    "M15": 15,
    "M30": 30,
    "H1": 60,
    "H4": 240,
}


@dataclass
class SimulatedTrade:
    symbol: str
    strategy_name: str
    direction: str  # BUY | SELL
    regime: str
    session: str
    split: str  # IS | OOS
    entry_time: float
    exit_time: float
    entry_price: float
    exit_price: float
    sl_price: float
    tp_price: float
    rr_planned: float
    r_multiple: float
    outcome: str  # TP | SL | TIME_EXIT
    score: float
    bars_held: int
    spread_cost_r: float


@dataclass
class PerformanceMetrics:
    trades_count: int = 0
    wins: int = 0
    losses: int = 0
    win_rate: float = 0.0
    profit_factor: float = 0.0
    expectancy_r: float = 0.0
    total_r: float = 0.0
    avg_rr: float = 0.0
    max_dd_pct: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def compute_performance_metrics(
    trades: Sequence[SimulatedTrade],
    risk_pct_per_trade: float = 1.0,
) -> PerformanceMetrics:
    if not trades:
        return PerformanceMetrics()
    ordered = sorted(trades, key=lambda t: t.exit_time)
    n = len(ordered)
    wins = sum(1 for t in ordered if t.r_multiple > 0.0)
    losses = sum(1 for t in ordered if t.r_multiple <= 0.0)
    gross_win = sum(t.r_multiple for t in ordered if t.r_multiple > 0.0)
    gross_loss = abs(sum(t.r_multiple for t in ordered if t.r_multiple < 0.0))
    total_r = sum(t.r_multiple for t in ordered)
    win_rate = (wins / n) * 100.0 if n > 0 else 0.0
    pf = (gross_win / gross_loss) if gross_loss > 1e-9 else (9.99 if gross_win > 0.0 else 0.0)
    exp_r = total_r / n if n > 0 else 0.0
    avg_rr = sum(t.rr_planned for t in ordered) / n if n > 0 else 0.0

    # Equity curve drawdown assuming risk_pct_per_trade per 1R
    equity = 100.0
    peak = 100.0
    max_dd = 0.0
    for t in ordered:
        equity *= max(0.01, 1.0 + (t.r_multiple * risk_pct_per_trade / 100.0))
        if equity > peak:
            peak = equity
        dd = ((peak - equity) / peak) * 100.0 if peak > 0 else 0.0
        if dd > max_dd:
            max_dd = dd

    return PerformanceMetrics(
        trades_count=n,
        wins=wins,
        losses=losses,
        win_rate=round(win_rate, 2),
        profit_factor=round(min(pf, 99.99), 3),
        expectancy_r=round(exp_r, 4),
        total_r=round(total_r, 2),
        avg_rr=round(avg_rr, 2),
        max_dd_pct=round(max_dd, 2),
    )


def _mt5_timeframe_const(mt5_mod: Any, timeframe_str: str) -> int:
    mapping = {
        "M15": mt5_mod.TIMEFRAME_M15,
        "M30": mt5_mod.TIMEFRAME_M30,
        "H1": mt5_mod.TIMEFRAME_H1,
        "H4": mt5_mod.TIMEFRAME_H4,
    }
    tf = timeframe_str.upper()
    if tf not in mapping:
        raise ValueError(f"Unsupported timeframe: {timeframe_str}")
    return mapping[tf]


def check_mt5_connection() -> dict[str, Any]:
    """Check whether MetaTrader5 terminal is reachable and connected right now."""
    try:
        import MetaTrader5 as mt5
    except Exception as exc:
        return {"available": False, "connected": False, "reason": f"ImportError: {exc}"}

    try:
        ok = mt5.initialize()
        if not ok:
            ok = mt5.initialize(path=r"C:\Program Files\MetaTrader 5\terminal64.exe")
        if not ok:
            return {"available": True, "connected": False, "reason": f"initialize failed: {mt5.last_error()}"}
        term = mt5.terminal_info()
        acc = mt5.account_info()
        connected = bool(term is not None and acc is not None and getattr(term, "connected", False))
        info = {
            "available": True,
            "connected": connected,
            "account_login": getattr(acc, "login", None) if acc else None,
            "server": getattr(acc, "server", None) if acc else None,
            "reason": "OK" if connected else "Terminal initialized but not connected/logged in",
        }
        return info
    except Exception as exc:
        return {"available": True, "connected": False, "reason": str(exc)}


def generate_synthetic_regime_bars(
    symbol: str,
    timeframe_str: str = "H1",
    years: float = 2.0,
    seed: int = 42,
) -> tuple[list[dict[str, float]], dict[str, Any]]:
    """
    Reproducible offline multi-regime OHLCV generator (alternating TREND_UP, TREND_DOWN, RANGE, HIGH_VOL_CHOP)
    used when MT5 terminal is unavailable or --offline-synthetic is specified.
    """
    tf_min = TIMEFRAME_MINUTES.get(timeframe_str.upper(), 60)
    digits, point, base_px = DEFAULT_SYMBOL_SPECS.get(symbol, (5, 1e-5, 1.0))
    is_crypto = symbol in CRYPTO_SYMBOLS
    bars_per_day = int((24 * 60) / tf_min) if is_crypto else int((24 * 60) / tf_min * 5 / 7)
    n_bars = max(600, int(years * 365 * bars_per_day))

    # Deterministic per-symbol seed
    sym_seed = seed + sum(ord(c) * (idx + 1) for idx, c in enumerate(symbol))
    rng = np.random.default_rng(sym_seed)

    asset_class = get_asset_class(symbol)
    base_vol_map = {"FOREX": 0.0012, "METALS": 0.0022, "INDICES": 0.0020, "CRYPTO": 0.0045}
    base_vol = base_vol_map.get(asset_class, 0.0015) * math.sqrt(tf_min / 60.0)

    end_dt = datetime(2026, 1, 1, 0, 0, tzinfo=timezone.utc)
    start_dt = end_dt - timedelta(days=int(years * 365))
    cur_ts = start_dt.timestamp()
    step_sec = tf_min * 60

    candles: list[dict[str, float]] = []
    price = base_px
    anchor = base_px
    regime_cycle = ["TREND_UP", "RANGE", "TREND_DOWN", "HIGH_VOL_CHOP", "TREND_UP", "RANGE"]
    regime_idx = 0
    bars_in_regime = 0
    regime_len = int(rng.integers(140, 320))

    for i in range(n_bars):
        if bars_in_regime >= regime_len:
            regime_idx = (regime_idx + 1) % len(regime_cycle)
            bars_in_regime = 0
            regime_len = int(rng.integers(140, 320))
            anchor = price
        reg = regime_cycle[regime_idx]
        bars_in_regime += 1

        if reg == "TREND_UP":
            drift = base_vol * 0.14
            vol = base_vol * 0.95
            ret = drift + rng.normal(0.0, vol)
        elif reg == "TREND_DOWN":
            drift = -base_vol * 0.14
            vol = base_vol * 0.95
            ret = drift + rng.normal(0.0, vol)
        elif reg == "RANGE":
            pull = (anchor - price) / max(anchor, 1e-6) * 0.08
            vol = base_vol * 0.65
            ret = pull + rng.normal(0.0, vol)
        else:  # HIGH_VOL_CHOP
            vol = base_vol * 2.1
            ret = rng.normal(0.0, vol)

        o = price
        c = max(point * 100.0, o * (1.0 + ret))
        wick_up = abs(rng.normal(0.0, vol * 0.55)) * max(o, c)
        wick_dn = abs(rng.normal(0.0, vol * 0.55)) * max(o, c)
        h = max(o, c) + wick_up
        l = max(point * 10.0, min(o, c) - wick_dn)

        candles.append(
            {
                "time": float(cur_ts),
                "open": round(o, digits),
                "high": round(h, digits),
                "low": round(l, digits),
                "close": round(c, digits),
                "volume": float(int(rng.integers(150, 2500))),
            }
        )
        price = c
        cur_ts += step_sec
        if not is_crypto:
            dt = datetime.fromtimestamp(cur_ts, tz=timezone.utc)
            if dt.weekday() == 5:  # skip Saturday/Sunday
                cur_ts += 48 * 3600

    meta = {
        "symbol": symbol,
        "timeframe": timeframe_str.upper(),
        "digits": digits,
        "point": point,
        "spread_points": int(round(MAX_ALLOWED_SPREAD_POINTS.get(symbol, 20) * 0.6)),
        "data_source": "SYNTHETIC_BENCHMARK",
        "bars_count": len(candles),
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    return candles, meta


def _save_cache(csv_path: Path, meta_path: Path, candles: Sequence[dict[str, float]], meta: dict[str, Any]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "open", "high", "low", "close", "volume"])
        for c in candles:
            writer.writerow([int(c["time"]), c["open"], c["high"], c["low"], c["close"], c["volume"]])
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def _load_cache(csv_path: Path, meta_path: Path) -> tuple[list[dict[str, float]], dict[str, Any]] | None:
    if not csv_path.exists() or not meta_path.exists():
        return None
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        candles: list[dict[str, float]] = []
        with csv_path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                candles.append(
                    {
                        "time": float(row["time"]),
                        "open": float(row["open"]),
                        "high": float(row["high"]),
                        "low": float(row["low"]),
                        "close": float(row["close"]),
                        "volume": float(row["volume"]),
                    }
                )
        if len(candles) >= 300:
            return candles, meta
    except Exception:
        return None
    return None


def fetch_mt5_history(
    symbol: str,
    timeframe_str: str = "H1",
    years: float = 2.0,
    cache_dir: Path = Path("data/mt5_history_cache"),
    use_cache: bool = True,
    force_refresh: bool = False,
    allow_synthetic_fallback: bool = True,
    force_synthetic: bool = False,
) -> tuple[list[dict[str, float]], dict[str, Any]]:
    """
    Fetch historical OHLCV bars from MetaTrader 5 via mt5.copy_rates_range with local CSV caching.
    Falls back gracefully to reproducible synthetic multi-regime bars if MT5 is unavailable.
    """
    tf = timeframe_str.upper()
    days = int(round(years * 365))
    csv_path = cache_dir / f"{symbol}_{tf}_{days}d.csv"
    meta_path = cache_dir / f"{symbol}_{tf}_{days}d.meta.json"

    if force_synthetic:
        return generate_synthetic_regime_bars(symbol, tf, years=years)

    if use_cache and not force_refresh:
        cached = _load_cache(csv_path, meta_path)
        if cached is not None:
            return cached

    try:
        import MetaTrader5 as mt5

        if not mt5.initialize():
            mt5.initialize(path=r"C:\Program Files\MetaTrader 5\terminal64.exe")
        term = mt5.terminal_info()
        acc = mt5.account_info()
        if term is not None and acc is not None and getattr(term, "connected", False):
            mt5.symbol_select(symbol, True)
            info = mt5.symbol_info(symbol)
            tf_const = _mt5_timeframe_const(mt5, tf)
            end_dt = datetime.now(timezone.utc)
            start_dt = end_dt - timedelta(days=days)

            # Chunk in 180-day slices so large M15 histories load reliably
            all_rows: dict[int, dict[str, float]] = {}
            chunk_start = start_dt
            while chunk_start < end_dt:
                chunk_end = min(end_dt, chunk_start + timedelta(days=180))
                rates = mt5.copy_rates_range(symbol, tf_const, chunk_start, chunk_end)
                if rates is not None and len(rates) > 0:
                    for r in rates:
                        ts = int(r["time"])
                        all_rows[ts] = {
                            "time": float(ts),
                            "open": float(r["open"]),
                            "high": float(r["high"]),
                            "low": float(r["low"]),
                            "close": float(r["close"]),
                            "volume": float(r["tick_volume"]),
                        }
                chunk_start = chunk_end

            if len(all_rows) >= 300:
                candles = [all_rows[k] for k in sorted(all_rows.keys())]
                digits = int(info.digits) if info else DEFAULT_SYMBOL_SPECS.get(symbol, (5, 1e-5, 1.0))[0]
                point = float(info.point) if info else DEFAULT_SYMBOL_SPECS.get(symbol, (5, 1e-5, 1.0))[1]
                broker_spread = int(info.spread) if info and info.spread > 0 else int(
                    round(MAX_ALLOWED_SPREAD_POINTS.get(symbol, 20) * 0.6)
                )
                meta = {
                    "symbol": symbol,
                    "timeframe": tf,
                    "digits": digits,
                    "point": point,
                    "spread_points": min(broker_spread, MAX_ALLOWED_SPREAD_POINTS.get(symbol, broker_spread)),
                    "broker_live_spread_points": broker_spread,
                    "data_source": "MT5_LIVE",
                    "bars_count": len(candles),
                    "start_utc": datetime.fromtimestamp(candles[0]["time"], tz=timezone.utc).isoformat(),
                    "end_utc": datetime.fromtimestamp(candles[-1]["time"], tz=timezone.utc).isoformat(),
                    "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
                }
                if use_cache:
                    _save_cache(csv_path, meta_path, candles, meta)
                return candles, meta
    except Exception:
        pass

    if not allow_synthetic_fallback:
        raise RuntimeError(f"MT5 historical bars unavailable for {symbol} {tf} and synthetic fallback disabled")
    return generate_synthetic_regime_bars(symbol, tf, years=years)


def _simulate_single_trade(
    sig: StrategySignal,
    ind: Any,
    entry_idx: int,
    spread_price: float,
    max_hold_bars: int,
    split: str,
    session: str,
) -> tuple[SimulatedTrade, int] | None:
    """
    Simulate execution on bar `entry_idx + 1` open (or entry_idx close + spread) with conservative SL-first resolution.
    Returns (SimulatedTrade, exit_idx).
    """
    n = ind.n
    if entry_idx + 1 >= n:
        return None
    raw_entry = float(ind.closes[entry_idx])
    sl = float(sig.sl_price)
    tp = float(sig.tp_price)
    if sig.direction == "BUY":
        entry = raw_entry + spread_price * 0.5
        risk = entry - sl
        if risk <= 0.0:
            return None
        spread_cost_r = spread_price / risk
        exit_idx = min(n - 1, entry_idx + max_hold_bars)
        exit_px = float(ind.closes[exit_idx]) - spread_price * 0.5
        outcome = "TIME_EXIT"
        for j in range(entry_idx + 1, min(n, entry_idx + max_hold_bars + 1)):
            lo = float(ind.lows[j])
            hi = float(ind.highs[j])
            # Conservative: SL checked before TP if both touched in same bar
            if lo <= sl:
                exit_px = sl
                exit_idx = j
                outcome = "SL"
                break
            if hi >= tp:
                exit_px = tp - spread_price * 0.5
                exit_idx = j
                outcome = "TP"
                break
        r_mult = (exit_px - entry) / risk
    else:  # SELL
        entry = raw_entry - spread_price * 0.5
        risk = sl - entry
        if risk <= 0.0:
            return None
        spread_cost_r = spread_price / risk
        exit_idx = min(n - 1, entry_idx + max_hold_bars)
        exit_px = float(ind.closes[exit_idx]) + spread_price * 0.5
        outcome = "TIME_EXIT"
        for j in range(entry_idx + 1, min(n, entry_idx + max_hold_bars + 1)):
            lo = float(ind.lows[j])
            hi = float(ind.highs[j])
            if hi >= sl:
                exit_px = sl
                exit_idx = j
                outcome = "SL"
                break
            if lo <= tp:
                exit_px = tp + spread_price * 0.5
                exit_idx = j
                outcome = "TP"
                break
        r_mult = (entry - exit_px) / risk

    trade = SimulatedTrade(
        symbol=sig.symbol,
        strategy_name=sig.strategy_name,
        direction=sig.direction,
        regime=sig.regime,
        session=session,
        split=split,
        entry_time=float(ind.times[entry_idx]),
        exit_time=float(ind.times[exit_idx]),
        entry_price=entry,
        exit_price=exit_px,
        sl_price=sl,
        tp_price=tp,
        rr_planned=sig.rr_ratio,
        r_multiple=round(r_mult, 4),
        outcome=outcome,
        score=sig.score,
        bars_held=exit_idx - entry_idx,
        spread_cost_r=round(spread_cost_r, 4),
    )
    return trade, exit_idx


class MT5Backtester:
    """2-Year IS/OOS Multi-Strategy Backtester and 15m vs 30m Cadence Comparator."""

    def __init__(
        self,
        engine: MT5StrategyEngine | None = None,
        cache_dir: Path = Path("data/mt5_history_cache"),
        risk_pct_per_trade: float = 1.0,
        skip_rollover_non_crypto: bool = True,
    ) -> None:
        self.engine = engine or MT5StrategyEngine()
        self.cache_dir = cache_dir
        self.risk_pct_per_trade = risk_pct_per_trade
        self.skip_rollover_non_crypto = skip_rollover_non_crypto

    def backtest_symbol(
        self,
        symbol: str,
        candles: Sequence[dict[str, float]],
        meta: dict[str, Any],
        max_hold_bars: int = 72,
    ) -> list[SimulatedTrade]:
        if len(candles) < 250:
            return []
        ind = compute_indicators(candles)
        digits = int(meta.get("digits", 5))
        point = float(meta.get("point", 1e-5))
        max_sp = MAX_ALLOWED_SPREAD_POINTS.get(symbol, 25)
        spread_pts = min(int(meta.get("spread_points", round(max_sp * 0.6))), max_sp)
        spread_price = spread_pts * point

        # Midpoint timestamp splits Year 1 (IS) vs Year 2 (OOS)
        t_start = float(ind.times[210])
        t_end = float(ind.times[-1])
        t_mid = t_start + (t_end - t_start) * 0.5
        is_crypto = symbol in CRYPTO_SYMBOLS

        # Track busy_until_idx per strategy so strategies evaluate independently
        busy_until: dict[str, int] = {name: 0 for name in self.engine.strategy_names}
        trades: list[SimulatedTrade] = []

        for idx in range(210, ind.n - 2):
            session = classify_session(float(ind.times[idx]))
            if self.skip_rollover_non_crypto and (not is_crypto) and session == SESSION_ROLLOVER:
                continue

            regime_snap, signals = self.engine.evaluate_at_index(symbol, ind, idx, digits=digits, point=point)
            if not signals:
                continue
            split = "IS" if float(ind.times[idx]) < t_mid else "OOS"
            for sig in signals:
                if sig.setup_stage != "READY":
                    continue
                if idx <= busy_until.get(sig.strategy_name, 0):
                    continue
                res = _simulate_single_trade(
                    sig=sig,
                    ind=ind,
                    entry_idx=idx,
                    spread_price=spread_price,
                    max_hold_bars=max_hold_bars,
                    split=split,
                    session=session,
                )
                if res is not None:
                    trade, exit_idx = res
                    trades.append(trade)
                    busy_until[sig.strategy_name] = exit_idx

        return trades

    def run_2yr_study(
        self,
        symbols: Sequence[str] | None = None,
        timeframe_str: str = "H1",
        years: float = 2.0,
        use_cache: bool = True,
        force_refresh: bool = False,
        force_synthetic: bool = False,
    ) -> dict[str, Any]:
        target_symbols = list(symbols) if symbols else list(DEFAULT_MT5_SYMBOLS)
        max_hold = 72 if timeframe_str.upper() == "H1" else 120
        all_trades: list[SimulatedTrade] = []
        symbol_meta: dict[str, dict[str, Any]] = {}
        data_sources: set[str] = set()

        for sym in target_symbols:
            candles, meta = fetch_mt5_history(
                symbol=sym,
                timeframe_str=timeframe_str,
                years=years,
                cache_dir=self.cache_dir,
                use_cache=use_cache,
                force_refresh=force_refresh,
                allow_synthetic_fallback=True,
                force_synthetic=force_synthetic,
            )
            symbol_meta[sym] = meta
            data_sources.add(str(meta.get("data_source", "UNKNOWN")))
            sym_trades = self.backtest_symbol(sym, candles, meta, max_hold_bars=max_hold)
            all_trades.extend(sym_trades)

        # Aggregate overall, per-strategy, and per-(symbol, strategy, regime)
        overall_all = compute_performance_metrics(all_trades, self.risk_pct_per_trade).to_dict()
        overall_is = compute_performance_metrics(
            [t for t in all_trades if t.split == "IS"], self.risk_pct_per_trade
        ).to_dict()
        overall_oos = compute_performance_metrics(
            [t for t in all_trades if t.split == "OOS"], self.risk_pct_per_trade
        ).to_dict()

        by_strategy: dict[str, dict[str, Any]] = {}
        for sname in self.engine.strategy_names:
            st = [t for t in all_trades if t.strategy_name == sname]
            st_is = [t for t in st if t.split == "IS"]
            st_oos = [t for t in st if t.split == "OOS"]
            by_strategy[sname] = {
                "all": compute_performance_metrics(st, self.risk_pct_per_trade).to_dict(),
                "is": compute_performance_metrics(st_is, self.risk_pct_per_trade).to_dict(),
                "oos": compute_performance_metrics(st_oos, self.risk_pct_per_trade).to_dict(),
            }

        # Detailed priors table: (symbol, strategy_name, regime, session="ALL")
        now_iso = datetime.now(timezone.utc).isoformat()
        priors: list[dict[str, Any]] = []
        grouped: dict[tuple[str, str, str], list[SimulatedTrade]] = {}
        for t in all_trades:
            grouped.setdefault((t.symbol, t.strategy_name, t.regime), []).append(t)
            grouped.setdefault((t.symbol, t.strategy_name, "ALL"), []).append(t)

        for (sym, sname, reg), grp in sorted(grouped.items()):
            m_all = compute_performance_metrics(grp, self.risk_pct_per_trade)
            m_is = compute_performance_metrics([t for t in grp if t.split == "IS"], self.risk_pct_per_trade)
            m_oos = compute_performance_metrics([t for t in grp if t.split == "OOS"], self.risk_pct_per_trade)
            is_oos_ok = (
                m_is.trades_count >= 3
                and m_oos.trades_count >= 3
                and m_is.expectancy_r > 0.0
                and m_oos.expectancy_r > 0.0
            )
            enabled = (m_all.trades_count >= 6 and m_all.expectancy_r > 0.0 and m_all.profit_factor >= 1.05) or is_oos_ok
            priors.append(
                {
                    "symbol": sym,
                    "strategy_name": sname,
                    "regime": reg,
                    "session": "ALL",
                    "trades_count": m_all.trades_count,
                    "wins": m_all.wins,
                    "losses": m_all.losses,
                    "win_rate": m_all.win_rate,
                    "profit_factor": m_all.profit_factor,
                    "expectancy_r": m_all.expectancy_r,
                    "avg_rr": m_all.avg_rr,
                    "max_dd_pct": m_all.max_dd_pct,
                    "is_oos_consistent": bool(is_oos_ok),
                    "enabled": bool(enabled),
                    "is_stats": m_is.to_dict(),
                    "oos_stats": m_oos.to_dict(),
                    "updated_at": now_iso,
                }
            )

        return {
            "generated_at_utc": now_iso,
            "data_source": ",".join(sorted(data_sources)) if data_sources else "NONE",
            "timeframe": timeframe_str.upper(),
            "years": years,
            "symbols": target_symbols,
            "symbol_meta": symbol_meta,
            "overall": {"all": overall_all, "is": overall_is, "oos": overall_oos},
            "by_strategy": by_strategy,
            "priors": priors,
        }

    def compare_evaluation_cadence(
        self,
        symbols: Sequence[str] | None = None,
        years: float = 2.0,
        use_cache: bool = True,
        force_refresh: bool = False,
        force_synthetic: bool = False,
    ) -> dict[str, Any]:
        """
        Compare 15m base vs 30m base vs 30m base + FORMING sniper wakes on M15 bars.
        Measures trade quality, missed READY entries vs 15m, sniper captures, and AI cycle/API call counts.
        """
        target_symbols = list(symbols) if symbols else list(DEFAULT_MT5_SYMBOLS)
        trades_by_mode: dict[str, list[SimulatedTrade]] = {
            "15m_base": [],
            "30m_base": [],
            "30m_plus_sniper": [],
        }
        ts_slots_15m: set[int] = set()
        ts_slots_30m: set[int] = set()
        ts_slots_sniper: set[int] = set()
        sniper_wakes = 0
        sniper_triggered = 0
        data_sources: set[str] = set()
        total_days_est = 0.0

        for sym in target_symbols:
            candles, meta = fetch_mt5_history(
                symbol=sym,
                timeframe_str="M15",
                years=years,
                cache_dir=self.cache_dir,
                use_cache=use_cache,
                force_refresh=force_refresh,
                allow_synthetic_fallback=True,
                force_synthetic=force_synthetic,
            )
            data_sources.add(str(meta.get("data_source", "UNKNOWN")))
            if len(candles) < 300:
                continue

            ind = compute_indicators(candles)
            digits = int(meta.get("digits", 5))
            point = float(meta.get("point", 1e-5))
            max_sp = MAX_ALLOWED_SPREAD_POINTS.get(sym, 25)
            spread_pts = min(int(meta.get("spread_points", round(max_sp * 0.6))), max_sp)
            spread_price = spread_pts * point
            t_start = float(ind.times[210])
            t_end = float(ind.times[-1])
            t_mid = t_start + (t_end - t_start) * 0.5
            total_days_est = max(total_days_est, (t_end - t_start) / 86400.0)
            is_crypto = sym in CRYPTO_SYMBOLS

            busy_15: dict[str, int] = {}
            busy_30: dict[str, int] = {}
            busy_sn: dict[str, int] = {}
            sniper_scheduled_next = False

            for idx in range(210, ind.n - 2):
                ts = float(ind.times[idx])
                ts_slot = int(ts // 900)
                dt = datetime.fromtimestamp(ts, tz=timezone.utc)
                is_30m_boundary = (dt.minute % 30) == 0
                session = classify_session(ts)
                if self.skip_rollover_non_crypto and (not is_crypto) and session == SESSION_ROLLOVER:
                    sniper_scheduled_next = False
                    continue

                ts_slots_15m.add(ts_slot)
                if is_30m_boundary:
                    ts_slots_30m.add(ts_slot)
                eval_sniper_now = is_30m_boundary or sniper_scheduled_next
                was_sniper_wake = (not is_30m_boundary) and sniper_scheduled_next
                if was_sniper_wake:
                    sniper_wakes += 1
                    ts_slots_sniper.add(ts_slot)
                sniper_scheduled_next = False

                _, signals = self.engine.evaluate_at_index(sym, ind, idx, digits=digits, point=point)
                if not signals:
                    continue

                split = "IS" if ts < t_mid else "OOS"
                ready_sigs = [s for s in signals if s.setup_stage == "READY"]
                # Schedule exact sniper wake only for high-conviction FORMING setups (score >= 54)
                forming_sigs = [s for s in signals if s.setup_stage == "FORMING" and s.score >= 54.0]

                if is_30m_boundary and forming_sigs:
                    sniper_scheduled_next = True

                for sig in ready_sigs:
                    # 15m_base
                    if idx > busy_15.get(sig.strategy_name, 0):
                        res = _simulate_single_trade(sig, ind, idx, spread_price, 96, split, session)
                        if res:
                            trades_by_mode["15m_base"].append(res[0])
                            busy_15[sig.strategy_name] = res[1]

                    # 30m_base
                    if is_30m_boundary and idx > busy_30.get(sig.strategy_name, 0):
                        res = _simulate_single_trade(sig, ind, idx, spread_price, 96, split, session)
                        if res:
                            trades_by_mode["30m_base"].append(res[0])
                            busy_30[sig.strategy_name] = res[1]

                    # 30m_plus_sniper
                    if eval_sniper_now and idx > busy_sn.get(sig.strategy_name, 0):
                        if was_sniper_wake:
                            sniper_triggered += 1
                        res = _simulate_single_trade(sig, ind, idx, spread_price, 96, split, session)
                        if res:
                            trades_by_mode["30m_plus_sniper"].append(res[0])
                            busy_sn[sig.strategy_name] = res[1]

        days = max(1.0, total_days_est)
        # Exact deduplicated global AI call counts per day across the tested universe
        global_cycles_15m_day = len(ts_slots_15m) / days
        global_cycles_30m_day = len(ts_slots_30m) / days
        sniper_slots_day = len(ts_slots_sniper - ts_slots_30m) / days

        summary_modes: dict[str, dict[str, Any]] = {}
        base15_trades = max(1, len(trades_by_mode["15m_base"]))
        for mode_name, tlist in trades_by_mode.items():
            m = compute_performance_metrics(tlist, self.risk_pct_per_trade)
            if mode_name == "15m_base":
                calls_day = round(global_cycles_15m_day, 1)
                missed = 0
                capture_pct = 100.0
            elif mode_name == "30m_base":
                calls_day = round(global_cycles_30m_day, 1)
                missed = max(0, base15_trades - m.trades_count)
                capture_pct = round((m.trades_count / base15_trades) * 100.0, 1)
            else:
                calls_day = round(global_cycles_30m_day + sniper_slots_day, 1)
                missed = max(0, base15_trades - m.trades_count)
                capture_pct = round((m.trades_count / base15_trades) * 100.0, 1)
            summary_modes[mode_name] = {
                **m.to_dict(),
                "est_ai_calls_per_day": calls_day,
                "missed_entries_vs_15m": missed,
                "capture_rate_vs_15m_pct": capture_pct,
            }

        m15 = summary_modes["15m_base"]
        m30 = summary_modes["30m_base"]
        msn = summary_modes["30m_plus_sniper"]

        # Data-backed recommendation
        if msn["expectancy_r"] >= m15["expectancy_r"] - 0.015 and msn["est_ai_calls_per_day"] < m15["est_ai_calls_per_day"] * 0.85:
            rec = "30m_base + adaptive sniper wakes (FORMING setups)"
            rationale = (
                f"30m+Sniper captures {msn['capture_rate_vs_15m_pct']}% of 15m entries "
                f"(+{sniper_triggered} sniper-triggered trades, PF {msn['profit_factor']}, Exp {msn['expectancy_r']:+.3f}R) "
                f"vs 15m base (PF {m15['profit_factor']}, Exp {m15['expectancy_r']:+.3f}R) while cutting AI calls from "
                f"~{m15['est_ai_calls_per_day']}/day to ~{msn['est_ai_calls_per_day']}/day."
            )
        elif m15["expectancy_r"] > msn["expectancy_r"] + 0.02 and m15["profit_factor"] > msn["profit_factor"]:
            rec = "15m_base (with FORMING sniper wakes for sub-15m precision)"
            rationale = (
                f"15m base delivers materially better expectancy ({m15['expectancy_r']:+.3f}R, PF {m15['profit_factor']}) "
                f"than 30m base ({m30['expectancy_r']:+.3f}R, PF {m30['profit_factor']}) and 30m+Sniper ({msn['expectancy_r']:+.3f}R)."
            )
        else:
            rec = "30m_base + adaptive sniper wakes (FORMING setups)"
            rationale = (
                f"30m+Sniper balances API quota (~{msn['est_ai_calls_per_day']} calls/day vs ~{m15['est_ai_calls_per_day']} for 15m) "
                f"with {msn['capture_rate_vs_15m_pct']}% entry capture and PF {msn['profit_factor']} (vs 30m-only PF {m30['profit_factor']})."
            )

        return {
            "data_source": ",".join(sorted(data_sources)),
            "symbols_tested": target_symbols,
            "days_covered": round(days, 1),
            "sniper_wakes_total": sniper_wakes,
            "sniper_triggered_trades": sniper_triggered,
            "modes": summary_modes,
            "recommended_cadence": rec,
            "rationale": rationale,
        }


def export_strategy_priors(
    study_result: dict[str, Any],
    output_path: Path | str | None = None,
    cadence_comparison: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Export structured JSON summary compatible with MT5KnowledgeDB (`strategy_priors` table).
    """
    payload = {
        "schema_version": "1.0",
        "generated_at_utc": study_result.get("generated_at_utc", datetime.now(timezone.utc).isoformat()),
        "data_source": study_result.get("data_source", "UNKNOWN"),
        "timeframe": study_result.get("timeframe", "H1"),
        "years": study_result.get("years", 2.0),
        "symbols": study_result.get("symbols", []),
        "overall": study_result.get("overall", {}),
        "by_strategy": study_result.get("by_strategy", {}),
        "cadence_comparison": cadence_comparison or study_result.get("cadence_comparison"),
        "priors": study_result.get("priors", []),
    }
    if output_path is not None:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload
