from __future__ import annotations

from decimal import Decimal
from pathlib import Path
from typing import Any

from src.binance_client import SymbolFilters
from src.bot_engine import AutonomousTradingBot
from src.config import BotConfig
from src.gemini_agent import AIAnalysisResult, AIDecision, GeminiTradingAgent
from src.market_scanner import (
    MarketScanner,
    TechnicalSnapshot,
    calc_bollinger_bands,
    calc_ema_series,
    calc_macd,
    calc_rsi,
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
    def is_eligible_symbol(self, symbol: str) -> bool:
        return symbol.endswith("USDT") and not symbol.startswith("USDC")

    def build_snapshots(self, must_include_symbols: list[str] | None = None) -> list[TechnicalSnapshot]:
        return [
            TechnicalSnapshot(
                symbol="SOLUSDT",
                current_price=210.0,
                price_change_24h_pct=6.5,
                quote_volume_24h_usdt=450_000_000.0,
                high_24h=215.0,
                low_24h=195.0,
                rsi_14=58.0,
                ema_9=208.0,
                ema_21=204.0,
                ema_50=198.0,
                trend_primary="BULLISH",
                macd_line=1.5,
                macd_signal=1.1,
                macd_hist=0.4,
                bb_upper=216.0,
                bb_lower=196.0,
                bb_pct_b=0.7,
                atr_pct=1.8,
                volume_ratio=1.45,
                support_level=200.0,
                resistance_level=215.0,
                htf_rsi_14=61.0,
                htf_ema_21=202.0,
                htf_ema_50=194.0,
                htf_trend="BULLISH",
            )
        ]


class FakeAIAgent:
    def __init__(self, decisions: list[AIDecision]) -> None:
        self._decisions = decisions

    def analyze_market(self, **kwargs: Any) -> AIAnalysisResult:
        return AIAnalysisResult(
            market_regime="BULLISH",
            summary="Tendencia alcista saludable en SOLUSDT.",
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


def test_technical_indicators() -> None:
    closes = [100.0 + i * 0.8 for i in range(60)]
    rsi = calc_rsi(closes, 14)
    assert 70.0 <= rsi <= 100.0

    ema9 = calc_ema_series(closes, 9)
    assert len(ema9) == 60
    assert ema9[-1] > ema9[0]

    macd_l, macd_s, _ = calc_macd(closes)
    assert macd_l > 0 and macd_s > 0

    upper, lower, pct_b = calc_bollinger_bands(closes, 20, 2.0)
    assert upper > lower
    assert 0.5 <= pct_b <= 1.2


def test_gemini_json_parser() -> None:
    agent = GeminiTradingAgent(api_key="test-key")
    raw = """```json
    {
      "market_regime": "BULLISH",
      "summary": "Mercado con fuerte impulso comprador.",
      "decisions": [
        {
          "symbol": "SOLUSDT",
          "action": "BUY",
          "confidence": 85,
          "allocation_pct": 0.30,
          "stop_loss_pct": 0.035,
          "take_profit_pct": 0.070,
          "reasoning": "Ruptura de EMA 21 con volumen."
        }
      ]
    }
    ```"""
    res = agent._parse_response(raw, max_position_pct=0.25, default_sl_pct=0.035, default_tp_pct=0.07)
    assert res.market_regime == "BULLISH"
    assert len(res.decisions) == 1
    # Verifica que allocation_pct se limite automaticamente a max_position_pct (0.25)
    assert res.decisions[0].allocation_pct == 0.25


def test_bot_cycle_stop_loss_and_ai_buy(tmp_path: Path) -> None:
    cfg = BotConfig(
        binance_api_key="key",
        binance_api_secret="secret",
        gemini_api_key="gemini",
        dry_run=False,
        max_open_positions=3,
        max_position_pct=0.25,
        stop_loss_pct=0.035,
        take_profit_pct=0.070,
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
                confidence=84,
                allocation_pct=0.20,
                stop_loss_pct=0.035,
                take_profit_pct=0.070,
                reasoning="Impulso alcista confirmado en 15m y 1h.",
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

    # Ciclo 1: adopta ETHUSDT existente y compra SOLUSDT recomendado por Gemini
    summary = bot.run_cycle()
    assert "SOLUSDT" in summary["open_positions"]
    assert "ETHUSDT" in summary["open_positions"]
    assert len(fake_client.buys) == 1
    assert fake_client.buys[0][0] == "SOLUSDT"

    # Ciclo 2: simulamos caida de ETHUSDT por debajo de su Stop-Loss (-5%)
    fake_client.prices["ETHUSDT"] = 3000.0
    summary_2 = bot.run_cycle()
    assert len(fake_client.sells) == 1
    assert fake_client.sells[0][0] == "ETHUSDT"
    assert "ETHUSDT" not in summary_2["open_positions"]


if __name__ == "__main__":
    import tempfile

    test_symbol_filters_rounding()
    test_technical_indicators()
    test_gemini_json_parser()
    test_bot_cycle_stop_loss_and_ai_buy(Path(tempfile.mkdtemp()))
    print("Todas las pruebas unitarias e integrales pasaron exitosamente.")

