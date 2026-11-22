from __future__ import annotations

import json
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
from src.mt5_adaptive_scheduler import AdaptiveWakeScheduler, WakePlan, WatchTarget, ensure_utc, utc_iso
from src.mt5_ai_brain import (
    AdaptiveCycleDecision,
    MT5AdaptiveAIBrain,
    SymbolAdaptiveDecision,
    estimate_gemini_quota_usage,
    extract_json_object,
)
from src.mt5_backtester import (
    MT5Backtester,
    SimulatedTrade,
    compute_performance_metrics,
    export_strategy_priors,
    generate_synthetic_regime_bars,
)
from src.mt5_bot import ExnessMT5AutonomousBot, MT5_MAGIC_NUMBER, MT5SymbolSnapshot
from src.mt5_knowledge_db import MT5KnowledgeDB
from src.mt5_strategies import (
    ALL_REGIMES,
    DEFAULT_STRATEGIES,
    MT5StrategyEngine,
    MarketRegimeClassifier,
    REGIME_HIGH_VOL_CHOP,
    REGIME_RANGE,
    REGIME_TREND_DOWN,
    REGIME_TREND_UP,
    SESSION_ASIA,
    SESSION_LONDON,
    SESSION_NEW_YORK,
    SESSION_NY_OVERLAP,
    SESSION_ROLLOVER,
    StrategySignal,
    classify_session,
    compute_indicators,
)


# ---------------------------------------------------------------------------
# Helpers for deterministic synthetic candles & mocked MT5 objects
# ---------------------------------------------------------------------------


def _make_trend_candles(
    n: int = 260,
    start_price: float = 1.1000,
    step: float = 0.0005,
    noise_amp: float = 0.0003,
    timeframe_sec: int = 3600,
) -> list[dict[str, float]]:
    base_ts = datetime(2025, 1, 2, 8, 0, tzinfo=timezone.utc).timestamp()
    candles: list[dict[str, float]] = []
    px = start_price
    for i in range(n):
        wave = np.sin(i / 4.0) * noise_amp
        o = px
        c = max(0.001, o + step + wave * 0.25)
        h = max(o, c) + abs(step) * 0.6 + noise_amp * 0.4
        l = min(o, c) - abs(step) * 0.6 - noise_amp * 0.4
        candles.append(
            {
                "time": base_ts + i * timeframe_sec,
                "open": round(o, 5),
                "high": round(h, 5),
                "low": round(l, 5),
                "close": round(c, 5),
                "volume": 500.0 + (i % 10) * 50.0,
            }
        )
        px = c
    return candles


def _make_range_candles(
    n: int = 260,
    center: float = 1.1000,
    amp: float = 0.0020,
    timeframe_sec: int = 3600,
) -> list[dict[str, float]]:
    base_ts = datetime(2025, 1, 2, 8, 0, tzinfo=timezone.utc).timestamp()
    candles: list[dict[str, float]] = []
    prev = center
    for i in range(n):
        target = center + amp * np.sin(i * 0.45)
        o = prev
        c = float(target)
        h = max(o, c) + amp * 0.18
        l = min(o, c) - amp * 0.18
        candles.append(
            {
                "time": base_ts + i * timeframe_sec,
                "open": round(o, 5),
                "high": round(h, 5),
                "low": round(l, 5),
                "close": round(c, 5),
                "volume": 400.0,
            }
        )
        prev = c
    return candles


def _make_high_vol_chop_candles(n: int = 260, center: float = 1.1000) -> list[dict[str, float]]:
    candles = _make_range_candles(n=n - 15, center=center, amp=0.0008)
    last_ts = candles[-1]["time"]
    prev = candles[-1]["close"]
    for i in range(15):
        sign = 1.0 if i % 2 == 0 else -1.0
        o = prev
        c = center + sign * 0.0065
        h = max(o, c) + 0.0055
        l = min(o, c) - 0.0055
        candles.append(
            {
                "time": last_ts + (i + 1) * 3600,
                "open": round(o, 5),
                "high": round(h, 5),
                "low": round(l, 5),
                "close": round(c, 5),
                "volume": 2500.0,
            }
        )
        prev = c
    return candles


def _make_snapshot(
    symbol: str = "EURUSDm",
    bid: float = 1.10000,
    ask: float = 1.10010,
    spread_points: int = 10,
    digits: int = 5,
    point: float = 1e-5,
    atr_price: float = 0.0012,
    strategy_setup: str = "LONG_ENTRY",
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
        margin_min_lot_usd=2.2,
        usd_per_1pct_move_min_lot=11.0,
        ema_200=bid - 0.0020,
        ema_50=bid - 0.0008,
        ema_21=bid - 0.0003,
        above_ema_200=True,
        dist_to_ema200_atr=1.6,
        ema200_slope_positive=True,
        stoch_k=24.0,
        stoch_d=20.0,
        stoch_recent_min=18.0,
        stoch_recent_max=42.0,
        stoch_turning_up=True,
        stoch_turning_down=False,
        rsi_14=46.0,
        bb_upper=bid + 0.0025,
        bb_lower=bid - 0.0025,
        bb_pct_b=0.35,
        macd_hist=0.00012,
        macd_improving=True,
        atr_price=atr_price,
        atr_pct=(atr_price / bid) * 100.0,
        candle_pattern="BULLISH_ENGULFING",
        prev_candle_low=bid - 0.0010,
        prev_candle_high=bid + 0.0006,
        entry_pillar="P1_EMA200_PULLBACK_LONG",
        strategy_setup=strategy_setup,
        structural_long_sl=bid - 0.0020,
        structural_short_sl=ask + 0.0020,
        htf_trend="BULLISH",
        adx_14=27.0,
        atr_15_price=0.0005,
        recent_h1_closes=[bid - 0.0004, bid - 0.0002, bid],
        swing_high_20=bid + 0.0030,
        swing_low_20=bid - 0.0025,
    )


# ---------------------------------------------------------------------------
# 1. Multi-Strategy Engine & MarketRegimeClassifier Tests
# ---------------------------------------------------------------------------


def test_session_classification_utc() -> None:
    assert classify_session(datetime(2026, 5, 1, 2, 0, tzinfo=timezone.utc)) == SESSION_ASIA
    assert classify_session(datetime(2026, 5, 1, 8, 30, tzinfo=timezone.utc)) == SESSION_LONDON
    assert classify_session(datetime(2026, 5, 1, 13, 15, tzinfo=timezone.utc)) == SESSION_NY_OVERLAP
    assert classify_session(datetime(2026, 5, 1, 18, 0, tzinfo=timezone.utc)) == SESSION_NEW_YORK
    assert classify_session(datetime(2026, 5, 1, 21, 0, tzinfo=timezone.utc)) == SESSION_ROLLOVER


def test_regime_classifier_all_four_regimes() -> None:
    classifier = MarketRegimeClassifier()

    up_snap = classifier.classify(_make_trend_candles(step=0.0007, noise_amp=0.00015))
    assert up_snap.regime == REGIME_TREND_UP
    assert up_snap.adx_14 >= 20.0
    assert up_snap.dist_ema200_atr > 0.0

    dn_snap = classifier.classify(_make_trend_candles(start_price=1.4000, step=-0.0007, noise_amp=0.00015))
    assert dn_snap.regime == REGIME_TREND_DOWN
    assert dn_snap.adx_14 >= 20.0
    assert dn_snap.dist_ema200_atr < 0.0

    rng_snap = classifier.classify(_make_range_candles(amp=0.0018))
    assert rng_snap.regime == REGIME_RANGE

    chop_snap = classifier.classify(_make_high_vol_chop_candles())
    assert chop_snap.regime == REGIME_HIGH_VOL_CHOP
    assert chop_snap.atr_percentile >= 88.0


def test_multi_strategy_engine_ready_and_forming_signals() -> None:
    engine = MT5StrategyEngine()
    assert len(engine.strategies) >= 5
    assert set(engine.strategy_names) == {s.name for s in DEFAULT_STRATEGIES}

    # Scan synthetic multi-regime bars to verify both READY and FORMING setups fire with valid fields
    candles, meta = generate_synthetic_regime_bars("EURUSDm", timeframe_str="H1", years=0.6, seed=7)
    ind = compute_indicators(candles)
    ready_count = 0
    forming_count = 0
    seen_regimes: set[str] = set()
    seen_strategies: set[str] = set()

    for idx in range(210, ind.n, 2):
        regime_snap, signals = engine.evaluate_at_index(
            "EURUSDm", ind, idx, digits=meta["digits"], point=meta["point"]
        )
        seen_regimes.add(regime_snap.regime)
        for sig in signals:
            seen_strategies.add(sig.strategy_name)
            assert sig.direction in ("BUY", "SELL")
            assert 0.0 <= sig.score <= 100.0
            assert sig.regime in ALL_REGIMES
            if sig.setup_stage == "READY":
                ready_count += 1
                assert sig.rr_ratio > 0.0
                if sig.direction == "BUY":
                    assert sig.sl_price < sig.entry_price < sig.tp_price
                else:
                    assert sig.tp_price < sig.entry_price < sig.sl_price
            elif sig.setup_stage == "FORMING":
                forming_count += 1
                assert sig.forming_hint != ""
                assert sig.invalidation_level > 0.0

    assert ready_count > 0
    assert forming_count > 0
    assert len(seen_regimes) >= 3
    assert len(seen_strategies) >= 4

    # select_best_signal must prioritize READY over FORMING regardless of score
    s_form = StrategySignal(
        symbol="EURUSDm",
        strategy_name="s_form",
        direction="BUY",
        score=85.0,
        entry_price=1.10,
        sl_price=1.09,
        tp_price=1.12,
        rr_ratio=2.0,
        regime=REGIME_TREND_UP,
        setup_stage="FORMING",
        forming_hint="waiting",
        invalidation_level=1.09,
    )
    s_ready = StrategySignal(
        symbol="EURUSDm",
        strategy_name="s_ready",
        direction="BUY",
        score=70.0,
        entry_price=1.10,
        sl_price=1.09,
        tp_price=1.12,
        rr_ratio=2.0,
        regime=REGIME_TREND_UP,
        setup_stage="READY",
        forming_hint="",
        invalidation_level=1.09,
    )
    best = MT5StrategyEngine.select_best_signal([s_form, s_ready])
    assert best is not None
    assert best.strategy_name == "s_ready"


# ---------------------------------------------------------------------------
# 2. 2-Year Backtester, IS/OOS Split & Priors Export -> DB Compatibility
# ---------------------------------------------------------------------------


def test_backtester_metrics_and_is_oos_split_and_db_export(tmp_path: Path) -> None:
    # Deterministic metrics check
    sample_trades = [
        SimulatedTrade("EURUSDm", "s1", "BUY", REGIME_TREND_UP, SESSION_LONDON, "IS", 1, 2, 1.1, 1.12, 1.09, 1.12, 2.0, 2.0, "TP", 75.0, 5, 0.05),
        SimulatedTrade("EURUSDm", "s1", "BUY", REGIME_TREND_UP, SESSION_LONDON, "IS", 3, 4, 1.1, 1.09, 1.09, 1.12, 2.0, -1.0, "SL", 72.0, 3, 0.05),
        SimulatedTrade("EURUSDm", "s1", "BUY", REGIME_TREND_UP, SESSION_LONDON, "OOS", 5, 6, 1.1, 1.12, 1.09, 1.12, 2.0, 2.0, "TP", 78.0, 6, 0.05),
    ]
    metrics = compute_performance_metrics(sample_trades, risk_pct_per_trade=1.0)
    assert metrics.trades_count == 3
    assert metrics.wins == 2
    assert metrics.losses == 1
    assert metrics.win_rate == pytest.approx(66.67, abs=0.05)
    assert metrics.profit_factor == pytest.approx(4.0, abs=0.01)
    assert metrics.expectancy_r == pytest.approx(1.0, abs=0.01)
    assert metrics.max_dd_pct > 0.0

    # End-to-end synthetic backtest with IS/OOS split + cadence comparison + export_strategy_priors -> MT5KnowledgeDB
    bt = MT5Backtester(cache_dir=tmp_path / "cache")
    study = bt.run_2yr_study(
        symbols=["EURUSDm", "XAUUSDm"],
        timeframe_str="H1",
        years=0.5,
        use_cache=False,
        force_synthetic=True,
    )
    assert study["data_source"] == "SYNTHETIC_BENCHMARK"
    assert study["overall"]["all"]["trades_count"] > 0
    assert study["overall"]["is"]["trades_count"] > 0
    assert study["overall"]["oos"]["trades_count"] > 0
    assert study["overall"]["is"]["trades_count"] + study["overall"]["oos"]["trades_count"] == study["overall"]["all"]["trades_count"]
    assert len(study["priors"]) > 0

    cadence = bt.compare_evaluation_cadence(
        symbols=["EURUSDm"],
        years=0.25,
        use_cache=False,
        force_synthetic=True,
    )
    assert set(cadence["modes"].keys()) == {"15m_base", "30m_base", "30m_plus_sniper"}
    assert cadence["modes"]["30m_base"]["est_ai_calls_per_day"] < cadence["modes"]["15m_base"]["est_ai_calls_per_day"]
    assert cadence["recommended_cadence"]

    out_json = tmp_path / "priors.json"
    exported = export_strategy_priors(study, output_path=out_json, cadence_comparison=cadence)
    assert out_json.exists()
    loaded_json = json.loads(out_json.read_text(encoding="utf-8"))
    assert len(loaded_json["priors"]) == len(exported["priors"])

    # Verify direct ingestion into MT5KnowledgeDB with rate normalization (0..100 -> 0..1)
    with MT5KnowledgeDB(tmp_path / "learning.db") as db:
        count = db.upsert_strategy_priors(exported["priors"])
        assert count == len(exported["priors"])
        stored = db.get_strategy_priors(symbol="EURUSDm")
        assert len(stored) > 0
        for row in stored:
            assert 0.0 <= row["win_rate"] <= 1.0


# ---------------------------------------------------------------------------
# 3. SQLite MT5KnowledgeDB Persistence, Bayesian Shrinkage & Memory Context
# ---------------------------------------------------------------------------


def test_knowledge_db_persistence_bayesian_blending_and_memory(tmp_path: Path) -> None:
    db_file = tmp_path / "mt5_learning.db"
    db = MT5KnowledgeDB(db_path=db_file, prior_strength=15.0)
    try:
        # Verify WAL mode & foreign keys enabled
        journal_mode = db._conn.execute("PRAGMA journal_mode;").fetchone()[0]
        fk_enabled = db._conn.execute("PRAGMA foreign_keys;").fetchone()[0]
        assert str(journal_mode).lower() == "wal"
        assert int(fk_enabled) == 1

        # Seed prior (60% win rate in 0..100 format -> normalized to 0.60)
        db.upsert_strategy_priors(
            [
                {
                    "symbol": "XAUUSDm",
                    "strategy_name": "trend_pullback_ema_stoch",
                    "regime": REGIME_TREND_UP,
                    "session": "ALL",
                    "trades_count": 50,
                    "wins": 30,
                    "losses": 20,
                    "win_rate": 60.0,
                    "profit_factor": 1.80,
                    "expectancy_r": 0.45,
                    "avg_rr": 2.1,
                    "max_dd_pct": 8.5,
                    "is_oos_consistent": True,
                    "enabled": True,
                }
            ]
        )

        # 0 live trades -> blended == prior
        b0 = db.get_blended_strategy_stats("XAUUSDm", regime=REGIME_TREND_UP, session=SESSION_LONDON)
        assert len(b0) == 1
        assert b0[0]["live_trades"] == 0
        assert b0[0]["live_weight"] == 0.0
        assert b0[0]["blended_win_rate"] == pytest.approx(0.60, abs=1e-4)
        assert b0[0]["edge_status"] == "STRONG"
        assert b0[0]["prior_matched_regime"] == REGIME_TREND_UP
        assert b0[0]["prior_matched_session"] == "ALL"

        # 1 live losing trade -> Bayesian shrinkage keeps estimate anchored near prior (not 0%)
        db.record_trade_outcome(
            ticket=9001,
            symbol="XAUUSDm",
            direction="BUY",
            strategy_name="trend_pullback_ema_stoch",
            regime=REGIME_TREND_UP,
            session=SESSION_LONDON,
            profit_usd=-10.0,
            r_multiple=-1.0,
            close_reason="SL",
            ai_lesson="Avoid chasing Gold pullback when spread spikes.",
        )
        # Re-recording same ticket must be idempotent
        db.record_trade_outcome(
            ticket=9001,
            symbol="XAUUSDm",
            direction="BUY",
            strategy_name="trend_pullback_ema_stoch",
            regime=REGIME_TREND_UP,
            session=SESSION_LONDON,
            profit_usd=-10.0,
            r_multiple=-1.0,
            close_reason="SL",
            ai_lesson="Avoid chasing Gold pullback when spread spikes.",
        )
        b1 = db.get_blended_strategy_stats("XAUUSDm", regime=REGIME_TREND_UP, session=SESSION_LONDON)[0]
        assert b1["live_trades"] == 1
        assert b1["live_weight"] == pytest.approx(1.0 / 16.0, abs=1e-3)
        assert 0.50 < b1["blended_win_rate"] < 0.60

        # Add 29 more winning live trades (30 total: 29W/1L) -> live stats dominate (> 66% weight)
        for i in range(29):
            db.record_trade_outcome(
                ticket=9100 + i,
                symbol="XAUUSDm",
                direction="BUY",
                strategy_name="trend_pullback_ema_stoch",
                regime=REGIME_TREND_UP,
                session=SESSION_LONDON,
                profit_usd=20.0,
                r_multiple=2.0,
                close_reason="TP",
            )
        b30 = db.get_blended_strategy_stats("XAUUSDm", regime=REGIME_TREND_UP, session=SESSION_LONDON)[0]
        assert b30["live_trades"] == 30
        assert b30["live_weight"] > 0.65
        assert b30["blended_win_rate"] > 0.80
        assert b30["blended_expectancy_r"] > 1.0

        # Watch lifecycle in DB: ACTIVE -> POSTPONED -> EXPIRED when exceeding max_postpones=2
        w = db.upsert_watch(
            watch_id="w_test_1",
            symbol="XAUUSDm",
            strategy_name="trend_pullback_ema_stoch",
            wake_at_utc="2026-11-21T18:10:00Z",
            hypothesis="Pullback to EMA21",
            trigger_condition="Bullish M15 close",
            invalidation_condition="Break below 2400",
            max_postpones=2,
        )
        assert w["status"] == "ACTIVE"
        w1 = db.update_watch_status("w_test_1", "POSTPONED", outcome_note="Still forming")
        assert w1 is not None and w1["status"] == "POSTPONED" and w1["postpone_count"] == 1
        w2 = db.update_watch_status("w_test_1", "POSTPONED", outcome_note="Waiting candle close")
        assert w2 is not None and w2["status"] == "POSTPONED" and w2["postpone_count"] == 2
        w3 = db.update_watch_status("w_test_1", "POSTPONED", outcome_note="Too late")
        assert w3 is not None and w3["status"] == "EXPIRED" and w3["postpone_count"] == 3
        assert db.get_active_watches("XAUUSDm") == []

        # Decision journal + compact AI memory retrieval
        db.record_decision(
            symbol="XAUUSDm",
            regime=REGIME_TREND_UP,
            session=SESSION_LONDON,
            action="WATCH_EXACT",
            strategy_name="trend_pullback_ema_stoch",
            confidence=72.0,
            setup_stage="FORMING",
            next_wake_utc="2026-11-21T18:15:00Z",
            reasoning="Near EMA21 support",
        )
        mem = db.build_ai_memory_context("XAUUSDm", regime=REGIME_TREND_UP, session=SESSION_LONDON)
        assert set(mem.keys()) >= {
            "strategy_stats",
            "recent_trades",
            "learned_lessons",
            "active_watches",
            "recent_decisions",
        }
        assert len(mem["strategy_stats"]) == 1
        assert len(mem["recent_trades"]) == 5
        assert len(mem["learned_lessons"]) >= 1
        assert len(mem["recent_decisions"]) == 1
        assert len(json.dumps(mem)) < 4000  # compact token budget
    finally:
        db.close()

    # Reopen from disk to confirm full persistence
    with MT5KnowledgeDB(db_path=db_file) as db2:
        summary = db2.get_learning_summary()
        assert summary["counts"]["strategy_priors"] == 1
        assert summary["counts"]["trade_outcomes"] == 30
        assert summary["counts"]["decision_journal"] == 1
        assert summary["watch_breakdown"]["EXPIRED"] == 1


# ---------------------------------------------------------------------------
# 4. AdaptiveWakeScheduler Full State Machine & Serialization Tests
# ---------------------------------------------------------------------------


def test_adaptive_wake_scheduler_state_machine_and_persistence() -> None:
    t0 = datetime(2026, 11, 21, 10, 5, 0, tzinfo=timezone.utc)

    # Clock-aligned 30m and 15m base patrol boundaries
    sched30 = AdaptiveWakeScheduler(base_interval_minutes=30, min_wake_seconds=60, default_max_postpones=3)
    assert sched30.next_base_cycle_utc(t0) == datetime(2026, 11, 21, 10, 30, 0, tzinfo=timezone.utc)
    assert sched30.next_base_cycle_utc(datetime(2026, 11, 21, 10, 30, 0, tzinfo=timezone.utc)) == datetime(
        2026, 11, 21, 11, 0, 0, tzinfo=timezone.utc
    )

    sched15 = AdaptiveWakeScheduler(base_interval_minutes=15, min_wake_seconds=60)
    assert sched15.next_base_cycle_utc(t0) == datetime(2026, 11, 21, 10, 15, 0, tzinfo=timezone.utc)

    # Idle -> BASE_PATROL
    plan_idle = sched30.next_wakeup_plan(now_utc=t0)
    assert plan_idle.mode == "BASE_PATROL"
    assert plan_idle.wake_at_utc == datetime(2026, 11, 21, 10, 30, 0, tzinfo=timezone.utc)
    assert plan_idle.sleep_seconds == pytest.approx(25 * 60, abs=0.1)

    # Register exact sniper watch in 7 minutes -> SNIPER_WATCH beats 30m base patrol
    w_eur = sched30.register_watch(
        symbol="EURUSDm",
        strategy_name="trend_pullback_ema_stoch",
        wake_in_minutes=7,
        hypothesis="Pullback to EMA21",
        now_utc=t0,
    )
    assert sched30.symbol_mode("EURUSDm") == "SNIPER_WATCH"
    assert w_eur.wake_at_utc == datetime(2026, 11, 21, 10, 12, 0, tzinfo=timezone.utc)

    # Coalescing: second watch within 10s is batched into the same SNIPER_WATCH wake
    sched30.register_watch(
        symbol="GBPUSDm",
        strategy_name="volatility_squeeze_breakout",
        wake_at_utc=datetime(2026, 11, 21, 10, 12, 10, tzinfo=timezone.utc),
        now_utc=t0,
    )
    plan_sniper = sched30.next_wakeup_plan(now_utc=t0)
    assert plan_sniper.mode == "SNIPER_WATCH"
    assert set(plan_sniper.due_symbols) == {"EURUSDm", "GBPUSDm"}
    assert plan_sniper.sleep_seconds == pytest.approx(7 * 60, abs=0.1)

    # Clamping bounds: too short -> min_wake_seconds; too long -> base_interval_minutes
    w_short = sched30.register_watch("USDJPYm", "s", wake_in_minutes=0.1, now_utc=t0)
    assert w_short.wake_at_utc == t0 + timedelta(seconds=60)
    w_long = sched30.register_watch("USDJPYm", "s", wake_in_minutes=90, now_utc=t0)
    assert w_long.wake_at_utc == t0 + timedelta(minutes=30)

    # Confirm trigger -> TRIGGERED & returns to BASE_PATROL
    t1 = datetime(2026, 11, 21, 10, 12, 0, tzinfo=timezone.utc)
    trig = sched30.confirm_trigger("EURUSDm", outcome_note="Entered BUY", now_utc=t1)
    assert trig is not None and trig.status == "TRIGGERED"
    assert sched30.symbol_mode("EURUSDm") == "BASE_PATROL"

    # Postpone lifecycle up to max_postpones=3 -> 1st POSTPONED, 2nd POSTPONED, 3rd auto-INVALIDATED -> BASE_PATROL
    p1 = sched30.postpone_watch("GBPUSDm", wake_in_minutes=5, note="Wait 1", now_utc=t1)
    assert p1 is not None and p1.status == "POSTPONED" and p1.postpone_count == 1
    p2 = sched30.postpone_watch("GBPUSDm", wake_in_minutes=5, note="Wait 2", now_utc=t1 + timedelta(minutes=5))
    assert p2 is not None and p2.status == "POSTPONED" and p2.postpone_count == 2
    p3 = sched30.postpone_watch("GBPUSDm", wake_in_minutes=5, note="Wait 3", now_utc=t1 + timedelta(minutes=10))
    assert p3 is not None and p3.status == "INVALIDATED" and p3.postpone_count == 3
    assert sched30.symbol_mode("GBPUSDm") == "BASE_PATROL"

    # Explicit invalidate_watch -> INVALIDATED & returns to BASE_PATROL
    inv = sched30.invalidate_watch("USDJPYm", reason="Support broken", now_utc=t1)
    assert inv is not None and inv.status == "INVALIDATED"
    assert sched30.symbol_mode("USDJPYm") == "BASE_PATROL"

    # After all watches resolved, global loop returns cleanly to BASE_PATROL
    plan_after = sched30.next_wakeup_plan(now_utc=t1)
    assert plan_after.mode == "BASE_PATROL"

    # TTL expiration via prune_expired
    sched30.register_watch(
        "XAUUSDm",
        "s",
        wake_in_minutes=5,
        expires_at_utc=t1 + timedelta(minutes=10),
        now_utc=t1,
    )
    expired = sched30.prune_expired(now_utc=t1 + timedelta(minutes=15))
    assert len(expired) == 1 and expired[0].status == "EXPIRED"
    assert sched30.symbol_mode("XAUUSDm") == "BASE_PATROL"

    # VPS restart serialization round-trip (to_dict / from_dict) & sync_from_db_watches
    sched30.register_watch("BTCUSDm", "momentum_adx_continuation", wake_in_minutes=6, now_utc=t1)
    snap_dict = sched30.to_dict()
    restored = AdaptiveWakeScheduler.from_dict(snap_dict)
    assert restored.has_active_watch("BTCUSDm")
    assert restored.base_interval_minutes == 30
    assert len(restored.recent_history()) == len(sched30.recent_history())

    # Sync from MT5KnowledgeDB rows
    with MT5KnowledgeDB(":memory:") as db:
        db.upsert_watch(
            watch_id="w_db_sync",
            symbol="ETHUSDm",
            strategy_name="volatility_squeeze_breakout",
            wake_at_utc=utc_iso(t1 + timedelta(minutes=8)) or "",
            hypothesis="Squeeze breakout forming",
            status="ACTIVE",
        )
        fresh_sched = AdaptiveWakeScheduler(base_interval_minutes=30)
        loaded = fresh_sched.sync_from_db_watches(db.get_active_watches(), now_utc=t1)
        assert loaded == 1
        assert fresh_sched.has_active_watch("ETHUSDm")


# ---------------------------------------------------------------------------
# 5. MT5AdaptiveAIBrain JSON Parsing, 429 Fallback, Offline Fallback & Post-Mortem
# ---------------------------------------------------------------------------


def test_extract_json_object_variants() -> None:
    assert extract_json_object('{"a": 1}') == {"a": 1}
    assert extract_json_object('```json\n{"market_summary": "ok", "decisions": []}\n```')["market_summary"] == "ok"
    assert extract_json_object('Analisis:\n{"market_summary": "con prosa", "decisions": [],}\nGracias.')["market_summary"] == "con prosa"
    with pytest.raises(ValueError):
        extract_json_object("no json here")


def test_ai_brain_429_fallback_chain_and_response_guardrails(monkeypatch: pytest.MonkeyPatch) -> None:
    brain = MT5AdaptiveAIBrain(
        api_key="test-key",
        model="gemini-primary",
        high_priority_models=("gemini-primary", "gemini-secondary"),
        max_retries=0,
    )
    called_urls: list[str] = []

    class FakeResp:
        def __init__(self, status_code: int, body: dict[str, Any] | None = None, text: str = "", headers: dict[str, str] | None = None) -> None:
            self.status_code = status_code
            self._body = body or {}
            self.text = text
            self.headers = headers or {}

        def json(self) -> dict[str, Any]:
            return self._body

    def fake_post(url: str, **kwargs: Any) -> FakeResp:
        called_urls.append(url)
        if "gemini-primary" in url:
            return FakeResp(429, text="RESOURCE_EXHAUSTED", headers={"Retry-After": "120"})
        payload_json = json.dumps(
            {
                "market_summary": "EURUSDm formando pullback, GBPUSDm sin watch previo.",
                "decisions": [
                    {
                        "symbol": "eurusdm",
                        "action": "WATCH_EXACT",
                        "strategy_name": "trend_pullback_ema_stoch",
                        "confidence_pct": 72,
                        "wake_in_minutes": 6,
                        "watch_hypothesis": "Pullback a EMA21",
                        "trigger_condition": "Cierre alcista M15",
                        "invalidation_condition": "Bajo 1.0950",
                        "reasoning": "Esperando confirmacion",
                    },
                    {
                        # Guardrail test: POSTPONE_WATCH without an active watch -> normalized to WATCH_EXACT
                        "symbol": "GBPUSDm",
                        "action": "POSTPONE_WATCH",
                        "strategy_name": "volatility_squeeze_breakout",
                        "confidence_pct": 65,
                        "wake_in_minutes": 9,
                        "reasoning": "Aun comprimido",
                    },
                ],
            }
        )
        return FakeResp(200, body={"candidates": [{"content": {"parts": [{"text": payload_json}]}}]})

    monkeypatch.setattr("src.mt5_ai_brain.requests.post", fake_post)

    now = datetime(2026, 11, 21, 12, 0, 0, tzinfo=timezone.utc)
    res = brain.evaluate_market_cycle(
        market_context={"session": "NY_OVERLAP"},
        strategy_signals=[
            {"symbol": "EURUSDm", "strategy_name": "trend_pullback_ema_stoch", "direction": "BUY", "score": 55, "setup_stage": "FORMING"},
            {"symbol": "GBPUSDm", "strategy_name": "volatility_squeeze_breakout", "direction": "BUY", "score": 54, "setup_stage": "FORMING"},
        ],
        memory_context={},
        active_watches=[],
        open_positions=[],
        cycle_mode="BASE_PATROL",
        now_utc=now,
    )

    assert len(called_urls) == 2
    assert brain.calls_429 == 1
    assert res.fallback_used is False
    assert res.model_used == "gemini-secondary"
    # Canonical symbol casing preserved ("eurusdm" -> "EURUSDm")
    assert "EURUSDm" in res.decisions
    assert res.decisions["EURUSDm"].action == "WATCH_EXACT"
    assert res.decisions["EURUSDm"].wake_in_minutes == 6.0
    assert res.decisions["EURUSDm"].wake_at_utc == "2026-11-21T12:06:00Z"
    # Guardrail converted POSTPONE_WATCH (without active watch) -> WATCH_EXACT
    assert res.decisions["GBPUSDm"].action == "WATCH_EXACT"

    # Cooldown telemetry records primary model
    telem = brain.get_quota_telemetry()
    assert "gemini-primary" in telem["active_model_cooldowns_sec"]


def test_ai_brain_deterministic_fallback_and_post_mortem() -> None:
    brain = MT5AdaptiveAIBrain(api_key="")
    now = datetime(2026, 11, 21, 12, 0, 0, tzinfo=timezone.utc)

    res = brain.evaluate_market_cycle(
        market_context={},
        strategy_signals=[
            {"symbol": "EURUSDm", "strategy_name": "trend_pullback_ema_stoch", "direction": "BUY", "score": 78, "setup_stage": "READY"},
            {"symbol": "XAUUSDm", "strategy_name": "volatility_squeeze_breakout", "direction": "SELL", "score": 56, "setup_stage": "FORMING", "forming_hint": "Coiled near lower BB", "invalidation_level": 2460.0},
            {"symbol": "USDJPYm", "strategy_name": "mean_reversion_bb_rsi", "direction": "BUY", "score": 55, "setup_stage": "FORMING"},
        ],
        memory_context={},
        active_watches=[
            {"symbol": "USDJPYm", "strategy_name": "mean_reversion_bb_rsi", "postpone_count": 2, "max_postpones": 3},
        ],
        open_positions=[],
        now_utc=now,
    )

    assert res.fallback_used is True
    assert res.model_used == "quant_local"
    assert res.decisions["EURUSDm"].action == "ENTER_BUY"
    assert res.decisions["XAUUSDm"].action == "WATCH_EXACT"
    assert res.decisions["XAUUSDm"].wake_at_utc is not None
    # USDJPYm had postpone_count=2 with max_postpones=3 -> deterministic fallback invalidates
    assert res.decisions["USDJPYm"].action == "INVALIDATE_WATCH"

    lesson = brain.generate_post_mortem_lesson(
        {
            "symbol": "XAUUSDm",
            "strategy_name": "trend_pullback_ema_stoch",
            "direction": "BUY",
            "regime": "TREND_UP",
            "session": "LONDON",
            "profit_usd": 18.5,
            "r_multiple": 1.85,
            "close_reason": "TP",
        }
    )
    assert "XAUUSDm" in lesson
    assert "trend_pullback_ema_stoch" in lesson
    assert len(lesson) <= 240

    q30 = estimate_gemini_quota_usage(base_interval_minutes=30)
    q15 = estimate_gemini_quota_usage(base_interval_minutes=15)
    assert q30["estimated_rpd"] < q15["estimated_rpd"]
    assert q30["fits_flash_free_tier"] is True


# ---------------------------------------------------------------------------
# 6. End-to-End ExnessMT5AutonomousBot Adaptive Cycle & Guardrail Enforcement
# ---------------------------------------------------------------------------


def _build_mocked_adaptive_bot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    snapshot: MT5SymbolSnapshot | None = None,
    candles: list[dict[str, float]] | None = None,
) -> tuple[ExnessMT5AutonomousBot, list[dict[str, Any]]]:
    snap = snapshot or _make_snapshot()
    bar_series = candles or _make_trend_candles(n=260, step=0.0005)
    placed_orders: list[dict[str, Any]] = []

    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "report.md",
        history_file=tmp_path / "history.json",
        ai_state_file=tmp_path / "ai_state.json",
        adaptive_ai=True,
        base_interval_minutes=30,
        learning_db_path=tmp_path / "learning.db",
    )

    fake_acc = SimpleNamespace(
        login=123456,
        server="Exness-MT5Real",
        leverage=500,
        balance=500.0,
        equity=500.0,
        margin_free=450.0,
    )
    monkeypatch.setattr(mt5_bot_mod.mt5, "positions_get", lambda: ())
    monkeypatch.setattr(mt5_bot_mod.mt5, "account_info", lambda: fake_acc)
    monkeypatch.setattr(mt5_bot_mod.mt5, "history_deals_get", lambda d1, d2: [])
    monkeypatch.setattr(bot, "ensure_connected", lambda: (SimpleNamespace(connected=True), fake_acc))
    monkeypatch.setattr(bot, "build_snapshots", lambda free_margin_usd, open_symbols: [snap])
    monkeypatch.setattr(bot, "_fetch_candles", lambda symbol, tf, count=300: bar_series)
    monkeypatch.setattr(
        bot,
        "_evaluate_daily_risk_guard",
        lambda **kwargs: {
            "utc_date": "2026-11-21",
            "protection_mode": "NORMAL",
            "daily_closed_pnl_usd": 0.0,
            "consecutive_losses": 0,
            "mins_since_last_loss": 999.0,
            "pause_new_entries": False,
            "hard_daily_loss_stop": False,
            "pause_remaining_mins": 0.0,
            "min_ai_prob": 60,
            "risk_scale": 1.0,
            "max_positions": 3,
            "reason": "OK",
        },
    )
    monkeypatch.setattr(bot, "_passes_deterministic_shields", lambda **kwargs: (True, "OK"))
    monkeypatch.setattr(
        bot,
        "calculate_safe_lot_and_sl",
        lambda **kwargs: (0.02, round(snap.bid - 0.0020, snap.digits), round(snap.ask + 0.0044, snap.digits), 4.0),
    )

    def fake_place_order(
        snap: MT5SymbolSnapshot,
        side: str,
        lot: float,
        sl_price: float,
        tp_price: float,
        reason: str,
        risk_usd: float,
    ) -> dict[str, Any]:
        order = {
            "ticket": 77001 + len(placed_orders),
            "symbol": snap.symbol,
            "side": side,
            "lot": lot,
            "price": snap.ask if side == "BUY" else snap.bid,
            "sl": sl_price,
            "tp": tp_price,
            "risk_usd": risk_usd,
            "magic": MT5_MAGIC_NUMBER,
            "reason": reason,
        }
        placed_orders.append(order)
        bot.last_order_timestamp = time.time()
        return order

    monkeypatch.setattr(bot, "_place_mt5_order", fake_place_order)
    return bot, placed_orders


def test_bot_adaptive_cycle_watch_to_sniper_entry_and_postmortem(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    bot, placed_orders = _build_mocked_adaptive_bot(tmp_path, monkeypatch)
    assert bot.knowledge_db is not None
    assert bot.wake_scheduler is not None
    assert bot.adaptive_brain is not None

    # Cycle 1 (BASE_PATROL): AI returns WATCH_EXACT -> persisted in SQLite & scheduler plans SNIPER_WATCH
    def brain_watch(**kwargs: Any) -> AdaptiveCycleDecision:
        now = ensure_utc(kwargs.get("now_utc"))
        return AdaptiveCycleDecision(
            market_summary="EURUSDm formando pullback",
            decisions={
                "EURUSDm": SymbolAdaptiveDecision(
                    symbol="EURUSDm",
                    action="WATCH_EXACT",
                    strategy_name="trend_pullback_ema_stoch",
                    confidence_pct=70,
                    wake_in_minutes=5.0,
                    wake_at_utc=utc_iso(now + timedelta(minutes=5)),
                    watch_hypothesis="Pullback EMA21",
                    trigger_condition="Cierre M15 alcista",
                    invalidation_condition="Bajo 1.0960",
                    reasoning="Esperando gatillo exacto",
                )
            },
            model_used="mock-gemini",
            priority_tier="ALTA_PRIORIDAD",
            cycle_mode=str(kwargs.get("cycle_mode", "BASE_PATROL")),
            timestamp_utc=utc_iso(now) or "",
        )

    monkeypatch.setattr(bot.adaptive_brain, "evaluate_market_cycle", brain_watch)
    s1 = bot.run_cycle(cycle_num=1)
    assert s1["adaptive_ai"] is True
    assert s1["cycle_mode"] == "BASE_PATROL"
    assert len(placed_orders) == 0
    assert bot.wake_scheduler.has_active_watch("EURUSDm")
    assert len(bot.knowledge_db.get_active_watches("EURUSDm")) == 1
    assert s1["next_wake_plan"]["mode"] == "SNIPER_WATCH"
    assert "EURUSDm" in s1["next_wake_plan"]["due_symbols"]

    # Cycle 2 (SNIPER_WATCH): AI confirms ENTER_BUY -> order placed, watch TRIGGERED, back to BASE_PATROL
    def brain_enter(**kwargs: Any) -> AdaptiveCycleDecision:
        now = ensure_utc(kwargs.get("now_utc"))
        return AdaptiveCycleDecision(
            market_summary="Gatillo confirmado en EURUSDm",
            decisions={
                "EURUSDm": SymbolAdaptiveDecision(
                    symbol="EURUSDm",
                    action="ENTER_BUY",
                    strategy_name="trend_pullback_ema_stoch",
                    confidence_pct=78,
                    reasoning="Vela alcista confirmada en sniper wake",
                )
            },
            model_used="mock-gemini",
            priority_tier="ALTA_PRIORIDAD",
            cycle_mode=str(kwargs.get("cycle_mode", "SNIPER_WATCH")),
            timestamp_utc=utc_iso(now) or "",
        )

    monkeypatch.setattr(bot.adaptive_brain, "evaluate_market_cycle", brain_enter)
    s2 = bot.run_cycle(cycle_num=2, cycle_mode="SNIPER_WATCH", due_symbols=["EURUSDm"])
    assert s2["cycle_mode"] == "SNIPER_WATCH"
    assert len(placed_orders) == 1
    assert placed_orders[0]["symbol"] == "EURUSDm"
    assert placed_orders[0]["magic"] == MT5_MAGIC_NUMBER
    assert not bot.wake_scheduler.has_active_watch("EURUSDm")
    assert bot.knowledge_db.get_active_watches("EURUSDm") == []
    assert s2["next_wake_plan"]["mode"] == "BASE_PATROL"
    assert 77001 in bot.position_meta

    # Cycle 3: Trade closes -> post-mortem lesson generated and persisted to SQLite
    monkeypatch.setattr(
        bot,
        "_collect_recent_closed_deals",
        lambda **kwargs: [
            {
                "ticket": 77001,
                "position_id": 77001,
                "symbol": "EURUSDm",
                "side": "BUY",
                "profit_usd": 8.4,
                "close_type": "POSITIVE",
                "closed_at_utc": "2026-11-21T13:00:00Z",
                "snapshot": {"bid": 1.1042},
            }
        ],
    )
    monkeypatch.setattr(
        bot.adaptive_brain,
        "evaluate_market_cycle",
        lambda **kwargs: AdaptiveCycleDecision("Idle", {}, "mock-gemini"),
    )
    s3 = bot.run_cycle(cycle_num=3)
    assert s3["recorded_outcomes"] == 1
    trades = bot.knowledge_db.get_recent_trades("EURUSDm")
    assert len(trades) == 1
    assert trades[0]["ticket"] == 77001
    assert trades[0]["strategy_name"] == "trend_pullback_ema_stoch"
    assert len(bot.knowledge_db.get_lessons("EURUSDm")) >= 1
    bot.knowledge_db.close()


def test_bot_adaptive_cycle_guardrails_block_unsafe_entries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    bot, placed_orders = _build_mocked_adaptive_bot(tmp_path, monkeypatch)
    assert bot.adaptive_brain is not None
    assert bot.knowledge_db is not None

    def make_enter_brain(confidence: int) -> Any:
        def _eval(**kwargs: Any) -> AdaptiveCycleDecision:
            return AdaptiveCycleDecision(
                market_summary="Entry candidate",
                decisions={
                    "EURUSDm": SymbolAdaptiveDecision(
                        symbol="EURUSDm",
                        action="ENTER_BUY",
                        strategy_name="trend_pullback_ema_stoch",
                        confidence_pct=confidence,
                        reasoning="Signal ready",
                    )
                },
                model_used="mock-gemini",
            )
        return _eval

    # 1. Low AI confidence (< min_ai_confidence=68) blocked
    monkeypatch.setattr(bot.adaptive_brain, "evaluate_market_cycle", make_enter_brain(55))
    bot.run_cycle(cycle_num=1)
    assert len(placed_orders) == 0

    # 2. Deterministic shields rejection (e.g., spread shield / correlation) blocks high-confidence ENTER_BUY
    monkeypatch.setattr(bot.adaptive_brain, "evaluate_market_cycle", make_enter_brain(85))
    monkeypatch.setattr(bot, "_passes_deterministic_shields", lambda **kwargs: (False, "SPREAD_TOO_HIGH"))
    bot.run_cycle(cycle_num=2)
    assert len(placed_orders) == 0

    # 3. Daily risk guard pause_new_entries=True blocks high-confidence ENTER_BUY
    monkeypatch.setattr(bot, "_passes_deterministic_shields", lambda **kwargs: (True, "OK"))
    monkeypatch.setattr(
        bot,
        "_evaluate_daily_risk_guard",
        lambda **kwargs: {
            "protection_mode": "HARD_STOP",
            "pause_new_entries": True,
            "min_ai_prob": 75,
            "risk_scale": 0.5,
            "max_positions": 1,
        },
    )
    bot.run_cycle(cycle_num=3)
    assert len(placed_orders) == 0

    # 4. 8-minute spacing shield blocks immediate second entry
    monkeypatch.setattr(
        bot,
        "_evaluate_daily_risk_guard",
        lambda **kwargs: {
            "protection_mode": "NORMAL",
            "pause_new_entries": False,
            "min_ai_prob": 60,
            "risk_scale": 1.0,
            "max_positions": 3,
        },
    )
    bot.last_order_timestamp = time.time() - 60.0  # 1 minute ago (< 8m)
    bot.run_cycle(cycle_num=4)
    assert len(placed_orders) == 0

    # 5. Once spacing elapsed and all shields pass, entry succeeds
    bot.last_order_timestamp = time.time() - 600.0
    bot.run_cycle(cycle_num=5)
    assert len(placed_orders) == 1
    bot.knowledge_db.close()


def test_bot_adaptive_cycle_postpone_and_invalidate_watch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    bot, placed_orders = _build_mocked_adaptive_bot(tmp_path, monkeypatch)
    assert bot.knowledge_db is not None
    assert bot.wake_scheduler is not None
    assert bot.adaptive_brain is not None

    # Register an active watch directly via Cycle 1 (WATCH_EXACT)
    def brain_watch(**kwargs: Any) -> AdaptiveCycleDecision:
        now = ensure_utc(kwargs.get("now_utc"))
        return AdaptiveCycleDecision(
            market_summary="Watch setup",
            decisions={
                "EURUSDm": SymbolAdaptiveDecision(
                    symbol="EURUSDm",
                    action="WATCH_EXACT",
                    strategy_name="trend_pullback_ema_stoch",
                    confidence_pct=65,
                    wake_in_minutes=5.0,
                    wake_at_utc=utc_iso(now + timedelta(minutes=5)),
                    watch_hypothesis="Pullback forming",
                    reasoning="Setup forming",
                )
            },
            model_used="mock-gemini",
        )

    monkeypatch.setattr(bot.adaptive_brain, "evaluate_market_cycle", brain_watch)
    bot.run_cycle(cycle_num=1)
    assert bot.wake_scheduler.has_active_watch("EURUSDm")

    # Cycle 2: POSTPONE_WATCH -> watch stays active with postpone_count=1 in both scheduler & DB
    def brain_postpone(**kwargs: Any) -> AdaptiveCycleDecision:
        now = ensure_utc(kwargs.get("now_utc"))
        return AdaptiveCycleDecision(
            market_summary="Still forming",
            decisions={
                "EURUSDm": SymbolAdaptiveDecision(
                    symbol="EURUSDm",
                    action="POSTPONE_WATCH",
                    strategy_name="trend_pullback_ema_stoch",
                    confidence_pct=62,
                    wake_in_minutes=6.0,
                    wake_at_utc=utc_iso(now + timedelta(minutes=6)),
                    reasoning="Need one more candle",
                )
            },
            model_used="mock-gemini",
        )

    monkeypatch.setattr(bot.adaptive_brain, "evaluate_market_cycle", brain_postpone)
    bot.run_cycle(cycle_num=2, cycle_mode="SNIPER_WATCH", due_symbols=["EURUSDm"])
    w = bot.wake_scheduler.get_watch("EURUSDm")
    assert w is not None and w.status == "POSTPONED" and w.postpone_count == 1
    db_w = bot.knowledge_db.get_watch(w.watch_id)
    assert db_w is not None and db_w["status"] == "POSTPONED" and db_w["postpone_count"] == 1

    # Cycle 3: INVALIDATE_WATCH -> watch invalidated, returns to BASE_PATROL, lesson recorded in SQLite
    def brain_invalidate(**kwargs: Any) -> AdaptiveCycleDecision:
        return AdaptiveCycleDecision(
            market_summary="Invalidated",
            decisions={
                "EURUSDm": SymbolAdaptiveDecision(
                    symbol="EURUSDm",
                    action="INVALIDATE_WATCH",
                    strategy_name="trend_pullback_ema_stoch",
                    confidence_pct=30,
                    reasoning="Support broken cleanly",
                    lesson_note="EURUSDm pullback failed when ADX dropped below 18.",
                )
            },
            model_used="mock-gemini",
        )

    monkeypatch.setattr(bot.adaptive_brain, "evaluate_market_cycle", brain_invalidate)
    s3 = bot.run_cycle(cycle_num=3, cycle_mode="SNIPER_WATCH", due_symbols=["EURUSDm"])
    assert len(placed_orders) == 0
    assert not bot.wake_scheduler.has_active_watch("EURUSDm")
    assert s3["next_wake_plan"]["mode"] == "BASE_PATROL"
    db_w_after = bot.knowledge_db.get_watch(w.watch_id)
    assert db_w_after is not None and db_w_after["status"] == "INVALIDATED"
    lessons = bot.knowledge_db.get_lessons("EURUSDm")
    assert any("ADX dropped below 18" in l["lesson_text"] for l in lessons)
    bot.knowledge_db.close()


def test_bot_seed_historical_priors_idempotent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("src.mt5_backtester.DEFAULT_MT5_SYMBOLS", ["EURUSDm"])
    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r.md",
        history_file=tmp_path / "h.json",
        ai_state_file=tmp_path / "a.json",
        adaptive_ai=True,
        learning_db_path=tmp_path / "seed.db",
    )
    res1 = bot.seed_historical_priors(years=0.4, timeframe_str="H1", only_if_empty=True, force_synthetic=True)
    assert res1["seeded"] is True
    assert res1["priors_count"] > 0

    res2 = bot.seed_historical_priors(years=0.4, timeframe_str="H1", only_if_empty=True, force_synthetic=True)
    assert res2["seeded"] is False
    assert res2["reason"] == "already_populated"
    assert bot.knowledge_db is not None
    bot.knowledge_db.close()
