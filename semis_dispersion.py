#!/usr/bin/env python3
"""Semiconductor Dispersion — Equity-Only Regime Test.

See README.md for the thesis, what is being measured, and (important) the
caveats about why this is a proxy and not the real options dispersion trade.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from datetime import date
from typing import Optional, Tuple

import numpy as np
import pandas as pd


DEFAULT_UNIVERSE = [
    "NVDA", "AMD", "INTC", "AVGO", "QCOM", "TSM", "MU", "MRVL",
    "AMAT", "LRCX", "KLAC", "ASML", "SNPS", "CDNS",
    "TXN", "ADI", "MCHP", "ON", "MPWR", "SWKS", "QRVO", "NXPI",
    "STM", "GFS", "ARM",
]
DEFAULT_INDEX = "SMH"
TRADING_DAYS = 252
CORR_WINDOW = 60
DISP_SMOOTH = 21
FAVORABLE_CORR_PCTILE = 33
FAVORABLE_DISP_PCTILE = 67


# ---------------------------------------------------------------------------
# data
# ---------------------------------------------------------------------------

def fetch_data(tickers, start, end):
    """Download adjusted closes from yfinance."""
    try:
        import yfinance as yf
    except ImportError:
        sys.exit("yfinance not installed. Run: pip install -r requirements.txt")

    data = yf.download(
        tickers, start=start, end=end,
        auto_adjust=True, progress=False, group_by="column",
    )
    if data is None or data.empty:
        sys.exit(f"no data returned for {tickers}")

    if isinstance(data.columns, pd.MultiIndex):
        field = "Close" if "Close" in data.columns.get_level_values(0) else "Adj Close"
        prices = data[field]
    else:
        field = "Close" if "Close" in data.columns else "Adj Close"
        prices = data[[field]].rename(columns={field: tickers[0]})

    return prices.sort_index().dropna(how="all")


def synthetic_data(start="2018-01-01", end="2024-12-31", n_names=25, seed=42):
    """Two-regime dataset for pipeline validation.

    First half: high pairwise correlation (rho ~ 0.7).
    Second half: rotation regime, low correlation (rho ~ 0.15).
    Index = equal-weighted basket, so every name has population beta = 1.
    """
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(start, end)
    n = len(dates)
    half = n // 2

    def block(n_days, rho, mu=0.0003, sigma=0.02):
        # r_i = sqrt(rho)*F + sqrt(1-rho)*eps_i  =>  pairwise corr = rho
        a, b = np.sqrt(rho), np.sqrt(1 - rho)
        f = rng.standard_normal(n_days)
        e = rng.standard_normal((n_days, n_names))
        return mu + sigma * (a * f[:, None] + b * e)

    rets = np.vstack([block(half, 0.7), block(n - half, 0.15)])
    tickers = [f"SYN{i:02d}" for i in range(n_names)]
    name_rets = pd.DataFrame(rets, index=dates, columns=tickers)
    name_prices = (1 + name_rets).cumprod() * 100

    idx_rets = name_rets.mean(axis=1)
    idx_prices = (1 + idx_rets).cumprod() * 100

    all_prices = name_prices.copy()
    all_prices["SYNX"] = idx_prices
    return all_prices, "SYNX", tickers


# ---------------------------------------------------------------------------
# diagnostics
# ---------------------------------------------------------------------------

def compute_returns(prices):
    return prices.pct_change().dropna(how="all")


def rolling_avg_pairwise_corr(returns, window=CORR_WINDOW):
    """Mean off-diagonal pairwise correlation over a rolling window."""
    out = pd.Series(index=returns.index, dtype=float)
    if returns.shape[1] < 2:
        return out
    vals = returns.values
    for i in range(window - 1, len(returns)):
        block = vals[i - window + 1 : i + 1]
        # drop names with no data in this window
        keep = ~np.all(np.isnan(block), axis=0)
        sub = block[:, keep]
        if sub.shape[1] < 2:
            continue
        c = pd.DataFrame(sub).corr().values
        n = c.shape[0]
        # mean of strictly off-diagonal entries
        out.iloc[i] = (np.nansum(c) - np.trace(c)) / (n * (n - 1))
    return out


def cross_sectional_dispersion(returns, smooth=DISP_SMOOTH):
    """Daily cross-sectional std of returns, smoothed with a rolling mean."""
    daily = returns.std(axis=1)
    return daily.rolling(smooth, min_periods=max(5, smooth // 2)).mean()


def rolling_beta_and_idio_vol(returns, idx_returns, window=60):
    """Rolling beta-to-index and idiosyncratic vol for each name."""
    idx_returns = idx_returns.reindex(returns.index)
    cov = returns.rolling(window).cov(idx_returns)
    var_i = idx_returns.rolling(window).var()
    beta = cov.div(var_i, axis=0)
    var_s = returns.rolling(window).var()
    resid_var = var_s.sub(beta.pow(2).mul(var_i, axis=0))
    idio_vol = resid_var.clip(lower=0).pow(0.5)
    return beta, idio_vol


# ---------------------------------------------------------------------------
# regime report
# ---------------------------------------------------------------------------

def percentile_rank(series, value):
    """Empirical CDF of `value` within `series`, returned as 0–100."""
    s = series.dropna()
    if len(s) == 0 or np.isnan(value):
        return float("nan")
    return float((s <= value).mean() * 100)


@dataclass
class RegimeReport:
    as_of: str
    n_names: int
    avg_pairwise_corr: float
    corr_percentile: float
    corr_60d_change: float
    dispersion: float
    dispersion_percentile: float
    verdict: str


def build_regime_report(corr_series, disp_series, n_names):
    corr_clean = corr_series.dropna()
    disp_clean = disp_series.dropna()
    if corr_clean.empty or disp_clean.empty:
        raise ValueError("not enough data to build regime report")

    corr_last = float(corr_clean.iloc[-1])
    disp_last = float(disp_clean.iloc[-1])

    corr_pctile = percentile_rank(corr_series, corr_last)
    disp_pctile = percentile_rank(disp_series, disp_last)

    if len(corr_clean) >= 61:
        corr_60d_change = float(corr_clean.iloc[-1] - corr_clean.iloc[-61])
    else:
        corr_60d_change = float("nan")

    favorable = (
        not np.isnan(corr_pctile)
        and not np.isnan(disp_pctile)
        and corr_pctile < FAVORABLE_CORR_PCTILE
        and disp_pctile > FAVORABLE_DISP_PCTILE
    )
    verdict = "FAVORABLE" if favorable else "NEUTRAL / UNFAVORABLE"

    return RegimeReport(
        as_of=str(corr_clean.index[-1].date()),
        n_names=n_names,
        avg_pairwise_corr=corr_last,
        corr_percentile=corr_pctile,
        corr_60d_change=corr_60d_change,
        dispersion=disp_last,
        dispersion_percentile=disp_pctile,
        verdict=verdict,
    )


# ---------------------------------------------------------------------------
# backtest
# ---------------------------------------------------------------------------

@dataclass
class BacktestResult:
    ann_return: float
    ann_vol: float
    sharpe: float
    max_drawdown: float
    realized_beta_to_index: float
    avg_monthly_turnover: float
    strat_dispersion_corr: float
    n_rebalances: int
    avg_basket_size: float


def run_backtest(returns, idx_returns, idio_vols, betas, disp_series,
                 top_quantile=0.20):
    """Monthly: long top-quantile of idio_vol (equal weight), short index sized
    to net beta = 0. Weights and short size are held constant within month
    (i.e. rebalanced daily back to equal weight — a small simplification).
    Returns on a rebalance day reflect the PRIOR month's positioning; new
    weights take effect the next day.
    """
    returns = returns.dropna(how="all")
    idx_returns = idx_returns.reindex(returns.index)

    month_ends = list(returns.groupby(pd.Grouper(freq="ME")).tail(1).index)
    if len(month_ends) < 2:
        raise ValueError("not enough data for monthly rebalance")

    strat_returns = pd.Series(index=returns.index, dtype=float)
    weights = pd.Series(0.0, index=returns.columns)
    prev_weights = weights.copy()
    short_size = 0.0
    turnovers = []
    basket_sizes = []
    is_active = False

    for dt in returns.index:
        if is_active:
            day_rets = returns.loc[dt].fillna(0.0)
            r_long = float((weights * day_rets).sum())
            idx_r = idx_returns.loc[dt]
            r_short = short_size * (0.0 if pd.isna(idx_r) else float(idx_r))
            strat_returns.loc[dt] = r_long - r_short

        if dt in month_ends:
            iv = idio_vols.loc[dt].dropna() if dt in idio_vols.index else pd.Series(dtype=float)
            b = betas.loc[dt].dropna() if dt in betas.index else pd.Series(dtype=float)
            usable = iv.index.intersection(b.index)
            if len(usable) < 3:
                continue
            iv = iv.loc[usable]
            b = b.loc[usable]
            n_pick = max(1, int(round(len(iv) * top_quantile)))
            picked = iv.nlargest(n_pick).index
            new_weights = pd.Series(0.0, index=returns.columns)
            new_weights[picked] = 1.0 / n_pick
            new_short = float(b.loc[picked].mean())

            turn = float((new_weights - prev_weights).abs().sum()
                         + abs(new_short - short_size))
            turnovers.append(turn)
            basket_sizes.append(n_pick)

            weights = new_weights
            short_size = new_short
            prev_weights = new_weights.copy()
            is_active = True

    strat_returns = strat_returns.dropna()
    if len(strat_returns) < 30:
        raise ValueError("backtest produced too few observations")

    ann_return = float(strat_returns.mean() * TRADING_DAYS)
    ann_vol = float(strat_returns.std() * np.sqrt(TRADING_DAYS))
    sharpe = float(ann_return / ann_vol) if ann_vol > 0 else float("nan")

    cum = (1 + strat_returns).cumprod()
    max_dd = float((cum / cum.cummax() - 1).min())

    idx_aligned = idx_returns.reindex(strat_returns.index).dropna()
    common = strat_returns.index.intersection(idx_aligned.index)
    if len(common) > 30 and idx_aligned.loc[common].var() > 0:
        rb = float(
            np.cov(strat_returns.loc[common], idx_aligned.loc[common])[0, 1]
            / np.var(idx_aligned.loc[common])
        )
    else:
        rb = float("nan")

    disp_aligned = disp_series.reindex(strat_returns.index).dropna()
    common2 = strat_returns.index.intersection(disp_aligned.index)
    if len(common2) > 30:
        sd_corr = float(np.corrcoef(strat_returns.loc[common2],
                                    disp_aligned.loc[common2])[0, 1])
    else:
        sd_corr = float("nan")

    return BacktestResult(
        ann_return=ann_return,
        ann_vol=ann_vol,
        sharpe=sharpe,
        max_drawdown=max_dd,
        realized_beta_to_index=rb,
        avg_monthly_turnover=float(np.mean(turnovers)) if turnovers else float("nan"),
        strat_dispersion_corr=sd_corr,
        n_rebalances=len(turnovers),
        avg_basket_size=float(np.mean(basket_sizes)) if basket_sizes else float("nan"),
    )


# ---------------------------------------------------------------------------
# output
# ---------------------------------------------------------------------------

def plot_diagnostic(corr_series, disp_series, outfile):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed, skipping chart", file=sys.stderr)
        return False

    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

    axes[0].plot(corr_series.index, corr_series.values, lw=1.2)
    axes[0].axhline(corr_series.dropna().median(), color="gray", ls="--",
                    lw=0.8, label="median")
    axes[0].set_title(f"Rolling avg pairwise correlation ({CORR_WINDOW}d)")
    axes[0].set_ylabel("rho-bar")
    axes[0].legend(loc="upper right", fontsize=8)
    axes[0].grid(alpha=0.3)

    axes[1].plot(disp_series.index, disp_series.values, lw=1.2, color="tab:orange")
    axes[1].axhline(disp_series.dropna().median(), color="gray", ls="--",
                    lw=0.8, label="median")
    axes[1].set_title(f"Cross-sectional return dispersion ({DISP_SMOOTH}d smoothed)")
    axes[1].set_ylabel("sigma_cs")
    axes[1].set_xlabel("date")
    axes[1].legend(loc="upper right", fontsize=8)
    axes[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(outfile, dpi=120)
    plt.close(fig)
    return True


def format_report(report, backtest, universe, index, json_mode=False):
    if json_mode:
        return json.dumps({
            "regime": asdict(report),
            "backtest": asdict(backtest) if backtest else None,
            "universe": universe,
            "index": index,
        }, indent=2)

    lines = []
    lines.append("=" * 64)
    lines.append("SEMICONDUCTOR DISPERSION  —  REGIME REPORT")
    lines.append("=" * 64)
    lines.append(f"as of:                  {report.as_of}")
    lines.append(f"index / # names:        {index} / {report.n_names}")
    lines.append("")
    lines.append(f"avg pairwise corr:      {report.avg_pairwise_corr:+.3f}")
    lines.append(f"  percentile:           {report.corr_percentile:5.1f}   (low = thesis playing out)")
    lines.append(f"  60d change:           {report.corr_60d_change:+.3f}   (negative = decoupling)")
    lines.append("")
    lines.append(f"dispersion (sigma_cs):  {report.dispersion:.4f}")
    lines.append(f"  percentile:           {report.dispersion_percentile:5.1f}   (high = thesis playing out)")
    lines.append("")
    lines.append(f"VERDICT:                {report.verdict}")
    lines.append("")

    if backtest is not None:
        lines.append("=" * 64)
        lines.append("BETA-NEUTRAL DISPERSION-PROXY BACKTEST")
        lines.append("=" * 64)
        lines.append(f"ann return:             {backtest.ann_return:+.2%}")
        lines.append(f"ann vol:                {backtest.ann_vol:.2%}")
        lines.append(f"Sharpe:                 {backtest.sharpe:+.2f}")
        lines.append(f"max drawdown:           {backtest.max_drawdown:.2%}")
        lines.append(f"realized beta:          {backtest.realized_beta_to_index:+.3f}   (should be ~ 0)")
        lines.append(f"avg monthly turnover:   {backtest.avg_monthly_turnover:.2f}")
        lines.append(f"strat <-> dispersion:   {backtest.strat_dispersion_corr:+.3f}   (should be > 0)")
        lines.append(f"# rebalances:           {backtest.n_rebalances}")
        lines.append(f"avg basket size:        {backtest.avg_basket_size:.1f}")
        lines.append("")
        lines.append("Reminder: no transaction costs, no borrow, survivorship-biased universe.")
        lines.append("Equity proxy, NOT the options dispersion trade. Not investment advice.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--index", default=DEFAULT_INDEX)
    p.add_argument("--universe", default=None,
                   help="comma-separated tickers; default = ~25 liquid semis")
    p.add_argument("--start", default="2015-01-01")
    p.add_argument("--end", default=None, help="default = today")
    p.add_argument("--beta-window", type=int, default=60)
    p.add_argument("--top-quantile", type=float, default=0.20)
    p.add_argument("--synthetic", action="store_true",
                   help="run on synthetic two-regime data (no network)")
    p.add_argument("--json", action="store_true")
    p.add_argument("--no-plot", action="store_true")
    p.add_argument("--outfile", default="dispersion_report.png")
    return p.parse_args()


def main():
    args = parse_args()

    if args.synthetic:
        all_prices, index, universe = synthetic_data()
    else:
        universe = (
            [t.strip().upper() for t in args.universe.split(",") if t.strip()]
            if args.universe else list(DEFAULT_UNIVERSE)
        )
        index = args.index.upper()
        end = args.end or str(date.today())
        tickers = sorted(set(universe + [index]))
        all_prices = fetch_data(tickers, args.start, end)

    if index not in all_prices.columns:
        sys.exit(f"index {index} not in fetched data. got: {list(all_prices.columns)}")

    universe_actual = [t for t in universe if t in all_prices.columns]
    if len(universe_actual) < 5:
        sys.exit(f"only {len(universe_actual)} of {len(universe)} universe tickers had data")
    missing = sorted(set(universe) - set(universe_actual))
    if missing:
        print(f"warning: dropping {missing} (no data)", file=sys.stderr)

    prices_universe = all_prices[universe_actual]
    prices_index = all_prices[index]

    returns = compute_returns(prices_universe)
    idx_returns = prices_index.pct_change().dropna()

    corr_series = rolling_avg_pairwise_corr(returns, window=CORR_WINDOW)
    disp_series = cross_sectional_dispersion(returns, smooth=DISP_SMOOTH)

    report = build_regime_report(corr_series, disp_series, len(universe_actual))

    betas, idio_vols = rolling_beta_and_idio_vol(
        returns, idx_returns, window=args.beta_window
    )
    backtest = run_backtest(
        returns, idx_returns, idio_vols, betas, disp_series,
        top_quantile=args.top_quantile,
    )

    print(format_report(report, backtest, universe_actual, index,
                        json_mode=args.json))

    if not args.no_plot:
        ok = plot_diagnostic(corr_series, disp_series, args.outfile)
        if ok and not args.json:
            print(f"chart: {args.outfile}", file=sys.stderr)


if __name__ == "__main__":
    main()
