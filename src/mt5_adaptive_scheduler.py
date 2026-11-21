from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

VALID_WATCH_STATUSES: tuple[str, ...] = (
    "ACTIVE",
    "POSTPONED",
    "TRIGGERED",
    "INVALIDATED",
    "EXPIRED",
)
ACTIVE_WATCH_STATUSES: frozenset[str] = frozenset({"ACTIVE", "POSTPONED"})


def ensure_utc(dt: datetime | str | None, default: datetime | None = None) -> datetime:
    """Normalize a datetime or ISO-8601 string into a timezone-aware UTC datetime."""
    if dt is None:
        if default is not None:
            return ensure_utc(default)
        return datetime.now(timezone.utc)
    if isinstance(dt, str):
        raw = dt.strip()
        if raw.endswith("Z"):
            raw = raw[:-1] + "+00:00"
        parsed = datetime.fromisoformat(raw)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def utc_iso(dt: datetime | None) -> str | None:
    """Serialize a UTC datetime to an ISO-8601 string with Z suffix."""
    if dt is None:
        return None
    return ensure_utc(dt).isoformat().replace("+00:00", "Z")


@dataclass
class WatchTarget:
    """Represents a symbol-scoped sniper wake-up target for a forming setup."""

    symbol: str
    strategy_name: str
    wake_at_utc: datetime
    hypothesis: str = ""
    trigger_condition: str = ""
    invalidation_condition: str = ""
    postpone_count: int = 0
    max_postpones: int = 3
    expires_at_utc: datetime | None = None
    watch_id: str = field(default_factory=lambda: f"w_{uuid.uuid4().hex[:12]}")
    created_at_utc: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at_utc: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    status: str = "ACTIVE"  # ACTIVE | POSTPONED | TRIGGERED | INVALIDATED | EXPIRED
    outcome_note: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.symbol = str(self.symbol).strip()
        self.strategy_name = str(self.strategy_name).strip()
        self.wake_at_utc = ensure_utc(self.wake_at_utc)
        self.created_at_utc = ensure_utc(self.created_at_utc)
        self.updated_at_utc = ensure_utc(self.updated_at_utc)
        if self.expires_at_utc is not None:
            self.expires_at_utc = ensure_utc(self.expires_at_utc)
        else:
            self.expires_at_utc = self.wake_at_utc + timedelta(minutes=60)
        self.postpone_count = max(0, int(self.postpone_count))
        self.max_postpones = max(0, int(self.max_postpones))
        status_up = str(self.status).strip().upper()
        self.status = status_up if status_up in VALID_WATCH_STATUSES else "ACTIVE"

    @property
    def is_active(self) -> bool:
        return self.status in ACTIVE_WATCH_STATUSES

    def is_expired(self, now_utc: datetime) -> bool:
        now = ensure_utc(now_utc)
        return self.expires_at_utc is not None and now >= self.expires_at_utc

    def to_dict(self) -> dict[str, Any]:
        return {
            "watch_id": self.watch_id,
            "symbol": self.symbol,
            "strategy_name": self.strategy_name,
            "wake_at_utc": utc_iso(self.wake_at_utc),
            "hypothesis": self.hypothesis,
            "trigger_condition": self.trigger_condition,
            "invalidation_condition": self.invalidation_condition,
            "postpone_count": self.postpone_count,
            "max_postpones": self.max_postpones,
            "expires_at_utc": utc_iso(self.expires_at_utc),
            "created_at_utc": utc_iso(self.created_at_utc),
            "updated_at_utc": utc_iso(self.updated_at_utc),
            "status": self.status,
            "outcome_note": self.outcome_note,
            "metadata": dict(self.metadata),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WatchTarget:
        created_raw = data.get("created_at_utc")
        wake_raw = data.get("wake_at_utc")
        updated_raw = data.get("updated_at_utc") or created_raw or wake_raw
        expires_raw = data.get("expires_at_utc")

        wake_dt = ensure_utc(wake_raw)
        created_dt = ensure_utc(created_raw, default=wake_dt)
        updated_dt = ensure_utc(updated_raw, default=created_dt)
        expires_dt = ensure_utc(expires_raw) if expires_raw else None

        return cls(
            watch_id=str(data.get("watch_id") or f"w_{uuid.uuid4().hex[:12]}"),
            symbol=str(data.get("symbol", "")).strip(),
            strategy_name=str(data.get("strategy_name", "")).strip(),
            wake_at_utc=wake_dt,
            hypothesis=str(data.get("hypothesis", "")),
            trigger_condition=str(data.get("trigger_condition", "")),
            invalidation_condition=str(data.get("invalidation_condition", "")),
            postpone_count=int(data.get("postpone_count", 0) or 0),
            max_postpones=int(data.get("max_postpones", 3) if data.get("max_postpones") is not None else 3),
            expires_at_utc=expires_dt,
            created_at_utc=created_dt,
            updated_at_utc=updated_dt,
            status=str(data.get("status", "ACTIVE")),
            outcome_note=str(data.get("outcome_note", "")),
            metadata=dict(data.get("metadata") or {}),
        )


@dataclass
class WakePlan:
    """Next scheduled wake-up plan for the global MT5 bot loop."""

    sleep_seconds: float
    wake_at_utc: datetime
    mode: str  # "BASE_PATROL" | "SNIPER_WATCH"
    due_symbols: list[str] = field(default_factory=list)
    due_watches: list[WatchTarget] = field(default_factory=list)
    next_base_at_utc: datetime | None = None
    reason: str = ""

    def __post_init__(self) -> None:
        self.sleep_seconds = max(0.0, float(self.sleep_seconds))
        self.wake_at_utc = ensure_utc(self.wake_at_utc)
        if self.next_base_at_utc is not None:
            self.next_base_at_utc = ensure_utc(self.next_base_at_utc)
        mode_up = str(self.mode).strip().upper()
        self.mode = mode_up if mode_up in ("BASE_PATROL", "SNIPER_WATCH") else "BASE_PATROL"

    def to_dict(self) -> dict[str, Any]:
        return {
            "sleep_seconds": round(self.sleep_seconds, 2),
            "wake_at_utc": utc_iso(self.wake_at_utc),
            "mode": self.mode,
            "due_symbols": list(self.due_symbols),
            "due_watches": [w.to_dict() for w in self.due_watches],
            "next_base_at_utc": utc_iso(self.next_base_at_utc),
            "reason": self.reason,
        }


class AdaptiveWakeScheduler:
    """
    Adaptive wake-up scheduler combining clock-aligned base patrols (default 30m,
    configurable to 15m or any interval) with exact sniper wake-ups for forming setups.

    Lifecycle per symbol:
      BASE_PATROL
        --[register_watch]--> SNIPER_WATCH (ACTIVE)
        --[confirm_trigger]--> TRIGGERED  --> returns to BASE_PATROL
        --[postpone_watch]---> POSTPONED  (or auto-INVALIDATED/EXPIRED if limit/TTL hit -> BASE_PATROL)
        --[invalidate_watch]-> INVALIDATED --> returns to BASE_PATROL
        --[expires_at_utc]---> EXPIRED     --> returns to BASE_PATROL
    """

    def __init__(
        self,
        base_interval_minutes: int = 30,
        min_wake_seconds: int = 60,
        default_max_postpones: int = 3,
        default_watch_ttl_minutes: int | None = None,
        coalesce_window_seconds: int = 15,
        max_history: int = 200,
    ) -> None:
        if base_interval_minutes < 1:
            raise ValueError("base_interval_minutes must be >= 1")
        if min_wake_seconds < 1:
            raise ValueError("min_wake_seconds must be >= 1")
        if default_max_postpones < 0:
            raise ValueError("default_max_postpones must be >= 0")

        self.base_interval_minutes: int = int(base_interval_minutes)
        self.min_wake_seconds: int = int(min_wake_seconds)
        self.default_max_postpones: int = int(default_max_postpones)
        self.default_watch_ttl_minutes: int = (
            int(default_watch_ttl_minutes)
            if default_watch_ttl_minutes is not None
            else max(self.base_interval_minutes * 3, 90)
        )
        self.coalesce_window_seconds: int = max(0, int(coalesce_window_seconds))
        self.max_history: int = max(10, int(max_history))

        self._active_watches: dict[str, WatchTarget] = {}
        self._history: list[WatchTarget] = []

    @property
    def max_wake_seconds(self) -> int:
        return self.base_interval_minutes * 60

    @property
    def active_watches(self) -> list[WatchTarget]:
        return sorted(self._active_watches.values(), key=lambda w: w.wake_at_utc)

    def get_watch(self, symbol: str) -> WatchTarget | None:
        key = str(symbol).strip()
        if key in self._active_watches:
            return self._active_watches[key]
        key_up = key.upper()
        for sym, watch in self._active_watches.items():
            if sym.upper() == key_up:
                return watch
        return None

    def has_active_watch(self, symbol: str) -> bool:
        return self.get_watch(symbol) is not None

    def symbol_mode(self, symbol: str) -> str:
        return "SNIPER_WATCH" if self.has_active_watch(symbol) else "BASE_PATROL"

    def recent_history(self, limit: int = 50) -> list[WatchTarget]:
        if limit <= 0:
            return []
        return list(self._history[-limit:])

    def _archive_watch(self, watch: WatchTarget) -> None:
        self._history.append(watch)
        if len(self._history) > self.max_history:
            self._history = self._history[-self.max_history :]

    def _clamp_wake_at(self, wake_at_utc: datetime, now_utc: datetime) -> datetime:
        now = ensure_utc(now_utc)
        target = ensure_utc(wake_at_utc)
        min_dt = now + timedelta(seconds=self.min_wake_seconds)
        max_dt = now + timedelta(seconds=self.max_wake_seconds)
        if target < min_dt:
            return min_dt
        if target > max_dt:
            return max_dt
        return target

    def next_base_cycle_utc(self, now_utc: datetime | None = None) -> datetime:
        """
        Compute the next clock-aligned UTC boundary for `base_interval_minutes`.
        Examples:
          - base=30m, now=10:05:00 -> 10:30:00
          - base=30m, now=10:30:00 -> 11:00:00
          - base=15m, now=10:14:59 -> 10:15:00
        """
        now = ensure_utc(now_utc)
        interval_sec = self.base_interval_minutes * 60
        epoch_sec = int(now.timestamp())
        next_epoch = ((epoch_sec // interval_sec) + 1) * interval_sec
        return datetime.fromtimestamp(next_epoch, tz=timezone.utc)

    def register_watch(
        self,
        symbol: str,
        strategy_name: str,
        wake_at_utc: datetime | str | None = None,
        wake_in_minutes: float | None = None,
        hypothesis: str = "",
        trigger_condition: str = "",
        invalidation_condition: str = "",
        max_postpones: int | None = None,
        expires_at_utc: datetime | str | None = None,
        now_utc: datetime | None = None,
        watch_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> WatchTarget:
        """Register or replace an exact sniper watch for a symbol."""
        sym = str(symbol).strip()
        if not sym:
            raise ValueError("symbol must be non-empty")

        now = ensure_utc(now_utc)
        if wake_at_utc is not None:
            raw_wake = ensure_utc(wake_at_utc)
        elif wake_in_minutes is not None:
            raw_wake = now + timedelta(minutes=float(wake_in_minutes))
        else:
            raw_wake = now + timedelta(minutes=min(10.0, self.base_interval_minutes / 2.0))

        clamped_wake = self._clamp_wake_at(raw_wake, now)

        if expires_at_utc is not None:
            exp_dt = ensure_utc(expires_at_utc)
            if exp_dt < clamped_wake:
                exp_dt = clamped_wake
        else:
            exp_dt = now + timedelta(minutes=self.default_watch_ttl_minutes)
            if exp_dt < clamped_wake:
                exp_dt = clamped_wake

        watch = WatchTarget(
            watch_id=watch_id or f"w_{uuid.uuid4().hex[:12]}",
            symbol=sym,
            strategy_name=str(strategy_name).strip(),
            wake_at_utc=clamped_wake,
            hypothesis=str(hypothesis).strip(),
            trigger_condition=str(trigger_condition).strip(),
            invalidation_condition=str(invalidation_condition).strip(),
            postpone_count=0,
            max_postpones=self.default_max_postpones if max_postpones is None else max(0, int(max_postpones)),
            expires_at_utc=exp_dt,
            created_at_utc=now,
            updated_at_utc=now,
            status="ACTIVE",
            outcome_note="",
            metadata=dict(metadata or {}),
        )
        self._active_watches[sym] = watch
        return watch

    def prune_expired(self, now_utc: datetime | None = None) -> list[WatchTarget]:
        """Expire any active watches whose `expires_at_utc` has passed."""
        now = ensure_utc(now_utc)
        expired: list[WatchTarget] = []
        for sym in list(self._active_watches.keys()):
            watch = self._active_watches[sym]
            if watch.is_expired(now):
                watch.status = "EXPIRED"
                watch.updated_at_utc = now
                if not watch.outcome_note:
                    watch.outcome_note = "Watch expired before trigger condition was met"
                del self._active_watches[sym]
                self._archive_watch(watch)
                expired.append(watch)
        return expired

    def get_due_watches(
        self,
        now_utc: datetime | None = None,
        grace_seconds: float = 0.0,
    ) -> list[WatchTarget]:
        """Return active watches due at or before `now_utc + grace_seconds`."""
        now = ensure_utc(now_utc)
        self.prune_expired(now)
        cutoff = now + timedelta(seconds=max(0.0, float(grace_seconds)))
        due = [w for w in self._active_watches.values() if w.wake_at_utc <= cutoff]
        due.sort(key=lambda w: w.wake_at_utc)
        return due

    def next_wakeup_plan(self, now_utc: datetime | None = None) -> WakePlan:
        """
        Decide the next wake-up for the global loop:
        chooses whichever comes first between the earliest active sniper watch
        and the next clock-aligned base patrol cycle.
        """
        now = ensure_utc(now_utc)
        self.prune_expired(now)
        next_base = self.next_base_cycle_utc(now)

        active = self.active_watches
        if active:
            earliest = active[0].wake_at_utc
            if earliest < next_base:
                batch_cutoff = max(now, earliest) + timedelta(seconds=self.coalesce_window_seconds)
                due = [w for w in active if w.wake_at_utc <= batch_cutoff]
                wake_at = max(now, earliest)
                sleep_sec = max(0.0, (earliest - now).total_seconds())
                due_syms = [w.symbol for w in due]
                return WakePlan(
                    sleep_seconds=sleep_sec,
                    wake_at_utc=wake_at,
                    mode="SNIPER_WATCH",
                    due_symbols=due_syms,
                    due_watches=due,
                    next_base_at_utc=next_base,
                    reason=f"Sniper watch due for {', '.join(due_syms)} before base patrol",
                )

        # Base patrol wins (no active watches, or all active watches are at/after next_base)
        base_cutoff = next_base + timedelta(seconds=self.coalesce_window_seconds)
        due_at_base = [w for w in active if w.wake_at_utc <= base_cutoff]
        sleep_sec = max(0.0, (next_base - now).total_seconds())
        return WakePlan(
            sleep_seconds=sleep_sec,
            wake_at_utc=next_base,
            mode="BASE_PATROL",
            due_symbols=[w.symbol for w in due_at_base],
            due_watches=due_at_base,
            next_base_at_utc=next_base,
            reason=f"Aligned {self.base_interval_minutes}m base patrol cycle",
        )

    def confirm_trigger(
        self,
        symbol: str,
        outcome_note: str = "Entry confirmed and executed",
        now_utc: datetime | None = None,
    ) -> WatchTarget | None:
        """Mark a firing sniper watch as TRIGGERED and return the symbol to base patrol."""
        now = ensure_utc(now_utc)
        watch = self.get_watch(symbol)
        if watch is None:
            return None
        watch.status = "TRIGGERED"
        watch.outcome_note = str(outcome_note).strip() or "Entry confirmed"
        watch.updated_at_utc = now
        self._active_watches.pop(watch.symbol, None)
        self._archive_watch(watch)
        return watch

    def postpone_watch(
        self,
        symbol: str,
        new_wake_at_utc: datetime | str | None = None,
        wake_in_minutes: float | None = None,
        hypothesis: str | None = None,
        trigger_condition: str | None = None,
        invalidation_condition: str | None = None,
        note: str = "",
        now_utc: datetime | None = None,
    ) -> WatchTarget | None:
        """
        Postpone an active sniper watch to a new exact wake time.
        Auto-invalidates (or expires) and returns the symbol to base patrol if:
          - `postpone_count >= max_postpones`, or
          - the watch is already expired, or
          - the newly clamped wake time exceeds `expires_at_utc`.
        """
        now = ensure_utc(now_utc)
        watch = self.get_watch(symbol)
        if watch is None:
            return None

        watch.postpone_count += 1
        watch.updated_at_utc = now

        if watch.is_expired(now):
            watch.status = "EXPIRED"
            watch.outcome_note = (
                f"{note} | Auto-expired on postpone #{watch.postpone_count}".strip(" |")
                if note
                else f"Auto-expired on postpone #{watch.postpone_count}"
            )
            self._active_watches.pop(watch.symbol, None)
            self._archive_watch(watch)
            return watch

        if watch.postpone_count >= watch.max_postpones:
            watch.status = "INVALIDATED"
            watch.outcome_note = (
                f"{note} | Auto-invalidated: max postpones reached ({watch.postpone_count}/{watch.max_postpones})".strip(" |")
                if note
                else f"Auto-invalidated: max postpones reached ({watch.postpone_count}/{watch.max_postpones})"
            )
            self._active_watches.pop(watch.symbol, None)
            self._archive_watch(watch)
            return watch

        if new_wake_at_utc is not None:
            raw_wake = ensure_utc(new_wake_at_utc)
        elif wake_in_minutes is not None:
            raw_wake = now + timedelta(minutes=float(wake_in_minutes))
        else:
            raw_wake = now + timedelta(minutes=min(10.0, self.base_interval_minutes / 2.0))

        clamped_wake = self._clamp_wake_at(raw_wake, now)
        if watch.expires_at_utc is not None and clamped_wake > watch.expires_at_utc:
            watch.status = "EXPIRED"
            watch.outcome_note = (
                f"{note} | Auto-expired: postponed wake exceeds watch TTL".strip(" |")
                if note
                else "Auto-expired: postponed wake exceeds watch TTL"
            )
            self._active_watches.pop(watch.symbol, None)
            self._archive_watch(watch)
            return watch

        watch.wake_at_utc = clamped_wake
        watch.status = "POSTPONED"
        if hypothesis is not None and str(hypothesis).strip():
            watch.hypothesis = str(hypothesis).strip()
        if trigger_condition is not None and str(trigger_condition).strip():
            watch.trigger_condition = str(trigger_condition).strip()
        if invalidation_condition is not None and str(invalidation_condition).strip():
            watch.invalidation_condition = str(invalidation_condition).strip()
        if note:
            watch.outcome_note = str(note).strip()
        return watch

    def invalidate_watch(
        self,
        symbol: str,
        reason: str = "Setup invalidated",
        now_utc: datetime | None = None,
    ) -> WatchTarget | None:
        """Mark an active sniper watch as INVALIDATED and return the symbol to base patrol."""
        now = ensure_utc(now_utc)
        watch = self.get_watch(symbol)
        if watch is None:
            return None
        watch.status = "INVALIDATED"
        watch.outcome_note = str(reason).strip() or "Setup invalidated"
        watch.updated_at_utc = now
        self._active_watches.pop(watch.symbol, None)
        self._archive_watch(watch)
        return watch

    def sync_from_db_watches(
        self,
        watch_rows: list[dict[str, Any]],
        now_utc: datetime | None = None,
    ) -> int:
        """
        Restore active/postponed watch targets from `MT5KnowledgeDB` watch_hypotheses rows.
        Returns the number of active watches loaded.
        """
        now = ensure_utc(now_utc)
        loaded = 0
        for row in watch_rows:
            if not isinstance(row, dict):
                continue
            status = str(row.get("status", "")).strip().upper()
            if status not in ACTIVE_WATCH_STATUSES:
                continue
            watch = WatchTarget.from_dict(row)
            if not watch.symbol or watch.is_expired(now):
                continue
            self._active_watches[watch.symbol] = watch
            loaded += 1
        return loaded

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": 1,
            "base_interval_minutes": self.base_interval_minutes,
            "min_wake_seconds": self.min_wake_seconds,
            "default_max_postpones": self.default_max_postpones,
            "default_watch_ttl_minutes": self.default_watch_ttl_minutes,
            "coalesce_window_seconds": self.coalesce_window_seconds,
            "max_history": self.max_history,
            "active_watches": [w.to_dict() for w in self.active_watches],
            "history": [w.to_dict() for w in self._history],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AdaptiveWakeScheduler:
        scheduler = cls(
            base_interval_minutes=int(data.get("base_interval_minutes", 30) or 30),
            min_wake_seconds=int(data.get("min_wake_seconds", 60) or 60),
            default_max_postpones=int(
                data.get("default_max_postpones", 3)
                if data.get("default_max_postpones") is not None
                else 3
            ),
            default_watch_ttl_minutes=(
                int(data["default_watch_ttl_minutes"])
                if data.get("default_watch_ttl_minutes") is not None
                else None
            ),
            coalesce_window_seconds=int(
                data.get("coalesce_window_seconds", 15)
                if data.get("coalesce_window_seconds") is not None
                else 15
            ),
            max_history=int(data.get("max_history", 200) or 200),
        )
        for item in data.get("active_watches", []) or []:
            if isinstance(item, dict):
                watch = WatchTarget.from_dict(item)
                if watch.symbol and watch.is_active:
                    scheduler._active_watches[watch.symbol] = watch
        for item in data.get("history", []) or []:
            if isinstance(item, dict):
                watch = WatchTarget.from_dict(item)
                if watch.symbol:
                    scheduler._history.append(watch)
        if len(scheduler._history) > scheduler.max_history:
            scheduler._history = scheduler._history[-scheduler.max_history :]
        return scheduler
