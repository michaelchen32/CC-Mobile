"""
% of companies trading below their 200-day SMA: S&P 500 and Nasdaq-100,
plus an IWM (Russell 2000 ETF) 200-day-SMA proxy.

Methodology / caveats
---------------------
- Daily prices, auto-adjusted (splits + dividends), from Yahoo Finance.
- Window: trailing 20 years ending TODAY. Extra lead-in is downloaded so the
  200-day SMA is already valid on the first displayed day.
- Index membership is CURRENT membership only (free data has no point-in-time
  history). Companies that failed / were delisted / removed are excluded, so
  historical breadth looks somewhat healthier than it really was. This
  survivorship bias is strongest for small caps; it is labelled on the charts.
- Russell 2000: the official ~2000-name list is bot-blocked and a 20yr
  small-cap pull is infeasible on free APIs, so we use IWM (iShares Russell
  2000 ETF) priced against its OWN 200-day SMA as a single-line regime proxy
  (NOT a true breadth percentage).
"""

import io
import sys
import time
import datetime as dt

import numpy as np
import pandas as pd
import requests
import yfinance as yf
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

UA = {"User-Agent": "Mozilla/5.0 (research; breadth-study)"}
SMA_WINDOW = 200
YEARS = 20

TODAY = dt.date.today()
DISPLAY_START = TODAY - dt.timedelta(days=int(YEARS * 365.25))
# ~420 calendar days of lead-in => ~280 trading days, enough for a 200d SMA.
DL_START = DISPLAY_START - dt.timedelta(days=420)


def log(msg):
    print(f"[{dt.datetime.now():%H:%M:%S}] {msg}", flush=True)


# --------------------------------------------------------------------------- #
# Constituent lists
# --------------------------------------------------------------------------- #
def get_sp500():
    r = requests.get(
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
        headers=UA,
        timeout=30,
    )
    r.raise_for_status()
    tbl = pd.read_html(io.StringIO(r.text))[0]
    syms = [str(s).strip().upper().replace(".", "-") for s in tbl["Symbol"]]
    return sorted(set(syms))


def get_nasdaq100():
    r = requests.get(
        "https://en.wikipedia.org/wiki/Nasdaq-100", headers=UA, timeout=30
    )
    r.raise_for_status()
    tables = pd.read_html(io.StringIO(r.text))
    for t in tables:
        cols = [str(c) for c in t.columns]
        if any(c in ("Ticker", "Symbol") for c in cols):
            key = "Ticker" if "Ticker" in cols else "Symbol"
            syms = [str(s).strip().upper().replace(".", "-") for s in t[key]]
            return sorted(set(syms))
    raise RuntimeError("Nasdaq-100 constituent table not found")


# --------------------------------------------------------------------------- #
# Price download (chunked, with retry/backoff against rate limits)
# --------------------------------------------------------------------------- #
def download_closes(tickers, start, end, chunk=80):
    frames = []
    for i in range(0, len(tickers), chunk):
        batch = tickers[i : i + chunk]
        for attempt in range(5):
            try:
                data = yf.download(
                    batch,
                    start=start,
                    end=end,
                    auto_adjust=True,
                    progress=False,
                    threads=True,
                    group_by="column",
                )
                if data is None or len(data) == 0:
                    raise RuntimeError("empty frame")
                close = data["Close"] if "Close" in data.columns.get_level_values(0) else data
                if isinstance(close, pd.Series):
                    close = close.to_frame()
                frames.append(close)
                log(
                    f"  batch {i//chunk+1}: {len(batch)} tickers, "
                    f"{close.shape[1]} cols, {close.shape[0]} rows"
                )
                break
            except Exception as e:
                wait = 2 ** (attempt + 1)
                log(f"  batch {i//chunk+1} attempt {attempt+1} failed: {repr(e)[:90]}; wait {wait}s")
                time.sleep(wait)
        else:
            log(f"  batch {i//chunk+1}: GAVE UP")
        time.sleep(1.5)  # be polite between batches
    if not frames:
        raise RuntimeError("no price data downloaded")
    closes = pd.concat(frames, axis=1)
    closes = closes.loc[:, ~closes.columns.duplicated()]
    closes.index = pd.to_datetime(closes.index)
    return closes.sort_index()


# --------------------------------------------------------------------------- #
# Breadth: % of names below their 200-day SMA
# --------------------------------------------------------------------------- #
def pct_below_200dma(closes):
    closes = closes.dropna(axis=1, how="all")
    sma = closes.rolling(SMA_WINDOW, min_periods=SMA_WINDOW).mean()
    valid = closes.notna() & sma.notna()
    below = (closes < sma) & valid
    n_valid = valid.sum(axis=1)
    pct = 100.0 * below.sum(axis=1) / n_valid.replace(0, np.nan)
    out = pd.DataFrame({"pct_below_200dma": pct, "n_constituents": n_valid})
    return out.loc[out.index >= pd.Timestamp(DISPLAY_START)].dropna()


# --------------------------------------------------------------------------- #
# Charts
# --------------------------------------------------------------------------- #
CAVEAT = (
    "Daily auto-adjusted prices, Yahoo Finance. Uses CURRENT index membership "
    "(no point-in-time history) -> survivorship bias: failed/removed names "
    "excluded, so past breadth looks healthier than it was."
)


def chart_breadth(df, index_name, color, fname):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df.index, df["pct_below_200dma"], color=color, lw=1.0)
    ax.axhline(50, color="grey", ls="--", lw=0.8, alpha=0.7)
    ax.fill_between(
        df.index, 50, df["pct_below_200dma"],
        where=df["pct_below_200dma"] >= 50, color=color, alpha=0.15,
    )
    ax.set_ylim(0, 100)
    ax.set_ylabel("% of constituents below 200-day SMA")
    ax.set_title(
        f"{index_name}: % of companies trading below their 200-day SMA\n"
        f"{df.index.min():%Y-%m-%d} to {df.index.max():%Y-%m-%d}  "
        f"(~{int(df['n_constituents'].median())} current constituents, daily)",
        fontsize=13, fontweight="bold",
    )
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.25)
    fig.text(0.5, 0.012, CAVEAT, ha="center", fontsize=8, style="italic", color="dimgray", wrap=True)
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(fname, dpi=140)
    plt.close(fig)
    log(f"  wrote {fname}")


def chart_iwm(iwm, fname):
    iwm = iwm.dropna().copy()
    iwm["sma200"] = iwm["Close"].rolling(SMA_WINDOW, min_periods=SMA_WINDOW).mean()
    iwm = iwm.dropna()
    iwm = iwm.loc[iwm.index >= pd.Timestamp(DISPLAY_START)]
    iwm["dev"] = 100.0 * (iwm["Close"] / iwm["sma200"] - 1.0)

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(iwm.index, iwm["dev"], color="#1b7837", lw=1.0)
    ax.axhline(0, color="black", lw=0.9)
    ax.fill_between(iwm.index, 0, iwm["dev"], where=iwm["dev"] < 0,
                    color="#b2182b", alpha=0.30, label="IWM below its 200-day SMA")
    ax.fill_between(iwm.index, 0, iwm["dev"], where=iwm["dev"] >= 0,
                    color="#1b7837", alpha=0.20, label="IWM above its 200-day SMA")
    pct_below = 100.0 * (iwm["dev"] < 0).mean()
    ax.set_ylabel("IWM price vs its own 200-day SMA  (% deviation)")
    ax.set_title(
        "Russell 2000 proxy — IWM ETF relative to its 200-day SMA\n"
        f"{iwm.index.min():%Y-%m-%d} to {iwm.index.max():%Y-%m-%d}  "
        f"(below 200d SMA on {pct_below:.0f}% of trading days, daily)",
        fontsize=13, fontweight="bold",
    )
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.25)
    ax.legend(loc="lower left", fontsize=9)
    fig.text(
        0.5, 0.012,
        "Single-line PROXY (not a breadth %): the full Russell 2000 constituent "
        "history is infeasible on free data. Daily auto-adjusted IWM prices, Yahoo Finance.",
        ha="center", fontsize=8, style="italic", color="dimgray",
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(fname, dpi=140)
    plt.close(fig)
    log(f"  wrote {fname}  (IWM below 200d SMA {pct_below:.1f}% of days)")


# --------------------------------------------------------------------------- #
def main():
    end = (TODAY + dt.timedelta(days=1)).isoformat()
    start = DL_START.isoformat()
    log(f"Window: display {DISPLAY_START} -> {TODAY}; download from {start}")

    log("Fetching constituent lists...")
    sp = get_sp500()
    ndx = get_nasdaq100()
    log(f"  S&P 500: {len(sp)} tickers | Nasdaq-100: {len(ndx)} tickers")

    log("Downloading S&P 500 daily closes...")
    sp_close = download_closes(sp, start, end)
    log("Downloading Nasdaq-100 daily closes...")
    ndx_close = download_closes(ndx, start, end)
    log("Downloading IWM daily closes...")
    iwm = yf.download("IWM", start=start, end=end, auto_adjust=True,
                      progress=False)[["Close"]]
    if isinstance(iwm.columns, pd.MultiIndex):
        iwm.columns = ["Close"]

    log("Computing breadth...")
    sp_b = pct_below_200dma(sp_close)
    ndx_b = pct_below_200dma(ndx_close)

    sp_b.to_csv("data/sp500_pct_below_200dma.csv")
    ndx_b.to_csv("data/nasdaq100_pct_below_200dma.csv")
    iwm.to_csv("data/iwm_close.csv")

    log("Rendering charts...")
    chart_breadth(sp_b, "S&P 500", "#2166ac", "charts/sp500_pct_below_200dma.png")
    chart_breadth(ndx_b, "Nasdaq-100", "#762a83", "charts/nasdaq100_pct_below_200dma.png")
    chart_iwm(iwm, "charts/russell2000_iwm_200dma_proxy.png")

    log("DONE")
    log(f"  S&P 500 rows: {len(sp_b)}  latest %below={sp_b['pct_below_200dma'].iloc[-1]:.1f}")
    log(f"  Nasdaq-100 rows: {len(ndx_b)}  latest %below={ndx_b['pct_below_200dma'].iloc[-1]:.1f}")


if __name__ == "__main__":
    sys.exit(main())
