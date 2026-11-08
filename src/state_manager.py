from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


@dataclass
class PositionState:
    symbol: str
    base_asset: str
    quantity: float
    entry_price: float
    highest_price: float
    stop_loss_price: float
    take_profit_price: float
    opened_at: str
    entry_reason: str = ""

    def unrealized_pnl_pct(self, current_price: float) -> float:
        if self.entry_price <= 0:
            return 0.0
        return ((current_price - self.entry_price) / self.entry_price) * 100.0

    def drawdown_from_peak_pct(self, current_price: float) -> float:
        peak = max(self.highest_price, self.entry_price)
        if peak <= 0:
            return 0.0
        return ((peak - current_price) / peak) * 100.0


@dataclass
class BotState:
    updated_at: str = field(default_factory=utc_now_iso)
    daily_date: str = field(default_factory=utc_today_str)
    daily_start_equity_usdt: float = 0.0
    last_equity_usdt: float = 0.0
    total_cycles: int = 0
    positions: dict[str, PositionState] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "updated_at": self.updated_at,
            "daily_date": self.daily_date,
            "daily_start_equity_usdt": round(self.daily_start_equity_usdt, 4),
            "last_equity_usdt": round(self.last_equity_usdt, 4),
            "total_cycles": self.total_cycles,
            "positions": {sym: asdict(pos) for sym, pos in self.positions.items()},
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BotState:
        raw_positions = data.get("positions", {}) or {}
        positions: dict[str, PositionState] = {}
        for sym, pos_dict in raw_positions.items():
            positions[sym] = PositionState(
                symbol=pos_dict["symbol"],
                base_asset=pos_dict.get("base_asset", sym.replace("USDT", "")),
                quantity=float(pos_dict["quantity"]),
                entry_price=float(pos_dict["entry_price"]),
                highest_price=float(pos_dict.get("highest_price", pos_dict["entry_price"])),
                stop_loss_price=float(pos_dict.get("stop_loss_price", 0.0)),
                take_profit_price=float(pos_dict.get("take_profit_price", 0.0)),
                opened_at=pos_dict.get("opened_at", utc_now_iso()),
                entry_reason=pos_dict.get("entry_reason", ""),
            )
        return cls(
            updated_at=data.get("updated_at", utc_now_iso()),
            daily_date=data.get("daily_date", utc_today_str()),
            daily_start_equity_usdt=float(data.get("daily_start_equity_usdt", 0.0)),
            last_equity_usdt=float(data.get("last_equity_usdt", 0.0)),
            total_cycles=int(data.get("total_cycles", 0)),
            positions=positions,
        )


class StateManager:
    """Administra la persistencia del estado y el historial de operaciones en el repositorio."""

    def __init__(self, state_file: Path, history_file: Path, report_file: Path) -> None:
        self.state_file = state_file
        self.history_file = history_file
        self.report_file = report_file
        self.state_file.parent.mkdir(parents=True, exist_ok=True)

    def load_state(self) -> BotState:
        if not self.state_file.exists():
            return BotState()
        try:
            data = json.loads(self.state_file.read_text(encoding="utf-8"))
            return BotState.from_dict(data)
        except Exception as exc:
            logger.warning("No se pudo leer %s (%s). Inicializando estado limpio.", self.state_file, exc)
            return BotState()

    def save_state(self, state: BotState) -> None:
        state.updated_at = utc_now_iso()
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(
            json.dumps(state.to_dict(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def load_history(self) -> list[dict[str, Any]]:
        if not self.history_file.exists():
            return []
        try:
            return json.loads(self.history_file.read_text(encoding="utf-8"))
        except Exception:
            return []

    def append_trade(self, trade_record: dict[str, Any], max_records: int = 500) -> None:
        history = self.load_history()
        history.append(trade_record)
        if len(history) > max_records:
            history = history[-max_records:]
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        self.history_file.write_text(
            json.dumps(history, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def write_report(self, markdown_content: str) -> None:
        self.report_file.parent.mkdir(parents=True, exist_ok=True)
        self.report_file.write_text(markdown_content, encoding="utf-8")
