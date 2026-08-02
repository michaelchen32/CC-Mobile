"""High-recall breakout system: 3-year backtest over the SPY+QQQ universe
and today's live signals.

  python run_recall.py

Writes results/recall_report.md, results/recall_summary.csv,
results/recall_by_ticker.csv, results/today_signals.csv.
"""
from __future__ import annotations

import os

import pandas as pd

from breakout.data import bulk_fetch
from breakout.recall_backtest import aggregate, evaluate
from breakout.recall_system import todays_signal
from breakout.universe import universe

START, END = "2022-05-01", "2026-05-18"
EVAL_START = "2023-05-15"  # last ~3 years scored; earlier bars warm up MAs
RESULTS = os.path.join(os.path.dirname(__file__), "results")


def md_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "_none_\n"
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |",
           "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(
            "" if pd.isna(v) else str(v) for v in r) + " |")
    return "\n".join(out) + "\n"


def main() -> None:
    os.makedirs(RESULTS, exist_ok=True)
    tickers = universe()
    print(f"Universe: {len(tickers)} SPY+QQQ names. Fetching {START}..{END} ...")
    data = bulk_fetch(tickers, START, END)
    print(f"Resolved data for {len(data)} / {len(tickers)} tickers.")

    per_ticker: dict[str, dict] = {}
    today_rows = []
    for t, df in data.items():
        if len(df) < 260:  # need warm-up for 200-day average
            continue
        try:
            per_ticker[t] = evaluate(df, eval_start=EVAL_START)
        except Exception:  # noqa: BLE001 - never let one name break the run
            continue
        sig = todays_signal(df)
        if sig:
            sig = {"ticker": t, **sig}
            today_rows.append(sig)

    summary = aggregate(per_ticker)
    summary.to_csv(os.path.join(RESULTS, "recall_summary.csv"), index=False)

    by_ticker = pd.DataFrame(
        [
            {
                "ticker": t,
                "episodes": r["union"]["episodes"],
                "caught": r["union"]["caught"],
                "recall_%": r["union"]["recall_%"],
                "signals": r["union"]["signals"],
                "false_alarm_%": r["union"]["false_alarm_%"],
                "signals_per_yr": r["union"]["signals_per_yr"],
            }
            for t, r in per_ticker.items()
        ]
    ).sort_values("episodes", ascending=False)
    by_ticker.to_csv(os.path.join(RESULTS, "recall_by_ticker.csv"), index=False)

    today = pd.DataFrame(today_rows)
    if not today.empty:
        today = today.sort_values(
            ["n_detectors", "trend"], ascending=[False, True]
        ).reset_index(drop=True)
    today.to_csv(os.path.join(RESULTS, "today_signals.csv"), index=False)

    union = summary[summary["detector"] == "union"].iloc[0]
    best_single = summary[summary["detector"] != "union"].iloc[0]
    last_date = max(df.index[-1] for df in data.values()).date().isoformat()

    rep = []
    rep.append("# High-recall breakout system — SPY+QQQ, last 3 years\n")
    rep.append(
        "Goal: **minimise missed breakouts** (opportunity cost of a miss >> "
        "cost of a false alarm). The system is an OR-union of 8 deliberately "
        "loose detectors (see `breakout/recall_system.py`); a soft trend tag "
        "is attached but never suppresses a signal.\n"
    )
    rep.append(
        "\n**Ground truth (independent of the detector):** a day is an "
        "opportunity launch if price gains ≥ +20% within 30 trading days "
        "*and* it is near the start of the move (not already extended). "
        "Launches are clustered so each distinct move counts once. An episode "
        "is *caught* if the system fired from 3 bars before to 15 bars after "
        "the launch while price was still within +12% of it (i.e. still "
        "actionable).\n"
    )
    rep.append(
        f"\nUniverse: {len(per_ticker)} names with sufficient history. "
        f"Scored window: {EVAL_START} → {last_date}.\n"
    )

    rep.append("\n## Recall vs. cost, by detector\n\n")
    rep.append(md_table(summary))
    rep.append(
        f"\n**Headline:** the union catches **{union['recall_%']}%** of all "
        f"+20% episodes vs. **{best_single['recall_%']}%** for the best "
        f"single detector (`{best_single['detector']}`) — the OR-ensemble is "
        f"the entire point. Cost: ~{union['avg_signals_per_name_yr']} "
        f"signals/name/yr and a {union['false_alarm_%']}% false-alarm rate, "
        "which is the accepted trade for high recall.\n"
    )

    miss = by_ticker[(by_ticker["episodes"] >= 3)].nsmallest(12, "recall_%")
    rep.append("\n## Where recall is weakest (>=3 episodes)\n\n")
    rep.append(md_table(miss))

    rep.append(f"\n## Live signals on {last_date}\n\n")
    rep.append(
        f"{len(today)} names firing today. Higher `n_detectors` = more "
        "independent triggers agreeing; `trend=up` = above a rising 50-day "
        "average.\n\n"
    )
    strong = today[today["n_detectors"] >= 2] if not today.empty else today
    rep.append("**Multi-detector signals (n_detectors >= 2):**\n\n")
    rep.append(md_table(
        strong.drop(columns=["date"]) if not strong.empty else strong))
    rep.append(
        f"\n_Full list of {len(today)} names in "
        "`results/today_signals.csv`._\n"
    )

    with open(os.path.join(RESULTS, "recall_report.md"), "w") as fh:
        fh.write("\n".join(rep))

    print("\n=== RECALL SUMMARY (by detector) ===")
    print(summary.to_string(index=False))
    print(f"\nLive signals on {last_date}: {len(today)} names "
          f"({len(strong)} with >=2 detectors)")
    print(f"Artifacts in {RESULTS}/")


if __name__ == "__main__":
    main()
