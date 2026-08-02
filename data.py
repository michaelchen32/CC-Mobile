"""Data acquisition, caching, and validation for the SOXX regime study.

Sources:
- SOXX daily OHLCV (dividend/split adjusted) via yfinance with
  ``auto_adjust=True``. Behind a TLS-intercepting egress proxy, yfinance's
  default curl_cffi browser fingerprint (recent Chrome, with ECH/post-quantum
  extensions) gets its handshake reset; we therefore hand yfinance a
  curl_cffi session impersonating an older browser (chrome116 first) that
  such proxies accept, trying several fingerprints in order.
- Fallback: Nasdaq's free API (split-adjusted prices, ~10y of history,
  dividend back-adjusted locally).
- ^VIX and ^VIX3M daily closes from CBOE's published history CSVs
  (authoritative source, no rate limits).

Everything is cached to ``cache/*.parquet``; delete the cache to force a
re-download.
"""
from __future__ import annotations

import os
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

CACHE_DIR = Path(__file__).resolve().parent / "cache"

_UA = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "application/json,text/html;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

_CBOE_URLS = {
    "^VIX": "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",
    "^VIX3M": "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX3M_History.csv",
}


# Browser TLS fingerprints tried in order. Recent Chrome/Firefox fingerprints
# carry ECH / post-quantum key-share extensions that TLS-intercepting egress
# proxies commonly reset; the older ones below are broadly accepted.
_IMPERSONATE_TARGETS = ("chrome116", "safari17_0", "edge101", "chrome110")


def _yahoo_ohlcv(symbol: str, start: str, retries: int = 2) -> pd.DataFrame:
    """Daily OHLCV for ``symbol`` via yfinance, adjusted for splits/dividends.

    Tries several curl_cffi browser fingerprints because (a) Yahoo blocks
    non-browser TLS fingerprints with 429s and (b) intercepting proxies
    reset the newest fingerprints (see module docstring).
    """
    import yfinance as yf
    from curl_cffi import requests as cfr

    ca = os.environ.get("CURL_CA_BUNDLE") or True
    last_err: Exception | None = None
    for attempt in range(retries):
        for imp in _IMPERSONATE_TARGETS:
            try:
                sess = cfr.Session(impersonate=imp, verify=ca)
                raw = yf.download(
                    symbol, start=start, auto_adjust=True, progress=False,
                    session=sess,
                )
            except Exception as exc:
                last_err = exc
                continue
            if raw is None or len(raw) == 0:
                continue
            if isinstance(raw.columns, pd.MultiIndex):
                raw.columns = raw.columns.droplevel(1)
            df = raw[["Open", "High", "Low", "Close", "Volume"]].copy()
            idx = pd.DatetimeIndex(df.index, name="Date")
            if idx.tz is not None:
                idx = idx.tz_localize(None)
            df.index = idx
            df = df.dropna(subset=["Close"])
            df = df[~df.index.duplicated(keep="last")].sort_index()
            return df
        if attempt < retries - 1:
            time.sleep(30)
    raise RuntimeError(f"yfinance failed for {symbol}: {last_err!r}")


def _cboe_close(symbol: str) -> pd.DataFrame:
    """Daily close for a CBOE index from its published history CSV."""
    r = requests.get(_CBOE_URLS[symbol], headers=_UA, timeout=60)
    r.raise_for_status()
    from io import StringIO

    raw = pd.read_csv(StringIO(r.text))
    raw.columns = [c.strip().title() for c in raw.columns]
    raw["Date"] = pd.to_datetime(raw["Date"], format="mixed")
    df = raw.set_index("Date")[["Close"]].sort_index()
    df = df[~df.index.duplicated(keep="last")]
    return df


def _nasdaq_ohlcv(symbol: str) -> pd.DataFrame:
    """Fallback source: Nasdaq's free API (max ~10 years of daily history).

    Prices come split-adjusted but NOT dividend-adjusted, so we back-adjust
    with Nasdaq's own dividend history: for each ex-date, all prior prices
    are scaled by (1 - dividend / previous close) — the same convention
    Yahoo/CRSP use for total-return adjusted closes.
    """
    headers = dict(_UA)
    headers.update({"Accept": "application/json", "Origin": "https://www.nasdaq.com",
                    "Referer": "https://www.nasdaq.com/"})
    today = pd.Timestamp.today().strftime("%Y-%m-%d")
    r = requests.get(
        f"https://api.nasdaq.com/api/quote/{symbol}/historical",
        params={"assetclass": "etf", "fromdate": "2005-01-01", "todate": today,
                "limit": "9999"},
        headers=headers, timeout=60,
    )
    r.raise_for_status()
    rows = r.json()["data"]["tradesTable"]["rows"]

    def num(x: str) -> float:
        return float(str(x).replace("$", "").replace(",", ""))

    df = pd.DataFrame(
        {
            "Date": pd.to_datetime([row["date"] for row in rows]),
            "Open": [num(row["open"]) for row in rows],
            "High": [num(row["high"]) for row in rows],
            "Low": [num(row["low"]) for row in rows],
            "Close": [num(row["close"]) for row in rows],
            "Volume": [num(row["volume"]) for row in rows],
        }
    ).set_index("Date").sort_index()
    df = df[~df.index.duplicated(keep="last")]

    rd = requests.get(
        f"https://api.nasdaq.com/api/quote/{symbol}/dividends",
        params={"assetclass": "etf"}, headers=headers, timeout=60,
    )
    rd.raise_for_status()
    div_rows = rd.json()["data"]["dividends"]["rows"] or []
    factor = pd.Series(1.0, index=df.index)
    for row in div_rows:
        ex = pd.to_datetime(row["exOrEffDate"], errors="coerce")
        if ex is pd.NaT or ex <= df.index[0] or ex > df.index[-1]:
            continue
        amount = num(row["amount"])
        prev_close = float(df["Close"].loc[: ex - pd.Timedelta(days=1)].iloc[-1])
        factor.loc[: ex - pd.Timedelta(days=1)] *= 1.0 - amount / prev_close
    for col in ("Open", "High", "Low", "Close"):
        df[col] = df[col] * factor
    return df


def validate_prices(df: pd.DataFrame, name: str) -> None:
    """Hard checks: unique monotonic dates, strictly positive prices."""
    assert df.index.is_unique, f"{name}: duplicate dates"
    assert df.index.is_monotonic_increasing, f"{name}: non-monotonic index"
    price_cols = [c for c in ("Open", "High", "Low", "Close") if c in df.columns]
    assert (df[price_cols] > 0).all().all(), f"{name}: zero/negative prices"
    print(
        f"[data] {name}: {len(df)} rows, "
        f"{df.index[0].date()} -> {df.index[-1].date()}"
    )


def load_ohlcv(symbol: str, start: str = "2005-01-01") -> pd.DataFrame:
    """Cached, validated daily adjusted OHLCV from Yahoo."""
    CACHE_DIR.mkdir(exist_ok=True)
    cache = CACHE_DIR / f"{symbol.replace('^', '_')}.parquet"
    if cache.exists():
        df = pd.read_parquet(cache)
    else:
        try:
            df = _yahoo_ohlcv(symbol, start)
            print(f"[data] {symbol}: fetched from Yahoo")
        except Exception as exc:
            print(f"[data] Yahoo failed for {symbol} ({exc}); falling back to Nasdaq")
            df = _nasdaq_ohlcv(symbol)
            print(f"[data] {symbol}: fetched from Nasdaq (dividend back-adjusted)")
        df.to_parquet(cache)
    validate_prices(df, symbol)
    if pd.Timestamp(df.index[0]) > pd.Timestamp(start) + pd.Timedelta(days=40):
        print(
            f"[data] NOTE: {symbol} history starts {df.index[0].date()}, later than "
            f"requested {start} — train window adjusted accordingly."
        )
    return df


def load_vix_pair() -> pd.DataFrame | None:
    """VIX and VIX3M closes joined on date; ``None`` if unavailable."""
    CACHE_DIR.mkdir(exist_ok=True)
    cache = CACHE_DIR / "vix_pair.parquet"
    if cache.exists():
        df = pd.read_parquet(cache)
        validate_prices(df.rename(columns={"VIX": "Close"})[["Close"]], "VIX pair")
        return df
    try:
        vix = _cboe_close("^VIX")["Close"].rename("VIX")
        vix3m = _cboe_close("^VIX3M")["Close"].rename("VIX3M")
    except Exception as exc:  # graceful skip per spec
        print(f"[data] VIX data unavailable ({exc}); skipping the VIX overlay")
        return None
    df = pd.concat([vix, vix3m], axis=1).dropna()
    df.to_parquet(cache)
    validate_prices(df.rename(columns={"VIX": "Close"})[["Close"]], "VIX pair")
    return df


def log_returns(close: pd.Series) -> pd.Series:
    """Daily log returns."""
    return np.log(close).diff().dropna()
