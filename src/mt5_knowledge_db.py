from __future__ import annotations

import json
import math
import sqlite3
import threading
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

VALID_WATCH_STATUSES: tuple[str, ...] = (
    "ACTIVE",
    "TRIGGERED",
    "POSTPONED",
    "INVALIDATED",
    "EXPIRED",
)

DEFAULT_DB_PATH = Path("data/mt5_learning.db")
DEFAULT_PRIOR_STRENGTH = 15.0
MAX_LIVE_PF_CAP = 5.0
LESSON_HALF_LIFE_DAYS = 30.0


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_iso_utc(ts: str | None) -> datetime | None:
    if not ts:
        return None
    text = str(ts).strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _normalize_rate(value: float) -> float:
    """Normalize a win rate to [0.0, 1.0], accepting either 0..1 or 0..100 inputs."""
    val = float(value or 0.0)
    if val > 1.0:
        val = val / 100.0
    return max(0.0, min(1.0, val))


def _safe_float(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default
    try:
        out = float(value)
        if math.isnan(out) or math.isinf(out):
            return default
        return out
    except (TypeError, ValueError):
        return default


def _safe_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _norm_key(value: str | None, default: str = "ALL") -> str:
    if value is None:
        return default
    cleaned = str(value).strip()
    return cleaned if cleaned else default


class MT5KnowledgeDB:
    """
    Persistent SQLite knowledge, episodic memory, and Bayesian adaptive learning DB
    for the MetaTrader 5 (MT5) AI trading bot.

    Features:
    - SQLite WAL mode, foreign keys enabled, busy timeout, and context-managed transactions.
    - 2-year historical strategy priors (`strategy_priors`) blended with live execution
      metrics (`live_strategy_stats`) via Bayesian shrinkage.
    - Full AI decision journal (`decision_journal`) and sniper wake-up watch lifecycle
      (`watch_hypotheses`).
    - Closed trade ledger (`trade_outcomes`) with automatic live-stat rollups and
      recency-weighted distilled lessons (`learned_lessons`).
    """

    def __init__(
        self,
        db_path: str | Path = DEFAULT_DB_PATH,
        prior_strength: float = DEFAULT_PRIOR_STRENGTH,
    ) -> None:
        self.is_memory = str(db_path) == ":memory:"
        self.db_path = Path(db_path) if not self.is_memory else Path(":memory:")
        self.prior_strength = max(1.0, float(prior_strength))
        self._lock = threading.RLock()

        if not self.is_memory:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self._conn = sqlite3.connect(
            ":memory:" if self.is_memory else str(self.db_path),
            timeout=10.0,
            isolation_level=None,
            check_same_thread=False,
        )
        self._conn.row_factory = sqlite3.Row
        self._configure_pragmas()
        self._init_schema()

    def __enter__(self) -> MT5KnowledgeDB:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()

    def close(self) -> None:
        with self._lock:
            if self._conn is not None:
                try:
                    self._conn.close()
                finally:
                    self._conn = None  # type: ignore[assignment]

    def _configure_pragmas(self) -> None:
        with self._lock:
            cur = self._conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON;")
            cur.execute("PRAGMA busy_timeout = 5000;")
            if not self.is_memory:
                cur.execute("PRAGMA journal_mode = WAL;")
                cur.execute("PRAGMA synchronous = NORMAL;")
            cur.close()

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Cursor]:
        """Thread-safe, atomic SQLite transaction context manager."""
        with self._lock:
            in_tx = self._conn.in_transaction
            cur = self._conn.cursor()
            if not in_tx:
                cur.execute("BEGIN IMMEDIATE;")
            try:
                yield cur
                if not in_tx:
                    self._conn.commit()
            except Exception:
                if not in_tx and self._conn.in_transaction:
                    self._conn.rollback()
                raise
            finally:
                cur.close()

    def _init_schema(self) -> None:
        with self.transaction() as cur:
            cur.executescript(
                """
                CREATE TABLE IF NOT EXISTS strategy_priors (
                    symbol TEXT NOT NULL,
                    strategy_name TEXT NOT NULL,
                    regime TEXT NOT NULL DEFAULT 'ALL',
                    session TEXT NOT NULL DEFAULT 'ALL',
                    trades_count INTEGER NOT NULL DEFAULT 0,
                    wins INTEGER NOT NULL DEFAULT 0,
                    losses INTEGER NOT NULL DEFAULT 0,
                    win_rate REAL NOT NULL DEFAULT 0.0,
                    profit_factor REAL NOT NULL DEFAULT 0.0,
                    expectancy_r REAL NOT NULL DEFAULT 0.0,
                    avg_rr REAL NOT NULL DEFAULT 0.0,
                    max_dd_pct REAL NOT NULL DEFAULT 0.0,
                    is_oos_consistent INTEGER NOT NULL DEFAULT 0,
                    enabled INTEGER NOT NULL DEFAULT 1,
                    updated_at TEXT NOT NULL,
                    PRIMARY KEY (symbol, strategy_name, regime, session)
                );

                CREATE INDEX IF NOT EXISTS idx_priors_lookup
                    ON strategy_priors (symbol, regime, session, enabled);

                CREATE TABLE IF NOT EXISTS live_strategy_stats (
                    symbol TEXT NOT NULL,
                    strategy_name TEXT NOT NULL,
                    regime TEXT NOT NULL DEFAULT 'ALL',
                    session TEXT NOT NULL DEFAULT 'ALL',
                    trades_count INTEGER NOT NULL DEFAULT 0,
                    wins INTEGER NOT NULL DEFAULT 0,
                    losses INTEGER NOT NULL DEFAULT 0,
                    win_rate REAL NOT NULL DEFAULT 0.0,
                    gross_profit_usd REAL NOT NULL DEFAULT 0.0,
                    gross_loss_usd REAL NOT NULL DEFAULT 0.0,
                    net_profit_usd REAL NOT NULL DEFAULT 0.0,
                    profit_factor REAL NOT NULL DEFAULT 0.0,
                    total_r REAL NOT NULL DEFAULT 0.0,
                    expectancy_r REAL NOT NULL DEFAULT 0.0,
                    avg_rr REAL NOT NULL DEFAULT 0.0,
                    avg_win_r REAL NOT NULL DEFAULT 0.0,
                    avg_loss_r REAL NOT NULL DEFAULT 0.0,
                    consecutive_losses INTEGER NOT NULL DEFAULT 0,
                    last_trade_utc TEXT,
                    updated_at TEXT NOT NULL,
                    PRIMARY KEY (symbol, strategy_name, regime, session)
                );

                CREATE INDEX IF NOT EXISTS idx_live_stats_lookup
                    ON live_strategy_stats (symbol, regime, session);

                CREATE TABLE IF NOT EXISTS decision_journal (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts_utc TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    regime TEXT NOT NULL DEFAULT '',
                    session TEXT NOT NULL DEFAULT '',
                    action TEXT NOT NULL,
                    strategy_name TEXT NOT NULL DEFAULT '',
                    confidence REAL NOT NULL DEFAULT 0.0,
                    setup_stage TEXT NOT NULL DEFAULT 'NONE',
                    next_wake_utc TEXT,
                    reasoning TEXT NOT NULL DEFAULT '',
                    snapshot_json TEXT NOT NULL DEFAULT '{}'
                );

                CREATE INDEX IF NOT EXISTS idx_decision_symbol_ts
                    ON decision_journal (symbol, ts_utc DESC);

                CREATE TABLE IF NOT EXISTS watch_hypotheses (
                    watch_id TEXT PRIMARY KEY,
                    symbol TEXT NOT NULL,
                    strategy_name TEXT NOT NULL DEFAULT '',
                    created_at_utc TEXT NOT NULL,
                    wake_at_utc TEXT NOT NULL,
                    hypothesis TEXT NOT NULL DEFAULT '',
                    trigger_condition TEXT NOT NULL DEFAULT '',
                    invalidation_condition TEXT NOT NULL DEFAULT '',
                    postpone_count INTEGER NOT NULL DEFAULT 0,
                    max_postpones INTEGER NOT NULL DEFAULT 3,
                    status TEXT NOT NULL DEFAULT 'ACTIVE'
                        CHECK (status IN ('ACTIVE', 'TRIGGERED', 'POSTPONED', 'INVALIDATED', 'EXPIRED')),
                    outcome_note TEXT NOT NULL DEFAULT '',
                    updated_at_utc TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_watch_status_wake
                    ON watch_hypotheses (status, wake_at_utc ASC);

                CREATE INDEX IF NOT EXISTS idx_watch_symbol_status
                    ON watch_hypotheses (symbol, status);

                CREATE TABLE IF NOT EXISTS trade_outcomes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticket INTEGER NOT NULL UNIQUE,
                    symbol TEXT NOT NULL,
                    direction TEXT NOT NULL,
                    strategy_name TEXT NOT NULL DEFAULT 'UNKNOWN',
                    regime TEXT NOT NULL DEFAULT 'ALL',
                    session TEXT NOT NULL DEFAULT 'ALL',
                    entry_time TEXT NOT NULL,
                    exit_time TEXT NOT NULL,
                    entry_price REAL NOT NULL DEFAULT 0.0,
                    exit_price REAL NOT NULL DEFAULT 0.0,
                    sl_price REAL,
                    tp_price REAL,
                    profit_usd REAL NOT NULL DEFAULT 0.0,
                    r_multiple REAL NOT NULL DEFAULT 0.0,
                    mae_r REAL,
                    mfe_r REAL,
                    close_reason TEXT NOT NULL DEFAULT '',
                    ai_lesson TEXT NOT NULL DEFAULT '',
                    recorded_at_utc TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_trade_outcomes_symbol_exit
                    ON trade_outcomes (symbol, exit_time DESC);

                CREATE INDEX IF NOT EXISTS idx_trade_outcomes_bucket
                    ON trade_outcomes (symbol, strategy_name, regime, session);

                CREATE TABLE IF NOT EXISTS learned_lessons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    strategy_name TEXT NOT NULL DEFAULT 'ALL',
                    regime TEXT NOT NULL DEFAULT 'ALL',
                    lesson_text TEXT NOT NULL,
                    lesson_type TEXT NOT NULL DEFAULT 'GENERAL',
                    weight REAL NOT NULL DEFAULT 1.0,
                    reinforcement_count INTEGER NOT NULL DEFAULT 1,
                    source_ticket INTEGER,
                    created_at_utc TEXT NOT NULL,
                    updated_at_utc TEXT NOT NULL,
                    last_applied_utc TEXT,
                    FOREIGN KEY (source_ticket) REFERENCES trade_outcomes(ticket) ON DELETE SET NULL
                );

                CREATE INDEX IF NOT EXISTS idx_lessons_lookup
                    ON learned_lessons (symbol, strategy_name, regime, updated_at_utc DESC);
                """
            )

    # ------------------------------------------------------------------
    # 1. Strategy Priors (2-Year Historical Backtest Seeding)
    # ------------------------------------------------------------------

    def upsert_strategy_priors(self, priors: list[dict[str, Any]]) -> int:
        """
        Insert or update 2-year historical backtest priors per
        `(symbol, strategy_name, regime, session)`.

        Returns the number of rows upserted.
        """
        if not priors:
            return 0

        now_iso = _utc_now_iso()
        upserted = 0
        with self.transaction() as cur:
            for item in priors:
                symbol = str(item.get("symbol", "")).strip()
                strategy_name = str(
                    item.get("strategy_name") or item.get("strategy") or ""
                ).strip()
                if not symbol or not strategy_name:
                    continue

                regime = _norm_key(item.get("regime"), "ALL")
                session = _norm_key(item.get("session"), "ALL")
                trades_count = max(0, _safe_int(item.get("trades_count", item.get("trades", 0))))
                wins = max(0, _safe_int(item.get("wins", 0)))
                losses = max(0, _safe_int(item.get("losses", max(0, trades_count - wins))))
                if "win_rate" in item and item["win_rate"] is not None:
                    win_rate = _normalize_rate(_safe_float(item["win_rate"]))
                else:
                    win_rate = (wins / trades_count) if trades_count > 0 else 0.0

                profit_factor = max(0.0, _safe_float(item.get("profit_factor", 0.0)))
                expectancy_r = _safe_float(item.get("expectancy_r", 0.0))
                avg_rr = max(0.0, _safe_float(item.get("avg_rr", 0.0)))
                max_dd_pct = max(0.0, _safe_float(item.get("max_dd_pct", 0.0)))
                is_oos_consistent = 1 if bool(item.get("is_oos_consistent", False)) else 0
                enabled = 1 if bool(item.get("enabled", True)) else 0
                updated_at = str(item.get("updated_at") or now_iso)

                cur.execute(
                    """
                    INSERT INTO strategy_priors (
                        symbol, strategy_name, regime, session,
                        trades_count, wins, losses, win_rate,
                        profit_factor, expectancy_r, avg_rr, max_dd_pct,
                        is_oos_consistent, enabled, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(symbol, strategy_name, regime, session) DO UPDATE SET
                        trades_count = excluded.trades_count,
                        wins = excluded.wins,
                        losses = excluded.losses,
                        win_rate = excluded.win_rate,
                        profit_factor = excluded.profit_factor,
                        expectancy_r = excluded.expectancy_r,
                        avg_rr = excluded.avg_rr,
                        max_dd_pct = excluded.max_dd_pct,
                        is_oos_consistent = excluded.is_oos_consistent,
                        enabled = excluded.enabled,
                        updated_at = excluded.updated_at
                    """,
                    (
                        symbol,
                        strategy_name,
                        regime,
                        session,
                        trades_count,
                        wins,
                        losses,
                        round(win_rate, 6),
                        round(profit_factor, 4),
                        round(expectancy_r, 4),
                        round(avg_rr, 4),
                        round(max_dd_pct, 4),
                        is_oos_consistent,
                        enabled,
                        updated_at,
                    ),
                )
                upserted += 1
        return upserted

    def get_strategy_priors(
        self,
        symbol: str | None = None,
        regime: str | None = None,
        session: str | None = None,
        enabled_only: bool = False,
    ) -> list[dict[str, Any]]:
        clauses: list[str] = []
        params: list[Any] = []
        if symbol:
            clauses.append("symbol = ?")
            params.append(symbol)
        if regime:
            clauses.append("regime = ?")
            params.append(regime)
        if session:
            clauses.append("session = ?")
            params.append(session)
        if enabled_only:
            clauses.append("enabled = 1")

        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        sql = f"SELECT * FROM strategy_priors {where} ORDER BY symbol, expectancy_r DESC"
        with self._lock:
            rows = self._conn.execute(sql, params).fetchall()
        return [self._row_to_prior(r) for r in rows]

    @staticmethod
    def _row_to_prior(row: sqlite3.Row) -> dict[str, Any]:
        d = dict(row)
        d["is_oos_consistent"] = bool(d["is_oos_consistent"])
        d["enabled"] = bool(d["enabled"])
        return d

    # ------------------------------------------------------------------
    # 2. Decision Journal
    # ------------------------------------------------------------------

    def record_decision(
        self,
        symbol: str,
        regime: str = "",
        session: str = "",
        action: str = "HOLD",
        strategy_name: str = "",
        confidence: float = 0.0,
        setup_stage: str = "NONE",
        next_wake_utc: str | None = None,
        reasoning: str = "",
        snapshot: dict[str, Any] | str | None = None,
        ts_utc: str | None = None,
    ) -> int:
        """Record a single AI evaluation cycle decision and return its row id."""
        ts = ts_utc or _utc_now_iso()
        if snapshot is None:
            snapshot_json = "{}"
        elif isinstance(snapshot, str):
            snapshot_json = snapshot
        else:
            snapshot_json = json.dumps(snapshot, ensure_ascii=False, separators=(",", ":"))

        with self.transaction() as cur:
            cur.execute(
                """
                INSERT INTO decision_journal (
                    ts_utc, symbol, regime, session, action,
                    strategy_name, confidence, setup_stage,
                    next_wake_utc, reasoning, snapshot_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    ts,
                    str(symbol).strip(),
                    str(regime or ""),
                    str(session or ""),
                    str(action or "HOLD").strip().upper(),
                    str(strategy_name or ""),
                    _safe_float(confidence, 0.0),
                    str(setup_stage or "NONE").strip().upper(),
                    next_wake_utc,
                    str(reasoning or ""),
                    snapshot_json,
                ),
            )
            return int(cur.lastrowid)

    def get_recent_decisions(
        self,
        symbol: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        limit = max(1, int(limit))
        with self._lock:
            if symbol:
                rows = self._conn.execute(
                    """
                    SELECT * FROM decision_journal
                    WHERE symbol = ?
                    ORDER BY ts_utc DESC, id DESC
                    LIMIT ?
                    """,
                    (symbol, limit),
                ).fetchall()
            else:
                rows = self._conn.execute(
                    """
                    SELECT * FROM decision_journal
                    ORDER BY ts_utc DESC, id DESC
                    LIMIT ?
                    """,
                    (limit,),
                ).fetchall()
        return [dict(r) for r in rows]

    # ------------------------------------------------------------------
    # 3. Watch Hypotheses (Sniper Wake-Up Lifecycle)
    # ------------------------------------------------------------------

    def upsert_watch(
        self,
        watch_id: str | None,
        symbol: str,
        strategy_name: str = "",
        wake_at_utc: str = "",
        hypothesis: str = "",
        trigger_condition: str = "",
        invalidation_condition: str = "",
        postpone_count: int = 0,
        max_postpones: int = 3,
        status: str = "ACTIVE",
        outcome_note: str = "",
        created_at_utc: str | None = None,
        updated_at_utc: str | None = None,
    ) -> dict[str, Any]:
        """Create or update a sniper wake-up watch hypothesis."""
        status_norm = str(status or "ACTIVE").strip().upper()
        if status_norm not in VALID_WATCH_STATUSES:
            raise ValueError(
                f"Invalid watch status '{status_norm}'. Expected one of {VALID_WATCH_STATUSES}."
            )

        wid = str(watch_id).strip() if watch_id else f"w_{uuid.uuid4().hex[:12]}"
        now_iso = _utc_now_iso()
        created = created_at_utc or now_iso
        updated = updated_at_utc or now_iso
        wake = wake_at_utc or now_iso
        p_count = max(0, int(postpone_count))
        p_max = max(0, int(max_postpones))

        with self.transaction() as cur:
            cur.execute(
                """
                INSERT INTO watch_hypotheses (
                    watch_id, symbol, strategy_name, created_at_utc, wake_at_utc,
                    hypothesis, trigger_condition, invalidation_condition,
                    postpone_count, max_postpones, status, outcome_note, updated_at_utc
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(watch_id) DO UPDATE SET
                    symbol = excluded.symbol,
                    strategy_name = excluded.strategy_name,
                    wake_at_utc = excluded.wake_at_utc,
                    hypothesis = excluded.hypothesis,
                    trigger_condition = excluded.trigger_condition,
                    invalidation_condition = excluded.invalidation_condition,
                    postpone_count = excluded.postpone_count,
                    max_postpones = excluded.max_postpones,
                    status = excluded.status,
                    outcome_note = excluded.outcome_note,
                    updated_at_utc = excluded.updated_at_utc
                """,
                (
                    wid,
                    str(symbol).strip(),
                    str(strategy_name or "").strip(),
                    created,
                    wake,
                    str(hypothesis or ""),
                    str(trigger_condition or ""),
                    str(invalidation_condition or ""),
                    p_count,
                    p_max,
                    status_norm,
                    str(outcome_note or ""),
                    updated,
                ),
            )
            row = cur.execute(
                "SELECT * FROM watch_hypotheses WHERE watch_id = ?", (wid,)
            ).fetchone()
        return dict(row)

    def get_watch(self, watch_id: str) -> dict[str, Any] | None:
        with self._lock:
            row = self._conn.execute(
                "SELECT * FROM watch_hypotheses WHERE watch_id = ?", (watch_id,)
            ).fetchone()
        return dict(row) if row is not None else None

    def get_active_watches(
        self,
        symbol: str | None = None,
        include_postponed: bool = True,
    ) -> list[dict[str, Any]]:
        """Return active (and optionally postponed) watches ordered by soonest wake_at_utc."""
        statuses = ("ACTIVE", "POSTPONED") if include_postponed else ("ACTIVE",)
        placeholders = ",".join("?" for _ in statuses)
        params: list[Any] = list(statuses)
        symbol_clause = ""
        if symbol:
            symbol_clause = " AND symbol = ?"
            params.append(symbol)

        sql = (
            f"SELECT * FROM watch_hypotheses "
            f"WHERE status IN ({placeholders}){symbol_clause} "
            f"ORDER BY wake_at_utc ASC, created_at_utc ASC"
        )
        with self._lock:
            rows = self._conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]

    def update_watch_status(
        self,
        watch_id: str,
        status: str,
        outcome_note: str = "",
        wake_at_utc: str | None = None,
        increment_postpone: bool = False,
    ) -> dict[str, Any] | None:
        """
        Update watch lifecycle status.
        When status == 'POSTPONED' (or increment_postpone=True), increments postpone_count
        and automatically transitions to 'EXPIRED' if postpone_count exceeds max_postpones.
        """
        status_norm = str(status).strip().upper()
        if status_norm not in VALID_WATCH_STATUSES:
            raise ValueError(
                f"Invalid watch status '{status_norm}'. Expected one of {VALID_WATCH_STATUSES}."
            )

        now_iso = _utc_now_iso()
        with self.transaction() as cur:
            existing = cur.execute(
                "SELECT * FROM watch_hypotheses WHERE watch_id = ?", (watch_id,)
            ).fetchone()
            if existing is None:
                return None

            postpone_count = int(existing["postpone_count"])
            max_postpones = int(existing["max_postpones"])
            final_status = status_norm
            final_note = outcome_note if outcome_note else str(existing["outcome_note"])
            final_wake = wake_at_utc if wake_at_utc else str(existing["wake_at_utc"])

            if status_norm == "POSTPONED" or increment_postpone:
                postpone_count += 1
                if postpone_count > max_postpones:
                    final_status = "EXPIRED"
                    auto_msg = f"Max postpones ({max_postpones}) exceeded."
                    final_note = f"{final_note} | {auto_msg}".strip(" |")

            cur.execute(
                """
                UPDATE watch_hypotheses
                SET status = ?,
                    postpone_count = ?,
                    wake_at_utc = ?,
                    outcome_note = ?,
                    updated_at_utc = ?
                WHERE watch_id = ?
                """,
                (
                    final_status,
                    postpone_count,
                    final_wake,
                    final_note,
                    now_iso,
                    watch_id,
                ),
            )
            updated = cur.execute(
                "SELECT * FROM watch_hypotheses WHERE watch_id = ?", (watch_id,)
            ).fetchone()
        return dict(updated) if updated is not None else None

    # ------------------------------------------------------------------
    # 4. Trade Outcomes, Live Stats Rollup & Learned Lessons
    # ------------------------------------------------------------------

    def record_trade_outcome(
        self,
        ticket: int,
        symbol: str,
        direction: str,
        strategy_name: str = "UNKNOWN",
        regime: str = "ALL",
        session: str = "ALL",
        entry_time: str = "",
        exit_time: str = "",
        entry_price: float = 0.0,
        exit_price: float = 0.0,
        sl_price: float | None = None,
        tp_price: float | None = None,
        profit_usd: float = 0.0,
        r_multiple: float = 0.0,
        mae_r: float | None = None,
        mfe_r: float | None = None,
        close_reason: str = "",
        ai_lesson: str = "",
        lesson_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Persist a closed trade outcome (idempotent by `ticket`), recompute
        `live_strategy_stats` for `(symbol, strategy_name, regime, session)`,
        and optionally store/reinforce `ai_lesson` in `learned_lessons`.
        """
        now_iso = _utc_now_iso()
        ticket_int = int(ticket)
        sym = str(symbol).strip()
        strat = _norm_key(strategy_name, "UNKNOWN")
        reg = _norm_key(regime, "ALL")
        sess = _norm_key(session, "ALL")
        dir_norm = str(direction or "").strip().upper()
        entry_ts = entry_time or now_iso
        exit_ts = exit_time or now_iso
        pnl = _safe_float(profit_usd, 0.0)
        r_mult = _safe_float(r_multiple, 0.0)
        lesson_clean = str(ai_lesson or "").strip()

        with self.transaction() as cur:
            cur.execute(
                """
                INSERT INTO trade_outcomes (
                    ticket, symbol, direction, strategy_name, regime, session,
                    entry_time, exit_time, entry_price, exit_price,
                    sl_price, tp_price, profit_usd, r_multiple,
                    mae_r, mfe_r, close_reason, ai_lesson, recorded_at_utc
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(ticket) DO UPDATE SET
                    symbol = excluded.symbol,
                    direction = excluded.direction,
                    strategy_name = excluded.strategy_name,
                    regime = excluded.regime,
                    session = excluded.session,
                    entry_time = excluded.entry_time,
                    exit_time = excluded.exit_time,
                    entry_price = excluded.entry_price,
                    exit_price = excluded.exit_price,
                    sl_price = excluded.sl_price,
                    tp_price = excluded.tp_price,
                    profit_usd = excluded.profit_usd,
                    r_multiple = excluded.r_multiple,
                    mae_r = excluded.mae_r,
                    mfe_r = excluded.mfe_r,
                    close_reason = excluded.close_reason,
                    ai_lesson = CASE
                        WHEN excluded.ai_lesson != '' THEN excluded.ai_lesson
                        ELSE trade_outcomes.ai_lesson
                    END
                """,
                (
                    ticket_int,
                    sym,
                    dir_norm,
                    strat,
                    reg,
                    sess,
                    entry_ts,
                    exit_ts,
                    _safe_float(entry_price),
                    _safe_float(exit_price),
                    None if sl_price is None else _safe_float(sl_price),
                    None if tp_price is None else _safe_float(tp_price),
                    round(pnl, 4),
                    round(r_mult, 4),
                    None if mae_r is None else round(_safe_float(mae_r), 4),
                    None if mfe_r is None else round(_safe_float(mfe_r), 4),
                    str(close_reason or ""),
                    lesson_clean,
                    now_iso,
                ),
            )

            self._recompute_live_bucket(cur, sym, strat, reg, sess, now_iso)

            if lesson_clean:
                inferred_type = lesson_type or ("MISTAKE" if pnl < 0 else "WIN_PATTERN")
                self._upsert_lesson_in_tx(
                    cur=cur,
                    symbol=sym,
                    strategy_name=strat,
                    regime=reg,
                    lesson_text=lesson_clean,
                    lesson_type=inferred_type,
                    weight=1.2 if pnl < 0 else 1.0,
                    source_ticket=ticket_int,
                    now_iso=now_iso,
                )

            row = cur.execute(
                "SELECT * FROM trade_outcomes WHERE ticket = ?", (ticket_int,)
            ).fetchone()
        return dict(row)

    def _recompute_live_bucket(
        self,
        cur: sqlite3.Cursor,
        symbol: str,
        strategy_name: str,
        regime: str,
        session: str,
        now_iso: str,
    ) -> None:
        rows = cur.execute(
            """
            SELECT profit_usd, r_multiple, exit_time
            FROM trade_outcomes
            WHERE symbol = ? AND strategy_name = ? AND regime = ? AND session = ?
            ORDER BY exit_time ASC, id ASC
            """,
            (symbol, strategy_name, regime, session),
        ).fetchall()

        if not rows:
            return

        trades_count = len(rows)
        wins = 0
        losses = 0
        gross_profit = 0.0
        gross_loss = 0.0
        total_r = 0.0
        win_rs: list[float] = []
        loss_rs: list[float] = []
        consec_losses = 0
        last_trade_utc: str | None = None

        for r in rows:
            pnl = float(r["profit_usd"])
            rm = float(r["r_multiple"])
            total_r += rm
            last_trade_utc = str(r["exit_time"])
            if pnl > 0 or (pnl == 0 and rm > 0):
                wins += 1
                gross_profit += max(0.0, pnl)
                win_rs.append(rm)
                consec_losses = 0
            else:
                losses += 1
                gross_loss += abs(min(0.0, pnl))
                loss_rs.append(abs(rm))
                consec_losses += 1

        win_rate = wins / trades_count if trades_count > 0 else 0.0
        net_profit = gross_profit - gross_loss
        if gross_loss > 0:
            profit_factor = min(MAX_LIVE_PF_CAP, gross_profit / gross_loss)
        elif gross_profit > 0:
            profit_factor = MAX_LIVE_PF_CAP
        else:
            profit_factor = 0.0

        expectancy_r = total_r / trades_count if trades_count > 0 else 0.0
        avg_win_r = (sum(win_rs) / len(win_rs)) if win_rs else 0.0
        avg_loss_r = (sum(loss_rs) / len(loss_rs)) if loss_rs else 0.0
        if avg_loss_r > 0:
            avg_rr = avg_win_r / avg_loss_r
        else:
            avg_rr = avg_win_r if avg_win_r > 0 else 0.0

        cur.execute(
            """
            INSERT INTO live_strategy_stats (
                symbol, strategy_name, regime, session,
                trades_count, wins, losses, win_rate,
                gross_profit_usd, gross_loss_usd, net_profit_usd,
                profit_factor, total_r, expectancy_r,
                avg_rr, avg_win_r, avg_loss_r,
                consecutive_losses, last_trade_utc, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(symbol, strategy_name, regime, session) DO UPDATE SET
                trades_count = excluded.trades_count,
                wins = excluded.wins,
                losses = excluded.losses,
                win_rate = excluded.win_rate,
                gross_profit_usd = excluded.gross_profit_usd,
                gross_loss_usd = excluded.gross_loss_usd,
                net_profit_usd = excluded.net_profit_usd,
                profit_factor = excluded.profit_factor,
                total_r = excluded.total_r,
                expectancy_r = excluded.expectancy_r,
                avg_rr = excluded.avg_rr,
                avg_win_r = excluded.avg_win_r,
                avg_loss_r = excluded.avg_loss_r,
                consecutive_losses = excluded.consecutive_losses,
                last_trade_utc = excluded.last_trade_utc,
                updated_at = excluded.updated_at
            """,
            (
                symbol,
                strategy_name,
                regime,
                session,
                trades_count,
                wins,
                losses,
                round(win_rate, 6),
                round(gross_profit, 4),
                round(gross_loss, 4),
                round(net_profit, 4),
                round(profit_factor, 4),
                round(total_r, 4),
                round(expectancy_r, 4),
                round(avg_rr, 4),
                round(avg_win_r, 4),
                round(avg_loss_r, 4),
                consec_losses,
                last_trade_utc,
                now_iso,
            ),
        )

    def add_lesson(
        self,
        symbol: str,
        strategy_name: str = "ALL",
        regime: str = "ALL",
        lesson_text: str = "",
        lesson_type: str = "GENERAL",
        weight: float = 1.0,
        source_ticket: int | None = None,
    ) -> int:
        """Store or reinforce a distilled adaptive lesson."""
        text = str(lesson_text or "").strip()
        if not text:
            raise ValueError("lesson_text must be non-empty")
        now_iso = _utc_now_iso()
        with self.transaction() as cur:
            return self._upsert_lesson_in_tx(
                cur=cur,
                symbol=str(symbol).strip(),
                strategy_name=_norm_key(strategy_name, "ALL"),
                regime=_norm_key(regime, "ALL"),
                lesson_text=text,
                lesson_type=str(lesson_type or "GENERAL").strip().upper(),
                weight=max(0.1, _safe_float(weight, 1.0)),
                source_ticket=source_ticket,
                now_iso=now_iso,
            )

    def _upsert_lesson_in_tx(
        self,
        cur: sqlite3.Cursor,
        symbol: str,
        strategy_name: str,
        regime: str,
        lesson_text: str,
        lesson_type: str,
        weight: float,
        source_ticket: int | None,
        now_iso: str,
    ) -> int:
        existing = cur.execute(
            """
            SELECT id, weight, reinforcement_count
            FROM learned_lessons
            WHERE symbol = ? AND strategy_name = ? AND regime = ? AND lesson_text = ?
            LIMIT 1
            """,
            (symbol, strategy_name, regime, lesson_text),
        ).fetchone()

        if existing is not None:
            new_count = int(existing["reinforcement_count"]) + 1
            new_weight = min(5.0, float(existing["weight"]) + 0.35 * weight)
            cur.execute(
                """
                UPDATE learned_lessons
                SET weight = ?,
                    reinforcement_count = ?,
                    updated_at_utc = ?,
                    source_ticket = COALESCE(?, source_ticket)
                WHERE id = ?
                """,
                (round(new_weight, 4), new_count, now_iso, source_ticket, int(existing["id"])),
            )
            return int(existing["id"])

        cur.execute(
            """
            INSERT INTO learned_lessons (
                symbol, strategy_name, regime, lesson_text, lesson_type,
                weight, reinforcement_count, source_ticket,
                created_at_utc, updated_at_utc, last_applied_utc
            ) VALUES (?, ?, ?, ?, ?, ?, 1, ?, ?, ?, NULL)
            """,
            (
                symbol,
                strategy_name,
                regime,
                lesson_text,
                lesson_type,
                round(weight, 4),
                source_ticket,
                now_iso,
                now_iso,
            ),
        )
        return int(cur.lastrowid)

    def get_recent_trades(
        self,
        symbol: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        limit = max(1, int(limit))
        with self._lock:
            if symbol:
                rows = self._conn.execute(
                    """
                    SELECT * FROM trade_outcomes
                    WHERE symbol = ?
                    ORDER BY exit_time DESC, id DESC
                    LIMIT ?
                    """,
                    (symbol, limit),
                ).fetchall()
            else:
                rows = self._conn.execute(
                    """
                    SELECT * FROM trade_outcomes
                    ORDER BY exit_time DESC, id DESC
                    LIMIT ?
                    """,
                    (limit,),
                ).fetchall()
        return [dict(r) for r in rows]

    def get_lessons(
        self,
        symbol: str | None = None,
        strategy_name: str | None = None,
        regime: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Return lessons ranked by effective score = weight * recency_decay * specificity_bonus.
        """
        clauses: list[str] = []
        params: list[Any] = []
        if symbol:
            clauses.append("(symbol = ? OR symbol = 'ALL')")
            params.append(symbol)
        if strategy_name and strategy_name != "ALL":
            clauses.append("(strategy_name = ? OR strategy_name = 'ALL')")
            params.append(strategy_name)
        if regime and regime != "ALL":
            clauses.append("(regime = ? OR regime = 'ALL')")
            params.append(regime)

        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        sql = f"SELECT * FROM learned_lessons {where} ORDER BY updated_at_utc DESC LIMIT 200"
        with self._lock:
            rows = self._conn.execute(sql, params).fetchall()

        now_dt = datetime.now(timezone.utc)
        scored: list[dict[str, Any]] = []
        for r in rows:
            item = dict(r)
            updated_dt = _parse_iso_utc(item.get("updated_at_utc"))
            age_days = max(0.0, (now_dt - updated_dt).total_seconds() / 86400.0) if updated_dt else 0.0
            recency = math.exp(-math.log(2.0) * age_days / LESSON_HALF_LIFE_DAYS)
            specificity = 1.0
            if symbol and item["symbol"] == symbol:
                specificity += 0.25
            if regime and regime != "ALL" and item["regime"] == regime:
                specificity += 0.25
            if strategy_name and strategy_name != "ALL" and item["strategy_name"] == strategy_name:
                specificity += 0.15
            item["effective_score"] = round(float(item["weight"]) * recency * specificity, 4)
            scored.append(item)

        scored.sort(key=lambda x: (x["effective_score"], x["updated_at_utc"]), reverse=True)
        return scored[: max(1, int(limit))]

    # ------------------------------------------------------------------
    # 5. Bayesian Blending (2-Year Priors + Rolling Live Stats)
    # ------------------------------------------------------------------

    def _select_best_prior(
        self,
        priors_for_strategy: list[dict[str, Any]],
        regime: str | None,
        session: str | None,
    ) -> dict[str, Any] | None:
        if not priors_for_strategy:
            return None

        req_reg = _norm_key(regime, "ALL")
        req_sess = _norm_key(session, "ALL")

        by_key = {(p["regime"], p["session"]): p for p in priors_for_strategy}
        candidates = [
            (req_reg, req_sess),
            (req_reg, "ALL"),
            ("ALL", req_sess),
            ("ALL", "ALL"),
        ]
        for key in candidates:
            if key in by_key:
                return by_key[key]
        # Fallback: highest sample size prior for that strategy
        return max(priors_for_strategy, key=lambda p: p["trades_count"])

    @staticmethod
    def _aggregate_live_rows(rows: list[sqlite3.Row]) -> dict[str, Any]:
        if not rows:
            return {
                "trades_count": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0.0,
                "gross_profit_usd": 0.0,
                "gross_loss_usd": 0.0,
                "net_profit_usd": 0.0,
                "profit_factor": 0.0,
                "total_r": 0.0,
                "expectancy_r": 0.0,
                "avg_rr": 0.0,
                "consecutive_losses": 0,
                "last_trade_utc": None,
            }

        trades_count = sum(int(r["trades_count"]) for r in rows)
        wins = sum(int(r["wins"]) for r in rows)
        losses = sum(int(r["losses"]) for r in rows)
        gross_profit = sum(float(r["gross_profit_usd"]) for r in rows)
        gross_loss = sum(float(r["gross_loss_usd"]) for r in rows)
        net_profit = gross_profit - gross_loss
        total_r = sum(float(r["total_r"]) for r in rows)
        win_rate = (wins / trades_count) if trades_count > 0 else 0.0
        if gross_loss > 0:
            profit_factor = min(MAX_LIVE_PF_CAP, gross_profit / gross_loss)
        elif gross_profit > 0:
            profit_factor = MAX_LIVE_PF_CAP
        else:
            profit_factor = 0.0
        expectancy_r = (total_r / trades_count) if trades_count > 0 else 0.0

        weighted_rr = sum(float(r["avg_rr"]) * int(r["trades_count"]) for r in rows)
        avg_rr = (weighted_rr / trades_count) if trades_count > 0 else 0.0

        latest_row = max(rows, key=lambda r: str(r["last_trade_utc"] or ""))
        consec_losses = int(latest_row["consecutive_losses"])
        last_trade_utc = latest_row["last_trade_utc"]

        return {
            "trades_count": trades_count,
            "wins": wins,
            "losses": losses,
            "win_rate": round(win_rate, 6),
            "gross_profit_usd": round(gross_profit, 4),
            "gross_loss_usd": round(gross_loss, 4),
            "net_profit_usd": round(net_profit, 4),
            "profit_factor": round(profit_factor, 4),
            "total_r": round(total_r, 4),
            "expectancy_r": round(expectancy_r, 4),
            "avg_rr": round(avg_rr, 4),
            "consecutive_losses": consec_losses,
            "last_trade_utc": last_trade_utc,
        }

    def get_blended_strategy_stats(
        self,
        symbol: str,
        regime: str | None = None,
        session: str | None = None,
        prior_strength: float | None = None,
    ) -> list[dict[str, Any]]:
        """
        Compute Bayesian-shrunk blended performance metrics combining 2-year
        `strategy_priors` with `live_strategy_stats` for `(symbol, regime, session)`.

        With 1-2 live trades, shrinkage keeps estimates anchored near the historical
        prior; as live trades grow past `prior_strength`, live performance dominates.
        """
        k_cap = self.prior_strength if prior_strength is None else max(1.0, float(prior_strength))
        req_reg = _norm_key(regime, "ALL")
        req_sess = _norm_key(session, "ALL")

        with self._lock:
            prior_rows = self._conn.execute(
                "SELECT * FROM strategy_priors WHERE symbol = ?", (symbol,)
            ).fetchall()

            live_clauses = ["symbol = ?"]
            live_params: list[Any] = [symbol]
            if req_reg != "ALL":
                live_clauses.append("regime = ?")
                live_params.append(req_reg)
            if req_sess != "ALL":
                live_clauses.append("session = ?")
                live_params.append(req_sess)

            live_rows = self._conn.execute(
                f"SELECT * FROM live_strategy_stats WHERE {' AND '.join(live_clauses)}",
                live_params,
            ).fetchall()

        priors_by_strat: dict[str, list[dict[str, Any]]] = {}
        for r in prior_rows:
            p = self._row_to_prior(r)
            priors_by_strat.setdefault(p["strategy_name"], []).append(p)

        live_by_strat: dict[str, list[sqlite3.Row]] = {}
        for r in live_rows:
            live_by_strat.setdefault(str(r["strategy_name"]), []).append(r)

        all_strategies = sorted(set(priors_by_strat.keys()) | set(live_by_strat.keys()))
        results: list[dict[str, Any]] = []

        for strat in all_strategies:
            prior = self._select_best_prior(priors_by_strat.get(strat, []), req_reg, req_sess)
            live = self._aggregate_live_rows(live_by_strat.get(strat, []))

            live_n = int(live["trades_count"])
            if prior is not None:
                prior_n = int(prior["trades_count"])
                # Effective prior pseudocounts: bounded so live data can eventually adapt
                k_eff = max(5.0, min(float(prior_n), k_cap)) if prior_n > 0 else 5.0
                p_wr = float(prior["win_rate"])
                p_pf = float(prior["profit_factor"])
                p_exp = float(prior["expectancy_r"])
                p_rr = float(prior["avg_rr"])
                p_dd = float(prior["max_dd_pct"])
                is_oos = bool(prior["is_oos_consistent"])
                enabled = bool(prior["enabled"])
                prior_matched_regime = prior["regime"]
                prior_matched_session = prior["session"]
            else:
                prior_n = 0
                k_eff = 5.0
                p_wr = 0.50
                p_pf = 1.00
                p_exp = 0.00
                p_rr = 1.50
                p_dd = 0.0
                is_oos = False
                enabled = True
                prior_matched_regime = None
                prior_matched_session = None

            w_live = live_n / (live_n + k_eff) if live_n > 0 else 0.0
            w_prior = 1.0 - w_live

            blended_wr = (w_prior * p_wr) + (w_live * float(live["win_rate"]))
            blended_pf = (w_prior * p_pf) + (w_live * float(live["profit_factor"]))
            blended_exp_r = (w_prior * p_exp) + (w_live * float(live["expectancy_r"]))
            blended_avg_rr = (w_prior * p_rr) + (w_live * float(live["avg_rr"]))

            if not enabled:
                edge_status = "DISABLED"
            elif blended_exp_r >= 0.15 and blended_pf >= 1.25:
                edge_status = "STRONG"
            elif blended_exp_r >= 0.0 and blended_pf >= 1.0:
                edge_status = "NEUTRAL"
            else:
                edge_status = "WEAK"

            results.append(
                {
                    "symbol": symbol,
                    "strategy_name": strat,
                    "regime": req_reg,
                    "session": req_sess,
                    "enabled": enabled,
                    "is_oos_consistent": is_oos,
                    "edge_status": edge_status,
                    "prior_trades": prior_n,
                    "live_trades": live_n,
                    "live_weight": round(w_live, 4),
                    "prior_strength_used": round(k_eff, 2),
                    "prior_win_rate": round(p_wr, 4),
                    "live_win_rate": round(float(live["win_rate"]), 4),
                    "blended_win_rate": round(blended_wr, 4),
                    "prior_profit_factor": round(p_pf, 4),
                    "live_profit_factor": round(float(live["profit_factor"]), 4),
                    "blended_profit_factor": round(blended_pf, 4),
                    "prior_expectancy_r": round(p_exp, 4),
                    "live_expectancy_r": round(float(live["expectancy_r"]), 4),
                    "blended_expectancy_r": round(blended_exp_r, 4),
                    "blended_avg_rr": round(blended_avg_rr, 4),
                    "prior_max_dd_pct": round(p_dd, 4),
                    "live_net_profit_usd": round(float(live["net_profit_usd"]), 2),
                    "live_consecutive_losses": int(live["consecutive_losses"]),
                    "last_trade_utc": live["last_trade_utc"],
                    "prior_matched_regime": prior_matched_regime,
                    "prior_matched_session": prior_matched_session,
                }
            )

        results.sort(
            key=lambda x: (x["enabled"], x["blended_expectancy_r"], x["blended_profit_factor"]),
            reverse=True,
        )
        return results

    # ------------------------------------------------------------------
    # 6. AI Memory Context & Reporting Summary
    # ------------------------------------------------------------------

    def build_ai_memory_context(
        self,
        symbol: str,
        regime: str = "ALL",
        session: str = "ALL",
        max_recent_trades: int = 5,
        max_lessons: int = 5,
        max_decisions: int = 3,
    ) -> dict[str, Any]:
        """
        Build a compact, token-efficient episodic memory payload ready for
        direct injection into Gemini AI prompts.
        """
        blended = self.get_blended_strategy_stats(symbol, regime=regime, session=session)
        compact_stats = [
            {
                "strategy": s["strategy_name"],
                "enabled": s["enabled"],
                "oos": s["is_oos_consistent"],
                "edge": s["edge_status"],
                "prior_n": s["prior_trades"],
                "live_n": s["live_trades"],
                "wr": round(s["blended_win_rate"], 3),
                "pf": round(s["blended_profit_factor"], 2),
                "exp_r": round(s["blended_expectancy_r"], 3),
                "rr": round(s["blended_avg_rr"], 2),
                "consec_loss": s["live_consecutive_losses"],
            }
            for s in blended
        ]

        trades = self.get_recent_trades(symbol=symbol, limit=max_recent_trades)
        compact_trades = [
            {
                "ticket": t["ticket"],
                "dir": t["direction"],
                "strategy": t["strategy_name"],
                "regime": t["regime"],
                "r": round(float(t["r_multiple"]), 2),
                "pnl": round(float(t["profit_usd"]), 2),
                "reason": t["close_reason"][:80],
                "exit": t["exit_time"][:19],
            }
            for t in trades
        ]

        lessons = self.get_lessons(symbol=symbol, regime=regime, limit=max_lessons)
        compact_lessons = [
            {
                "strategy": l["strategy_name"],
                "regime": l["regime"],
                "type": l["lesson_type"],
                "score": round(float(l["effective_score"]), 2),
                "hits": int(l["reinforcement_count"]),
                "lesson": l["lesson_text"][:220],
            }
            for l in lessons
        ]

        watches = self.get_active_watches(symbol=symbol, include_postponed=True)
        compact_watches = [
            {
                "watch_id": w["watch_id"],
                "strategy": w["strategy_name"],
                "status": w["status"],
                "wake_at_utc": w["wake_at_utc"],
                "postpones": f"{w['postpone_count']}/{w['max_postpones']}",
                "hypothesis": w["hypothesis"][:160],
                "trigger": w["trigger_condition"][:140],
                "invalidation": w["invalidation_condition"][:140],
            }
            for w in watches
        ]

        decisions = self.get_recent_decisions(symbol=symbol, limit=max_decisions)
        compact_decisions = [
            {
                "ts": d["ts_utc"][:19],
                "action": d["action"],
                "strategy": d["strategy_name"],
                "stage": d["setup_stage"],
                "conf": round(float(d["confidence"]), 1),
                "next_wake": d["next_wake_utc"],
                "reason": d["reasoning"][:140],
            }
            for d in decisions
        ]

        return {
            "symbol": symbol,
            "regime": _norm_key(regime, "ALL"),
            "session": _norm_key(session, "ALL"),
            "strategy_stats": compact_stats,
            "recent_trades": compact_trades,
            "learned_lessons": compact_lessons,
            "active_watches": compact_watches,
            "recent_decisions": compact_decisions,
        }

    def get_learning_summary(self) -> dict[str, Any]:
        """Return a dashboard/reporting summary of the entire learning database."""
        with self._lock:
            counts = {
                "strategy_priors": int(
                    self._conn.execute("SELECT COUNT(*) FROM strategy_priors").fetchone()[0]
                ),
                "live_strategy_stats": int(
                    self._conn.execute("SELECT COUNT(*) FROM live_strategy_stats").fetchone()[0]
                ),
                "decision_journal": int(
                    self._conn.execute("SELECT COUNT(*) FROM decision_journal").fetchone()[0]
                ),
                "watch_hypotheses": int(
                    self._conn.execute("SELECT COUNT(*) FROM watch_hypotheses").fetchone()[0]
                ),
                "active_watches": int(
                    self._conn.execute(
                        "SELECT COUNT(*) FROM watch_hypotheses WHERE status IN ('ACTIVE', 'POSTPONED')"
                    ).fetchone()[0]
                ),
                "trade_outcomes": int(
                    self._conn.execute("SELECT COUNT(*) FROM trade_outcomes").fetchone()[0]
                ),
                "learned_lessons": int(
                    self._conn.execute("SELECT COUNT(*) FROM learned_lessons").fetchone()[0]
                ),
            }

            watch_rows = self._conn.execute(
                "SELECT status, COUNT(*) AS cnt FROM watch_hypotheses GROUP BY status"
            ).fetchall()
            watch_breakdown = {s: 0 for s in VALID_WATCH_STATUSES}
            for r in watch_rows:
                watch_breakdown[str(r["status"])] = int(r["cnt"])

            trade_agg = self._conn.execute(
                """
                SELECT
                    COUNT(*) AS total_trades,
                    SUM(CASE WHEN profit_usd > 0 OR (profit_usd = 0 AND r_multiple > 0) THEN 1 ELSE 0 END) AS wins,
                    SUM(CASE WHEN profit_usd < 0 OR (profit_usd = 0 AND r_multiple <= 0) THEN 1 ELSE 0 END) AS losses,
                    COALESCE(SUM(CASE WHEN profit_usd > 0 THEN profit_usd ELSE 0 END), 0.0) AS gross_profit,
                    COALESCE(SUM(CASE WHEN profit_usd < 0 THEN ABS(profit_usd) ELSE 0 END), 0.0) AS gross_loss,
                    COALESCE(SUM(profit_usd), 0.0) AS net_profit,
                    COALESCE(AVG(r_multiple), 0.0) AS avg_r
                FROM trade_outcomes
                """
            ).fetchone()

            total_trades = int(trade_agg["total_trades"] or 0)
            wins = int(trade_agg["wins"] or 0)
            losses = int(trade_agg["losses"] or 0)
            gross_profit = float(trade_agg["gross_profit"] or 0.0)
            gross_loss = float(trade_agg["gross_loss"] or 0.0)
            net_profit = float(trade_agg["net_profit"] or 0.0)
            avg_r = float(trade_agg["avg_r"] or 0.0)
            win_rate = (wins / total_trades) if total_trades > 0 else 0.0
            if gross_loss > 0:
                pf = min(MAX_LIVE_PF_CAP, gross_profit / gross_loss)
            elif gross_profit > 0:
                pf = MAX_LIVE_PF_CAP
            else:
                pf = 0.0

            top_prior_rows = self._conn.execute(
                """
                SELECT symbol, strategy_name, regime, session, trades_count,
                       win_rate, profit_factor, expectancy_r, is_oos_consistent
                FROM strategy_priors
                WHERE enabled = 1
                ORDER BY expectancy_r DESC, profit_factor DESC
                LIMIT 5
                """
            ).fetchall()

            top_live_rows = self._conn.execute(
                """
                SELECT symbol, strategy_name, regime, session, trades_count,
                       win_rate, profit_factor, expectancy_r, net_profit_usd
                FROM live_strategy_stats
                ORDER BY expectancy_r DESC, net_profit_usd DESC
                LIMIT 5
                """
            ).fetchall()

            recent_lessons = self._conn.execute(
                """
                SELECT symbol, strategy_name, regime, lesson_type,
                       weight, reinforcement_count, lesson_text, updated_at_utc
                FROM learned_lessons
                ORDER BY updated_at_utc DESC, id DESC
                LIMIT 5
                """
            ).fetchall()

        return {
            "db_path": ":memory:" if self.is_memory else str(self.db_path),
            "generated_at_utc": _utc_now_iso(),
            "counts": counts,
            "live_performance": {
                "total_trades": total_trades,
                "wins": wins,
                "losses": losses,
                "win_rate": round(win_rate, 4),
                "net_profit_usd": round(net_profit, 2),
                "profit_factor": round(pf, 4),
                "expectancy_r": round(avg_r, 4),
            },
            "watch_breakdown": watch_breakdown,
            "top_priors": [dict(r) for r in top_prior_rows],
            "top_live_strategies": [dict(r) for r in top_live_rows],
            "recent_lessons": [dict(r) for r in recent_lessons],
        }
