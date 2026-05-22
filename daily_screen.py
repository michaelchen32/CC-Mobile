"""Daily market-close breakout screen.

Designed to be invoked once per day (by a Claude Code on the web
scheduled trigger, an in-session loop, or cron). It:

  1. refreshes price data for the SPY+QQQ universe (cache key includes the
     run date, so each calendar day pulls a fresh latest bar),
  2. runs the high-recall screen on the most recent bar,
  3. diffs against the previous run to flag NEW / DROPPED names,
  4. for every NEW name, pulls a 4-quarter earnings recap and the price-
     rise drivers,
  5. writes a dated snapshot + a human-readable markdown brief.

Usage:
  python daily_screen.py [YYYY-MM-DD]   # default: today

Outputs:
  results/screen_history/<date>.csv        full ranked list that day
  results/daily_screen_latest.md           today's brief (full list + new)
"""
from __future__ import annotations

import os
import sys
from datetime import date, timedelta

import pandas as pd

from breakout.data import bulk_fetch
from breakout.recall_system import todays_signal
from breakout.transcripts import save_transcripts
from breakout.universe import universe
from collect_fundamentals import (
    _m,
    _pct,
    annual_series,
    breakout_reason,
    earnings_recap,
    fetch,
    perf,
)

RESULTS = os.path.join(os.path.dirname(__file__), "results")
HIST = os.path.join(RESULTS, "screen_history")
LOOKBACK_DAYS = 420  # enough history for SMA200 + 126-day high warm-up


def prev_snapshot(run_day: date) -> tuple[str | None, set]:
    if not os.path.isdir(HIST):
        return None, set()
    snaps = sorted(
        f for f in os.listdir(HIST)
        if f.endswith(".csv") and f[:-4] < run_day.isoformat()
    )
    if not snaps:
        return None, set()
    last = snaps[-1]
    df = pd.read_csv(os.path.join(HIST, last))
    return last[:-4], set(df["ticker"])


def rise_drivers(tk: str, t, info: dict, pf: dict, eps: pd.DataFrame,
                 ann: pd.DataFrame) -> str:
    bits = []
    if pf.get("L1M_%") is not None:
        bits.append(
            f"price L1M {_pct(pf['L1M_%'])} / L3M {_pct(pf.get('L3M_%'))} / "
            f"L12M {_pct(pf.get('L12M_%'))}")
    if not eps.empty:
        beats = (eps["Surprise(%)"] > 0).sum()
        bits.append(
            f"EPS beat {beats}/{len(eps)} of last quarters "
            f"(latest surprise {eps['Surprise(%)'].iloc[0]}%)")
    if not ann.empty:
        g = ann["Rev_growth"].dropna()
        if not g.empty:
            trend = ("accelerating" if len(g) >= 2 and g.iloc[-1] > g.iloc[-2]
                     else "decelerating" if len(g) >= 2 else "n/a")
            bits.append(
                f"revenue growth {_pct(g.iloc[-1])} latest FY ({trend})")
    rg = info.get("revenueGrowth")
    if rg is not None:
        bits.append(f"TTM revenue growth {_pct(rg)}")
    fav = []
    for k in ("fiftyTwoWeekChange", "industry"):
        if info.get(k):
            fav.append(f"{k}={info.get(k)}")
    if pf.get("pct_from_12m_high_%") is not None:
        v = pf["pct_from_12m_high_%"]
        bits.append("breaking to fresh 12-mo highs" if v > -0.02
                     else f"recovering ({_pct(v)} below 12-mo high)")
    return "; ".join(bits) if bits else "drivers n/a"


def main() -> None:
    run_day = (date.fromisoformat(sys.argv[1])
               if len(sys.argv) > 1 else date.today())
    start = (run_day - timedelta(days=LOOKBACK_DAYS)).isoformat()
    end = (run_day + timedelta(days=1)).isoformat()
    os.makedirs(HIST, exist_ok=True)

    tickers = universe()
    print(f"[{run_day}] fetching {len(tickers)} names {start}..{end}")
    data = bulk_fetch(tickers, start, end)
    print(f"resolved {len(data)} names")

    rows = []
    for tk, df in data.items():
        if len(df) < 260:
            continue
        sig = todays_signal(df)
        if sig:
            rows.append({"ticker": tk, **sig})
    today = pd.DataFrame(rows)
    if today.empty:
        print("no signals today")
        return
    today = today.sort_values(
        ["n_detectors", "trend"], ascending=[False, True]
    ).reset_index(drop=True)

    snap_path = os.path.join(HIST, f"{run_day.isoformat()}.csv")
    today.to_csv(snap_path, index=False)

    prev_day, prev_set = prev_snapshot(run_day)
    cur_set = set(today["ticker"])
    new_names = sorted(cur_set - prev_set)
    dropped = sorted(prev_set - cur_set)

    md = [f"# Daily breakout screen — {run_day.isoformat()}\n"]
    md.append(
        f"Universe: {len(data)} SPY+QQQ names. **{len(today)} signals** on "
        f"the latest bar. High-recall technical screen (OR of 8 detectors); "
        f"`trend` is context only, not a filter.\n")
    if prev_day:
        md.append(
            f"\nCompared to previous run ({prev_day}): "
            f"**{len(new_names)} new**, {len(dropped)} dropped.\n")
    else:
        md.append("\n_First run — no prior baseline to diff against._\n")

    md.append("\n## Full list (ranked by detector count)\n\n")
    md.append("| # | ticker | close | n_det | detectors | trend | NEW? |\n")
    md.append("|---|---|---|---|---|---|---|\n")
    for i, r in today.iterrows():
        flag = "🟢 NEW" if r["ticker"] in new_names else ""
        md.append(
            f"| {i+1} | {r['ticker']} | {r['close']} | {r['n_detectors']} "
            f"| {r['detectors']} | {r['trend']} | {flag} |\n")

    if dropped:
        md.append(f"\n**Dropped since {prev_day}:** {', '.join(dropped)}\n")

    md.append("\n## New additions — earnings recap & rise drivers\n")
    if not new_names:
        md.append("\n_No new names vs. the previous run._\n")
    for tk in new_names:
        t, info = fetch(tk)
        md.append(f"\n### {tk}"
                  + (f" — {info.get('shortName','')}" if info else "") + "\n")
        if t is None:
            md.append("_data unavailable_\n")
            continue
        try:
            ann = annual_series(t)
        except Exception:  # noqa: BLE001
            ann = pd.DataFrame()
        eps = earnings_recap(t)
        pf = perf(tk) or {}
        row = today[today["ticker"] == tk].iloc[0]

        md.append("\n_Last 4 reported quarters (EPS):_\n\n")
        if eps.empty:
            md.append("EPS history n/a\n")
        else:
            md.append("| date | est | reported | surprise % |\n|---|---|---|---|\n")
            for d, e in eps.iterrows():
                md.append(f"| {d} | {e['EPS Estimate']} | "
                          f"{e['Reported EPS']} | {e['Surprise(%)']} |\n")
        if not ann.empty:
            last = ann.iloc[-1]
            md.append(
                f"\n_Latest FY:_ revenue {_m(last.Revenue)} "
                f"({_pct(last.Rev_growth)} YoY), net margin "
                f"{_pct(last.Net_margin)}, FCF {_m(last.FCF)} "
                f"({_pct(last.FCF_margin)} margin).\n")
        md.append(f"\n_Breakout trigger:_ {breakout_reason(row, pf)}\n")
        md.append(f"\n_Why the stock has been rising:_ "
                  f"{rise_drivers(tk, t, info, pf, eps, ann)}\n")

        import breakout.transcripts as _tx
        saved = save_transcripts(
            tk, os.path.join(RESULTS, "transcripts"), quarters=4)
        if saved:
            md.append(
                f"\n_Call transcripts (last {len(saved)} q) saved for "
                f"summarisation:_ {', '.join(os.path.basename(p) for p in saved)}\n")
        else:
            md.append(
                f"\n_Call-transcript narrative unavailable — {_tx.last_reason}. "
                "Above is a quantitative recap from reported figures._\n")

    with open(os.path.join(RESULTS, "daily_screen_latest.md"), "w") as fh:
        fh.write("".join(md))
    print(f"{len(today)} signals; {len(new_names)} new; "
          f"snapshot -> {snap_path}")


if __name__ == "__main__":
    main()
