from __future__ import annotations

import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import src.mt5_bot as mt5_bot_mod
from src.mt5_bot import (
    MT5Bot,
    MT5SymbolSnapshot,
    MT5_MAGIC_NUMBER,
    STRATEGY_MODE_SUPERVISED_M15,
    is_within_trading_window,
)
from src.mt5_scalper_profiles import (
    SCALPER_PROFILES,
    SymbolScalperProfile,
    get_scalper_profile,
)
from src.mt5_strategies import (
    DEFAULT_STRATEGIES,
    IndicatorArrays,
    MT5StrategyEngine,
    MarketRegimeClassifier,
    REGIME_HIGH_VOL_CHOP,
    REGIME_RANGE,
    REGIME_TREND_DOWN,
    REGIME_TREND_UP,
    RegimeSnapshot,
    StrategySignal,
    SupervisedM15ScalperStrategy,
    compute_indicators,
)


# ---------------------------------------------------------------------------
# Deterministic synthetic data & mock helpers
# ---------------------------------------------------------------------------

EXPECTED_14_SYMBOLS = (
    "BTCUSDm",
    "ETHUSDm",
    "GBPUSDm",
    "EURUSDm",
    "USDJPYm",
    "USDCADm",
    "USDCHFm",
    "AUDUSDm",
    "NZDUSDm",
    "EURJPYm",
    "EURGBPm",
    "US500m",
    "USTECm",
    "XAUUSDm",
)

LEADER_SYMBOLS = ("BTCUSDm", "ETHUSDm", "GBPUSDm", "US500m", "USTECm")
CAUTIOUS_SYMBOLS = ("EURGBPm", "NZDUSDm", "EURJPYm", "XAUUSDm")


def _make_regime_snapshot(
    regime: str = REGIME_TREND_UP,
    *,
    adx_14: float = 26.0,
    ema200_slope_atr: float = 0.08,
    dist_ema200_atr: float = 1.8,
    atr_percentile: float = 50.0,
    bb_width_percentile: float = 50.0,
) -> RegimeSnapshot:
    return RegimeSnapshot(
        regime=regime,
        adx_14=adx_14,
        ema200_slope_atr=ema200_slope_atr,
        dist_ema200_atr=dist_ema200_atr,
        atr_percentile=atr_percentile,
        bb_width=0.01,
        bb_width_percentile=bb_width_percentile,
        confidence=0.85,
        reason="synthetic_test",
    )


def _make_m15_pullback_candles(
    *,
    direction: str = "LONG",
    n: int = 230,
    start_price: float = 1.1000,
    step: float = 0.00022,
    atr_like: float = 0.00080,
    bullish_engulfing: bool = False,
    bearish_engulfing: bool = False,
    exhaustion_last_bar: bool = False,
) -> list[dict[str, float]]:
    """Build deterministic M15 candles with realistic trend swings followed by a pullback & trigger bar."""
    base_ts = datetime(2026, 11, 20, 14, 0, tzinfo=timezone.utc).timestamp()
    candles: list[dict[str, float]] = []
    px = start_price
    sign = 1.0 if direction == "LONG" else -1.0

    # 1. Realistic trend with two-way swings (sign-symmetric so LONG and SHORT mirror each other)
    for i in range(n - 9):
        swing = sign * np.sin(i * 0.65) * (atr_like * 0.90)
        o = px
        c = o + sign * step + swing
        h = max(o, c) + atr_like * 0.35
        l = min(o, c) - atr_like * 0.35
        candles.append(
            {
                "time": base_ts + i * 900,
                "open": round(o, 5),
                "high": round(h, 5),
                "low": round(l, 5),
                "close": round(c, 5),
                "volume": 500.0,
            }
        )
        px = c

    # 2. Short impulse with trend followed by 3 sharp pullback bars to cool RSI & Stochastic
    for j in range(2):
        idx = n - 9 + j
        o = px
        c = o + sign * (atr_like * 0.65)
        h = max(o, c) + atr_like * 0.25
        l = min(o, c) - atr_like * 0.25
        candles.append(
            {
                "time": base_ts + idx * 900,
                "open": round(o, 5),
                "high": round(h, 5),
                "low": round(l, 5),
                "close": round(c, 5),
                "volume": 550.0,
            }
        )
        px = c

    for j in range(3):
        idx = n - 7 + j
        o = px
        c = o - sign * (atr_like * 0.62)
        h = max(o, c) + atr_like * 0.18
        l = min(o, c) - atr_like * 0.18
        candles.append(
            {
                "time": base_ts + idx * 900,
                "open": round(o, 5),
                "high": round(h, 5),
                "low": round(l, 5),
                "close": round(c, 5),
                "volume": 520.0,
            }
        )
        px = c

    # 3. Five stabilization/turn bars before trigger so 3-bar smoothed Stochastic K turns cleanly
    for j, mult in enumerate((-0.10, 0.05, 0.18, 0.40, 0.28)):
        idx = n - 6 + j
        o_stab = px
        c_stab = px + sign * (atr_like * mult)
        candles.append(
            {
                "time": base_ts + idx * 900,
                "open": round(o_stab, 5),
                "high": round(max(o_stab, c_stab) + atr_like * 0.15, 5),
                "low": round(min(o_stab, c_stab) - atr_like * 0.15, 5),
                "close": round(c_stab, 5),
                "volume": 580.0,
            }
        )
        px = c_stab

    # 4. Trigger bar resuming the trend
    if direction == "LONG":
        if exhaustion_last_bar:
            o = px
            c = px + atr_like * 3.0
            h = c + atr_like * 0.2
            l = o - atr_like * 0.1
        else:
            o = px
            c = px + atr_like * 0.28
            h = c + atr_like * 0.14
            l = o - atr_like * 0.10
    else:
        if exhaustion_last_bar:
            o = px
            c = px - atr_like * 3.0
            h = o + atr_like * 0.1
            l = c - atr_like * 0.2
        else:
            o = px
            c = px - atr_like * 0.28
            h = o + atr_like * 0.10
            l = c - atr_like * 0.14

    candles.append(
        {
            "time": base_ts + (n - 1) * 900,
            "open": round(o, 5),
            "high": round(h, 5),
            "low": round(l, 5),
            "close": round(c, 5),
            "volume": 650.0,
        }
    )
    return candles


def _make_indicator_arrays(
    *,
    n: int = 80,
    close: float = 1.1050,
    open_px: float = 1.1045,
    high: float = 1.1055,
    low: float = 1.1040,
    prev_open: float = 1.1049,
    prev_close: float = 1.1044,
    prev_high: float = 1.1051,
    prev_low: float = 1.1041,
    ema_9: float = 1.1046,
    ema_21: float = 1.1038,
    ema_50: float = 1.1025,
    ema_200: float = 1.0980,
    atr: float = 0.0010,
    adx: float = 26.0,
    rsi: float = 52.0,
    stoch_k: float = 40.0,
    prev_stoch_k: float = 34.0,
    stoch_d: float = 36.0,
    macd_hist: float = 0.0002,
    prev_macd_hist: float = 0.0001,
) -> IndicatorArrays:
    """Create a minimal deterministic IndicatorArrays fixture for exact filter boundary tests."""
    times = np.arange(n, dtype=float) * 900.0
    opens = np.full(n, prev_open, dtype=float)
    highs = np.full(n, prev_high, dtype=float)
    lows = np.full(n, prev_low, dtype=float)
    closes = np.full(n, prev_close, dtype=float)
    volumes = np.full(n, 500.0, dtype=float)

    opens[-1] = open_px
    highs[-1] = high
    lows[-1] = low
    closes[-1] = close

    e9 = np.full(n, ema_9, dtype=float)
    e21 = np.full(n, ema_21, dtype=float)
    e50 = np.full(n, ema_50, dtype=float)
    e200 = np.full(n, ema_200, dtype=float)
    atr_arr = np.full(n, atr, dtype=float)
    adx_arr = np.full(n, adx, dtype=float)
    rsi_arr = np.full(n, rsi, dtype=float)
    k_arr = np.full(n, prev_stoch_k, dtype=float)
    k_arr[-1] = stoch_k
    d_arr = np.full(n, stoch_d, dtype=float)
    macd_arr = np.full(n, prev_macd_hist, dtype=float)
    macd_arr[-1] = macd_hist

    return IndicatorArrays(
        n=n,
        times=times,
        opens=opens,
        highs=highs,
        lows=lows,
        closes=closes,
        volumes=volumes,
        ema_9=e9,
        ema_21=e21,
        ema_50=e50,
        ema_200=e200,
        atr_14=atr_arr,
        adx_14=adx_arr,
        plus_di=np.full(n, 28.0, dtype=float),
        minus_di=np.full(n, 14.0, dtype=float),
        rsi_14=rsi_arr,
        stoch_k=k_arr,
        stoch_d=d_arr,
        bb_mid=e21.copy(),
        bb_upper=e21 + 2.0 * atr,
        bb_lower=e21 - 2.0 * atr,
        bb_pct_b=np.full(n, 0.55, dtype=float),
        bb_width=np.full(n, 0.01, dtype=float),
        macd_line=macd_arr.copy(),
        macd_signal=np.zeros(n, dtype=float),
        macd_hist=macd_arr,
        atr_pctile=np.full(n, 50.0, dtype=float),
        bb_width_pctile=np.full(n, 50.0, dtype=float),
        ema200_slope_atr=np.full(n, 0.05, dtype=float),
        dist_ema200_atr=np.full(n, 2.0, dtype=float),
        swing_high_20=np.full(n, close + 3.0 * atr, dtype=float),
        swing_low_20=np.full(n, close - 3.0 * atr, dtype=float),
    )


def _make_snapshot(
    symbol: str = "GBPUSDm",
    bid: float = 1.27000,
    ask: float = 1.27012,
    spread_points: int = 12,
    digits: int = 5,
    point: float = 1e-5,
    atr_price: float = 0.0012,
    atr_15_price: float = 0.0008,
) -> MT5SymbolSnapshot:
    return MT5SymbolSnapshot(
        symbol=symbol,
        bid=bid,
        ask=ask,
        spread_points=spread_points,
        digits=digits,
        point=point,
        min_lot=0.01,
        lot_step=0.01,
        margin_min_lot_usd=2.5,
        usd_per_1pct_move_min_lot=12.7,
        ema_200=bid - 0.0030,
        ema_50=bid - 0.0012,
        ema_21=bid - 0.0004,
        above_ema_200=True,
        dist_to_ema200_atr=2.0,
        ema200_slope_positive=True,
        stoch_k=36.0,
        stoch_d=32.0,
        stoch_recent_min=28.0,
        stoch_recent_max=48.0,
        stoch_turning_up=True,
        stoch_turning_down=False,
        rsi_14=52.0,
        bb_upper=bid + 0.0025,
        bb_lower=bid - 0.0025,
        bb_pct_b=0.52,
        macd_hist=0.00015,
        macd_improving=True,
        atr_price=atr_price,
        atr_pct=(atr_price / bid) * 100.0,
        candle_pattern="BULLISH_ENGULFING",
        prev_candle_low=bid - 0.0009,
        prev_candle_high=bid + 0.0005,
        entry_pillar="M15_SCALPER_PULLBACK_LONG",
        strategy_setup="LONG_ENTRY",
        structural_long_sl=bid - 0.0018,
        structural_short_sl=ask + 0.0018,
        htf_trend="BULLISH",
        adx_14=26.0,
        atr_15_price=atr_15_price,
        recent_h1_closes=[bid - 0.0005, bid - 0.0002, bid],
        swing_high_20=bid + 0.0035,
        swing_low_20=bid - 0.0028,
    )


def _build_mocked_supervised_bot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    snapshot: MT5SymbolSnapshot | None = None,
    raw_positions: tuple[Any, ...] = (),
    ready_signal: StrategySignal | None = None,
) -> tuple[MT5Bot, list[dict[str, Any]], list[dict[str, Any]]]:
    snap = snapshot or _make_snapshot()
    placed_orders: list[dict[str, Any]] = []
    sl_modifications: list[dict[str, Any]] = []

    bot = MT5Bot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "mt5_latest_report.md",
        history_file=tmp_path / "mt5_trade_history.json",
        ai_state_file=tmp_path / "mt5_ai_state.json",
        strategy_mode=STRATEGY_MODE_SUPERVISED_M15,
        trading_window_start=8,
        trading_window_end=23,
        local_tz_offset=-6,
        supervised_max_positions=6,
        supervised_entry_cooldown_sec=60.0,
    )

    fake_acc = SimpleNamespace(
        login=999001,
        server="Exness-MT5Real",
        leverage=500,
        balance=200.0,
        equity=200.0,
        margin_free=180.0,
    )
    monkeypatch.setattr(mt5_bot_mod.mt5, "positions_get", lambda: raw_positions)
    monkeypatch.setattr(mt5_bot_mod.mt5, "account_info", lambda: fake_acc)
    monkeypatch.setattr(mt5_bot_mod.mt5, "history_deals_get", lambda d1, d2: [])
    monkeypatch.setattr(bot, "ensure_connected", lambda: (SimpleNamespace(connected=True), fake_acc))
    monkeypatch.setattr(bot, "build_snapshots", lambda free_margin_usd, open_symbols: [snap])
    monkeypatch.setattr(
        bot,
        "_fetch_candles",
        lambda symbol, tf, count=250: _make_m15_pullback_candles(direction="LONG", n=120),
    )
    monkeypatch.setattr(
        bot,
        "_evaluate_daily_risk_guard",
        lambda **kwargs: {
            "utc_date": "2026-11-23",
            "protection_mode": "NORMAL",
            "daily_closed_pnl_usd": 0.0,
            "consecutive_losses": 0,
            "mins_since_last_loss": 999.0,
            "pause_new_entries": False,
            "hard_daily_loss_stop": False,
            "pause_remaining_mins": 0.0,
            "min_ai_prob": 60,
            "risk_scale": 1.0,
            "max_positions": 6,
            "reason": "OK",
        },
    )
    monkeypatch.setattr(bot, "_passes_deterministic_shields", lambda **kwargs: (True, "OK"))
    monkeypatch.setattr(
        bot,
        "calculate_safe_lot_and_sl",
        lambda **kwargs: (
            0.02,
            round(snap.bid - 0.0016, snap.digits),
            round(snap.ask + 0.0036, snap.digits),
            3.2,
        ),
    )

    if ready_signal is not None:
        regime_stub = _make_regime_snapshot(REGIME_TREND_UP)
        monkeypatch.setattr(
            bot.supervised_scalper_strategy,
            "evaluate_candles",
            lambda **kwargs: (regime_stub, ready_signal),
        )

    def fake_place_order(
        snap: MT5SymbolSnapshot,
        side: str,
        lot: float,
        sl_price: float,
        tp_price: float,
        reason: str,
        risk_usd: float,
        comment_override: str | None = None,
    ) -> dict[str, Any]:
        order = {
            "ticket": 88001 + len(placed_orders),
            "symbol": snap.symbol,
            "side": side,
            "lot": lot,
            "price": snap.ask if side == "BUY" else snap.bid,
            "sl": sl_price,
            "tp": tp_price,
            "risk_usd": risk_usd,
            "magic": MT5_MAGIC_NUMBER,
            "reason": reason,
            "comment": comment_override or "",
        }
        placed_orders.append(order)
        bot.last_order_timestamp = time.time()
        return order

    def fake_modify_sl_tp(ticket: int, symbol: str, new_sl: float, new_tp: float) -> bool:
        sl_modifications.append(
            {
                "ticket": int(ticket),
                "symbol": str(symbol),
                "new_sl": float(new_sl),
                "new_tp": float(new_tp),
            }
        )
        for p in raw_positions:
            if int(p.ticket) == int(ticket):
                p.sl = float(new_sl)
                p.tp = float(new_tp)
        return True

    monkeypatch.setattr(bot, "_place_mt5_order", fake_place_order)
    monkeypatch.setattr(bot, "_modify_mt5_sl_tp", fake_modify_sl_tp)
    return bot, placed_orders, sl_modifications


# ---------------------------------------------------------------------------
# 1. Per-Symbol Scalper Profiles Validation Tests
# ---------------------------------------------------------------------------


def test_all_14_scalper_profiles_exist_with_valid_bounds() -> None:
    assert set(SCALPER_PROFILES.keys()) == set(EXPECTED_14_SYMBOLS)
    assert len(SCALPER_PROFILES) == 14

    for sym, profile in SCALPER_PROFILES.items():
        assert isinstance(profile, SymbolScalperProfile)
        assert profile.symbol == sym
        assert profile.asset_class in ("CRYPTO", "FOREX", "INDICES", "METALS")
        assert profile.tier in ("LEADER", "CORE", "CAUTIOUS")

        # Risk & RR bounds
        assert 0.50 <= profile.risk_multiplier <= 1.30
        assert 1.5 <= profile.sl_atr_mult <= 2.6
        assert profile.tp_atr_mult > profile.sl_atr_mult
        assert profile.min_rr >= 1.8
        assert (profile.tp_atr_mult / profile.sl_atr_mult) >= profile.min_rr - 1e-6

        # Fast BE (+0.35 ATR) & Trailing Lock (68% - 80%)
        assert 0.70 <= profile.be_trigger_atr <= 1.25
        assert profile.be_lock_atr == pytest.approx(0.35, abs=0.05)
        assert 0.68 <= profile.trailing_lock_pct <= 0.80

        # No contra-trend traps enabled by default
        assert profile.allow_counter_trend is False

        # Indicator & spread bounds
        assert 35.0 <= profile.stoch_long_max <= 60.0
        assert 40.0 <= profile.stoch_short_min <= 65.0
        assert profile.rsi_long_min < profile.rsi_long_max
        assert profile.rsi_short_min < profile.rsi_short_max
        assert 0.05 <= profile.max_spread_sl_ratio <= 0.20
        assert 12.0 <= profile.min_adx < profile.max_adx <= 65.0

        # Serialization
        d = profile.to_dict()
        assert d["symbol"] == sym
        assert d["allow_counter_trend"] is False


def test_weaker_crosses_have_stricter_filters_than_leaders() -> None:
    leaders = [SCALPER_PROFILES[s] for s in LEADER_SYMBOLS]
    cautious = [SCALPER_PROFILES[s] for s in CAUTIOUS_SYMBOLS]

    for lp in leaders:
        assert lp.tier == "LEADER"
        assert lp.risk_multiplier >= 1.10
        assert lp.require_candle_pattern is False

    for cp in cautious:
        assert cp.tier == "CAUTIOUS"
        assert cp.risk_multiplier <= 0.70
        assert cp.require_candle_pattern is True

    min_leader_risk = min(p.risk_multiplier for p in leaders)
    max_cautious_risk = max(p.risk_multiplier for p in cautious)
    assert max_cautious_risk < min_leader_risk

    min_leader_stoch_long = min(p.stoch_long_max for p in leaders)
    max_cautious_stoch_long = max(p.stoch_long_max for p in cautious)
    assert max_cautious_stoch_long < min_leader_stoch_long

    max_leader_stoch_short = max(p.stoch_short_min for p in leaders)
    min_cautious_stoch_short = min(p.stoch_short_min for p in cautious)
    assert min_cautious_stoch_short > max_leader_stoch_short

    min_leader_spread = min(p.max_spread_sl_ratio for p in leaders)
    max_cautious_spread = max(p.max_spread_sl_ratio for p in cautious)
    assert max_cautious_spread < min_leader_spread

    max_leader_min_adx = max(p.min_adx for p in leaders)
    min_cautious_min_adx = min(p.min_adx for p in cautious)
    assert min_cautious_min_adx > max_leader_min_adx


def test_get_scalper_profile_lookup_and_asset_class_fallbacks() -> None:
    # Exact and case-insensitive / missing-'m' resolution
    assert get_scalper_profile("BTCUSDm") == SCALPER_PROFILES["BTCUSDm"]
    assert get_scalper_profile("btcusd") == SCALPER_PROFILES["BTCUSDm"]
    assert get_scalper_profile("GBPUSD") == SCALPER_PROFILES["GBPUSDm"]

    # Asset-class fallbacks for unlisted symbols
    sol = get_scalper_profile("SOLUSDm")
    assert sol.asset_class == "CRYPTO"
    assert sol.allow_counter_trend is False

    xag = get_scalper_profile("XAGUSDm")
    assert xag.asset_class == "METALS"
    assert xag.require_candle_pattern is True
    assert xag.allow_counter_trend is False

    us30 = get_scalper_profile("US30m")
    assert us30.asset_class == "INDICES"
    assert us30.allow_counter_trend is False

    cadjpy = get_scalper_profile("CADJPYm")
    assert cadjpy.asset_class == "FOREX"
    assert cadjpy.allow_counter_trend is False

    other = get_scalper_profile("CUSTOM_ASSET_99")
    assert other.asset_class == "OTHER"
    assert other.tier == "CAUTIOUS"
    assert other.allow_counter_trend is False


# ---------------------------------------------------------------------------
# 2. SupervisedM15ScalperStrategy Signal Generation & Filter Tests
# ---------------------------------------------------------------------------


def test_supervised_scalper_registered_in_engine() -> None:
    engine = MT5StrategyEngine()
    assert STRATEGY_MODE_SUPERVISED_M15 in engine.strategy_names
    assert any(isinstance(s, SupervisedM15ScalperStrategy) for s in DEFAULT_STRATEGIES)


def test_supervised_scalper_generates_ready_long_and_short_on_synthetic_candles() -> None:
    strat = SupervisedM15ScalperStrategy()

    # Trend-aligned LONG pullback on GBPUSDm (LEADER)
    long_candles = _make_m15_pullback_candles(direction="LONG", bullish_engulfing=True)
    regime_up, sig_long = strat.evaluate_candles(
        "GBPUSDm", long_candles, digits=5, point=1e-5, spread_points=10
    )
    assert regime_up.regime == REGIME_TREND_UP
    assert sig_long.strategy_name == STRATEGY_MODE_SUPERVISED_M15
    assert sig_long.setup_stage == "READY"
    assert sig_long.direction == "BUY"
    assert sig_long.sl_price < sig_long.entry_price < sig_long.tp_price
    assert sig_long.rr_ratio >= get_scalper_profile("GBPUSDm").min_rr
    assert sig_long.metadata["entry_pillar"] == "M15_SCALPER_PULLBACK_LONG"
    assert sig_long.metadata["profile_tier"] == "LEADER"
    assert sig_long.metadata["be_lock_atr"] == pytest.approx(0.35, abs=1e-6)

    # Trend-aligned SHORT pullback on GBPUSDm (LEADER)
    short_candles = _make_m15_pullback_candles(
        direction="SHORT", start_price=1.4000, bearish_engulfing=True
    )
    regime_dn, sig_short = strat.evaluate_candles(
        "GBPUSDm", short_candles, digits=5, point=1e-5, spread_points=10
    )
    assert regime_dn.regime == REGIME_TREND_DOWN
    assert sig_short.setup_stage == "READY"
    assert sig_short.direction == "SELL"
    assert sig_short.tp_price < sig_short.entry_price < sig_short.sl_price
    assert sig_short.rr_ratio >= get_scalper_profile("GBPUSDm").min_rr
    assert sig_short.metadata["entry_pillar"] == "M15_SCALPER_PULLBACK_SHORT"


def test_supervised_scalper_respects_spread_pattern_and_stoch_filters() -> None:
    strat = SupervisedM15ScalperStrategy()
    regime_up = _make_regime_snapshot(REGIME_TREND_UP, adx_14=26.0, dist_ema200_atr=2.0)

    # Plain bullish close (NOT an engulfing/hammer pattern):
    # prev bar was small green, current bar is small green near EMA9
    ind_plain = _make_indicator_arrays(
        open_px=1.1046,
        close=1.1049,
        high=1.1051,
        low=1.1044,
        prev_open=1.1045,
        prev_close=1.1047,
        prev_high=1.1049,
        prev_low=1.1043,
        stoch_k=40.0,
        prev_stoch_k=34.0,
        stoch_d=36.0,
        rsi=52.0,
        adx=26.0,
    )

    # 1. Leader (BTCUSDm: require_candle_pattern=False) -> READY on plain bullish close
    sig_leader = strat.evaluate_at(
        "BTCUSDm", ind_plain, ind_plain.n - 1, regime_up, digits=5, point=1e-5, spread_points=10
    )
    assert sig_leader.setup_stage == "READY"
    assert sig_leader.direction == "BUY"

    # 2. Cautious (EURGBPm: require_candle_pattern=True) -> NOT READY without pattern (FORMING instead)
    sig_cautious_no_pat = strat.evaluate_at(
        "EURGBPm", ind_plain, ind_plain.n - 1, regime_up, digits=5, point=1e-5, spread_points=10
    )
    assert sig_cautious_no_pat.setup_stage != "READY"

    # With a genuine BULLISH_ENGULFING pattern on EURGBPm -> READY
    ind_engulf = _make_indicator_arrays(
        open_px=1.1042,
        close=1.1051,
        high=1.1052,
        low=1.1041,
        prev_open=1.1049,
        prev_close=1.1043,
        prev_high=1.1050,
        prev_low=1.1042,
        stoch_k=38.0,
        prev_stoch_k=32.0,
        stoch_d=34.0,
        rsi=52.0,
        adx=26.0,
    )
    sig_cautious_pat = strat.evaluate_at(
        "EURGBPm", ind_engulf, ind_engulf.n - 1, regime_up, digits=5, point=1e-5, spread_points=10
    )
    assert sig_cautious_pat.setup_stage == "READY"
    assert sig_cautious_pat.direction == "BUY"
    assert sig_cautious_pat.metadata["pattern"] == "BULLISH_ENGULFING"

    # 3. Spread-to-SL ratio guard: EURGBPm max_spread_sl_ratio=0.09, sl_dist=2.2*0.001=0.0022
    # spread_points=40 -> spread_price=0.0004 -> ratio 0.18 > 0.09 -> NONE
    sig_wide_spread = strat.evaluate_at(
        "EURGBPm", ind_engulf, ind_engulf.n - 1, regime_up, digits=5, point=1e-5, spread_points=40
    )
    assert sig_wide_spread.setup_stage == "NONE"

    # 4. Stochastic filter: stoch_k=50 passes GBPUSDm (stoch_long_max=55), fails EURGBPm (stoch_long_max=42)
    ind_mid_stoch = _make_indicator_arrays(
        open_px=1.1042,
        close=1.1051,
        high=1.1052,
        low=1.1041,
        prev_open=1.1049,
        prev_close=1.1043,
        prev_high=1.1050,
        prev_low=1.1042,
        stoch_k=50.0,
        prev_stoch_k=46.0,
        stoch_d=47.0,
        rsi=52.0,
        adx=26.0,
    )
    assert strat.evaluate_at("GBPUSDm", ind_mid_stoch, -1, regime_up, spread_points=10).setup_stage == "READY"
    assert strat.evaluate_at("EURGBPm", ind_mid_stoch, -1, regime_up, spread_points=10).setup_stage == "NONE"


def test_supervised_scalper_rejects_contra_trend_exhaustion_and_chop() -> None:
    strat = SupervisedM15ScalperStrategy()

    # Contra-trend oversold LONG attempt in TREND_DOWN below EMA200 -> rejected (NONE)
    regime_dn = _make_regime_snapshot(
        REGIME_TREND_DOWN, adx_14=28.0, ema200_slope_atr=-0.06, dist_ema200_atr=-2.5
    )
    ind_oversold_contra = _make_indicator_arrays(
        open_px=1.0900,
        close=1.0906,
        high=1.0908,
        low=1.0898,
        ema_9=1.0920,
        ema_21=1.0940,
        ema_50=1.0970,
        ema_200=1.1050,
        rsi=26.0,
        stoch_k=18.0,
        prev_stoch_k=14.0,
        stoch_d=16.0,
        adx=28.0,
    )
    sig_contra_long = strat.evaluate_at("BTCUSDm", ind_oversold_contra, -1, regime_dn)
    assert sig_contra_long.setup_stage == "NONE"

    # Contra-trend overbought SHORT attempt in TREND_UP above EMA200 -> rejected (NONE)
    regime_up = _make_regime_snapshot(
        REGIME_TREND_UP, adx_14=28.0, ema200_slope_atr=0.06, dist_ema200_atr=2.5
    )
    ind_overbought_contra = _make_indicator_arrays(
        open_px=1.1150,
        close=1.1144,
        high=1.1152,
        low=1.1142,
        ema_9=1.1130,
        ema_21=1.1110,
        ema_50=1.1080,
        ema_200=1.1000,
        rsi=74.0,
        stoch_k=84.0,
        prev_stoch_k=88.0,
        stoch_d=86.0,
        adx=28.0,
    )
    sig_contra_short = strat.evaluate_at("BTCUSDm", ind_overbought_contra, -1, regime_up)
    assert sig_contra_short.setup_stage == "NONE"

    # Exhaustion candle (body > max_body_atr * atr) -> rejected (NONE)
    exh_candles = _make_m15_pullback_candles(direction="LONG", exhaustion_last_bar=True)
    _, sig_exh = strat.evaluate_candles("BTCUSDm", exh_candles, digits=5, point=1e-5)
    assert sig_exh.setup_stage == "NONE"

    # HIGH_VOL_CHOP regime -> rejected (NONE)
    regime_chop = _make_regime_snapshot(
        REGIME_HIGH_VOL_CHOP,
        adx_14=24.0,
        ema200_slope_atr=0.0,
        dist_ema200_atr=0.2,
        atr_percentile=95.0,
        bb_width_percentile=92.0,
    )
    ind_valid = _make_indicator_arrays()
    assert strat.evaluate_at("BTCUSDm", ind_valid, -1, regime_chop).setup_stage == "NONE"


# ---------------------------------------------------------------------------
# 3. Trading Window Helper Tests (UTC-6 & Custom Overrides)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "local_h, local_m, expected_open",
    [
        (7, 59, False),
        (8, 0, True),
        (15, 30, True),
        (22, 59, True),
        (23, 0, False),
        (2, 0, False),
    ],
)
def test_is_within_trading_window_utc_minus_6_boundaries(
    local_h: int, local_m: int, expected_open: bool
) -> None:
    local_tz = timezone(timedelta(hours=-6))
    local_dt = datetime(2026, 11, 23, local_h, local_m, tzinfo=local_tz)
    utc_dt = local_dt.astimezone(timezone.utc)

    is_open, status = is_within_trading_window(
        now_utc=utc_dt, start_hour=8, end_hour=23, tz_offset_hours=-6
    )
    assert is_open is expected_open
    if expected_open:
        assert "ACTIVA 08:00-23:00" in status
        assert f"{local_h:02d}:{local_m:02d}" in status
    else:
        assert "PAUSADA FUERA DE HORARIO" in status
        assert f"{local_h:02d}:{local_m:02d}" in status


def test_is_within_trading_window_custom_tz_and_hours() -> None:
    # UTC+0 with 09:00-17:00 window
    assert is_within_trading_window(
        datetime(2026, 11, 23, 8, 59, tzinfo=timezone.utc),
        start_hour=9,
        end_hour=17,
        tz_offset_hours=0,
    )[0] is False
    assert is_within_trading_window(
        datetime(2026, 11, 23, 9, 0, tzinfo=timezone.utc),
        start_hour=9,
        end_hour=17,
        tz_offset_hours=0,
    )[0] is True
    assert is_within_trading_window(
        datetime(2026, 11, 23, 17, 0, tzinfo=timezone.utc),
        start_hour=9,
        end_hour=17,
        tz_offset_hours=0,
    )[0] is False

    # Custom UTC+2 offset: 14:00 UTC == 16:00 local
    ok, label = is_within_trading_window(
        datetime(2026, 11, 23, 14, 0, tzinfo=timezone.utc),
        start_hour=10,
        end_hour=18,
        tz_offset_hours=2,
    )
    assert ok is True
    assert "UTC+2" in label
    assert "16:00" in label

    # Overnight wrap-around window [22:00, 06:00) in UTC
    assert is_within_trading_window(
        datetime(2026, 11, 23, 23, 30, tzinfo=timezone.utc),
        start_hour=22,
        end_hour=6,
        tz_offset_hours=0,
    )[0] is True
    assert is_within_trading_window(
        datetime(2026, 11, 23, 12, 0, tzinfo=timezone.utc),
        start_hour=22,
        end_hour=6,
        tz_offset_hours=0,
    )[0] is False

    # Naive datetime is treated as UTC without raising
    ok_naive, _ = is_within_trading_window(
        datetime(2026, 11, 23, 15, 0),  # 09:00 UTC-6
        start_hour=8,
        end_hour=23,
        tz_offset_hours=-6,
    )
    assert ok_naive is True


# ---------------------------------------------------------------------------
# 4. MT5Bot Integration in SUPERVISED_M15_SCALPER Mode
# ---------------------------------------------------------------------------


def test_bot_supervised_mode_blocks_entries_outside_window_but_manages_positions_24_7(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    snap = _make_snapshot(symbol="GBPUSDm", bid=1.27200, ask=1.27210, atr_15_price=0.0010)
    # Open winning BUY position at +2.0 ATR profit -> should trigger BE/Trailing even at 02:00 local
    open_pos = SimpleNamespace(
        ticket=55501,
        identifier=55501,
        symbol="GBPUSDm",
        type=mt5_bot_mod.mt5.POSITION_TYPE_BUY,
        volume=0.02,
        price_open=1.27000,
        price_current=1.27200,
        sl=1.26800,
        tp=1.27400,
        profit=4.0,
        magic=MT5_MAGIC_NUMBER,
        comment="GeminiBot_SUPM15_BUY",
    )
    ready_sig = StrategySignal(
        symbol="GBPUSDm",
        strategy_name=STRATEGY_MODE_SUPERVISED_M15,
        direction="BUY",
        score=84.0,
        entry_price=1.27210,
        sl_price=1.27020,
        tp_price=1.27610,
        rr_ratio=2.1,
        regime=REGIME_TREND_UP,
        setup_stage="READY",
        forming_hint="",
        invalidation_level=1.27020,
        metadata={"entry_pillar": "M15_SCALPER_PULLBACK_LONG"},
    )

    bot, placed_orders, sl_mods = _build_mocked_supervised_bot(
        tmp_path,
        monkeypatch,
        snapshot=snap,
        raw_positions=(open_pos,),
        ready_signal=ready_sig,
    )
    # Also test a second symbol candidate (not open) to prove entry gate blocks new symbols too
    snap_eth = _make_snapshot(symbol="ETHUSDm", bid=3200.0, ask=3201.0, digits=2, point=0.01, atr_15_price=12.0)
    monkeypatch.setattr(bot, "build_snapshots", lambda free_margin_usd, open_symbols: [snap, snap_eth])

    # 02:00 local (UTC-6) == 08:00 UTC -> OUTSIDE 08:00-23:00
    outside_utc = datetime(2026, 11, 23, 8, 0, tzinfo=timezone.utc)
    res = bot.run_cycle(cycle_num=1, now_utc=outside_utc)

    assert res["strategy_mode"] == STRATEGY_MODE_SUPERVISED_M15
    assert res["trading_window_open"] is False
    assert res["new_entries_blocked_reason"] == "OUTSIDE_TRADING_WINDOW"
    assert len(placed_orders) == 0

    # Open position management (BE/Trailing) MUST still have executed 24/7!
    assert len(sl_mods) >= 1
    assert sl_mods[0]["ticket"] == 55501
    assert sl_mods[0]["new_sl"] > open_pos.price_open

    report_text = (tmp_path / "mt5_latest_report.md").read_text(encoding="utf-8")
    assert "PAUSADA FUERA DE HORARIO" in report_text


def test_bot_supervised_mode_allows_entries_inside_window_with_profile_metadata(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    snap = _make_snapshot(symbol="GBPUSDm", bid=1.27000, ask=1.27012, atr_15_price=0.0008)
    ready_sig = StrategySignal(
        symbol="GBPUSDm",
        strategy_name=STRATEGY_MODE_SUPERVISED_M15,
        direction="BUY",
        score=85.0,
        entry_price=1.27012,
        sl_price=1.26850,
        tp_price=1.27350,
        rr_ratio=2.1,
        regime=REGIME_TREND_UP,
        setup_stage="READY",
        forming_hint="",
        invalidation_level=1.26850,
        metadata={"entry_pillar": "M15_SCALPER_PULLBACK_LONG"},
    )

    bot, placed_orders, _ = _build_mocked_supervised_bot(
        tmp_path,
        monkeypatch,
        snapshot=snap,
        raw_positions=(),
        ready_signal=ready_sig,
    )

    # 10:30 local (UTC-6) == 16:30 UTC -> INSIDE 08:00-23:00
    inside_utc = datetime(2026, 11, 23, 16, 30, tzinfo=timezone.utc)
    res = bot.run_cycle(cycle_num=2, now_utc=inside_utc)

    assert res["strategy_mode"] == STRATEGY_MODE_SUPERVISED_M15
    assert res["trading_window_open"] is True
    assert res["new_entries_blocked_reason"] is None
    assert res["ready_signals"] == 1
    assert len(placed_orders) == 1

    order = placed_orders[0]
    assert order["symbol"] == "GBPUSDm"
    assert order["side"] == "BUY"
    assert order["magic"] == MT5_MAGIC_NUMBER
    assert order["sl"] < order["price"] < order["tp"]
    assert "SUPERVISED_M15" in order["reason"]

    # Position metadata persists per-symbol BE/Trailing profile parameters
    profile = get_scalper_profile("GBPUSDm")
    meta = bot.position_meta[order["ticket"]]
    assert meta["is_supervised_m15"] is True
    assert meta["profile_tier"] == profile.tier
    assert meta["be_lock_atr"] == pytest.approx(profile.be_lock_atr)
    assert meta["trailing_lock_pct"] == pytest.approx(profile.trailing_lock_pct)
    assert meta["risk_multiplier"] == pytest.approx(profile.risk_multiplier)

    report_text = (tmp_path / "mt5_latest_report.md").read_text(encoding="utf-8")
    assert "ACTIVA 08:00-23:00" in report_text
