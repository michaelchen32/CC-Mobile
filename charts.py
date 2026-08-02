"""Chart generation for the SOXX regime study.

Static PNGs, light mode. Colors follow a validated categorical palette in
fixed slot order; regime shading is light blue (bull) / light red (bear) as
specified. Grids and axes are recessive; every panel has dated x-axes.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Fixed-order categorical palette (validated; see dataviz reference palette).
PALETTE = {
    "buy_and_hold": "#898781",  # muted ink — benchmark, not a competing series
    "hmm": "#2a78d6",
    "hmm_walkforward": "#4a3aa7",
    "cusum": "#eb6834",
    "coppock": "#1baf7a",
    "kalman": "#eda100",
    "vix_ts": "#e87ba4",
    "composite": "#008300",
    "composite_gated": "#e34948",
}
LABELS = {
    "buy_and_hold": "Buy & hold",
    "hmm": "HMM (frozen)",
    "hmm_walkforward": "HMM (walk-forward)",
    "cusum": "CUSUM",
    "coppock": "Coppock",
    "kalman": "Kalman drift",
    "vix_ts": "VIX term structure",
    "composite": "Composite",
    "composite_gated": "Composite + contango gate",
}
BULL_SHADE = "#cde2fb"  # light blue
BEAR_SHADE = "#fbd2d1"  # light red
SURFACE = "#fcfcfb"
GRID = "#e1e0d9"
INK = "#0b0b0b"
MUTED = "#898781"

plt.rcParams.update(
    {
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "axes.edgecolor": "#c3c2b7",
        "axes.labelcolor": INK,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": INK,
        "font.size": 10,
        "axes.titlesize": 11,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "lines.linewidth": 2.0,
    }
)


def _fmt_dates(ax: plt.Axes) -> None:
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))


def _shade_regimes(ax: plt.Axes, signal: pd.Series) -> None:
    """Contiguous bull/bear spans as background shading."""
    sig = signal.dropna().astype(int)
    if sig.empty:
        return
    change = (sig != sig.shift()).cumsum()
    for _, block in sig.groupby(change):
        color = BULL_SHADE if block.iloc[0] == 1 else BEAR_SHADE
        ax.axvspan(block.index[0], block.index[-1], color=color, zorder=0, lw=0)


def regime_panels(
    close: pd.Series,
    signals: dict[str, pd.Series],
    out: Path,
    start: str = "2023-01-01",
) -> None:
    """One panel per algorithm: price with bull/bear shading."""
    px = close.loc[start:]
    names = list(signals)
    fig, axes = plt.subplots(
        len(names), 1, figsize=(11, 2.1 * len(names)), sharex=True
    )
    for ax, name in zip(np.atleast_1d(axes), names):
        sig = signals[name].reindex(close.index).ffill().loc[start:]
        _shade_regimes(ax, sig)
        ax.plot(px.index, px, color=INK, lw=1.2)
        ax.set_ylabel(LABELS.get(name, name), fontsize=9)
        ax.margins(x=0)
        _fmt_dates(ax)
    axes[0].set_title(
        "SOXX with regime shading by algorithm (bull = light blue, bear = light red)",
        loc="left",
    )
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def equity_curves(
    streams: dict[str, pd.DataFrame],
    out: Path,
    basis: str = "net",
) -> None:
    """All strategies vs buy & hold, compounded from 100, net of costs."""
    fig, ax = plt.subplots(figsize=(11, 6))
    order = ["buy_and_hold"] + [k for k in streams if k != "buy_and_hold"]
    ends: list[tuple[float, str]] = []
    for name in order:
        eq = 100.0 * np.exp(streams[name][basis].cumsum())
        lw = 2.6 if name == "buy_and_hold" else 1.8
        ax.plot(eq.index, eq, color=PALETTE[name], lw=lw, label=LABELS[name])
        ends.append((float(eq.iloc[-1]), name))
    # Direct labels at the right edge, staggered so they never overlap.
    ends.sort()
    span = max(e[0] for e in ends) - min(e[0] for e in ends)
    min_gap = span * 0.035
    ys: list[float] = []
    for y, _ in ends:
        if ys and y - ys[-1] < min_gap:
            y = ys[-1] + min_gap
        ys.append(y)
    x_last = streams[order[0]][basis].index[-1]
    for (y_true, name), y_lab in zip(ends, ys):
        ax.annotate(
            LABELS[name], xy=(x_last, y_lab), xytext=(8, 0),
            textcoords="offset points", color=PALETTE[name], fontsize=8,
            va="center",
        )
    ax.set_title(f"Equity curves ({basis} of costs), start = 100", loc="left")
    ax.legend(ncols=3, fontsize=8, loc="upper left")
    ax.margins(x=0.06)
    _fmt_dates(ax)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def drawdown_chart(streams: dict[str, pd.DataFrame], out: Path, basis: str = "net") -> None:
    from backtest import drawdown_curve

    fig, ax = plt.subplots(figsize=(11, 5))
    for name, df in streams.items():
        dd = drawdown_curve(df[basis]) * 100
        lw = 2.6 if name == "buy_and_hold" else 1.6
        ax.plot(dd.index, dd, color=PALETTE[name], lw=lw, label=LABELS[name])
    ax.set_title(f"Drawdowns ({basis} of costs), %", loc="left")
    ax.set_ylabel("Drawdown (%)")
    ax.legend(ncols=3, fontsize=8, loc="lower left")
    ax.margins(x=0)
    _fmt_dates(ax)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def cusum_diagnostic(
    paths: pd.DataFrame,
    signal: pd.Series,
    params: dict[str, float],
    out: Path,
    start: str = "2023-01-01",
) -> None:
    p = paths.loc[start:]
    sig = signal.loc[start:]
    fig, ax = plt.subplots(figsize=(11, 5))
    _shade_regimes(ax, sig)
    ax.plot(p.index, p["S_pos"], color="#2a78d6", lw=1.6, label="S⁺ (bull side)")
    ax.plot(p.index, p["S_neg"], color="#eb6834", lw=1.6, label="S⁻ (bear side)")
    ax.axhline(params["h"], color="#2a78d6", ls="--", lw=1.0)
    ax.axhline(-params["h"], color="#eb6834", ls="--", lw=1.0)
    ax.axhline(0, color="#c3c2b7", lw=0.8)
    ax.annotate(f"h = {params['h']:g}", xy=(p.index[2], params["h"]), fontsize=8,
                color="#2a78d6", va="bottom")
    ax.annotate(f"−h = −{params['h']:g}", xy=(p.index[2], -params["h"]), fontsize=8,
                color="#eb6834", va="top")
    ax.set_title(
        f"CUSUM diagnostic (k = {params['k']:g}, h = {params['h']:g}); "
        "shading = resulting regime",
        loc="left",
    )
    ax.legend(loc="upper left", fontsize=8)
    ax.margins(x=0)
    _fmt_dates(ax)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def hmm_prob_chart(
    close: pd.Series,
    p_bull: pd.Series,
    out: Path,
    start: str = "2023-01-01",
) -> None:
    px = close.loc[start:]
    pb = p_bull.loc[start:]
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(11, 6.5), sharex=True, height_ratios=[2, 1]
    )
    _shade_regimes(ax1, (pb > 0.5).astype(int))
    ax1.plot(px.index, px, color=INK, lw=1.4)
    ax1.set_ylabel("SOXX")
    ax1.set_title("SOXX price and HMM filtered P(bull), test window", loc="left")
    ax1.margins(x=0)
    ax2.plot(pb.index, pb, color="#2a78d6", lw=1.4)
    ax2.axhline(0.5, color="#c3c2b7", ls="--", lw=1.0)
    ax2.set_ylabel("Filtered P(bull)")
    ax2.set_ylim(-0.02, 1.02)
    ax2.margins(x=0)
    _fmt_dates(ax2)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def transition_timing_chart(
    close: pd.Series,
    signals: dict[str, pd.Series],
    episodes: list[dict],
    lags: pd.DataFrame,
    out: Path,
) -> None:
    """Key exhibit: when each algo flipped bear after the peak and bull after
    the trough, for the two biggest test-window drawdowns."""
    n = len(episodes)
    fig, axes = plt.subplots(1, n, figsize=(7.0 * n, 6.5), squeeze=False)
    names = list(signals)
    for j, ep in enumerate(episodes):
        ax = axes[0][j]
        pad = pd.Timedelta(days=40)
        end = ep["recovery"] if ep["recovery"] is not None else close.index[-1]
        win = close.loc[ep["peak"] - pad : end + pad]
        ax.plot(win.index, win, color=INK, lw=1.4)
        ax.axvline(ep["peak"], color=MUTED, ls=":", lw=1.2)
        ax.axvline(ep["trough"], color=MUTED, ls=":", lw=1.2)
        ax.annotate("peak", xy=(ep["peak"], win.max()), fontsize=8, color=MUTED,
                    ha="right", xytext=(-4, 0), textcoords="offset points")
        ax.annotate("trough", xy=(ep["trough"], win.min()), fontsize=8, color=MUTED,
                    ha="left", xytext=(4, 0), textcoords="offset points")
        sub = lags[lags["episode_peak"] == ep["peak"].date()]
        for i, name in enumerate(names):
            row = sub[sub["algorithm"] == name]
            if row.empty:
                continue
            row = row.iloc[0]
            y = win.min() * (0.995 - 0.028 * i)
            if row["bear_flip_date"] is not None and not pd.isna(row["bear_flip_date"]):
                d = pd.Timestamp(row["bear_flip_date"])
                if d in win.index or (win.index[0] <= d <= win.index[-1]):
                    ax.plot([d], [y], marker="v", color=PALETTE[name], ms=8,
                            markeredgecolor=SURFACE, markeredgewidth=1.0, zorder=5)
            if row["bull_flip_date"] is not None and not pd.isna(row["bull_flip_date"]):
                d = pd.Timestamp(row["bull_flip_date"])
                if win.index[0] <= d <= win.index[-1]:
                    ax.plot([d], [y], marker="^", color=PALETTE[name], ms=8,
                            markeredgecolor=SURFACE, markeredgewidth=1.0, zorder=5)
            ax.text(0.01, y, LABELS[name], fontsize=7, color=PALETTE[name],
                    va="center", ha="left",
                    transform=ax.get_yaxis_transform())
        ax.set_title(
            f"Drawdown {ep['depth']:.0%}: peak {ep['peak'].date()}, "
            f"trough {ep['trough'].date()}",
            loc="left", fontsize=10,
        )
        ax.margins(x=0)
        _fmt_dates(ax)
        # reserve a clear band on the left for the algorithm label ladder
        xmin, xmax = ax.get_xlim()
        ax.set_xlim(xmin - 0.17 * (xmax - xmin), xmax)
    fig.suptitle(
        "Transition timing: ▼ = algo turns bear after peak, ▲ = algo turns bull after trough",
        x=0.01, ha="left", fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(out, dpi=150)
    plt.close(fig)
