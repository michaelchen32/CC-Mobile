"""Run the breakout algorithms over the requested names and write a report.

Study windows
-------------
* GOOG ............... breakouts during calendar 2025
* memory names ....... breakouts in late 2025 / early 2026
* optics names ....... breakouts in late 2025 / early 2026
* QQQ/SPY sample ..... full 3-year scan, focused on false positives
"""
from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from breakout.algorithms import ALGORITHMS
from breakout.data import get_ohlcv
from breakout.evaluate import evaluate_ticker, summarize

START, END = "2021-04-01", "2026-05-18"
RESULTS = os.path.join(os.path.dirname(__file__), "results")
CHARTS = os.path.join(RESULTS, "charts")

GROUPS = {
    "GOOG (2025 study)": ["GOOG"],
    "Memory (late-25/early-26 study)": ["MU", "WDC", "STX", "SNDK"],
    "Optics (late-25/early-26 study)": ["COHR", "LITE", "FN", "CIEN", "AAOI", "POET"],
    "QQQ/SPY 3-yr false-positive sample": [
        "NVDA", "AAPL", "MSFT", "AMZN", "META", "TSLA", "AVGO", "AMD",
        "NFLX", "COST", "INTC", "PYPL", "SBUX", "PFE", "MRNA",
    ],
}

WINDOWS = {
    "GOOG": ("2025-01-01", "2025-12-31"),
    "MU": ("2025-09-01", "2026-05-18"),
    "WDC": ("2025-09-01", "2026-05-18"),
    "STX": ("2025-09-01", "2026-05-18"),
    "SNDK": ("2025-09-01", "2026-05-18"),
    "COHR": ("2025-09-01", "2026-05-18"),
    "LITE": ("2025-09-01", "2026-05-18"),
    "FN": ("2025-09-01", "2026-05-18"),
    "CIEN": ("2025-09-01", "2026-05-18"),
    "AAOI": ("2025-09-01", "2026-05-18"),
    "POET": ("2025-09-01", "2026-05-18"),
}

CHART_TICKERS = ["GOOG", "MU", "WDC", "COHR", "LITE", "FN", "NVDA", "PYPL"]


def in_window(df_sig: pd.DataFrame, ticker: str) -> pd.DataFrame:
    if ticker not in WINDOWS or df_sig.empty:
        return df_sig
    lo, hi = WINDOWS[ticker]
    d = pd.to_datetime(df_sig["entry_date"])
    return df_sig[(d >= lo) & (d <= hi)].reset_index(drop=True)


def make_chart(ticker: str, df: pd.DataFrame, sigs: pd.DataFrame, plot_from: str):
    sub = df[df.index >= plot_from]
    if sub.empty:
        return
    fig, ax = plt.subplots(figsize=(13, 6))
    ax.plot(sub.index, sub["Close"], color="#222", lw=1.1, label="Close")
    markers = {
        "true": ("^", "#1a9e54"),
        "false": ("v", "#d62728"),
        "timeout_up": ("o", "#9467bd"),
        "timeout_down": ("P", "#d62728"),
    }
    s = sigs.copy()
    s["d"] = pd.to_datetime(s["entry_date"])
    s = s[s["d"] >= plot_from]
    for outcome, (mk, col) in markers.items():
        m = s[s["outcome"] == outcome]
        if not m.empty:
            ax.scatter(
                m["d"], m["entry_price"], marker=mk, c=col, s=70,
                edgecolors="k", linewidths=0.4, zorder=5,
                label=f"{outcome} ({len(m)})",
            )
    ax.set_title(f"{ticker} — breakout signals ({plot_from} →)")
    ax.set_ylabel("Price ($)")
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    os.makedirs(CHARTS, exist_ok=True)
    fig.savefig(os.path.join(CHARTS, f"{ticker}.png"), dpi=110)
    plt.close(fig)


def md_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "_no signals_\n"
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join("" if pd.isna(v) else str(v) for v in r) + " |")
    return "\n".join(out) + "\n"


def main() -> None:
    os.makedirs(RESULTS, exist_ok=True)
    all_signals = []
    report = ["# Breakout-algorithm study\n"]
    report.append(
        "Algorithms: Donchian/Turtle (20), Darvas box, Bollinger squeeze, "
        "TTM squeeze, volume-confirmed resistance, 52-week-high momentum.\n\n"
        "Two views per signal (entry = signal-bar close, 20 trading-day "
        "horizon):\n\n"
        "1. **Tradeable outcome** — `true` = +8% target hit before −5% stop; "
        "`false` = stop first; `timeout_up/down` = neither. `stop_whipsaw_%` "
        "= (false + timeout_down) / signals.\n"
        "2. **Identification quality** (path-independent) — `confirmed` = "
        "price later ran ≥ +8%; `fakeout` = never made ≥ +4% upside or rolled "
        "over past −5%; `marginal` = in between. `fakeout_%` is the true "
        "false-positive rate for *breakout detection* (a tight stop can "
        "whipsaw a real breakout, which inflates view 1's false count).\n"
    )

    for group, tickers in GROUPS.items():
        report.append(f"\n## {group}\n")
        group_sigs = []
        for t in tickers:
            try:
                df = get_ohlcv(t, START, END)
            except Exception as exc:  # noqa: BLE001
                report.append(f"\n### {t}\n_data error: {exc}_\n")
                continue
            sigs = evaluate_ticker(df, ALGORITHMS)
            sigs.insert(0, "ticker", t)
            all_signals.append(sigs)

            focus = in_window(sigs, t)
            report.append(f"\n### {t}  ({df.index[0].date()} → {df.index[-1].date()})\n")
            if t in WINDOWS:
                lo, hi = WINDOWS[t]
                report.append(f"_signals in study window {lo} → {hi}:_\n\n")
                report.append(md_table(focus.drop(columns=["ticker"])))
            else:
                report.append("_per-algorithm summary (full 3-yr history):_\n\n")
                report.append(md_table(summarize(sigs)))
                fk = sigs[sigs["breakout_class"] == "fakeout"]
                if not fk.empty:
                    show = fk.nsmallest(6, "fwd_return_%")[
                        ["algorithm", "entry_date", "entry_price",
                         "fwd_return_%", "max_favorable_%", "max_adverse_%"]
                    ]
                    report.append(
                        f"\n_worst false positives (fakeouts) — "
                        f"{len(fk)} total:_\n\n"
                    )
                    report.append(md_table(show))
            group_sigs.append(sigs)

            if t in CHART_TICKERS:
                plot_from = WINDOWS.get(t, ("2024-09-01", ""))[0]
                if t == "GOOG":
                    plot_from = "2024-09-01"
                make_chart(t, df, sigs, plot_from)

        if group_sigs:
            gs = pd.concat(group_sigs, ignore_index=True)
            report.append(f"\n**{group} — summary across all signals (full history):**\n\n")
            report.append(md_table(summarize(gs)))

    signals = pd.concat(all_signals, ignore_index=True)
    signals.to_csv(os.path.join(RESULTS, "signals.csv"), index=False)
    overall = summarize(signals)
    overall.to_csv(os.path.join(RESULTS, "summary_by_algo.csv"), index=False)

    report.append("\n## Overall, every name, full history (false-positive view)\n\n")
    report.append(md_table(overall))

    with open(os.path.join(RESULTS, "report.md"), "w") as fh:
        fh.write("\n".join(report))

    print("=== OVERALL SUMMARY BY ALGORITHM ===")
    print(overall.to_string(index=False))
    print(f"\nTotal de-duplicated signals: {len(signals)}")
    print(f"Artifacts written to: {RESULTS}/")


if __name__ == "__main__":
    main()
