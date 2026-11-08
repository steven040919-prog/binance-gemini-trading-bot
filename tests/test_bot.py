from __future__ import annotations

import tempfile
from decimal import Decimal
from pathlib import Path
from typing import Any

from src.binance_client import SymbolFilters
from src.bot_engine import AutonomousTradingBot, calculate_position_size_1pct_risk
from src.config import BotConfig
from src.gemini_agent import AIAnalysisResult, AIDecision, GeminiTradingAgent
from src.market_scanner import (
    TechnicalSnapshot,
    calc_bollinger_bands,
    calc_ema_series,
    calc_macd,
    calc_rsi,
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

    def get_all_prices(self) -> dict[str, float]:
        return dict(self.prices)

    def get_account_balances(self) -> dict[str, float]:
        return dict(self.balances)

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
        self.eth_stoch_k = 45.0

    def is_eligible_symbol(self, symbol: str) -> bool:
        return symbol.endswith("USDT") and not symbol.startswith("USDC")

    def build_snapshots(self, must_include_symbols: list[str] | None = None) -> list[TechnicalSnapshot]:
        return [
            TechnicalSnapshot(
                symbol="SOLUSDT",
                current_price=210.0,
                price_change_24h_pct=4.5,
                quote_volume_24h_usdt=450_000_000.0,
                high_24h=215.0,
                low_24h=195.0,
                ema_200=195.0,
                above_ema_200=True,
                stoch_k=self.sol_stoch_k,
                stoch_d=19.5,
                stoch_recent_min=16.0,
                stoch_recent_max=28.0,
                candle_pattern="BULLISH_ENGULFING",
                prev_candle_low=205.8,  # 2% bajo 210.0
                prev_candle_high=212.0,
                strategy_setup="LONG_ENTRY",
                rsi_14=42.0,
                ema_9=208.0,
                ema_21=204.0,
                ema_50=198.0,
                trend_primary="BULLISH",
                macd_line=1.5,
                macd_signal=1.1,
                macd_hist=0.4,
                bb_upper=216.0,
                bb_lower=196.0,
                bb_pct_b=0.3,
                atr_pct=1.8,
                volume_ratio=1.45,
                support_level=205.8,
                resistance_level=215.0,
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
                candle_pattern="NONE",
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
        self._decisions = decisions

    def analyze_market(self, **kwargs: Any) -> AIAnalysisResult:
        return AIAnalysisResult(
            market_regime="BULLISH",
            summary="SOLUSDT sobre EMA 200 con Estocastico en 18 y vela envolvente alcista.",
            decisions=self._decisions,
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
    # 1. Bullish Hammer
    prev = {"open": 105.0, "high": 106.0, "low": 100.0, "close": 101.0}
    hammer = {"open": 101.0, "high": 102.5, "low": 95.0, "close": 102.0}
    assert detect_candle_pattern(hammer, prev) == "BULLISH_HAMMER"

    # 2. Bullish Engulfing
    prev_red = {"open": 102.0, "high": 102.5, "low": 99.5, "close": 100.0}
    curr_green = {"open": 99.8, "high": 103.0, "low": 99.5, "close": 102.5}
    assert detect_candle_pattern(curr_green, prev_red) == "BULLISH_ENGULFING"

    # 3. Bearish Shooting Star
    prev_up = {"open": 100.0, "high": 104.0, "low": 99.5, "close": 103.5}
    star = {"open": 103.5, "high": 110.0, "low": 102.5, "close": 102.8}
    assert detect_candle_pattern(star, prev_up) == "BEARISH_SHOOTING_STAR"

    # 4. Bearish Engulfing
    prev_green = {"open": 100.0, "high": 102.5, "low": 99.5, "close": 102.0}
    curr_red = {"open": 102.2, "high": 102.5, "low": 99.0, "close": 99.5}
    assert detect_candle_pattern(curr_red, prev_green) == "BEARISH_ENGULFING"

    # 5. Stochastic (14, 3, 3)
    candles = [{"open": 100 + i, "high": 102 + i, "low": 99 + i, "close": 101.5 + i} for i in range(25)]
    k_s, d_s = calc_stochastic(candles, 14, 3, 3)
    assert len(k_s) > 5 and 70.0 <= k_s[-1] <= 100.0 and 70.0 <= d_s[-1] <= 100.0


def test_1pct_risk_position_sizing() -> None:
    # Cuenta de $500 USD -> 1% de riesgo = $5 USD
    # Entrada en $100, Stop-Loss (bajo vela previa) en $98 (distancia 2%)
    # Para arriesgar $5 USD con 2% de SL, tamano ideal = $5 / 0.02 = $250 USD (acotado a max_position_pct=0.35 -> $175 USD)
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

    # Cuenta pequena de $50 USD -> 1% es $0.50, pero aplica piso minimo de $1.00 USD
    _, min_r = calculate_position_size_1pct_risk(
        total_equity_usdt=50.0,
        available_usdt=50.0,
        entry_price=100.0,
        stop_loss_price=95.0,
        risk_pct=0.01,
        min_risk_usd=1.0,
    )
    assert min_r == 1.0


def test_bot_cycle_strategy_ema200_stoch_and_exits(tmp_path: Path) -> None:
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
                take_profit_pct=0.06,
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

    # Ciclo 1: compra SOLUSDT con Stop-Loss en prev_candle_low (205.8)
    summary = bot.run_cycle()
    assert "SOLUSDT" in summary["open_positions"]
    saved_state = sm.load_state()
    assert saved_state.positions["SOLUSDT"].stop_loss_price == 205.8

    # Ciclo 2: el Estocastico de ETHUSDT llega a 82 (>= 80) -> debe cerrar ETHUSDT automaticamente
    fake_scanner.eth_stoch_k = 82.5
    summary_2 = bot.run_cycle()
    assert "ETHUSDT" not in summary_2["open_positions"]
    assert any(s[0] == "ETHUSDT" for s in fake_client.sells)


if __name__ == "__main__":
    test_symbol_filters_rounding()
    test_candlestick_patterns_and_stochastic()
    test_1pct_risk_position_sizing()
    test_bot_cycle_strategy_ema200_stoch_and_exits(Path(tempfile.mkdtemp()))
    print("Todas las pruebas de la estrategia EMA 200 + Estocastico (80/20) + Velas pasaron exitosamente.")
