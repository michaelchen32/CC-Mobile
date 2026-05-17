"""OHLCV download with a simple on-disk cache (keeps re-runs fast and
avoids hammering the data provider)."""
from __future__ import annotations

import os
import time

import pandas as pd
import yfinance as yf

CACHE_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "data_cache")


def _cache_path(ticker: str, start: str, end: str) -> str:
    return os.path.join(CACHE_DIR, f"{ticker}_{start}_{end}.csv")


def bulk_fetch(
    tickers: list[str], start: str, end: str, batch: int = 60
) -> dict[str, pd.DataFrame]:
    """Download many tickers, reusing/filling the same per-ticker CSV cache
    that get_ohlcv() uses. Returns {ticker: DataFrame} for everything that
    resolved (failed/delisted names are silently skipped)."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    out: dict[str, pd.DataFrame] = {}
    missing: list[str] = []
    for t in tickers:
        p = _cache_path(t, start, end)
        if os.path.exists(p):
            df = pd.read_csv(p, index_col=0, parse_dates=True)
            if not df.empty:
                out[t] = df
                continue
        missing.append(t)

    for i in range(0, len(missing), batch):
        chunk = missing[i : i + batch]
        try:
            raw = yf.download(
                chunk, start=start, end=end, progress=False,
                auto_adjust=True, group_by="ticker", threads=True,
            )
        except Exception:  # noqa: BLE001 - skip whole-batch provider errors
            continue
        for t in chunk:
            try:
                sub = raw[t] if isinstance(raw.columns, pd.MultiIndex) else raw
                df = sub[["Open", "High", "Low", "Close", "Volume"]].dropna()
                if df.empty:
                    continue
                df.to_csv(_cache_path(t, start, end))
                out[t] = df
            except Exception:  # noqa: BLE001 - skip individual bad ticker
                continue
    return out


def get_ohlcv(
    ticker: str, start: str, end: str, max_retries: int = 4
) -> pd.DataFrame:
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache = os.path.join(CACHE_DIR, f"{ticker}_{start}_{end}.csv")
    if os.path.exists(cache):
        df = pd.read_csv(cache, index_col=0, parse_dates=True)
        if not df.empty:
            return df

    last_err: Exception | None = None
    for attempt in range(max_retries):
        try:
            raw = yf.download(
                ticker, start=start, end=end, progress=False, auto_adjust=True
            )
            if raw is None or raw.empty:
                raise ValueError(f"no data for {ticker}")
            if isinstance(raw.columns, pd.MultiIndex):
                raw.columns = raw.columns.get_level_values(0)
            df = raw[["Open", "High", "Low", "Close", "Volume"]].dropna()
            df.to_csv(cache)
            return df
        except Exception as exc:  # noqa: BLE001 - retry on any provider error
            last_err = exc
            time.sleep(2 ** (attempt + 1))

    raise RuntimeError(f"failed to download {ticker}: {last_err}")
