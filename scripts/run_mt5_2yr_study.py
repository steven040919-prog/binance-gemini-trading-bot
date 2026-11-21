from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.mt5_backtester import (
    DEFAULT_MT5_SYMBOLS,
    MT5Backtester,
    check_mt5_connection,
    export_strategy_priors,
)


def format_markdown_report(
    mt5_status: dict[str, Any],
    study: dict[str, Any],
    cadence: dict[str, Any] | None,
) -> str:
    lines: list[str] = []
    lines.append("# MT5 2-Year Multi-Strategy Backtest & Cadence Study")
    lines.append("")
    lines.append(f"- **Generated (UTC):** `{study.get('generated_at_utc')}`")
    lines.append(f"- **MT5 Terminal Connected:** `{mt5_status.get('connected')}` ({mt5_status.get('reason')})")
    if mt5_status.get("account_login"):
        lines.append(f"- **MT5 Account:** `{mt5_status.get('account_login')}` @ `{mt5_status.get('server')}`")
    lines.append(f"- **Data Source:** `{study.get('data_source')}`")
    lines.append(f"- **Primary Timeframe:** `{study.get('timeframe')}` | **Years:** `{study.get('years')}` | **Symbols:** `{len(study.get('symbols', []))}`")
    lines.append("")

    ov = study.get("overall", {})
    lines.append("## Overall Performance (IS Year 1 vs OOS Year 2)")
    lines.append("")
    lines.append("| Split | Trades | Win Rate % | Profit Factor | Expectancy (R) | Total R | Avg RR | Max DD % |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for label, key in [("ALL (2Y)", "all"), ("IS (Year 1)", "is"), ("OOS (Year 2)", "oos")]:
        m = ov.get(key, {})
        lines.append(
            f"| {label} | {m.get('trades_count', 0)} | {m.get('win_rate', 0):.2f} | "
            f"{m.get('profit_factor', 0):.3f} | {m.get('expectancy_r', 0):+.4f} | "
            f"{m.get('total_r', 0):+.2f} | {m.get('avg_rr', 0):.2f} | {m.get('max_dd_pct', 0):.2f} |"
        )
    lines.append("")

    lines.append("## Strategy Breakdown (IS vs OOS)")
    lines.append("")
    lines.append("| Strategy | Trades | Win % | PF (All) | Exp R (All) | PF (IS) | Exp R (IS) | PF (OOS) | Exp R (OOS) | Max DD % |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for sname, sdata in study.get("by_strategy", {}).items():
        ma = sdata.get("all", {})
        mi = sdata.get("is", {})
        mo = sdata.get("oos", {})
        lines.append(
            f"| `{sname}` | {ma.get('trades_count', 0)} | {ma.get('win_rate', 0):.2f} | "
            f"{ma.get('profit_factor', 0):.3f} | {ma.get('expectancy_r', 0):+.4f} | "
            f"{mi.get('profit_factor', 0):.3f} | {mi.get('expectancy_r', 0):+.4f} | "
            f"{mo.get('profit_factor', 0):.3f} | {mo.get('expectancy_r', 0):+.4f} | {ma.get('max_dd_pct', 0):.2f} |"
        )
    lines.append("")

    priors = [p for p in study.get("priors", []) if p.get("regime") != "ALL" and p.get("trades_count", 0) >= 8]
    top_priors = sorted(priors, key=lambda p: (p.get("is_oos_consistent", False), p.get("expectancy_r", -9.0)), reverse=True)[:15]
    if top_priors:
        lines.append("## Top 15 (Symbol, Strategy, Regime) Priors (min 8 trades)")
        lines.append("")
        lines.append("| Symbol | Strategy | Regime | Trades | Win % | PF | Exp (R) | IS+OOS OK | Enabled |")
        lines.append("|---|---|---|---:|---:|---:|---:|:---:|:---:|")
        for p in top_priors:
            lines.append(
                f"| `{p['symbol']}` | `{p['strategy_name']}` | `{p['regime']}` | {p['trades_count']} | "
                f"{p['win_rate']:.1f} | {p['profit_factor']:.2f} | {p['expectancy_r']:+.3f} | "
                f"{'YES' if p['is_oos_consistent'] else 'no'} | {'YES' if p['enabled'] else 'no'} |"
            )
        lines.append("")

    if cadence:
        lines.append("## 15m vs 30m Evaluation Cadence Comparison (M15 Bars)")
        lines.append("")
        lines.append(f"- **Data Source:** `{cadence.get('data_source')}` | **Days Covered:** `{cadence.get('days_covered')}`")
        lines.append(f"- **Sniper Wakes Total:** `{cadence.get('sniper_wakes_total')}` | **Sniper Triggered Trades:** `{cadence.get('sniper_triggered_trades')}`")
        lines.append("")
        lines.append("| Cadence Mode | Est AI Calls/Day | Trades | Capture vs 15m | Missed vs 15m | Win % | PF | Exp (R) | Total R | Max DD % |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for mode_name, mm in cadence.get("modes", {}).items():
            lines.append(
                f"| `{mode_name}` | {mm.get('est_ai_calls_per_day', 0):.1f} | {mm.get('trades_count', 0)} | "
                f"{mm.get('capture_rate_vs_15m_pct', 0):.1f}% | {mm.get('missed_entries_vs_15m', 0)} | "
                f"{mm.get('win_rate', 0):.2f} | {mm.get('profit_factor', 0):.3f} | {mm.get('expectancy_r', 0):+.4f} | "
                f"{mm.get('total_r', 0):+.2f} | {mm.get('max_dd_pct', 0):.2f} |"
            )
        lines.append("")
        lines.append(f"**Recommendation:** {cadence.get('recommended_cadence')}")
        lines.append(f"> {cadence.get('rationale')}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run 2-year MT5 multi-strategy backtest & 15m vs 30m cadence study.")
    parser.add_argument("--years", type=float, default=2.0, help="Years of historical data to evaluate (default: 2.0)")
    parser.add_argument("--timeframe", type=str, default="H1", help="Primary study timeframe (default: H1)")
    parser.add_argument("--symbols", type=str, default="", help="Comma-separated symbols (default: all 14 MT5 symbols)")
    parser.add_argument("--cadence-symbols", type=str, default="", help="Optional subset of symbols for M15 cadence comparison")
    parser.add_argument("--skip-cadence", action="store_true", help="Skip 15m vs 30m cadence study")
    parser.add_argument("--offline-synthetic", action="store_true", help="Force reproducible synthetic multi-regime data")
    parser.add_argument("--refresh-cache", action="store_true", help="Force refresh MT5 history CSV cache")
    parser.add_argument("--output-json", type=str, default="data/mt5_2yr_strategy_priors.json", help="Output JSON priors path")
    parser.add_argument("--output-report", type=str, default="data/mt5_2yr_study_report.md", help="Output Markdown report path")
    args = parser.parse_args()

    t0 = time.time()
    mt5_status = check_mt5_connection()
    print(f"[MT5] Connection check: {mt5_status}")

    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()] if args.symbols else list(DEFAULT_MT5_SYMBOLS)
    bt = MT5Backtester()

    print(f"[STUDY] Running {args.years}Y {args.timeframe} backtest across {len(symbols)} symbols...")
    study = bt.run_2yr_study(
        symbols=symbols,
        timeframe_str=args.timeframe,
        years=args.years,
        use_cache=True,
        force_refresh=args.refresh_cache,
        force_synthetic=args.offline_synthetic,
    )

    cadence: dict[str, Any] | None = None
    if not args.skip_cadence:
        cad_syms = (
            [s.strip() for s in args.cadence_symbols.split(",") if s.strip()]
            if args.cadence_symbols
            else symbols
        )
        print(f"[CADENCE] Running 15m vs 30m vs 30m+Sniper comparison on M15 bars ({len(cad_syms)} symbols)...")
        cadence = bt.compare_evaluation_cadence(
            symbols=cad_syms,
            years=args.years,
            use_cache=True,
            force_refresh=args.refresh_cache,
            force_synthetic=args.offline_synthetic,
        )

    out_json = Path(args.output_json)
    export_strategy_priors(study, output_path=out_json, cadence_comparison=cadence)

    report_md = format_markdown_report(mt5_status, study, cadence)
    out_report = Path(args.output_report)
    out_report.parent.mkdir(parents=True, exist_ok=True)
    out_report.write_text(report_md, encoding="utf-8")

    elapsed = time.time() - t0
    print(f"\n=== DONE in {elapsed:.1f}s ===")
    print(f"JSON Priors: {out_json}")
    print(f"Report MD:   {out_report}\n")
    print(report_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
