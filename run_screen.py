#!/usr/bin/env python3
"""Entry point: run the >$10bn US large-cap breakout screen and write outputs.

    python run_screen.py                # today
    python run_screen.py 2026-07-17     # explicit trading session (latest close)

Outputs (in results/):
    screen_<date>.csv         ranked signal table
    breakout_brief_<date>.md  narrative brief (sector grouped, conviction tiers)
"""
from __future__ import annotations

import os
import sys
from collections import Counter, defaultdict

from screener.screen import run_screen, signals_dataframe

RESULTS = os.path.join(os.path.dirname(__file__), "results")

DETECTOR_LABEL = {
    "fast_donchian": "10-day base break",
    "donchian_20": "20-day high",
    "six_month_high": "6-month high",
    "volume_thrust": "volume thrust",
    "gap_go": "gap-and-go",
    "range_expansion": "range expansion",
    "squeeze_release": "squeeze release",
    "trend_continuation": "trend continuation",
}


def _fmt_mcap(bn: float) -> str:
    return f"${bn/1000:.2f}T" if bn >= 1000 else f"${bn:.0f}bn"


def _fmt_rev(g) -> str:
    return f"{g*100:+.0f}% rev" if isinstance(g, (int, float)) else ""


def write_brief(result: dict) -> str:
    sess = result["session_date"]
    sigs = result["signals"]
    path = os.path.join(RESULTS, f"breakout_brief_{sess}.md")

    trend_dist = Counter(s["trend"] for s in sigs)
    by_sector: dict[str, list] = defaultdict(list)
    for s in sigs:
        by_sector[s.get("sector", "Unknown")].append(s)

    top = [s for s in sigs if s["n_detectors"] >= 4]
    fragile = [s for s in sigs if s["n_detectors"] == 1 and s["detectors"] == ["gap_go"]]

    L: list[str] = []
    L.append(f"# US Large-Cap Breakout Screen — {sess}")
    L.append("")
    L.append(f"*Universe:* all US-listed stocks with market cap > "
             f"${result['min_market_cap']/1e9:.0f}bn "
             f"({result['universe_size']} names; OHLCV resolved for {result['resolved']}).  ")
    L.append(f"*Method:* 8-detector high-recall breakout union (any detector firing = "
             f"signal; `n_det` = confluence). Trend tag is context only.  ")
    L.append(f"*Signals this session:* **{len(sigs)}** "
             f"(trend mix — up {trend_dist['up']}, weak {trend_dist['weak']}, down {trend_dist['down']}).")
    L.append("")

    # Top conviction
    L.append("## Top conviction (n_det ≥ 4)")
    L.append("")
    if top:
        L.append("| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Detectors |")
        L.append("|---|---|--:|--:|--:|:--:|:--:|---|")
        for s in top:
            dets = ", ".join(DETECTOR_LABEL.get(d, d) for d in s["detectors"])
            L.append(f"| **{s['symbol']}** | {s['name'][:32]} | {_fmt_mcap(s['market_cap']/1e9)} "
                     f"| {s['close']:.2f} | {s['day_ret']:+.1f}% | {s['n_detectors']} "
                     f"| {s['trend']} | {dets} |")
    else:
        L.append("*None this session — no name tripped 4+ detectors at once.*")
    L.append("")

    # By sector
    L.append("## Signals by sector")
    L.append("")
    for sector in sorted(by_sector, key=lambda k: -len(by_sector[k])):
        group = sorted(by_sector[sector], key=lambda s: (s["n_detectors"], s["day_ret"]), reverse=True)
        L.append(f"### {sector} ({len(group)})")
        L.append("")
        L.append("| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |")
        L.append("|---|---|--:|--:|--:|:--:|:--:|---|")
        for s in group:
            dets = ", ".join(DETECTOR_LABEL.get(d, d) for d in s["detectors"])
            rev = _fmt_rev(s.get("rev_growth"))
            note = dets + (f" · {rev}" if rev else "")
            L.append(f"| {s['symbol']} | {s['name'][:30]} | {_fmt_mcap(s['market_cap']/1e9)} "
                     f"| {s['close']:.2f} | {s['day_ret']:+.1f}% | {s['n_detectors']} "
                     f"| {s['trend']} | {note} |")
        L.append("")

    # Fragile cohort
    L.append("## Fragility flag")
    L.append("")
    if fragile:
        L.append(f"{len(fragile)} single-detector **gap-and-go-only** fires "
                 f"(the high-false-alarm cohort — these often fade within 1–2 sessions):")
        L.append("")
        L.append(", ".join(f"`{s['symbol']}`" for s in fragile))
    else:
        L.append("*No single-detector gap-and-go-only fires this session.*")
    L.append("")

    L.append("---")
    L.append("")
    L.append("**Disclaimer.** Educational analysis only — **not investment advice**. "
             "Breakout detection is a high-recall/high-false-alarm screen; a signal is a "
             "starting point for research, not a recommendation. Prices are auto-adjusted "
             "OHLCV from Yahoo Finance and may contain errors. Past performance does not "
             "guarantee future results.")
    L.append("")

    with open(path, "w") as fh:
        fh.write("\n".join(L))
    return path


def main() -> None:
    asof = sys.argv[1] if len(sys.argv) > 1 else None
    os.makedirs(RESULTS, exist_ok=True)

    result = run_screen(asof=asof)
    sess = result["session_date"]

    df = signals_dataframe(result)
    csv_path = os.path.join(RESULTS, f"screen_{sess}.csv")
    df.to_csv(csv_path, index=False)

    brief_path = write_brief(result)

    print(f"\nSession screened: {sess}")
    print(f"Signals: {len(result['signals'])} / {result['universe_size']} universe "
          f"({result['resolved']} resolved)")
    print(f"  CSV:   {csv_path}")
    print(f"  Brief: {brief_path}")
    top = [s for s in result["signals"] if s["n_detectors"] >= 4]
    if top:
        print(f"  Top conviction (n_det>=4): "
              + ", ".join(f"{s['symbol']}({s['n_detectors']})" for s in top[:15]))


if __name__ == "__main__":
    main()
