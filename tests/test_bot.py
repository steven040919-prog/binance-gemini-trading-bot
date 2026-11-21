from __future__ import annotations

import json
import sys
import tempfile
import time
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
from typing import Any
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.binance_client import SymbolFilters
from src.bot_engine import AutonomousTradingBot, calculate_position_size_1pct_risk
from src.config import BotConfig
from src.gemini_agent import (
    AIAnalysisResult,
    AIDecision,
    GeminiTradingAgent,
    MT5AICycleEvaluation,
    MT5CandidateAIEval,
    MT5PositionAIReview,
    compute_mt5_quant_probability,
)
from src.mt5_bot import (
    ExnessMT5AutonomousBot,
    MT5_MAGIC_NUMBER,
    MT5SymbolSnapshot,
)
from src.market_scanner import (
    TechnicalSnapshot,
    calc_adx,
    calc_atr_wilder,
    calc_ema_series,
    calc_stochastic,
    detect_candle_pattern,
)
from src.state_manager import StateManager


class FakeBinanceClient:
    def __init__(self) -> None:
        self.prices = {
            "BTCUSDT": 90000.0,
            "ETHUSDT": 3200.0,
            "SOLUSDT": 210.0,
        }
        self.balances = {
            "USDT": 1000.0,
            "ETH": 0.1,  # 320 USDT
        }
        self.buys: list[tuple[str, float]] = []
        self.sells: list[tuple[str, float]] = []
        self.futures_usdt: float = 0.0
        self.futures_orders: list[tuple[str, str, float]] = []

    def get_all_prices(self) -> dict[str, float]:
        return dict(self.prices)

    def get_account_balances(self) -> dict[str, float]:
        return dict(self.balances)

    def get_futures_usdt_balance(self) -> float:
        return self.futures_usdt

    def place_futures_market_order(
        self,
        symbol: str,
        side: str,
        usdt_amount: float,
        leverage: int = 2,
        reduce_only: bool = False,
        quantity: float = 0.0,
        dry_run: bool = False,
    ) -> dict[str, Any]:
        price = self.prices[symbol]
        qty = quantity if (reduce_only and quantity > 0) else round(usdt_amount / price, 5)
        quote_qty = qty * price
        self.futures_orders.append((symbol, side, quote_qty))
        return {
            "symbol": symbol,
            "side": side,
            "executedQty": str(qty),
            "cummulativeQuoteQty": f"{quote_qty:.2f}",
            "avgPrice": price,
            "marketType": "FUTURES",
        }

    def place_market_buy_usdt(self, symbol: str, usdt_amount: float, dry_run: bool = False) -> dict[str, Any]:
        price = self.prices[symbol]
        qty = round(usdt_amount / price, 5)
        self.buys.append((symbol, usdt_amount))
        return {
            "symbol": symbol,
            "side": "BUY",
            "executedQty": str(qty),
            "cummulativeQuoteQty": f"{usdt_amount:.2f}",
            "avgPrice": price,
        }

    def place_market_sell_quantity(self, symbol: str, quantity: float, dry_run: bool = False) -> dict[str, Any]:
        price = self.prices[symbol]
        quote_qty = quantity * price
        self.sells.append((symbol, quantity))
        return {
            "symbol": symbol,
            "side": "SELL",
            "executedQty": str(quantity),
            "cummulativeQuoteQty": f"{quote_qty:.2f}",
            "avgPrice": price,
        }


class FakeScanner:
    def __init__(self) -> None:
        self.sol_stoch_k = 18.0
        self.sol_price = 210.0
        self.sol_prev_low = 205.8
        self.sol_pattern = "BULLISH_ENGULFING"
        self.eth_stoch_k = 45.0
        self.eth_pattern = "NONE"

    def is_eligible_symbol(self, symbol: str) -> bool:
        return symbol.endswith("USDT") and not symbol.startswith("USDC")

    def build_snapshots(self, must_include_symbols: list[str] | None = None) -> list[TechnicalSnapshot]:
        return [
            TechnicalSnapshot(
                symbol="SOLUSDT",
                current_price=self.sol_price,
                price_change_24h_pct=4.5,
                quote_volume_24h_usdt=450_000_000.0,
                high_24h=235.0,
                low_24h=195.0,
                ema_200=195.0,
                above_ema_200=True,
                stoch_k=self.sol_stoch_k,
                stoch_d=self.sol_stoch_k,
                stoch_recent_min=16.0,
                stoch_recent_max=self.sol_stoch_k,
                candle_pattern=self.sol_pattern,
                prev_candle_low=self.sol_prev_low,
                prev_candle_high=self.sol_price + 2.0,
                strategy_setup="LONG_ENTRY",
                rsi_14=52.0,
                ema_9=208.0,
                ema_21=204.0,
                ema_50=198.0,
                trend_primary="BULLISH",
                macd_line=1.5,
                macd_signal=1.1,
                macd_hist=0.4,
                bb_upper=230.0,
                bb_lower=196.0,
                bb_pct_b=0.5,
                atr_pct=2.0,
                volume_ratio=1.45,
                support_level=self.sol_prev_low,
                resistance_level=235.0,
                htf_rsi_14=55.0,
                htf_ema_21=202.0,
                htf_ema_50=194.0,
                htf_trend="BULLISH",
            ),
            TechnicalSnapshot(
                symbol="ETHUSDT",
                current_price=3200.0,
                price_change_24h_pct=2.1,
                quote_volume_24h_usdt=600_000_000.0,
                high_24h=3250.0,
                low_24h=3100.0,
                ema_200=3050.0,
                above_ema_200=True,
                stoch_k=self.eth_stoch_k,
                stoch_d=self.eth_stoch_k,
                stoch_recent_min=40.0,
                stoch_recent_max=self.eth_stoch_k,
                candle_pattern=self.eth_pattern,
                prev_candle_low=3120.0,
                prev_candle_high=3240.0,
                strategy_setup="WATCH",
                rsi_14=55.0,
                ema_9=3190.0,
                ema_21=3170.0,
                ema_50=3120.0,
                trend_primary="BULLISH",
                macd_line=5.0,
                macd_signal=4.0,
                macd_hist=1.0,
                bb_upper=3260.0,
                bb_lower=3100.0,
                bb_pct_b=0.6,
                atr_pct=1.5,
                volume_ratio=1.1,
                support_level=3120.0,
                resistance_level=3250.0,
                htf_rsi_14=58.0,
                htf_ema_21=3150.0,
                htf_ema_50=3080.0,
                htf_trend="BULLISH",
            ),
        ]


class FakeAIAgent:
    def __init__(self, decisions: list[AIDecision]) -> None:
        self.decisions = decisions

    def analyze_market(self, **kwargs: Any) -> AIAnalysisResult:
        return AIAnalysisResult(
            market_regime="BULLISH",
            summary="SOLUSDT en tendencia fuerte con gestion dinamica de SL/TP.",
            decisions=self.decisions,
        )


def test_symbol_filters_rounding() -> None:
    sf = SymbolFilters(
        symbol="SOLUSDT",
        base_asset="SOL",
        quote_asset="USDT",
        status="TRADING",
        step_size=Decimal("0.01"),
        min_qty=Decimal("0.01"),
        max_qty=Decimal("90000"),
        min_notional=Decimal("5.0"),
        tick_size=Decimal("0.01"),
        quote_order_qty_allowed=True,
    )
    assert sf.format_quantity(1.23987) == "1.23"


def test_candlestick_patterns_and_stochastic() -> None:
    prev = {"open": 105.0, "high": 106.0, "low": 100.0, "close": 101.0}
    hammer = {"open": 101.0, "high": 102.5, "low": 95.0, "close": 102.0}
    assert detect_candle_pattern(hammer, prev) == "BULLISH_HAMMER"

    prev_red = {"open": 102.0, "high": 102.5, "low": 99.5, "close": 100.0}
    curr_green = {"open": 99.8, "high": 103.0, "low": 99.5, "close": 102.5}
    assert detect_candle_pattern(curr_green, prev_red) == "BULLISH_ENGULFING"

    prev_up = {"open": 100.0, "high": 104.0, "low": 99.5, "close": 103.5}
    star = {"open": 103.5, "high": 110.0, "low": 102.5, "close": 102.8}
    assert detect_candle_pattern(star, prev_up) == "BEARISH_SHOOTING_STAR"

    prev_green = {"open": 100.0, "high": 102.5, "low": 99.5, "close": 102.0}
    curr_red = {"open": 102.2, "high": 102.5, "low": 99.0, "close": 99.5}
    assert detect_candle_pattern(curr_red, prev_green) == "BEARISH_ENGULFING"

    candles = [{"open": 100 + i, "high": 102 + i, "low": 99 + i, "close": 101.5 + i} for i in range(25)]
    k_s, d_s = calc_stochastic(candles, 14, 3, 3)
    assert len(k_s) > 5 and 70.0 <= k_s[-1] <= 100.0 and 70.0 <= d_s[-1] <= 100.0


def test_1pct_risk_position_sizing() -> None:
    order_usdt, risk_usd = calculate_position_size_1pct_risk(
        total_equity_usdt=500.0,
        available_usdt=400.0,
        entry_price=100.0,
        stop_loss_price=98.0,
        risk_pct=0.01,
        min_risk_usd=1.0,
        max_position_pct=0.35,
    )
    assert risk_usd == 5.0
    assert order_usdt == 175.0


def test_dynamic_sl_tp_trailing_and_ai_adjust(tmp_path: Path) -> None:
    cfg = BotConfig(
        binance_api_key="key",
        binance_api_secret="secret",
        gemini_api_key="gemini",
        dry_run=False,
        max_open_positions=3,
        max_position_pct=0.35,
        risk_per_trade_pct=0.01,
        min_risk_usd=1.0,
        state_file=tmp_path / "state.json",
        history_file=tmp_path / "history.json",
        report_file=tmp_path / "report.md",
    )
    fake_client = FakeBinanceClient()
    fake_scanner = FakeScanner()
    fake_ai = FakeAIAgent(
        decisions=[
            AIDecision(
                symbol="SOLUSDT",
                action="BUY",
                confidence=88,
                allocation_pct=0.35,
                stop_loss_pct=0.02,
                take_profit_pct=0.05,  # TP inicial = 210 * 1.05 = 220.5
                reasoning="Precio sobre EMA 200 en 1H, Estocastico en 18 y vela envolvente alcista.",
            )
        ]
    )
    sm = StateManager(cfg.state_file, cfg.history_file, cfg.report_file)

    bot = AutonomousTradingBot(
        config=cfg,
        binance_client=fake_client,  # type: ignore[arg-type]
        scanner=fake_scanner,  # type: ignore[arg-type]
        ai_agent=fake_ai,  # type: ignore[arg-type]
        state_manager=sm,
    )

    # Ciclo 1: compra SOLUSDT @ 210.0 con SL inicial en 205.8 y TP inicial en 220.5
    summary = bot.run_cycle()
    assert "SOLUSDT" in summary["open_positions"]
    saved = sm.load_state()
    sol_pos = saved.positions["SOLUSDT"]
    assert sol_pos.stop_loss_price == 205.8
    assert sol_pos.take_profit_price == 220.5
    # Simulamos que el saldo libre en Binance ahora incluye la posicion comprada de SOL
    fake_client.balances["SOL"] = sol_pos.quantity

    # Ciclo 2: SOLUSDT sube a 222.0 (supera el TP inicial de 220.5) y la IA ademas sugiere ADJUST a TP 235.0
    # El bot NO cierra la posicion: sube el SL por encima de la entrada (en ganancia asegurada) y expande el TP!
    fake_client.prices["SOLUSDT"] = 222.0
    fake_scanner.sol_price = 222.0
    fake_scanner.sol_prev_low = 217.5
    fake_scanner.sol_stoch_k = 83.0
    fake_scanner.sol_pattern = "NONE"  # Sin vela bajista de rechazo -> deja correr la operacion!
    fake_ai.decisions = [
        AIDecision(
            symbol="SOLUSDT",
            action="ADJUST",
            confidence=90,
            allocation_pct=0.35,
            stop_loss_pct=0.02,
            take_profit_pct=0.05,
            new_stop_loss_price=219.8,
            new_take_profit_price=235.0,
            reasoning="Tendencia alcista fuerte; subimos SL a 219.8 para asegurar ganancia y expandimos TP a 235.0.",
        )
    ]

    summary_2 = bot.run_cycle()
    assert "SOLUSDT" in summary_2["open_positions"]
    saved_2 = sm.load_state()
    sol_pos_2 = saved_2.positions["SOLUSDT"]
    # El SL subio de 205.8 a 219.8 (> 210.0 de entrada -> ganancia asegurada!) y el TP se expandio a 235.0
    assert sol_pos_2.stop_loss_price == 219.8
    assert sol_pos_2.take_profit_price == 235.0
    assert sol_pos_2.locked_profit_pct() > 4.0

    # Ciclo 3: Ahora el Estocastico sigue sobre 80 PERO aparece una vela envolvente bajista en ETHUSDT en ganancia -> cobra ganancia
    fake_client.prices["ETHUSDT"] = 3350.0
    fake_scanner.eth_stoch_k = 85.0
    fake_scanner.eth_pattern = "BEARISH_ENGULFING"
    summary_3 = bot.run_cycle()
    assert "ETHUSDT" not in summary_3["open_positions"]
    assert any(s[0] == "ETHUSDT" for s in fake_client.sells)


def test_futures_short_entry_and_downward_trailing(tmp_path: Path) -> None:
    cfg = BotConfig(
        binance_api_key="key",
        binance_api_secret="secret",
        gemini_api_key="gemini",
        dry_run=False,
        max_open_positions=3,
        max_position_pct=0.35,
        risk_per_trade_pct=0.01,
        min_risk_usd=1.0,
        state_file=tmp_path / "state_short.json",
        history_file=tmp_path / "history_short.json",
        report_file=tmp_path / "report_short.md",
    )
    fake_client = FakeBinanceClient()
    fake_client.balances = {"USDT": 0.0}
    fake_client.futures_usdt = 200.0
    fake_scanner = FakeScanner()
    fake_ai = FakeAIAgent(
        decisions=[
            AIDecision(
                symbol="SOLUSDT",
                action="SHORT",
                confidence=86,
                allocation_pct=0.65,
                stop_loss_pct=0.03,
                take_profit_pct=0.06,
                reasoning="Pilar SHORT S1: rechazo en EMA 200 con Estocastico en sobrecompra.",
            )
        ]
    )
    sm = StateManager(cfg.state_file, cfg.history_file, cfg.report_file)
    bot = AutonomousTradingBot(
        config=cfg,
        binance_client=fake_client,  # type: ignore[arg-type]
        scanner=fake_scanner,  # type: ignore[arg-type]
        ai_agent=fake_ai,  # type: ignore[arg-type]
        state_manager=sm,
    )

    # Ciclo 1: Abre SHORT en SOLUSDT @ 210.0 con SL arriba (212.0) y TP abajo (197.4)
    summary_1 = bot.run_cycle()
    assert "SOLUSDT" in summary_1["open_positions"]
    st_1 = sm.load_state()
    pos_1 = st_1.positions["SOLUSDT"]
    assert pos_1.side == "SHORT"
    assert pos_1.market_type == "FUTURES"
    assert pos_1.stop_loss_price == 212.0

    # Ciclo 2: SOLUSDT cae a 198.0 (+5.71% de ganancia en SHORT) con Estocastico en 45 -> el SL baja automaticamente asegurando ganancia!
    fake_client.prices["SOLUSDT"] = 198.0
    fake_scanner.sol_price = 198.0
    fake_scanner.sol_stoch_k = 45.0
    fake_scanner.sol_pattern = "NONE"
    fake_ai.decisions = []
    bot.run_cycle()
    st_2 = sm.load_state()
    pos_2 = st_2.positions["SOLUSDT"]
    assert pos_2.stop_loss_price < 210.0
    assert pos_2.locked_profit_pct() > 3.5

    # Ciclo 3: Estocastico llega a sobreventa (15.0) con Martillo Alcista -> cierra el SHORT cobrando la ganancia!
    fake_scanner.sol_stoch_k = 15.0
    fake_scanner.sol_pattern = "BULLISH_HAMMER"
    summary_3 = bot.run_cycle()
    assert "SOLUSDT" not in summary_3["open_positions"]


def test_mt5_ai_evaluation_and_90m_blocking(tmp_path: Path) -> None:
    # 1. Sin API key usa respaldo cuantitativo determinista
    agent = GeminiTradingAgent(api_key="", model="gemini-3.5-flash")

    weak_snap = {
        "htf_trend": "NEUTRAL",
        "above_ema_200": False,
        "ema200_slope_positive": False,
        "ema_50": 27200.0,
        "ema_200": 27600.0,
        "macd_improving": True,  # En contra de SELL
        "stoch_k": 55.0,
        "rsi_14": 46.0,
        "stoch_turning_up": True,
        "stoch_turning_down": False,
    }
    strong_snap = {
        "htf_trend": "BEARISH",
        "above_ema_200": False,
        "ema200_slope_positive": False,
        "ema_50": 0.673,
        "ema_200": 0.680,
        "macd_improving": False,  # A favor de SELL
        "stoch_k": 72.0,
        "rsi_14": 42.0,
        "stoch_turning_up": False,
        "stoch_turning_down": True,
    }

    # Cierre MANUAL hace 4 min en mercado debil -> < 60% -> debe bloquear 90 min
    # Cierre POSITIVE reciente hace 5 min con gran ganancia -> < 60% -> debe bloquear 90 min
    # Cierre NEGATIVE reciente hace 10 min -> < 60% -> debe bloquear 90 min
    # Cierre POSITIVE antiguo (30 min) con tendencia 4H/1H/MACD muy alineada -> >= 60% -> permite reactivar
    eval_res = agent.evaluate_mt5_market(
        open_positions_data=[
            {
                "ticket": 101,
                "symbol": "AUDUSDm",
                "side": "SELL",
                "profit_usd": 3.20,
                "tp_profit_usd": 11.28,
                "progress_to_tp_pct": 28.0,
                "rem_tp_in_atr1h": 1.8,
                "rem_sl_in_atr1h": 1.5,
                "snapshot": strong_snap,
            },
            {
                "ticket": 102,
                "symbol": "GBPUSDm",
                "side": "SELL",
                "profit_usd": 1.45,
                "tp_profit_usd": 13.77,
                "move_atr": 1.40,
                "progress_to_tp_pct": 10.0,
                "rem_tp_in_atr1h": 2.4,
                "rem_sl_in_atr1h": 0.9,
                "snapshot": {**weak_snap, "above_ema_200": True, "stoch_k": 18.0, "rsi_14": 31.0},  # Contra EMA200 + move_atr >= 1.25 -> PROTECT_PROFIT
            },
            {
                "ticket": 103,
                "symbol": "ETHUSDm",
                "side": "SELL",
                "profit_usd": 0.85,
                "tp_profit_usd": 8.24,
                "move_atr": 0.90,
                "progress_to_tp_pct": 10.0,
                "rem_tp_in_atr1h": 2.5,
                "rem_sl_in_atr1h": 0.4,
                "snapshot": {**weak_snap, "htf_trend": "BULLISH", "above_ema_200": True, "stoch_k": 15.0, "rsi_14": 28.0},  # Reversion inminente -> CLOSE_NOW
            },
        ],
        candidates_data=[],
        recent_closes_data=[
            {
                "ticket": 201,
                "symbol": "USTECm",
                "side": "SELL",
                "close_type": "MANUAL",
                "profit_usd": 0.66,
                "mins_since_close": 4.0,
                "snapshot": weak_snap,
            },
            {
                "ticket": 202,
                "symbol": "EURUSDm",
                "side": "SELL",
                "close_type": "POSITIVE",
                "profit_usd": 4.50,
                "mins_since_close": 5.0,
                "snapshot": weak_snap,
            },
            {
                "ticket": 203,
                "symbol": "USDCADm",
                "side": "BUY",
                "close_type": "NEGATIVE",
                "profit_usd": -2.90,
                "mins_since_close": 10.0,
                "snapshot": {**weak_snap, "above_ema_200": False, "htf_trend": "BEARISH"},
            },
            {
                "ticket": 204,
                "symbol": "NZDUSDm",
                "side": "SELL",
                "close_type": "POSITIVE",
                "profit_usd": 2.10,
                "mins_since_close": 35.0,
                "snapshot": strong_snap,
            },
        ],
    )

    # Verificar cierres recientes y regla < 60% vs >= 60%
    assert eval_res.closed_evals["USTECm"].reactivate_probability_pct < 60
    assert eval_res.closed_evals["USTECm"].should_block_90m is True
    assert eval_res.closed_evals["EURUSDm"].reactivate_probability_pct < 60
    assert eval_res.closed_evals["EURUSDm"].should_block_90m is True
    assert eval_res.closed_evals["USDCADm"].reactivate_probability_pct < 60
    assert eval_res.closed_evals["USDCADm"].should_block_90m is True

    assert eval_res.closed_evals["NZDUSDm"].reactivate_probability_pct >= 60
    assert eval_res.closed_evals["NZDUSDm"].should_block_90m is False

    # Verificar asistencia en posiciones abiertas (BUG-13: sin castigo -18 Stoch/RSI en ganancia; PROTECT_PROFIT exige move_atr>=1.25 y prob<65)
    assert eval_res.open_reviews["AUDUSDm"].tp_probability_pct >= 70
    assert eval_res.open_reviews["AUDUSDm"].action == "HOLD"
    assert eval_res.open_reviews["GBPUSDm"].tp_probability_pct < 65
    assert eval_res.open_reviews["GBPUSDm"].action in ("PROTECT_PROFIT", "CLOSE_NOW")
    assert eval_res.open_reviews["ETHUSDm"].tp_probability_pct <= 28
    assert eval_res.open_reviews["ETHUSDm"].action == "CLOSE_NOW"

    # Verificar persistencia de bloqueo 90 min en ExnessMT5AutonomousBot
    ai_state = tmp_path / "mt5_ai_state.json"
    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "mt5_report.md",
        history_file=tmp_path / "mt5_history.json",
        ai_state_file=ai_state,
    )
    bot.block_symbol_90m(
        symbol="USTECm",
        probability_pct=eval_res.closed_evals["USTECm"].reactivate_probability_pct,
        close_type="MANUAL",
        profit_usd=0.66,
        reason="Cierre manual con baja probabilidad",
        duration_minutes=90.0,
    )
    # Recargar desde disco como si el bot se reiniciara
    bot_reloaded = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "mt5_report.md",
        history_file=tmp_path / "mt5_history.json",
        ai_state_file=ai_state,
    )
    active = bot_reloaded.get_active_block("USTECm")
    assert active is not None
    assert active["close_type"] == "MANUAL"
    assert 89.0 <= active["remaining_minutes"] <= 90.1


def test_mt5_conviction_sizing_correlation_and_14d_perf(tmp_path: Path) -> None:
    # 1. Memoria 14d: activo con bajo WR (< 50%) exige >= 72% y bloquea si saca ~64-68%
    agent = GeminiTradingAgent(api_key="", model="gemini-3.5-flash")
    borderline_snap = {
        "htf_trend": "BEARISH",
        "above_ema_200": False,
        "ema200_slope_positive": False,
        "ema_50": 176.0,
        "ema_200": 178.0,
        "macd_improving": True,  # -8
        "stoch_k": 55.0,
        "rsi_14": 48.0,
        "stoch_turning_up": False,
        "stoch_turning_down": True,
    }
    low_wr_perf = {"trades": 11, "wins": 4, "win_rate_pct": 36.4, "net_pnl_usd": -4.58, "min_required_prob_pct": 72}
    star_perf = {"trades": 10, "wins": 8, "win_rate_pct": 80.0, "net_pnl_usd": 21.08, "min_required_prob_pct": 60}

    eval_cands = agent.evaluate_mt5_market(
        open_positions_data=[],
        candidates_data=[
            {
                "symbol": "EURJPYm",
                "side": "SELL",
                "entry_pillar": "M15_SCALPER_PULLBACK_SHORT",
                "snapshot": borderline_snap,
                "recent_close": None,
                "symbol_perf": low_wr_perf,
            },
            {
                "symbol": "USTECm",
                "side": "SELL",
                "entry_pillar": "M15_SCALPER_PULLBACK_SHORT",
                "snapshot": borderline_snap,
                "recent_close": None,
                "symbol_perf": star_perf,
            },
        ],
        recent_closes_data=[],
    )
    eurjpy_eval = eval_cands.candidate_evals["EURJPYm"]
    ustec_eval = eval_cands.candidate_evals["USTECm"]
    assert eurjpy_eval.required_probability_pct == 72
    assert eurjpy_eval.win_probability_pct == 64  # 58 + 10 + 10 - 8 - 6 = 64 (< 72%)
    assert eurjpy_eval.should_block_90m is True
    assert ustec_eval.required_probability_pct == 60
    assert ustec_eval.win_probability_pct == 74  # 58 + 10 + 10 - 8 + 4 = 74 (>= 60%)
    assert ustec_eval.should_block_90m is False

    # 2. Clasificacion de direccion USD (incluyendo XAUUSDm en bloque USD)
    assert ExnessMT5AutonomousBot._get_usd_direction("EURUSDm", "BUY") == "USD_SHORT"
    assert ExnessMT5AutonomousBot._get_usd_direction("GBPUSDm", "SELL") == "USD_LONG"
    assert ExnessMT5AutonomousBot._get_usd_direction("USDCHFm", "BUY") == "USD_LONG"
    assert ExnessMT5AutonomousBot._get_usd_direction("USDJPYm", "SELL") == "USD_SHORT"
    assert ExnessMT5AutonomousBot._get_usd_direction("EURJPYm", "BUY") == "NON_USD_FOREX"
    assert ExnessMT5AutonomousBot._get_usd_direction("XAUUSDm", "BUY") == "USD_SHORT"
    assert ExnessMT5AutonomousBot._get_usd_direction("XAUUSDm", "SELL") == "USD_LONG"

    # 3. Conviction Sizing: menor riesgo/lotaje con prob 62% vs 82%
    import src.mt5_bot as mt5_mod

    orig_profit = mt5_mod.mt5.order_calc_profit
    orig_margin = mt5_mod.mt5.order_calc_margin
    try:
        mt5_mod.mt5.order_calc_profit = lambda otype, sym, lot, p1, p2: -abs(p1 - p2) * 100000.0 * lot
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 5.0 * (lot / 0.01)

        bot = ExnessMT5AutonomousBot(
            gemini_api_key="",
            dry_run=True,
            report_file=tmp_path / "mt5_report2.md",
            history_file=tmp_path / "mt5_history2.json",
            ai_state_file=tmp_path / "mt5_ai2.json",
        )
        snap = MT5SymbolSnapshot(
            symbol="EURUSDm",
            bid=1.10000,
            ask=1.10008,
            spread_points=8,
            digits=5,
            point=0.00001,
            min_lot=0.01,
            lot_step=0.01,
            margin_min_lot_usd=5.5,
            usd_per_1pct_move_min_lot=11.0,
            ema_200=1.09500,
            ema_50=1.09800,
            ema_21=1.09950,
            above_ema_200=True,
            dist_to_ema200_atr=1.2,
            ema200_slope_positive=True,
            stoch_k=35.0,
            stoch_d=30.0,
            stoch_recent_min=28.0,
            stoch_recent_max=40.0,
            stoch_turning_up=True,
            stoch_turning_down=False,
            rsi_14=52.0,
            bb_upper=1.10500,
            bb_lower=1.09500,
            bb_pct_b=0.45,
            macd_hist=0.0002,
            macd_improving=True,
            atr_price=0.0010,
            atr_pct=0.09,
            candle_pattern="BULLISH_HAMMER",
            prev_candle_low=1.09900,
            prev_candle_high=1.10050,
            entry_pillar="M15_SCALPER_PULLBACK_LONG",
            strategy_setup="LONG_ENTRY",
            structural_long_sl=1.09930,  # 7.8 pips -> $0.78 per 0.01 lot
            structural_short_sl=1.10080,
            htf_trend="BULLISH",
        )
        lot_low, _, _, risk_low = bot.calculate_safe_lot_and_sl(
            snap=snap, side="BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=62
        )
        lot_high, _, _, risk_high = bot.calculate_safe_lot_and_sl(
            snap=snap, side="BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=82
        )
        assert lot_low < lot_high
        assert risk_low < risk_high
        assert lot_low <= 0.03
        assert lot_high == 0.05
    finally:
        mt5_mod.mt5.order_calc_profit = orig_profit
        mt5_mod.mt5.order_calc_margin = orig_margin


def test_gemini_priority_model_routing() -> None:
    agent = GeminiTradingAgent(api_key="", model="gemini-3.5-flash")
    high_order = agent._get_models_for_priority(high_priority=True)
    low_order = agent._get_models_for_priority(high_priority=False)
    assert high_order[0] == "gemini-4-hydrogen"
    assert high_order[1] == "gemini-3.5-flash"
    assert low_order[0] == "gemini-3.5-flash-lite"
    assert low_order[1] == "gemini-3.1-flash-lite"
    assert "gemini-3.5-flash" in low_order

    res_hi = agent.evaluate_mt5_market(open_positions_data=[], candidates_data=[], recent_closes_data=[], high_priority=True)
    res_lo = agent.evaluate_mt5_market(open_positions_data=[], candidates_data=[], recent_closes_data=[], high_priority=False)
    assert res_hi.priority_tier == "ALTA_PRIORIDAD"
    assert res_lo.priority_tier == "GENERAL"


def test_global_market_context_confluence_and_news_shield(tmp_path: Path) -> None:
    agent = GeminiTradingAgent(api_key="", model="gemini-3.5-flash")
    macro_ctx = {
        "usd_strength": {"usd_bias": "USD_STRONG_BULLISH", "usd_bullish_pairs": 6, "usd_bearish_pairs": 0},
        "crypto_pulse": {"crypto_regime": "CRYPTO_ALIGNED_BEARISH"},
        "indices_pulse": {"indices_regime": "WALL_STREET_BEARISH"},
        "news_and_session": {"session_name": "NUEVA_YORK", "news_volatility_alert": False},
    }
    neutral_snap = {
        "htf_trend": "NEUTRAL",
        "above_ema_200": False,
        "ema200_slope_positive": False,
        "ema_50": 1.10,
        "ema_200": 1.11,
        "macd_improving": False,
        "stoch_k": 55.0,
        "rsi_14": 48.0,
        "stoch_turning_up": False,
        "stoch_turning_down": True,
    }
    p_eur_sell, _ = compute_mt5_quant_probability({**neutral_snap, "symbol": "EURUSDm"}, "SELL", market_context=macro_ctx)
    p_eur_buy, _ = compute_mt5_quant_probability(
        {**neutral_snap, "symbol": "EURUSDm", "above_ema_200": True, "ema200_slope_positive": True, "macd_improving": True},
        "BUY",
        market_context=macro_ctx,
    )
    assert p_eur_sell > p_eur_buy

    p_eth_sell, _ = compute_mt5_quant_probability({**neutral_snap, "symbol": "ETHUSDm"}, "SELL", market_context=macro_ctx)
    p_eth_buy, _ = compute_mt5_quant_probability(
        {**neutral_snap, "symbol": "ETHUSDm", "above_ema_200": True, "ema200_slope_positive": True, "macd_improving": True},
        "BUY",
        market_context=macro_ctx,
    )
    assert p_eth_sell > p_eth_buy

    # Alerta de noticias/volatilidad: penaliza candidatos (-12%) pero NO sobrescribe HOLD a PROTECT_PROFIT en posiciones abiertas (BUG-02)
    macro_news = {
        **macro_ctx,
        "news_and_session": {"session_name": "LONDRES_NY_OVERLAP", "news_volatility_alert": True},
    }
    p_cand_normal, _ = compute_mt5_quant_probability({**neutral_snap, "symbol": "EURUSDm"}, "SELL", market_context=macro_ctx)
    p_cand_news, _ = compute_mt5_quant_probability({**neutral_snap, "symbol": "EURUSDm"}, "SELL", market_context=macro_news)
    assert p_cand_news == max(5, p_cand_normal - 12)

    eval_news = agent.evaluate_mt5_market(
        open_positions_data=[
            {
                "ticket": 901,
                "symbol": "AUDUSDm",
                "side": "SELL",
                "profit_usd": 1.35,
                "tp_profit_usd": 10.0,
                "move_atr": 0.45,
                "progress_to_tp_pct": 14.0,
                "rem_tp_in_atr1h": 2.0,
                "rem_sl_in_atr1h": 1.2,
                "snapshot": {**neutral_snap, "htf_trend": "BEARISH"},
            }
        ],
        candidates_data=[],
        recent_closes_data=[],
        high_priority=True,
        market_context=macro_news,
    )
    assert eval_news.open_reviews["AUDUSDm"].action == "HOLD"

    # Verificar build_global_market_context en bot
    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r.md",
        history_file=tmp_path / "h.json",
        ai_state_file=tmp_path / "a.json",
    )
    def mk_snap(sym: str, above: bool, htf: str, spread: int = 10) -> MT5SymbolSnapshot:
        return MT5SymbolSnapshot(
            symbol=sym, bid=1.0, ask=1.0001, spread_points=spread, digits=5, point=0.00001,
            min_lot=0.01, lot_step=0.01, margin_min_lot_usd=5.0, usd_per_1pct_move_min_lot=10.0,
            ema_200=1.0, ema_50=1.0, ema_21=1.0, above_ema_200=above, dist_to_ema200_atr=1.0,
            ema200_slope_positive=above, stoch_k=50.0, stoch_d=50.0, stoch_recent_min=40.0,
            stoch_recent_max=60.0, stoch_turning_up=above, stoch_turning_down=not above,
            rsi_14=50.0, bb_upper=1.1, bb_lower=0.9, bb_pct_b=0.5, macd_hist=0.0,
            macd_improving=above, atr_price=0.001, atr_pct=0.1, candle_pattern="NONE",
            prev_candle_low=0.99, prev_candle_high=1.01, entry_pillar="NONE",
            strategy_setup="WATCH", structural_long_sl=0.99, structural_short_sl=1.01, htf_trend=htf,
        )

    snaps = [
        mk_snap("EURUSDm", False, "BEARISH"),
        mk_snap("GBPUSDm", False, "BEARISH"),
        mk_snap("AUDUSDm", False, "BEARISH"),
        mk_snap("NZDUSDm", False, "BEARISH"),
        mk_snap("USDJPYm", True, "BULLISH"),
        mk_snap("BTCUSDm", False, "BEARISH"),
        mk_snap("ETHUSDm", False, "BEARISH"),
        mk_snap("US500m", False, "BEARISH"),
        mk_snap("USTECm", False, "BEARISH"),
    ]
    built = bot.build_global_market_context(snaps)
    assert built["usd_strength"]["usd_bias"] == "USD_STRONG_BULLISH"
    assert built["crypto_pulse"]["crypto_regime"] == "CRYPTO_ALIGNED_BEARISH"
    assert built["indices_pulse"]["indices_regime"] == "WALL_STREET_BEARISH"
    assert len(built["all_assets_overview"]) == len(snaps)


def test_pre_rollover_blackout_and_harvest_windows() -> None:
    # 14:30 local = 20:30 UTC -> True; 15:10 local = 21:10 UTC -> True; 16:30 local = 22:30 UTC -> True
    assert ExnessMT5AutonomousBot._is_pre_rollover_entry_blackout(datetime(2026, 11, 18, 20, 30, tzinfo=timezone.utc)) is True
    assert ExnessMT5AutonomousBot._is_pre_rollover_entry_blackout(datetime(2026, 11, 18, 21, 10, tzinfo=timezone.utc)) is True
    assert ExnessMT5AutonomousBot._is_pre_rollover_entry_blackout(datetime(2026, 11, 18, 22, 30, tzinfo=timezone.utc)) is True
    assert ExnessMT5AutonomousBot._is_pre_rollover_entry_blackout(datetime(2026, 11, 18, 23, 15, tzinfo=timezone.utc)) is True
    # 12:00 local = 18:00 UTC -> False; 17:30 local = 23:30 UTC -> False
    assert ExnessMT5AutonomousBot._is_pre_rollover_entry_blackout(datetime(2026, 11, 18, 18, 0, tzinfo=timezone.utc)) is False
    assert ExnessMT5AutonomousBot._is_pre_rollover_entry_blackout(datetime(2026, 11, 18, 23, 30, tzinfo=timezone.utc)) is False

    # Pre-Rollover Harvest eliminado permanentemente en CLEAN_DIFF
    assert not hasattr(ExnessMT5AutonomousBot, "_is_pre_rollover_profit_harvest_window")


def test_mt5_overextension_and_daily_guard_quant_penalties(tmp_path: Path) -> None:
    base_buy_snap = {
        "symbol": "EURUSDm",
        "htf_trend": "BULLISH",
        "above_ema_200": True,
        "ema200_slope_positive": True,
        "ema_50": 1.1050,
        "ema_200": 1.1000,
        "macd_improving": True,
        "stoch_k": 48.0,
        "rsi_14": 54.0,
        "stoch_turning_up": True,
        "stoch_turning_down": False,
        "dist_to_ema200_atr": 2.0,
    }
    p_buy_normal, _ = compute_mt5_quant_probability(base_buy_snap, "BUY")
    p_buy_ext5, reason_ext5 = compute_mt5_quant_probability({**base_buy_snap, "dist_to_ema200_atr": 5.5}, "BUY")
    p_buy_ext8, reason_ext8 = compute_mt5_quant_probability({**base_buy_snap, "dist_to_ema200_atr": 8.2}, "BUY")
    assert p_buy_normal - p_buy_ext5 == 16
    assert p_buy_normal - p_buy_ext8 == 24
    assert "sobre-extendida" in reason_ext5
    assert "sobre-extendida" in reason_ext8

    base_sell_snap = {
        "symbol": "EURUSDm",
        "htf_trend": "BEARISH",
        "above_ema_200": False,
        "ema200_slope_positive": False,
        "ema_50": 1.0950,
        "ema_200": 1.1000,
        "macd_improving": False,
        "stoch_k": 52.0,
        "rsi_14": 46.0,
        "stoch_turning_up": False,
        "stoch_turning_down": True,
        "dist_to_ema200_atr": -2.0,
    }
    p_sell_normal, _ = compute_mt5_quant_probability(base_sell_snap, "SELL")
    p_sell_ext5, _ = compute_mt5_quant_probability({**base_sell_snap, "dist_to_ema200_atr": -5.5}, "SELL")
    p_sell_ext8, _ = compute_mt5_quant_probability({**base_sell_snap, "dist_to_ema200_atr": -8.2}, "SELL")
    assert p_sell_normal - p_sell_ext5 == 16
    assert p_sell_normal - p_sell_ext8 == 24

    # En posiciones abiertas (>6x ATR) no se aplica -16/-24 ni sobrescritura forzada sobre HOLD (BUG-02)
    open_pos_sample = {
        "ticket": 555,
        "symbol": "EURUSDm",
        "side": "BUY",
        "profit_usd": 1.85,
        "move_atr": 0.90,
        "progress_to_tp_pct": 18.0,
        "rem_sl_in_atr1h": 1.4,
    }
    p_open_ext8, reason_open_ext8 = compute_mt5_quant_probability(
        {**base_buy_snap, "dist_to_ema200_atr": 8.2},
        "BUY",
        open_pos=open_pos_sample,
    )
    assert p_open_ext8 == p_buy_normal
    assert "extension 1H >6x ATR" in reason_open_ext8

    agent = GeminiTradingAgent(api_key="", model="gemini-3.5-flash")
    eval_open = agent.evaluate_mt5_market(
        open_positions_data=[{**open_pos_sample, "snapshot": {**base_buy_snap, "dist_to_ema200_atr": 7.4}}],
        candidates_data=[],
        recent_closes_data=[],
    )
    assert eval_open.open_reviews["EURUSDm"].tp_probability_pct >= 75
    assert eval_open.open_reviews["EURUSDm"].action == "HOLD"

    # BUG-13 FIX: eliminada la penalizacion duplicada -6 por daily_risk_guard (el umbral min_ai_prob ya sube a 68%)
    guard_ctx = {"daily_risk_guard": {"consecutive_losses": 2, "protection_mode": "MODO_PROTECCION_CAPITAL"}}
    p_cand_guard, _ = compute_mt5_quant_probability(base_buy_snap, "BUY", market_context=guard_ctx)
    assert p_cand_guard == p_buy_normal

    p_open_guard, _ = compute_mt5_quant_probability(
        base_buy_snap,
        "BUY",
        open_pos=open_pos_sample,
        market_context=guard_ctx,
    )
    assert p_open_guard == p_buy_normal

    # Cooldown de 15m en _call_gemini tras timeout (18s) en gemini-4-hydrogen
    import src.gemini_agent as gemini_mod

    called_models: list[str] = []
    orig_post = gemini_mod.requests.post

    def fake_post(url: str, **kwargs: Any) -> Any:
        mdl = url.split("/models/")[1].split(":")[0]
        called_models.append(mdl)
        if mdl == "gemini-4-hydrogen":
            assert kwargs.get("timeout") == 18
            raise requests.exceptions.Timeout("Read timed out")
        return SimpleNamespace(
            status_code=200,
            json=lambda: {"candidates": [{"content": {"parts": [{"text": "{}"}]}}]},
        )

    try:
        gemini_mod.requests.post = fake_post
        live_agent = GeminiTradingAgent(api_key="test-key", model="gemini-3.5-flash")
        out_1 = live_agent._call_gemini("ping", high_priority=True)
        out_2 = live_agent._call_gemini("ping", high_priority=True)
        assert out_1 == "{}" and out_2 == "{}"
        assert called_models == ["gemini-4-hydrogen", "gemini-3.5-flash", "gemini-3.5-flash"]
        assert "gemini-4-hydrogen" in live_agent._model_cooldown_until
    finally:
        gemini_mod.requests.post = orig_post


def test_mt5_daily_risk_guard_m15_filters_and_risk_scale(tmp_path: Path) -> None:
    import src.mt5_bot as mt5_mod

    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "mt5_guard_report.md",
        history_file=tmp_path / "mt5_guard_history.json",
        ai_state_file=tmp_path / "mt5_guard_ai.json",
    )

    # 1. M15_SCALPER exclusivo en CORE4 (US500m, USTECm, BTCUSDm, XAUUSDm) + limites de dist_atr y htf_trend
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("EURJPYm", True, 1.5, "BULLISH") is False
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("EURGBPm", False, -1.5, "BEARISH") is False
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("EURUSDm", True, 1.5, "BULLISH") is False
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("ETHUSDm", True, 1.5, "BULLISH") is False

    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("US500m", True, -0.5, "NEUTRAL") is True
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("USTECm", True, 4.8, "BULLISH") is True
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("US500m", True, 4.85, "BULLISH") is False
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("US500m", True, -0.55, "BULLISH") is False
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("US500m", True, 1.5, "BEARISH") is False

    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("BTCUSDm", False, 0.5, "NEUTRAL") is True
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("XAUUSDm", False, -4.8, "BEARISH") is True
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("BTCUSDm", False, -4.85, "BEARISH") is False
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("BTCUSDm", False, 0.55, "BEARISH") is False
    assert ExnessMT5AutonomousBot._is_m15_scalper_context_allowed("BTCUSDm", False, -1.5, "BULLISH") is False

    # 2. Evaluacion de _evaluate_daily_risk_guard (modo SOFT sobre equity=$600: -3%=-$18, +4%=+$24, 3L<45m)
    ref_now = datetime(2026, 11, 18, 18, 0, 0, tzinfo=timezone.utc)
    orig_deals_get = mt5_mod.mt5.history_deals_get
    orig_pos_get = mt5_mod.mt5.positions_get
    try:
        mt5_mod.mt5.positions_get = lambda: ()

        def mk_deal(
            ticket: int,
            pos_id: int,
            entry: int,
            mins_ago: float,
            profit: float,
            swap: float = 0.0,
            comm: float = 0.0,
            magic: int = MT5_MAGIC_NUMBER,
        ) -> Any:
            ts = int((ref_now - timedelta(minutes=mins_ago)).timestamp())
            return SimpleNamespace(
                ticket=ticket,
                position_id=pos_id,
                entry=entry,
                time=ts,
                profit=profit,
                swap=swap,
                commission=comm,
                magic=magic,
            )

        # Escenario A: Normal (+$6.00, 1 win)
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [
            mk_deal(1, 10, mt5_mod.mt5.DEAL_ENTRY_IN, 90, 0.0),
            mk_deal(2, 10, mt5_mod.mt5.DEAL_ENTRY_OUT, 80, 6.0),
        ]
        g_norm = bot._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0)
        assert g_norm["protection_mode"] == "NORMAL"
        assert g_norm["protection_active"] is False
        assert g_norm["pause_new_entries"] is False
        assert g_norm["min_ai_prob"] == 60
        assert g_norm["risk_scale"] == 1.0
        assert g_norm["max_positions"] == 4

        # Escenario B: Ganancia diaria >= +4% equity (+$24.00 en $600) activa MODO_PROTECCION_CAPITAL SOFT
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [
            mk_deal(11, 20, mt5_mod.mt5.DEAL_ENTRY_OUT, 180, 14.50, swap=-0.10),
            mk_deal(12, 21, mt5_mod.mt5.DEAL_ENTRY_OUT, 90, 10.20, comm=-0.10),
        ]
        g_profit = bot._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0)
        assert g_profit["daily_closed_pnl_usd"] == 24.5
        assert g_profit["protection_mode"] == "MODO_PROTECCION_CAPITAL"
        assert g_profit["protection_active"] is True
        assert g_profit["pause_new_entries"] is False
        assert g_profit["min_ai_prob"] == 68
        assert g_profit["risk_scale"] == 0.75
        assert g_profit["max_positions"] == 3

        # Escenario C: 2 perdidas consecutivas -> MODO_PROTECCION_CAPITAL SOFT (68%, 0.75x, max 3)
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [
            mk_deal(21, 30, mt5_mod.mt5.DEAL_ENTRY_OUT, 180, 12.0),
            mk_deal(22, 31, mt5_mod.mt5.DEAL_ENTRY_OUT, 120, -1.5),
            mk_deal(23, 31, mt5_mod.mt5.DEAL_ENTRY_OUT, 115, -1.0),
            mk_deal(24, 32, mt5_mod.mt5.DEAL_ENTRY_OUT, 30, -3.2),
        ]
        g_2loss = bot._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0)
        assert g_2loss["closed_trades_today"] == 3
        assert g_2loss["consecutive_losses"] == 2
        assert g_2loss["protection_mode"] == "MODO_PROTECCION_CAPITAL"
        assert g_2loss["pause_new_entries"] is False
        assert g_2loss["min_ai_prob"] == 68
        assert g_2loss["risk_scale"] == 0.75
        assert g_2loss["max_positions"] == 3

        # Escenario D: 3 perdidas consecutivas hace 25m (< 45m) -> pause_new_entries=True (~20m restantes)
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [
            mk_deal(31, 41, mt5_mod.mt5.DEAL_ENTRY_OUT, 90, -2.5),
            mk_deal(32, 42, mt5_mod.mt5.DEAL_ENTRY_OUT, 50, -3.1),
            mk_deal(33, 43, mt5_mod.mt5.DEAL_ENTRY_OUT, 25, -2.8),
        ]
        g_3loss_pause = bot._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0)
        assert g_3loss_pause["consecutive_losses"] == 3
        assert g_3loss_pause["protection_mode"] == "MODO_PROTECCION_CAPITAL"
        assert g_3loss_pause["pause_new_entries"] is True
        assert 19.5 <= g_3loss_pause["pause_remaining_mins"] <= 20.5
        line = ExnessMT5AutonomousBot._format_daily_risk_guard_line({"daily_risk_guard": g_3loss_pause})
        assert "MODO_PROTECCION_CAPITAL" in line and "FRENO 45m ACTIVO" in line

        # Escenario E: 3 perdidas consecutivas pero hace 50m (>= 45m) -> sin pausa, sigue proteccion
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [
            mk_deal(41, 51, mt5_mod.mt5.DEAL_ENTRY_OUT, 140, -2.5),
            mk_deal(42, 52, mt5_mod.mt5.DEAL_ENTRY_OUT, 100, -3.1),
            mk_deal(43, 53, mt5_mod.mt5.DEAL_ENTRY_OUT, 50, -2.8),
        ]
        g_3loss_expired = bot._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0)
        assert g_3loss_expired["consecutive_losses"] == 3
        assert g_3loss_expired["protection_mode"] == "MODO_PROTECCION_CAPITAL"
        assert g_3loss_expired["pause_new_entries"] is False

        # Escenario F: Hard Daily Loss Stop <= -3% equity (-$18.50 en $600) -> pause_new_entries=True
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [
            mk_deal(51, 61, mt5_mod.mt5.DEAL_ENTRY_OUT, 180, -9.5),
            mk_deal(52, 62, mt5_mod.mt5.DEAL_ENTRY_OUT, 120, -9.0),
        ]
        g_hard = bot._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0)
        assert g_hard["hard_daily_loss_stop"] is True
        assert g_hard["pause_new_entries"] is True
        assert "HARD STOP -3% ACTIVO" in ExnessMT5AutonomousBot._format_daily_risk_guard_line({"daily_risk_guard": g_hard})
    finally:
        mt5_mod.mt5.history_deals_get = orig_deals_get
        mt5_mod.mt5.positions_get = orig_pos_get

    # 3. En calculate_safe_lot_and_sl: risk_scale=0.75 reduce lotes pero NO estrangula raw_sl en min_lot; TP fijo 2.5R
    orig_profit = mt5_mod.mt5.order_calc_profit
    orig_margin = mt5_mod.mt5.order_calc_margin
    try:
        mt5_mod.mt5.order_calc_profit = lambda otype, sym, lot, p1, p2: -abs(p1 - p2) * (100.0 if sym == "XAUUSDm" else 100000.0) * lot
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 5.0 * (lot / 0.01)

        eur_m15_snap = MT5SymbolSnapshot(
            symbol="EURUSDm", bid=1.10000, ask=1.10008, spread_points=8, digits=5, point=0.00001,
            min_lot=0.01, lot_step=0.01, margin_min_lot_usd=5.5, usd_per_1pct_move_min_lot=11.0,
            ema_200=1.09500, ema_50=1.09800, ema_21=1.09950, above_ema_200=True, dist_to_ema200_atr=1.2,
            ema200_slope_positive=True, stoch_k=45.0, stoch_d=40.0, stoch_recent_min=38.0,
            stoch_recent_max=50.0, stoch_turning_up=True, stoch_turning_down=False, rsi_14=52.0,
            bb_upper=1.10500, bb_lower=1.09500, bb_pct_b=0.45, macd_hist=0.0002, macd_improving=False,
            atr_price=0.0010, atr_pct=0.09, candle_pattern="NONE", prev_candle_low=1.09900,
            prev_candle_high=1.10050, entry_pillar="M15_SCALPER_PULLBACK_LONG", strategy_setup="LONG_ENTRY",
            structural_long_sl=1.09908, structural_short_sl=1.10108, htf_trend="BULLISH",
        )
        lot_full, _, tp_m15, risk_full = bot.calculate_safe_lot_and_sl(
            snap=eur_m15_snap, side="BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=75, risk_scale=1.0
        )
        lot_scaled, _, _, risk_scaled = bot.calculate_safe_lot_and_sl(
            snap=eur_m15_snap, side="BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=75, risk_scale=0.75
        )
        assert lot_scaled < lot_full and risk_scaled < risk_full
        # TP fijo FIXED_2.5R: sl_dist = 0.00100 -> tp_dist = 0.00250
        assert round(tp_m15 - eur_m15_snap.ask, 5) == 0.00250

        xau_snap = MT5SymbolSnapshot(
            symbol="XAUUSDm", bid=2600.00, ask=2600.20, spread_points=200, digits=2, point=0.01,
            min_lot=0.01, lot_step=0.01, margin_min_lot_usd=13.0, usd_per_1pct_move_min_lot=26.0,
            ema_200=2580.00, ema_50=2592.00, ema_21=2598.00, above_ema_200=True, dist_to_ema200_atr=2.0,
            ema200_slope_positive=True, stoch_k=45.0, stoch_d=40.0, stoch_recent_min=38.0,
            stoch_recent_max=50.0, stoch_turning_up=True, stoch_turning_down=False, rsi_14=54.0,
            bb_upper=2610.0, bb_lower=2585.0, bb_pct_b=0.55, macd_hist=0.5, macd_improving=True,
            atr_price=5.00, atr_pct=0.19, candle_pattern="NONE", prev_candle_low=2595.0,
            prev_candle_high=2603.0, entry_pillar="M15_SCALPER_PULLBACK_LONG", strategy_setup="LONG_ENTRY",
            structural_long_sl=2596.40,  # $3.80 en 0.01 lot (<= max $5.10 en $600)
            structural_short_sl=2604.00, htf_trend="BULLISH",
        )
        lot_xau, sl_xau, _, _ = bot.calculate_safe_lot_and_sl(
            snap=xau_snap, side="BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=65, risk_scale=0.75
        )
        assert lot_xau == 0.01
        assert sl_xau == 2596.40
    finally:
        mt5_mod.mt5.order_calc_profit = orig_profit
        mt5_mod.mt5.order_calc_margin = orig_margin


def test_mt5_build_snapshots_m15_exclusion_and_dist_limit(tmp_path: Path) -> None:
    import src.mt5_bot as mt5_mod

    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "mt5_snap_report.md",
        history_file=tmp_path / "mt5_snap_history.json",
        ai_state_file=tmp_path / "mt5_snap_ai.json",
    )

    c1h = [
        {
            "open": 5000.0 + i * 0.1 + (0.4 if i % 2 == 0 else -0.2),
            "high": 5002.0 + i * 0.1,
            "low": 4998.0 + i * 0.1,
            "close": 5000.0 + i * 0.1 + (0.4 if i % 2 == 1 else -0.2),
            "volume": 100.0,
        }
        for i in range(260)
    ]
    c1h[-2]["close"] = c1h[-3]["close"] - 0.5  # vela cerrada: macd_improving = False en 1H

    c4h = [
        {
            "open": 5000.0 + i * 0.5,
            "high": 5004.0 + i * 0.5,
            "low": 4996.0 + i * 0.5,
            "close": 5002.0 + i * 0.5,
            "volume": 100.0,
        }
        for i in range(120)
    ]

    # 65 velas M15 (64 cerradas + 1 en curso que se ignora via c15[:-1])
    c15_closed_part = [
        {
            "open": 5015.0 + i * 0.25,
            "high": 5016.2 + i * 0.25,
            "low": 5014.4 + i * 0.25,
            "close": 5015.8 + i * 0.25,
            "volume": 100.0,
        }
        for i in range(60)
    ] + [
        {"open": 5029.8, "high": 5030.2, "low": 5028.0, "close": 5028.4, "volume": 100.0},
        {"open": 5028.4, "high": 5028.8, "low": 5027.0, "close": 5027.4, "volume": 100.0},
        {"open": 5027.4, "high": 5027.8, "low": 5026.2, "close": 5026.5, "volume": 100.0},
        {"open": 5026.5, "high": 5028.0, "low": 5026.4, "close": 5027.8, "volume": 100.0},
        {"open": 5027.8, "high": 5029.5, "low": 5027.5, "close": 5029.0, "volume": 100.0},
    ]
    c15 = c15_closed_part + [
        {"open": 5029.0, "high": 5029.1, "low": 5028.9, "close": 5029.0, "volume": 1.0}  # vela viva descartada
    ]
    expected_atr_15 = calc_atr_wilder(c15[:-1], 14)

    orig_select = mt5_mod.mt5.symbol_select
    orig_info = mt5_mod.mt5.symbol_info
    orig_tick = mt5_mod.mt5.symbol_info_tick
    orig_margin = mt5_mod.mt5.order_calc_margin
    orig_profit = mt5_mod.mt5.order_calc_profit
    orig_fetch = bot._fetch_candles
    m15_fetched_for: list[str] = []
    us500_bid = 5029.0

    try:
        mt5_mod.mt5.symbol_select = lambda sym, flag: True
        mt5_mod.mt5.symbol_info = lambda sym: (
            SimpleNamespace(digits=2, point=0.01, volume_min=0.14, volume_step=0.01, spread=40)
            if sym in ("US500m", "EURUSDm", "EURJPYm", "EURGBPm")
            else None
        )
        mt5_mod.mt5.symbol_info_tick = lambda sym: SimpleNamespace(
            bid=us500_bid if sym == "US500m" else 5029.0,
            ask=(us500_bid + 0.40) if sym == "US500m" else 5029.40,
        )
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 5.0
        mt5_mod.mt5.order_calc_profit = lambda otype, sym, lot, p1, p2: 10.0

        def fake_fetch(sym: str, timeframe: int, count: int = 600) -> list[dict[str, float]]:
            if timeframe == mt5_mod.mt5.TIMEFRAME_M15:
                m15_fetched_for.append(sym)
                return [dict(x) for x in c15]
            if timeframe == mt5_mod.mt5.TIMEFRAME_H1:
                return [dict(x) for x in c1h]
            if timeframe == mt5_mod.mt5.TIMEFRAME_H4:
                return [dict(x) for x in c4h]
            return []

        bot._fetch_candles = fake_fetch  # type: ignore[method-assign]

        snaps = {s.symbol: s for s in bot.build_snapshots(free_margin_usd=500.0, open_symbols=set())}
        # Solo CORE4 (US500m) descarga y opera M15; Forex (EURUSDm/EURJPYm/EURGBPm) no
        assert m15_fetched_for == ["US500m"]
        assert snaps["EURUSDm"].entry_pillar == "NONE"
        assert snaps["EURJPYm"].entry_pillar == "NONE"
        assert snaps["EURGBPm"].entry_pillar == "NONE"
        assert snaps["US500m"].dist_to_ema200_atr <= 4.8
        assert snaps["US500m"].entry_pillar == "M15_SCALPER_PULLBACK_LONG"
        assert snaps["US500m"].structural_long_sl == round(5029.0 - (2.0 * expected_atr_15), 2)
        assert len(snaps["US500m"].recent_h1_closes) == 5
        assert snaps["US500m"].swing_high_20 > snaps["US500m"].swing_low_20

        # Cuando US500m excede 4.8x ATR en 1H, M15_SCALPER no debe activarse
        us500_bid = 5060.0
        snaps_ext = {s.symbol: s for s in bot.build_snapshots(free_margin_usd=500.0, open_symbols=set())}
        assert snaps_ext["US500m"].dist_to_ema200_atr > 4.8
        assert snaps_ext["US500m"].entry_pillar == "NONE"
    finally:
        mt5_mod.mt5.symbol_select = orig_select
        mt5_mod.mt5.symbol_info = orig_info
        mt5_mod.mt5.symbol_info_tick = orig_tick
        mt5_mod.mt5.order_calc_margin = orig_margin
        mt5_mod.mt5.order_calc_profit = orig_profit
        bot._fetch_candles = orig_fetch  # type: ignore[method-assign]


# =============================================================================
# NUEVAS SUITES DE VERIFICACION B_FINAL_HYBRID_ADX_0.65PCT (BUG-01 .. BUG-13)
# =============================================================================

def _make_test_snapshot(
    symbol: str = "EURUSDm",
    bid: float = 1.10000,
    ask: float = 1.10010,
    spread_points: int = 10,
    digits: int = 5,
    point: float = 0.00001,
    min_lot: float = 0.01,
    lot_step: float = 0.01,
    atr_price: float = 0.0010,
    atr_15_price: float = 0.0005,
    entry_pillar: str = "P1_EMA200_PULLBACK_LONG",
    strategy_setup: str = "LONG_ENTRY",
    structural_long_sl: float = 1.09700,
    structural_short_sl: float = 1.10310,
    htf_trend: str = "BULLISH",
    adx_14: float = 25.0,
) -> MT5SymbolSnapshot:
    return MT5SymbolSnapshot(
        symbol=symbol,
        bid=bid,
        ask=ask,
        spread_points=spread_points,
        digits=digits,
        point=point,
        min_lot=min_lot,
        lot_step=lot_step,
        margin_min_lot_usd=5.5,
        usd_per_1pct_move_min_lot=11.0,
        ema_200=bid - atr_price,
        ema_50=bid - 0.5 * atr_price,
        ema_21=bid - 0.2 * atr_price,
        above_ema_200=(strategy_setup == "LONG_ENTRY"),
        dist_to_ema200_atr=1.0 if strategy_setup == "LONG_ENTRY" else -1.0,
        ema200_slope_positive=(strategy_setup == "LONG_ENTRY"),
        stoch_k=35.0,
        stoch_d=30.0,
        stoch_recent_min=20.0,
        stoch_recent_max=80.0,
        stoch_turning_up=(strategy_setup == "LONG_ENTRY"),
        stoch_turning_down=(strategy_setup == "SHORT_ENTRY"),
        rsi_14=42.0 if strategy_setup == "LONG_ENTRY" else 58.0,
        bb_upper=bid + 2 * atr_price,
        bb_lower=bid - 2 * atr_price,
        bb_pct_b=0.20 if strategy_setup == "LONG_ENTRY" else 0.80,
        macd_hist=0.0002,
        macd_improving=(strategy_setup == "LONG_ENTRY"),
        atr_price=atr_price,
        atr_pct=0.10,
        candle_pattern="BULLISH_HAMMER" if strategy_setup == "LONG_ENTRY" else "BEARISH_SHOOTING_STAR",
        prev_candle_low=bid - atr_price,
        prev_candle_high=bid + atr_price,
        entry_pillar=entry_pillar,
        strategy_setup=strategy_setup,
        structural_long_sl=structural_long_sl,
        structural_short_sl=structural_short_sl,
        htf_trend=htf_trend,
        adx_14=adx_14,
        atr_15_price=atr_15_price,
        recent_h1_closes=[bid - 0.0004, bid - 0.0003, bid - 0.0002, bid - 0.0001, bid],
        swing_high_20=bid + 3 * atr_price,
        swing_low_20=bid - 3 * atr_price,
    )


def test_suite1_clean_diff_exits_h1_m15_and_no_backdating(tmp_path: Path) -> None:
    """Cubre BUG-01, BUG-02, BUG-05, BUG-12: salidas CLEAN_DIFF H1/M15 sin backdating, sin ai_protect_profit ni parcial 50%."""
    import src.mt5_bot as mt5_mod

    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r1.md",
        history_file=tmp_path / "h1.json",
        ai_state_file=tmp_path / "a1.json",
    )

    orig_pos_get = mt5_mod.mt5.positions_get
    orig_info = mt5_mod.mt5.symbol_info
    orig_tick = mt5_mod.mt5.symbol_info_tick
    orig_send = mt5_mod.mt5.order_send
    orig_datetime = mt5_mod.datetime

    class WedDatetime(datetime):
        @classmethod
        def now(cls, tz=None):  # type: ignore[override]
            return datetime(2026, 11, 18, 15, 0, 0, tzinfo=timezone.utc)

    try:
        mt5_mod.datetime = WedDatetime  # type: ignore[misc]
        mt5_mod.mt5.symbol_info = lambda sym: SimpleNamespace(
            digits=2 if sym == "US500m" else 5,
            point=0.01 if sym == "US500m" else 0.00001,
            spread=20,
            volume_min=0.01,
            volume_step=0.01,
            trade_stops_level=5,
            filling_mode=2,
        )
        mt5_mod.mt5.symbol_info_tick = lambda sym: SimpleNamespace(bid=1.1050, ask=1.1052)

        # 1) M15: BE +0.05R @ 1.00R, SIN trailing en 2.0R ni partial close ni ai_protect_profit
        m15_snap = _make_test_snapshot(symbol="US500m", bid=5020.0, ask=5020.2, digits=2, point=0.01, atr_price=20.0, atr_15_price=10.0)
        m15_pos_early = SimpleNamespace(
            ticket=701, symbol="US500m", type=mt5_mod.mt5.POSITION_TYPE_BUY,
            price_open=5000.0, price_current=5018.0, sl=4980.0, tp=5050.0,
            volume=0.20, profit=2.50, time=int(time.time()) - 3600, comment="GeminiBot_M15_SCAL",
        )
        mt5_mod.mt5.positions_get = lambda: (m15_pos_early,)
        # move_r = 18 / 20 = 0.90 < 1.00 -> NO debe mover SL aunque IA diga PROTECT_PROFIT y profit=$2.50
        acts_early = bot.manage_open_positions(
            {"US500m": m15_snap},
            open_reviews={"US500m": MT5PositionAIReview("US500m", 40, "PROTECT_PROFIT", False, "test")},
        )
        assert acts_early == []

        # Ahora move_r = 21 / 20 = 1.05 >= 1.00 -> mueve SL a BE +0.05R = 5000 + 1.0 = 5001.0
        m15_pos_be = SimpleNamespace(**{**m15_pos_early.__dict__, "price_current": 5021.0, "profit": 3.0})
        mt5_mod.mt5.positions_get = lambda: (m15_pos_be,)
        acts_be = bot.manage_open_positions({"US500m": m15_snap})
        assert len(acts_be) == 1
        assert acts_be[0]["new_sl"] == 5001.0
        assert acts_be[0]["new_tp"] == 5050.0  # Sin expansion TP

        # Ahora move_r = 45 / 20 = 2.25 -> M15 NO hace trailing (SL ya esta en 5001.0)
        m15_pos_run = SimpleNamespace(**{**m15_pos_be.__dict__, "price_current": 5045.0, "sl": 5001.0, "profit": 6.5})
        mt5_mod.mt5.positions_get = lambda: (m15_pos_run,)
        acts_run = bot.manage_open_positions({"US500m": m15_snap})
        assert acts_run == []

        # 2) H1: BE +0.25*ATR @ 1.25*ATR; Chandelier 1.50*ATR @ 1.50R SIN backdating pos.time (BUG-01)
        h1_snap = _make_test_snapshot(symbol="EURUSDm", bid=1.10500, ask=1.10510, atr_price=0.00100, atr_15_price=0.00050)
        old_open_ts = int(WedDatetime.now(timezone.utc).timestamp()) - 18000  # abierta hace 5 horas
        # Posicion H1 con SL ya en ganancia (pre-update como NZDUSDm) y move_r >= 1.50
        h1_pos = SimpleNamespace(
            ticket=702, symbol="EURUSDm", type=mt5_mod.mt5.POSITION_TYPE_BUY,
            price_open=1.10000, price_current=1.10500, sl=1.10030, tp=1.10750,
            volume=0.02, profit=10.0, time=old_open_ts, comment="GeminiBot_P1_EMA200",
        )
        mt5_mod.mt5.positions_get = lambda: (h1_pos,)
        acts_h1 = bot.manage_open_positions({"EURUSDm": h1_snap})
        assert len(acts_h1) == 1
        # init_sl_dist fallback = 3.0 * 0.0010 = 0.0030 -> move_r = 0.0050 / 0.0030 = 1.67 >= 1.50
        # Chandelier = 1.10500 - 1.50 * 0.00100 = 1.10350
        assert acts_h1[0]["new_sl"] == 1.10350
        # BUG-01 FIX: trail_start_ts es now_ts (NO old_open_ts!)
        assert bot.position_meta[702]["trail_start_ts"] == WedDatetime.now(timezone.utc).timestamp()
        assert bot.position_meta[702]["trail_start_ts"] != float(old_open_ts)

        # 3) AI_DEFENSIVE_CLOSE solo emergencia: tp_prob <= 25 y move_atr >= 0.75 y profit >= 0.40
        h1_pos_emg = SimpleNamespace(
            ticket=703, symbol="EURUSDm", type=mt5_mod.mt5.POSITION_TYPE_BUY,
            price_open=1.10000, price_current=1.10080, sl=1.09700, tp=1.10750,
            volume=0.01, profit=0.80, time=old_open_ts, comment="GeminiBot_P1_EMA200",
        )
        mt5_mod.mt5.positions_get = lambda: (h1_pos_emg,)
        # Con tp_prob=28 NO cierra (umbral endurecido a <= 25)
        acts_no_close = bot.manage_open_positions(
            {"EURUSDm": h1_snap},
            open_reviews={"EURUSDm": MT5PositionAIReview("EURUSDm", 28, "CLOSE_NOW", False, "borderline")},
        )
        assert acts_no_close == []
        # Con tp_prob=22 y move_atr=0.80 >= 0.75 SI cierra
        acts_close = bot.manage_open_positions(
            {"EURUSDm": h1_snap},
            open_reviews={"EURUSDm": MT5PositionAIReview("EURUSDm", 22, "CLOSE_NOW", False, "reversion")},
        )
        assert len(acts_close) == 1 and acts_close[0]["side"] == "CLOSE"

        # 4) _modify_mt5_sl_tp devuelve False cuando broker rechaza en modo LIVE
        bot.dry_run = False
        mt5_mod.mt5.order_send = lambda req: SimpleNamespace(retcode=10016, comment="Invalid stops")
        assert bot._modify_mt5_sl_tp(702, "EURUSDm", 1.1035, 1.1075) is False
    finally:
        mt5_mod.mt5.positions_get = orig_pos_get
        mt5_mod.mt5.symbol_info = orig_info
        mt5_mod.mt5.symbol_info_tick = orig_tick
        mt5_mod.mt5.order_send = orig_send
        mt5_mod.datetime = orig_datetime  # type: ignore[misc]


def test_suite2_sizing_veto_sl_compression_conv_scale_and_floor(tmp_path: Path) -> None:
    """Cubre BUG-03 & BUG-08: veto compresion SL >20%, conv_scale no aplasta max_risk, math.floor, precision lot_step y None."""
    import src.mt5_bot as mt5_mod

    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r2.md",
        history_file=tmp_path / "h2.json",
        ai_state_file=tmp_path / "a2.json",
    )
    orig_profit = mt5_mod.mt5.order_calc_profit
    orig_margin = mt5_mod.mt5.order_calc_margin
    try:
        # 1) Veto SL >20% en XAUUSDm/USTECm ($15 loss en min_lot vs $5.10 max en $600 -> compresion 66% > 20%)
        mt5_mod.mt5.order_calc_profit = lambda otype, sym, lot, p1, p2: -abs(p1 - p2) * 100.0 * lot
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 12.0 * (lot / 0.01)
        xau_wide = _make_test_snapshot(
            symbol="XAUUSDm", bid=2600.0, ask=2600.20, digits=2, point=0.01,
            atr_price=15.0, structural_long_sl=2585.20,  # $15.00 en 0.01 lot
        )
        lot_v, sl_v, tp_v, risk_v = bot.calculate_safe_lot_and_sl(xau_wide, "BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=75)
        assert (lot_v, sl_v, tp_v, risk_v) == (0.0, 0.0, 0.0, 0.0)

        # Compresion <= 20% ($6.00 vs $5.10 -> 15% <= 20%) SI se permite y calcula TP 2.5R
        xau_ok = _make_test_snapshot(
            symbol="XAUUSDm", bid=2600.0, ask=2600.20, digits=2, point=0.01,
            atr_price=2.0, structural_long_sl=2594.20,  # $6.00 en 0.01 lot
        )
        lot_c, sl_c, tp_c, risk_c = bot.calculate_safe_lot_and_sl(xau_ok, "BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=75)
        assert lot_c == 0.01 and risk_c <= 5.10
        assert round(tp_c - xau_ok.ask, 2) == round((xau_ok.ask - sl_c) * 2.5, 2)

        # 2) BUG-08: conv_scale=0.75 (ai_prob=62) NO reduce max_allowed_risk_usd ($5.10 en $600)
        xau_48 = _make_test_snapshot(
            symbol="XAUUSDm", bid=2600.0, ask=2600.20, digits=2, point=0.01,
            atr_price=2.0, structural_long_sl=2595.40,  # $4.80 en 0.01 lot
        )
        lot_low_conv, sl_low_conv, _, risk_low_conv = bot.calculate_safe_lot_and_sl(
            xau_48, "BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=62
        )
        assert lot_low_conv == 0.01 and sl_low_conv == 2595.40 and risk_low_conv == 4.80

        # 3) BUG-08: math.floor acotado nunca viola max_allowed_risk_usd ($2.65 por 0.01 -> 0.01, NO 0.02=$5.30)
        mt5_mod.mt5.order_calc_profit = lambda otype, sym, lot, p1, p2: -abs(p1 - p2) * 100000.0 * lot
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 4.0 * (lot / 0.01)
        fx_snap = _make_test_snapshot(
            symbol="EURUSDm", bid=1.10000, ask=1.10005, digits=5, point=0.00001,
            structural_long_sl=1.09740,  # 26.5 pips = $2.65 per 0.01 lot
        )
        lot_fl, _, _, risk_fl = bot.calculate_safe_lot_and_sl(fx_snap, "BUY", equity_usd=600.0, free_margin_usd=500.0, ai_probability_pct=75)
        assert lot_fl == 0.01 and risk_fl <= 5.10

        # 4) Sin caps arbitrarios (0.05 FX) en equity alto ($2000 -> target=$13, max=$17) y precision lot_step=0.001
        fx_step3 = _make_test_snapshot(
            symbol="EURUSDm", bid=1.10000, ask=1.10005, digits=5, point=0.00001,
            min_lot=0.001, lot_step=0.001, structural_long_sl=1.09905,  # $0.10 per 0.001 lot -> 0.130 lots para $13
        )
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 0.5 * (lot / 0.001)
        lot_hi, _, _, risk_hi = bot.calculate_safe_lot_and_sl(fx_step3, "BUY", equity_usd=2000.0, free_margin_usd=1800.0, ai_probability_pct=75)
        assert lot_hi > 0.05 and risk_hi <= 17.0
        assert round(lot_hi * 1000) == lot_hi * 1000

        # 5) Escalado gradual por margen (no cae abruptamente a min_lot)
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 25.0 * (lot / 0.01)
        fx_m = _make_test_snapshot(
            symbol="EURUSDm", bid=1.10000, ask=1.10005, digits=5, point=0.00001,
            min_lot=0.01, lot_step=0.01, structural_long_sl=1.09905,  # $1.00 per 0.01 -> target $13 quiere 0.12 lot ($300 margin)
        )
        # equity=2000, free=400 -> budget = min(140, 300) = 140 -> 140/25 = 5 steps -> 0.05 lot (gradual, no 0.01!)
        lot_grad, _, _, _ = bot.calculate_safe_lot_and_sl(fx_m, "BUY", equity_usd=2000.0, free_margin_usd=400.0, ai_probability_pct=75)
        assert lot_grad == 0.05

        # 6) order_calc_profit == None -> aborta seguro con (0,0,0,0)
        mt5_mod.mt5.order_calc_profit = lambda *a, **kw: None
        assert bot.calculate_safe_lot_and_sl(fx_m, "BUY", equity_usd=600.0, free_margin_usd=500.0) == (0.0, 0.0, 0.0, 0.0)
    finally:
        mt5_mod.mt5.order_calc_profit = orig_profit
        mt5_mod.mt5.order_calc_margin = orig_margin


def test_suite3_deterministic_shields_before_escudo5_and_utc_deals(tmp_path: Path) -> None:
    """Cubre BUG-05, BUG-06, BUG-10, BUG-12: orden determinista antes de Escudo 5, gemelos, USD_STRONG, NY 13-14:29, Noct 07-10:59 y UTC/magic/swap."""
    import src.mt5_bot as mt5_mod

    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r3.md",
        history_file=tmp_path / "h3.json",
        ai_state_file=tmp_path / "a3.json",
    )
    orig_profit = mt5_mod.mt5.order_calc_profit
    orig_margin = mt5_mod.mt5.order_calc_margin
    orig_deals = mt5_mod.mt5.history_deals_get
    orig_pos = mt5_mod.mt5.positions_get
    try:
        mt5_mod.mt5.order_calc_profit = lambda otype, sym, lot, p1, p2: -abs(p1 - p2) * 100000.0 * lot
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 4.0 * (lot / 0.01)

        eur_cand = _make_test_snapshot(symbol="EURUSDm", structural_long_sl=1.09750)  # $2.60 en 0.01 lot
        aud_cand = _make_test_snapshot(symbol="AUDUSDm", structural_long_sl=1.09750)
        ustec_cand = _make_test_snapshot(
            symbol="USTECm", bid=20000.0, ask=20001.0, spread_points=100, digits=2, point=0.01,
            min_lot=0.05, lot_step=0.01, atr_price=100.0, atr_15_price=40.0,
            entry_pillar="M15_SCALPER_PULLBACK_LONG", structural_long_sl=19921.0,
        )

        # NY Open 13:00-14:29 UTC bloquea; 14:35 UTC permite
        ok_1330, r_1330 = bot._passes_deterministic_shields(
            eur_cand, "BUY", datetime(2026, 11, 18, 13, 30, tzinfo=timezone.utc),
            set(), {"USD_LONG": 0, "USD_SHORT": 0}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_1330 is False and r_1330 == "NY_OPEN_13_1430"

        ok_1435, _ = bot._passes_deterministic_shields(
            eur_cand, "BUY", datetime(2026, 11, 18, 14, 35, tzinfo=timezone.utc),
            set(), {"USD_LONG": 0, "USD_SHORT": 0}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_1435 is True

        # Nocturno 07:00-10:59 UTC bloquea AUDUSDm; 04:00 UTC (Asia) permite
        ok_0830, r_0830 = bot._passes_deterministic_shields(
            aud_cand, "BUY", datetime(2026, 11, 18, 8, 30, tzinfo=timezone.utc),
            set(), {"USD_LONG": 0, "USD_SHORT": 0}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_0830 is False and r_0830 == "NOCTURNAL_07_11"

        ok_0400, _ = bot._passes_deterministic_shields(
            aud_cand, "BUY", datetime(2026, 11, 18, 4, 0, tzinfo=timezone.utc),
            set(), {"USD_LONG": 0, "USD_SHORT": 0}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_0400 is True

        # London Fix 16:15-17:00 UTC
        ok_lfix, r_lfix = bot._passes_deterministic_shields(
            eur_cand, "BUY", datetime(2026, 11, 18, 16, 30, tzinfo=timezone.utc),
            set(), {"USD_LONG": 0, "USD_SHORT": 0}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_lfix is False and r_lfix == "LONDON_FIX"

        # Block FX vs USD_STRONG
        ok_usd, r_usd = bot._passes_deterministic_shields(
            eur_cand, "BUY", datetime(2026, 11, 18, 15, 0, tzinfo=timezone.utc),
            set(), {"USD_LONG": 0, "USD_SHORT": 0}, "USD_STRONG_BULLISH", 600.0, 500.0, 1.0,
        )
        assert ok_usd is False and r_usd == "FX_VS_USD_STRONG"

        # Twin Cluster Cap max 1 (US500m abierto bloquea USTECm; NZDUSDm abierto bloquea AUDUSDm)
        ok_twin1, r_twin1 = bot._passes_deterministic_shields(
            ustec_cand, "BUY", datetime(2026, 11, 18, 15, 0, tzinfo=timezone.utc),
            {"US500m"}, {"USD_LONG": 0, "USD_SHORT": 0}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_twin1 is False and r_twin1 == "TWIN_CLUSTER"

        ok_twin2, r_twin2 = bot._passes_deterministic_shields(
            aud_cand, "BUY", datetime(2026, 11, 18, 15, 0, tzinfo=timezone.utc),
            {"NZDUSDm"}, {"USD_LONG": 0, "USD_SHORT": 0}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_twin2 is False and r_twin2 == "TWIN_CLUSTER"

        # Correlacion USD max 2 (incluyendo XAUUSDm)
        ok_corr, r_corr = bot._passes_deterministic_shields(
            eur_cand, "BUY", datetime(2026, 11, 18, 15, 0, tzinfo=timezone.utc),
            {"GBPUSDm", "XAUUSDm"}, {"USD_LONG": 0, "USD_SHORT": 2}, "USD_MIXED", 600.0, 500.0, 1.0,
        )
        assert ok_corr is False and r_corr == "USD_CORRELATION"

        # UTC + swap/commission + magic + exclusion de posicion aun abierta en _collect_recent_closed_deals
        ref_now = datetime(2026, 11, 18, 18, 0, 0, tzinfo=timezone.utc)
        ts_10m = int((ref_now - timedelta(minutes=10)).timestamp())
        mt5_mod.mt5.positions_get = lambda: (SimpleNamespace(ticket=888, identifier=888),)
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [
            # Parcial de posicion aun abierta (#888) -> DEBE IGNORARSE
            SimpleNamespace(ticket=1, position_id=888, entry=mt5_mod.mt5.DEAL_ENTRY_OUT, time=ts_10m, symbol="GBPUSDm", profit=1.50, swap=0.0, commission=0.0, reason=3, type=mt5_mod.mt5.DEAL_TYPE_SELL, magic=MT5_MAGIC_NUMBER),
            # Deal de otro EA (magic != MT5_MAGIC_NUMBER) -> DEBE IGNORARSE
            SimpleNamespace(ticket=2, position_id=889, entry=mt5_mod.mt5.DEAL_ENTRY_OUT, time=ts_10m, symbol="EURUSDm", profit=-5.0, swap=0.0, commission=0.0, reason=4, type=mt5_mod.mt5.DEAL_TYPE_SELL, magic=999999),
            # Deal bot con profit=+0.15 pero swap=-0.40 -> neto=-0.25 -> NEGATIVE!
            SimpleNamespace(ticket=3, position_id=890, entry=mt5_mod.mt5.DEAL_ENTRY_OUT, time=ts_10m, symbol="USDJPYm", profit=0.15, swap=-0.40, commission=0.0, reason=4, type=mt5_mod.mt5.DEAL_TYPE_BUY, magic=MT5_MAGIC_NUMBER),
        ]
        closes = bot._collect_recent_closed_deals(snapshots_map={}, minutes_back=90, now_utc=ref_now)
        assert len(closes) == 1
        assert closes[0]["position_id"] == 890
        assert closes[0]["profit_usd"] == -0.25
        assert closes[0]["close_type"] == "NEGATIVE"

        # Cierre manual overnight (>2h / ayer) de posicion del bot: persiste tras _prune_position_meta y reinicio (48h TTL) y via 14d known_bot_pos_ids
        mt5_mod.mt5.positions_get = lambda: ()
        bot.position_meta[777] = {"is_bot": True, "is_m15": False, "init_sl_dist": 0.003}
        assert bot._prune_position_meta(set()) is True
        assert 777 not in bot.position_meta and 777 in bot.recent_bot_pos_ids
        bot._save_ai_state()

        # Recargar bot como tras reinicio: debe seguir reconociendo cierre manual de #777 y excluir trade 100% manual #999
        bot_reloaded = ExnessMT5AutonomousBot(
            gemini_api_key="",
            dry_run=True,
            report_file=tmp_path / "r3.md",
            history_file=tmp_path / "h3.json",
            ai_state_file=tmp_path / "a3.json",
        )
        overnight_manual_out = SimpleNamespace(
            ticket=77702, position_id=777, entry=mt5_mod.mt5.DEAL_ENTRY_OUT, time=ts_10m,
            symbol="EURUSDm", profit=-19.0, swap=0.0, commission=0.0, reason=0,
            type=mt5_mod.mt5.DEAL_TYPE_SELL, magic=0,
        )
        pure_manual_out = SimpleNamespace(
            ticket=99902, position_id=999, entry=mt5_mod.mt5.DEAL_ENTRY_OUT, time=ts_10m,
            symbol="USDJPYm", profit=-25.0, swap=0.0, commission=0.0, reason=0,
            type=mt5_mod.mt5.DEAL_TYPE_SELL, magic=0,
        )
        mt5_mod.mt5.history_deals_get = lambda d1, d2: [overnight_manual_out, pure_manual_out]
        dg_after_prune = bot_reloaded._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0)
        assert dg_after_prune["closed_trades_today"] == 1
        assert dg_after_prune["daily_closed_pnl_usd"] == -19.0
        assert dg_after_prune["hard_daily_loss_stop"] is True
        rc_after_prune = bot_reloaded._collect_recent_closed_deals(snapshots_map={}, minutes_back=90, now_utc=ref_now)
        assert len(rc_after_prune) == 1 and rc_after_prune[0]["position_id"] == 777 and rc_after_prune[0]["close_type"] == "MANUAL"

        # Ruta (a): bot nuevo sin ai_state descubre #777 via _compute_symbol_performance_14d (DEAL_ENTRY_IN de ayer con magic del bot)
        bot_fresh = ExnessMT5AutonomousBot(
            gemini_api_key="",
            dry_run=True,
            report_file=tmp_path / "r3b.md",
            history_file=tmp_path / "h3b.json",
            ai_state_file=tmp_path / "a3b.json",
        )
        ts_yesterday = int((ref_now - timedelta(hours=30)).timestamp())
        overnight_in = SimpleNamespace(
            ticket=77701, position_id=777, entry=mt5_mod.mt5.DEAL_ENTRY_IN, time=ts_yesterday,
            symbol="EURUSDm", profit=0.0, swap=0.0, commission=0.0, reason=3,
            type=mt5_mod.mt5.DEAL_TYPE_BUY, magic=MT5_MAGIC_NUMBER,
        )
        pure_manual_in = SimpleNamespace(
            ticket=99901, position_id=999, entry=mt5_mod.mt5.DEAL_ENTRY_IN, time=ts_yesterday,
            symbol="USDJPYm", profit=0.0, swap=0.0, commission=0.0, reason=0,
            type=mt5_mod.mt5.DEAL_TYPE_BUY, magic=0,
        )
        mt5_mod.mt5.history_deals_get = lambda d1, d2: (
            [overnight_in, overnight_manual_out, pure_manual_in, pure_manual_out]
            if (d2 - d1).days >= 7
            else [overnight_manual_out, pure_manual_out]
        )
        bot_fresh._compute_symbol_performance_14d(now_utc=ref_now)
        assert 777 in bot_fresh.known_bot_pos_ids and 999 not in bot_fresh.known_bot_pos_ids
        dg_14d = bot_fresh._evaluate_daily_risk_guard(now_utc=ref_now, equity_usd=600.0, known_bot_pos_ids=bot_fresh.known_bot_pos_ids)
        assert dg_14d["closed_trades_today"] == 1 and dg_14d["daily_closed_pnl_usd"] == -19.0
    finally:
        mt5_mod.mt5.order_calc_profit = orig_profit
        mt5_mod.mt5.order_calc_margin = orig_margin
        mt5_mod.mt5.history_deals_get = orig_deals
        mt5_mod.mt5.positions_get = orig_pos


def test_suite4_event_driven_ai_all_cooldown_and_hold_protection(tmp_path: Path) -> None:
    """Cubre BUG-06 & BUG-13: event-driven IA en run_cycle (0 llamadas idle, ATR milestone, heartbeat), 4 modelos en cooldown y _safe_int."""
    import src.gemini_agent as gemini_mod
    import src.mt5_bot as mt5_mod

    # 1) 4 modelos en cooldown -> RuntimeError inmediato en 0ms sin 1 sola llamada HTTP
    called_urls: list[str] = []
    orig_post = gemini_mod.requests.post
    try:
        def fake_post(url: str, **kwargs: Any) -> Any:
            called_urls.append(url)
            return SimpleNamespace(status_code=200, json=lambda: {"candidates": [{"content": {"parts": [{"text": "{}"}]}}]})

        gemini_mod.requests.post = fake_post
        agent = GeminiTradingAgent(api_key="test-key", model="gemini-3.5-flash")
        future_ts = time.time() + 600.0
        for mdl in agent._get_models_for_priority(high_priority=True):
            agent._model_cooldown_until[mdl] = future_ts
        threw = False
        try:
            agent._call_gemini("ping", high_priority=True, trigger_reason="TEST")
        except RuntimeError as exc:
            threw = "cooldown" in str(exc).lower()
        assert threw is True
        assert called_urls == []

        # evaluate_mt5_market cae limpiamente a quant_local en 0ms
        fallback_eval = agent.evaluate_mt5_market(
            open_positions_data=[],
            candidates_data=[{"symbol": "EURUSDm", "side": "BUY", "entry_pillar": "P1_EMA200_PULLBACK_LONG", "snapshot": asdict(_make_test_snapshot())}],
            recent_closes_data=[],
            high_priority=True,
            trigger_reason="CANDIDATES",
        )
        assert fallback_eval.model_used == "quant_local"
        assert called_urls == []

        # _safe_int con float string "67.5" en _build_mt5_eval_result
        parsed_float = {
            "market_summary": "ok",
            "open_reviews": [{"symbol": "EURUSDm", "tp_probability_pct": "67.5", "action": "HOLD", "reasoning": "solid"}],
            "candidate_evals": [],
            "closed_evals": [],
        }
        built = agent._build_mt5_eval_result(
            parsed=parsed_float,
            enriched_open=[{"symbol": "EURUSDm", "profit_usd": 2.0, "move_atr": 0.5, "snapshot": {"dist_to_ema200_atr": 7.0}}],
            enriched_cands=[],
            enriched_closes=[],
            quant_open={"EURUSDm": (72, "ok")},
            quant_cand={},
            quant_closed={},
            fallback_reason=None,
            priority_tier="ALTA_PRIORIDAD",
            model_used="gemini-4-hydrogen",
            news_alert=True,
        )
        assert built.open_reviews["EURUSDm"].action == "HOLD"
        assert built.open_reviews["EURUSDm"].tp_probability_pct == round(0.45 * 68 + 0.55 * 72)
    finally:
        gemini_mod.requests.post = orig_post

    # 2) Event-driven run_cycle: 0 llamadas en idle y durante blackout NY; llama en hito ATR y heartbeat
    bot = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r4.md",
        history_file=tmp_path / "h4.json",
        ai_state_file=tmp_path / "a4.json",
    )
    ai_calls: list[dict[str, Any]] = []

    def spy_eval(**kwargs: Any) -> MT5AICycleEvaluation:
        ai_calls.append(kwargs)
        open_revs = {
            p["symbol"]: MT5PositionAIReview(p["symbol"], 75, "HOLD", False, "ok")
            for p in kwargs.get("open_positions_data", [])
        }
        cand_evals = {
            c["symbol"]: MT5CandidateAIEval(c["symbol"], 45, True, "low prob")
            for c in kwargs.get("candidates_data", [])
        }
        return MT5AICycleEvaluation("spy", open_revs, cand_evals, {}, "ALTA_PRIORIDAD" if kwargs.get("high_priority") else "GENERAL", "spy_model")

    orig_pos = mt5_mod.mt5.positions_get
    orig_deals = mt5_mod.mt5.history_deals_get
    orig_profit = mt5_mod.mt5.order_calc_profit
    orig_margin = mt5_mod.mt5.order_calc_margin
    orig_info = mt5_mod.mt5.symbol_info
    orig_acc = mt5_mod.mt5.account_info
    orig_dt = mt5_mod.datetime

    class NyBlackoutDatetime(datetime):
        @classmethod
        def now(cls, tz=None):  # type: ignore[override]
            return datetime(2026, 11, 18, 13, 30, 0, tzinfo=timezone.utc)

    try:
        bot.ensure_connected = lambda: (SimpleNamespace(connected=True), SimpleNamespace(login=1, server="Exness", leverage=500, balance=600.0, equity=600.0, margin_free=550.0))  # type: ignore[method-assign]
        bot.ai_agent.evaluate_mt5_market = spy_eval  # type: ignore[method-assign]
        mt5_mod.mt5.account_info = lambda: SimpleNamespace(login=1, server="Exness", leverage=500, balance=600.0, equity=600.0, margin_free=550.0)
        mt5_mod.mt5.history_deals_get = lambda d1, d2: []
        mt5_mod.mt5.order_calc_profit = lambda otype, sym, lot, p1, p2: -abs(p1 - p2) * 100000.0 * lot
        mt5_mod.mt5.order_calc_margin = lambda otype, sym, lot, price: 4.0 * (lot / 0.01)
        mt5_mod.mt5.symbol_info = lambda sym: SimpleNamespace(digits=5, point=0.00001, spread=10, volume_min=0.01, volume_step=0.01, trade_stops_level=5, filling_mode=2)

        # Ciclo A: durante NY Blackout (13:30 UTC) con candidato EURUSDm -> escudo determinista filtra ANTES de Gemini -> 0 llamadas IA y 0 bloqueos 90m!
        mt5_mod.datetime = NyBlackoutDatetime  # type: ignore[misc]
        mt5_mod.mt5.positions_get = lambda: ()
        bot.build_snapshots = lambda free_margin_usd, open_symbols: [_make_test_snapshot(symbol="EURUSDm", structural_long_sl=1.09750)]  # type: ignore[method-assign]
        summary_a = bot.run_cycle(1)
        assert len(ai_calls) == 0
        assert summary_a["ai_model"] == "quant_local"
        assert bot.get_active_block("EURUSDm") is None

        # Ciclo B: con posicion abierta en 0.2 ATR -> 1ra vez dispara OPEN_SET_CHANGED; 2da vez sin cambio -> 0 llamadas adicionales
        pos_cur = SimpleNamespace(
            ticket=900, identifier=900, symbol="EURUSDm", type=mt5_mod.mt5.POSITION_TYPE_BUY,
            price_open=1.10000, price_current=1.10020, sl=1.09700, tp=1.10750,
            volume=0.01, profit=0.20, time=int(NyBlackoutDatetime.now(timezone.utc).timestamp()) - 600, comment="GeminiBot_P1_EMA200",
        )
        mt5_mod.mt5.positions_get = lambda: (pos_cur,)
        bot.build_snapshots = lambda free_margin_usd, open_symbols: [_make_test_snapshot(symbol="EURUSDm", strategy_setup="WATCH", entry_pillar="NONE")]  # type: ignore[method-assign]
        bot.run_cycle(2)
        assert len(ai_calls) == 1 and "OPEN_SET_CHANGED" in ai_calls[-1]["trigger_reason"]

        bot.run_cycle(3)
        assert len(ai_calls) == 1  # Cache reutilizado: 0 llamadas API

        # Ciclo C: cruza hito ATR (>= 0.75 ATR) -> dispara ALTA_PRIORIDAD con ATR_MILESTONE
        pos_milestone = SimpleNamespace(**{**pos_cur.__dict__, "price_current": 1.10085, "profit": 0.85})
        mt5_mod.mt5.positions_get = lambda: (pos_milestone,)
        bot.run_cycle(4)
        assert len(ai_calls) == 2 and "ATR_MILESTONE" in ai_calls[-1]["trigger_reason"] and ai_calls[-1]["high_priority"] is True

        # Ciclo D: heartbeat >= 900s con posicion abierta -> dispara GENERAL con HEARTBEAT_900S
        bot.last_ai_eval_ts = time.time() - 950.0
        bot.run_cycle(5)
        assert len(ai_calls) == 3 and "HEARTBEAT_900S" in ai_calls[-1]["trigger_reason"] and ai_calls[-1]["high_priority"] is False

        # Ciclo E: SL apretado en ganancia (BE/Chandelier: profit > 0 y rem_sl = 0.25 <= 0.45) NO dispara HP repetido
        pos_tight_be = SimpleNamespace(**{**pos_milestone.__dict__, "price_current": 1.10085, "sl": 1.10060, "profit": 0.85})
        mt5_mod.mt5.positions_get = lambda: (pos_tight_be,)
        bot.run_cycle(6)
        bot.run_cycle(7)
        assert len(ai_calls) == 3  # 0 llamadas HP en ganancia con SL apretado

        # Ciclo F: rem_sl <= 0.45 en perdida es edge-triggered con histeresis (dispara 1 vez, NO repite en ciclos consecutivos)
        pos_danger1 = SimpleNamespace(**{**pos_cur.__dict__, "price_current": 1.09735, "sl": 1.09700, "profit": -2.65})
        mt5_mod.mt5.positions_get = lambda: (pos_danger1,)
        bot.run_cycle(8)
        assert len(ai_calls) == 4 and "ATR_MILESTONE" in ai_calls[-1]["trigger_reason"] and ai_calls[-1]["high_priority"] is True

        # Ciclos consecutivos en peligro (0.30 ATR y 0.50 ATR dentro de histeresis <= 0.55) -> 0 llamadas extra
        pos_danger2 = SimpleNamespace(**{**pos_cur.__dict__, "price_current": 1.09730, "sl": 1.09700, "profit": -2.70})
        mt5_mod.mt5.positions_get = lambda: (pos_danger2,)
        bot.run_cycle(9)
        pos_hyst = SimpleNamespace(**{**pos_cur.__dict__, "price_current": 1.09750, "sl": 1.09700, "profit": -2.50})
        mt5_mod.mt5.positions_get = lambda: (pos_hyst,)
        bot.run_cycle(10)
        assert len(ai_calls) == 4

        # Recuperacion fuera de histeresis (rem_sl = 0.70 > 0.55) resetea estado sin llamar IA; nuevo re-ingreso SI dispara
        pos_recover = SimpleNamespace(**{**pos_cur.__dict__, "price_current": 1.09770, "sl": 1.09700, "profit": -2.30})
        mt5_mod.mt5.positions_get = lambda: (pos_recover,)
        bot.run_cycle(11)
        assert len(ai_calls) == 4 and bot._last_ai_sl_danger.get(900) is False
        mt5_mod.mt5.positions_get = lambda: (pos_danger1,)
        bot.run_cycle(12)
        assert len(ai_calls) == 5 and "ATR_MILESTONE" in ai_calls[-1]["trigger_reason"]
    finally:
        mt5_mod.mt5.positions_get = orig_pos
        mt5_mod.mt5.history_deals_get = orig_deals
        mt5_mod.mt5.order_calc_profit = orig_profit
        mt5_mod.mt5.order_calc_margin = orig_margin
        mt5_mod.mt5.symbol_info = orig_info
        mt5_mod.mt5.account_info = orig_acc
        mt5_mod.datetime = orig_dt  # type: ignore[misc]


def test_suite5_indicators_ema_sma_seed_wilder_morning_star_and_atomic_state(tmp_path: Path) -> None:
    """Cubre BUG-04, BUG-09, BUG-11: EMA semilla SMA, Wilder ADX/ATR, MORNING_STAR + min_range y persistencia atomica."""
    # 1) calc_ema_series con semilla SMA en indice period-1
    vals = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
    ema3 = calc_ema_series(vals, 3)
    assert len(ema3) == len(vals)
    assert ema3[2] == 20.0  # SMA(10, 20, 30)
    k = 2.0 / 4.0
    assert abs(ema3[3] - (40.0 * k + 20.0 * (1.0 - k))) < 1e-9
    # Compatibilidad si len < period
    assert len(calc_ema_series([10.0, 20.0], 5)) == 2

    # 2) calc_adx: default 20.0 si faltan velas; > 30 en tendencia fuerte
    short_c = [{"open": 100.0, "high": 101.0, "low": 99.0, "close": 100.5}] * 10
    assert calc_adx(short_c, 14) == 20.0
    trend_c = [
        {"open": 100.0 + i * 2.0, "high": 102.5 + i * 2.0, "low": 99.5 + i * 2.0, "close": 102.0 + i * 2.0}
        for i in range(60)
    ]
    assert calc_adx(trend_c, 14) > 30.0

    # 3) calc_atr_wilder: Wilder RMA 14
    atr_c = [
        {"open": 100.0, "high": 102.0, "low": 100.0, "close": 101.0}
        for _ in range(20)
    ]
    assert abs(calc_atr_wilder(atr_c, 14) - 2.0) < 1e-9

    # 4) detect_candle_pattern: min_range y MORNING_STAR con vela central pequena
    hammer = {"open": 101.0, "high": 102.5, "low": 95.0, "close": 102.0}  # range = 7.5
    prev = {"open": 105.0, "high": 106.0, "low": 100.0, "close": 101.0}
    assert detect_candle_pattern(hammer, prev, min_range=10.0) == "NONE"
    assert detect_candle_pattern(hammer, prev, min_range=5.0) == "BULLISH_HAMMER"

    p2_bear = {"open": 110.0, "high": 111.0, "low": 100.0, "close": 100.0}  # body = 10
    mid_small = {"open": 100.0, "high": 102.0, "low": 99.0, "close": 101.0}  # body = 1 (small)
    mid_big = {"open": 100.0, "high": 109.0, "low": 99.5, "close": 108.5}  # body = 8.5 (too large for morning star)
    sig_bull = {"open": 101.5, "high": 110.5, "low": 101.0, "close": 109.5}  # bullish close > mid(p2)=105
    assert detect_candle_pattern(sig_bull, mid_small, p2_bear) == "MORNING_STAR"
    assert detect_candle_pattern(sig_bull, mid_big, p2_bear) != "MORNING_STAR"

    # 5) Persistencia atomica de position_meta y last_order_timestamp tras reinicio + depuracion de tickets cerrados
    ai_state = tmp_path / "atomic_state.json"
    bot1 = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r5.md",
        history_file=tmp_path / "h5.json",
        ai_state_file=ai_state,
    )
    bot1.last_order_timestamp = 1795000000.0
    bot1.position_meta[555] = {
        "is_m15": True,
        "init_sl_dist": 15.0,
        "atr1h_at_entry": 20.0,
        "atr15_at_entry": 7.5,
        "peak_price": 5050.0,
        "peak_ts": 1795000100.0,
        "trail_start_ts": 1795000200.0,
    }
    bot1._save_ai_state()
    assert ai_state.exists()
    raw_saved = json.loads(ai_state.read_text(encoding="utf-8"))
    assert raw_saved["last_order_timestamp"] == 1795000000.0
    assert "555" in raw_saved["position_meta"]

    bot2 = ExnessMT5AutonomousBot(
        gemini_api_key="",
        dry_run=True,
        report_file=tmp_path / "r5.md",
        history_file=tmp_path / "h5.json",
        ai_state_file=ai_state,
    )
    assert bot2.last_order_timestamp == 1795000000.0
    assert bot2.position_meta[555]["is_m15"] is True
    assert bot2.peak_prices[555] == 5050.0
    assert bot2.profit_trail_start_ts[555] == 1795000200.0
    # Depuracion de tickets cerrados
    assert bot2._prune_position_meta(set()) is True
    assert 555 not in bot2.position_meta


if __name__ == "__main__":
    test_symbol_filters_rounding()
    test_candlestick_patterns_and_stochastic()
    test_1pct_risk_position_sizing()
    test_dynamic_sl_tp_trailing_and_ai_adjust(Path(tempfile.mkdtemp()))
    test_futures_short_entry_and_downward_trailing(Path(tempfile.mkdtemp()))
    test_mt5_ai_evaluation_and_90m_blocking(Path(tempfile.mkdtemp()))
    test_mt5_conviction_sizing_correlation_and_14d_perf(Path(tempfile.mkdtemp()))
    test_gemini_priority_model_routing()
    test_global_market_context_confluence_and_news_shield(Path(tempfile.mkdtemp()))
    test_pre_rollover_blackout_and_harvest_windows()
    test_mt5_overextension_and_daily_guard_quant_penalties(Path(tempfile.mkdtemp()))
    test_mt5_daily_risk_guard_m15_filters_and_risk_scale(Path(tempfile.mkdtemp()))
    test_mt5_build_snapshots_m15_exclusion_and_dist_limit(Path(tempfile.mkdtemp()))
    test_suite1_clean_diff_exits_h1_m15_and_no_backdating(Path(tempfile.mkdtemp()))
    test_suite2_sizing_veto_sl_compression_conv_scale_and_floor(Path(tempfile.mkdtemp()))
    test_suite3_deterministic_shields_before_escudo5_and_utc_deals(Path(tempfile.mkdtemp()))
    test_suite4_event_driven_ai_all_cooldown_and_hold_protection(Path(tempfile.mkdtemp()))
    test_suite5_indicators_ema_sma_seed_wilder_morning_star_and_atomic_state(Path(tempfile.mkdtemp()))
    print("Todas las pruebas (18 suites, incluyendo BUG-01..13 y B_FINAL_HYBRID_ADX_0.65PCT) pasaron exitosamente.")
