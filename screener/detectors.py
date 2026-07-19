"""The 6 canonical breakout algorithms.

Each function takes an OHLCV DataFrame and returns a boolean ``pd.Series``
(True on the trigger bar), matching the study-set specification:

    1. donchian_20        close > highest high of prior N bars           (N=20)
    2. darvas_box         break above a confirmed 60-day-high box top    (settle=4)
    3. bollinger_squeeze  bandwidth in bottom 25% of 126d range, then    (n=20,k=2)
                          close crosses above the upper band within 10 bars
    4. ttm_squeeze        Bollinger inside Keltner (coiled) -> fire on    (n=20)
                          release with positive momentum
    5. volume_resistance  close clears a horizontal swing-high by 0.5%    (piv=10,
                          on >=1.5x average volume                        look=60)
    6. high_52w_momentum  new 252-bar closing high above a rising 50d MA  (look=252)

Clean-room implementation — the maths is written here directly. The daily screen
evaluates each series on the latest bar. ``n_detectors`` = how many of the six
fired; a ``trend`` tag is attached for context only and never suppresses a
signal.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------
# Indicators
# ----------------------------------------------------------------------------


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def true_range(df: pd.DataFrame) -> pd.Series:
    prev_close = df["Close"].shift(1)
    hl = df["High"] - df["Low"]
    hc = (df["High"] - prev_close).abs()
    lc = (df["Low"] - prev_close).abs()
    return pd.concat([hl, hc, lc], axis=1).max(axis=1)


def atr(df: pd.DataFrame, n: int = 20) -> pd.Series:
    return true_range(df).rolling(n).mean()


def _false(df: pd.DataFrame) -> pd.Series:
    return pd.Series(False, index=df.index)


# ----------------------------------------------------------------------------
# 1. Donchian channel breakout
# ----------------------------------------------------------------------------


def donchian_20(df: pd.DataFrame, lookback: int = 20) -> pd.Series:
    """Close above the highest high of the prior ``lookback`` bars."""
    if len(df) < lookback + 1:
        return _false(df)
    prior_high = df["High"].rolling(lookback).max().shift(1)
    return df["Close"] > prior_high


# ----------------------------------------------------------------------------
# 2. Darvas box
# ----------------------------------------------------------------------------


def darvas_box(df: pd.DataFrame, high_lookback: int = 60, settle_days: int = 4) -> pd.Series:
    """A box top is a new ``high_lookback``-day high that then stalls (no higher
    high) for ``settle_days`` bars; fire on the bar whose close first exceeds the
    confirmed box top."""
    n = len(df)
    if n < high_lookback + settle_days + 1:
        return _false(df)
    high = df["High"].to_numpy()
    close = df["Close"].to_numpy()
    roll_max = df["High"].rolling(high_lookback).max().to_numpy()
    is_new_high = high >= roll_max  # NaN comparison -> False for warmup bars

    sig = np.zeros(n, dtype=bool)
    box_top = np.nan
    box_active = False
    for t in range(n):
        i = t - settle_days  # bar that would confirm exactly at t
        if i >= 0 and is_new_high[i] and not np.isnan(roll_max[i]):
            # bars i+1 .. t must have stayed at/below the candidate top
            if np.all(high[i + 1 : t + 1] <= high[i]):
                box_top = high[i]
                box_active = True
        if box_active and not np.isnan(box_top) and close[t] > box_top:
            sig[t] = True
            box_active = False  # box consumed; await the next one
    return pd.Series(sig, index=df.index)


# ----------------------------------------------------------------------------
# 3. Bollinger squeeze -> upper-band breakout
# ----------------------------------------------------------------------------


def bollinger_squeeze(
    df: pd.DataFrame,
    n: int = 20,
    k: float = 2.0,
    bw_lookback: int = 126,
    squeeze_pct: float = 0.25,
    squeeze_window: int = 10,
) -> pd.Series:
    """Bandwidth compresses into the bottom ``squeeze_pct`` of its trailing
    ``bw_lookback`` range (a squeeze), then price closes above the upper band
    within ``squeeze_window`` bars of that squeeze."""
    if len(df) < bw_lookback + n:
        return _false(df)
    close = df["Close"]
    mid = sma(close, n)
    sd = close.rolling(n).std()
    upper = mid + k * sd
    lower = mid - k * sd
    bw = (upper - lower) / mid
    thresh = bw.rolling(bw_lookback).quantile(squeeze_pct)
    squeeze = bw <= thresh
    squeeze_recent = squeeze.rolling(squeeze_window).max().fillna(0).astype(bool)
    cross_up = (close > upper) & (close.shift(1) <= upper.shift(1))
    return cross_up & squeeze_recent


# ----------------------------------------------------------------------------
# 4. TTM squeeze release
# ----------------------------------------------------------------------------


def ttm_squeeze(df: pd.DataFrame, n: int = 20, bb_k: float = 2.0, kc_k: float = 1.5) -> pd.Series:
    """Bollinger Bands inside Keltner Channels = coiled ("squeeze on"); fire on
    the bar where the squeeze releases (BB back outside KC) with positive
    momentum."""
    if len(df) < n + 2:
        return _false(df)
    close = df["Close"]
    mid = sma(close, n)
    sd = close.rolling(n).std()
    bb_up, bb_lo = mid + bb_k * sd, mid - bb_k * sd
    kc_mid = ema(close, n)
    rng = atr(df, n)
    kc_up, kc_lo = kc_mid + kc_k * rng, kc_mid - kc_k * rng

    squeeze_on = (bb_lo > kc_lo) & (bb_up < kc_up)
    release = (~squeeze_on) & squeeze_on.shift(1).fillna(False)

    # TTM momentum: close relative to the midline of the Donchian mid and SMA.
    donch_mid = (df["High"].rolling(n).max() + df["Low"].rolling(n).min()) / 2
    ref = (donch_mid + mid) / 2
    momentum = close - ref
    return release & (momentum > 0)


# ----------------------------------------------------------------------------
# 5. Volume-confirmed resistance breakout
# ----------------------------------------------------------------------------


def volume_resistance(
    df: pd.DataFrame,
    pivot_window: int = 10,
    resistance_lookback: int = 60,
    vol_mult: float = 1.5,
    vol_n: int = 20,
    buffer: float = 0.005,
) -> pd.Series:
    """Close clears a horizontal swing-high resistance by ``buffer`` on
    >=``vol_mult`` x average volume. Resistance = the highest confirmed pivot
    high (local max over +/-``pivot_window`` bars) within the trailing
    ``resistance_lookback`` bars."""
    if len(df) < resistance_lookback + pivot_window + 1:
        return _false(df)
    high = df["High"]
    close = df["Close"]
    vol = df["Volume"]

    win = 2 * pivot_window + 1
    centered_max = high.rolling(win, center=True).max()
    is_pivot = high >= centered_max  # tail bars are NaN -> not confirmable yet
    pivot_val = high.where(is_pivot)
    # A pivot at i is only confirmed pivot_window bars later -> shift, then take
    # the max over the resistance window.
    resistance = pivot_val.shift(pivot_window).rolling(
        resistance_lookback, min_periods=1
    ).max()

    avg_vol = vol.rolling(vol_n).mean().shift(1)
    level = resistance * (1 + buffer)
    clears = (close > level) & (close.shift(1) <= level)
    vol_ok = vol >= vol_mult * avg_vol
    return (clears & vol_ok).fillna(False)


# ----------------------------------------------------------------------------
# 6. 52-week-high momentum
# ----------------------------------------------------------------------------


def high_52w_momentum(
    df: pd.DataFrame,
    lookback: int = 252,
    trend_n: int = 50,
    slope_n: int = 50,
    min_slope: float = 0.0,
) -> pd.Series:
    """New ``lookback``-bar closing high while above a rising ``trend_n``-day MA."""
    if len(df) < lookback + slope_n:
        return _false(df)
    close = df["Close"]
    new_high = close >= close.rolling(lookback).max()  # today is the highest close
    ma = sma(close, trend_n)
    above = close > ma
    rising = (ma - ma.shift(slope_n)) > min_slope
    return (new_high & above & rising).fillna(False)


# ----------------------------------------------------------------------------
# Registry + latest-bar evaluation
# ----------------------------------------------------------------------------

ALGORITHMS = {
    "donchian_20": donchian_20,
    "darvas_box": darvas_box,
    "bollinger_squeeze": bollinger_squeeze,
    "ttm_squeeze": ttm_squeeze,
    "volume_resistance": volume_resistance,
    "high_52w_momentum": high_52w_momentum,
}

# The historical study found these two the most reliable (highest confirmed,
# lowest fakeout); raw Donchian fires most often but is the noisiest.
RELIABLE = {"volume_resistance", "high_52w_momentum"}

MIN_BARS = 65  # enough for Donchian/Darvas; longer algos self-guard above


def _trend_tag(df: pd.DataFrame) -> str:
    close = df["Close"]
    c = float(close.iloc[-1])
    sma50 = sma(close, 50)
    sma50_now = float(sma50.iloc[-1])
    sma200 = float(sma(close, 200).iloc[-1]) if len(close) >= 200 else float("nan")
    rising = len(sma50.dropna()) > 6 and sma50_now > float(sma50.iloc[-6])
    if not np.isnan(sma50_now) and c > sma50_now and rising:
        return "up"
    if not np.isnan(sma200) and c > sma200:
        return "weak"
    return "down"


def todays_signal(df: pd.DataFrame) -> dict | None:
    """Evaluate the 6 algorithms on the latest bar. Returns a signal dict if
    >=1 fired, else None (also None when history is too short)."""
    if df is None or len(df) < MIN_BARS:
        return None
    df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
    if len(df) < MIN_BARS:
        return None
    try:
        fired = [key for key, fn in ALGORITHMS.items() if bool(fn(df).iloc[-1])]
        trend = _trend_tag(df)
        c = float(df["Close"].iloc[-1])
        day_ret = round((c / float(df["Close"].iloc[-2]) - 1) * 100, 2)
    except Exception:  # noqa: BLE001 - one bad frame shouldn't kill the screen
        return None
    if not fired:
        return None
    return {
        "close": round(c, 2),
        "n_detectors": len(fired),
        "detectors": fired,
        "trend": trend,
        "day_ret": day_ret,
        "reliable_hit": bool(RELIABLE & set(fired)),
    }
