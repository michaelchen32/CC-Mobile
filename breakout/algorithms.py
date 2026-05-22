"""Breakout-detection algorithms.

Each function takes an OHLCV DataFrame (columns: Open, High, Low, Close,
Volume; DatetimeIndex) and returns a boolean Series that is True on the bar
where a long breakout triggers.

The six implemented here are the ones most widely used / cited by
practitioners for *breakout* (as opposed to mean-reversion) detection:

1. Donchian channel breakout      - the classic Turtle Trading system
2. Darvas box breakout            - Nicolas Darvas' box method
3. Bollinger-band squeeze         - volatility contraction -> expansion
4. TTM squeeze release            - Bollinger inside Keltner, then fires
5. Volume-confirmed resistance    - horizontal S/R break on volume surge
6. 52-week-high momentum          - new 252-day high with trend filter
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .indicators import atr, ema, rolling_slope, sma


# 1 -------------------------------------------------------------------------
def donchian_breakout(df: pd.DataFrame, lookback: int = 20) -> pd.Series:
    """Turtle system: close above the highest high of the prior `lookback`
    bars (the prior bar's value is used so the current bar can't reference
    itself)."""
    prior_high = df["High"].rolling(lookback, min_periods=lookback).max().shift(1)
    sig = df["Close"] > prior_high
    return sig.fillna(False)


# 2 -------------------------------------------------------------------------
def darvas_box_breakout(
    df: pd.DataFrame, high_lookback: int = 60, settle_days: int = 4
) -> pd.Series:
    """Darvas box: a box top is confirmed once price makes a new
    `high_lookback`-day high and then fails to exceed it for `settle_days`
    consecutive sessions. A breakout fires when a later close exceeds the
    confirmed box top."""
    high = df["High"].to_numpy(dtype=float)
    close = df["Close"].to_numpy(dtype=float)
    n = len(df)
    out = np.zeros(n, dtype=bool)

    box_top = np.nan
    pending_top = np.nan
    days_since_top = 0

    roll_max = df["High"].rolling(high_lookback, min_periods=high_lookback).max()
    roll_max_prev = roll_max.shift(1).to_numpy(dtype=float)

    for i in range(n):
        # New local high -> start (or restart) a tentative box top.
        if not np.isnan(roll_max_prev[i]) and high[i] >= roll_max_prev[i]:
            pending_top = high[i]
            days_since_top = 0
        elif not np.isnan(pending_top):
            if high[i] > pending_top:
                pending_top = high[i]
                days_since_top = 0
            else:
                days_since_top += 1
                if days_since_top >= settle_days:
                    box_top = pending_top
                    pending_top = np.nan

        if not np.isnan(box_top) and close[i] > box_top:
            out[i] = True
            box_top = np.nan  # require a fresh box before the next signal

    return pd.Series(out, index=df.index)


# 3 -------------------------------------------------------------------------
def bollinger_squeeze_breakout(
    df: pd.DataFrame,
    n: int = 20,
    k: float = 2.0,
    bw_lookback: int = 126,
    squeeze_pct: float = 0.25,
    squeeze_window: int = 10,
) -> pd.Series:
    """Bandwidth contracts into the lowest `squeeze_pct` of its trailing
    range (a "squeeze"), then price closes above the upper band within
    `squeeze_window` bars of that squeeze."""
    mid = sma(df["Close"], n)
    sd = df["Close"].rolling(n, min_periods=n).std()
    upper = mid + k * sd
    lower = mid - k * sd
    bandwidth = (upper - lower) / mid

    bw_min = bandwidth.rolling(bw_lookback, min_periods=n).min()
    bw_max = bandwidth.rolling(bw_lookback, min_periods=n).max()
    bw_rank = (bandwidth - bw_min) / (bw_max - bw_min)
    is_squeeze = bw_rank <= squeeze_pct
    squeeze_recent = is_squeeze.rolling(squeeze_window, min_periods=1).max().astype(bool)

    cross_up = (df["Close"] > upper) & (df["Close"].shift(1) <= upper.shift(1))
    sig = cross_up & squeeze_recent
    return sig.fillna(False)


# 4 -------------------------------------------------------------------------
def ttm_squeeze_breakout(
    df: pd.DataFrame, n: int = 20, bb_k: float = 2.0, kc_k: float = 1.5
) -> pd.Series:
    """John Carter's TTM squeeze: Bollinger bands sitting *inside* Keltner
    channels marks a coiled market; the trade fires on the bar the squeeze
    releases (BB expands back outside KC) while momentum is positive."""
    mid = sma(df["Close"], n)
    sd = df["Close"].rolling(n, min_periods=n).std()
    bb_u, bb_l = mid + bb_k * sd, mid - bb_k * sd

    kc_mid = ema(df["Close"], n)
    rng = atr(df, n)
    kc_u, kc_l = kc_mid + kc_k * rng, kc_mid - kc_k * rng

    squeeze_on = (bb_u < kc_u) & (bb_l > kc_l)
    released = (~squeeze_on) & squeeze_on.shift(1).fillna(False)

    # Momentum: close relative to the Donchian/SMA midline (Carter's proxy).
    dc_mid = (
        df["High"].rolling(n, min_periods=n).max()
        + df["Low"].rolling(n, min_periods=n).min()
    ) / 2
    momentum = df["Close"] - (dc_mid + mid) / 2

    sig = released & (momentum > 0)
    return sig.fillna(False)


# 5 -------------------------------------------------------------------------
def volume_resistance_breakout(
    df: pd.DataFrame,
    pivot_window: int = 10,
    resistance_lookback: int = 60,
    vol_mult: float = 1.5,
    vol_n: int = 20,
    buffer: float = 0.005,
) -> pd.Series:
    """Detect horizontal resistance from swing-high pivots, then require a
    close that clears the most recent resistance by `buffer` on volume at
    least `vol_mult`x the `vol_n`-day average."""
    high = df["High"]
    is_pivot = (
        high == high.rolling(2 * pivot_window + 1, center=True, min_periods=1).max()
    )
    # Resistance available at bar i = highest confirmed pivot high in the
    # prior `resistance_lookback` bars (shifted so it is known in advance).
    pivot_high = high.where(is_pivot)
    resistance = (
        pivot_high.rolling(resistance_lookback, min_periods=1)
        .max()
        .shift(pivot_window + 1)
    )

    avg_vol = df["Volume"].rolling(vol_n, min_periods=vol_n).mean()
    vol_ok = df["Volume"] >= vol_mult * avg_vol

    clears = df["Close"] > resistance * (1 + buffer)
    fresh = clears & ~clears.shift(1).fillna(False)
    sig = fresh & vol_ok & resistance.notna()
    return sig.fillna(False)


# 6 -------------------------------------------------------------------------
def high_52w_momentum_breakout(
    df: pd.DataFrame,
    lookback: int = 252,
    trend_n: int = 50,
    slope_n: int = 50,
    min_slope: float = 0.0,
) -> pd.Series:
    """New 52-week (252-bar) closing high while in a confirmed uptrend
    (price above a rising 50-day average). The momentum/Driehaus/Minervini
    style of breakout."""
    prior_high = df["Close"].rolling(lookback, min_periods=lookback).max().shift(1)
    new_high = df["Close"] > prior_high

    ma = sma(df["Close"], trend_n)
    slope = rolling_slope(df["Close"], slope_n)
    trend_ok = (df["Close"] > ma) & (slope > min_slope)

    sig = new_high & trend_ok
    return sig.fillna(False)


ALGORITHMS = {
    "donchian_20": donchian_breakout,
    "darvas_box": darvas_box_breakout,
    "bollinger_squeeze": bollinger_squeeze_breakout,
    "ttm_squeeze": ttm_squeeze_breakout,
    "volume_resistance": volume_resistance_breakout,
    "high_52w_momentum": high_52w_momentum_breakout,
}
