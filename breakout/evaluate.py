"""Turn raw signal series into de-duplicated trades and score each one as a
true breakout vs. a false positive (failed breakout / "fakeout").

Outcome definition for a long breakout entered at the signal bar's close P:

* target = P * (1 + tp)        (default +8%)
* stop   = P * (1 - sl)        (default -5%)

Walking forward up to `horizon` bars, intrabar:

* "true"      -> target touched before stop
* "false"     -> stop touched before target (a failed breakout)
* "timeout_up"   -> neither touched, but final close is above entry
* "timeout_down" -> neither touched, and final close is at/below entry

False-positive rate = (false + timeout_down) / total signals.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def dedup_signals(sig: pd.Series, cooldown: int = 10) -> pd.DatetimeIndex:
    """Keep only "fresh" signals: drop any that fire within `cooldown` bars
    of an already-counted one."""
    idx = list(sig.index[sig.fillna(False)])
    kept: list[pd.Timestamp] = []
    last_pos = -(10**9)
    pos_of = {ts: i for i, ts in enumerate(sig.index)}
    for ts in idx:
        p = pos_of[ts]
        if p - last_pos > cooldown:
            kept.append(ts)
            last_pos = p
    return pd.DatetimeIndex(kept)


def classify_trade(
    df: pd.DataFrame,
    entry_ts: pd.Timestamp,
    horizon: int = 20,
    tp: float = 0.08,
    sl: float = 0.05,
) -> dict:
    loc = df.index.get_loc(entry_ts)
    entry = float(df["Close"].iloc[loc])
    target, stop = entry * (1 + tp), entry * (1 - sl)

    fwd = df.iloc[loc + 1 : loc + 1 + horizon]
    outcome, days = "timeout_up", len(fwd)
    if fwd.empty:
        outcome = "no_data"
    else:
        for d, (_, bar) in enumerate(fwd.iterrows(), start=1):
            hit_t = bar["High"] >= target
            hit_s = bar["Low"] <= stop
            if hit_t and hit_s:  # ambiguous bar -> assume stop first (conservative)
                outcome, days = "false", d
                break
            if hit_s:
                outcome, days = "false", d
                break
            if hit_t:
                outcome, days = "true", d
                break
        else:
            final = float(fwd["Close"].iloc[-1])
            outcome = "timeout_up" if final > entry else "timeout_down"

    mfe = mae = np.nan
    fwd_ret = np.nan
    if not fwd.empty:
        mfe = float(fwd["High"].max() / entry - 1)
        mae = float(fwd["Low"].min() / entry - 1)
        fwd_ret = float(fwd["Close"].iloc[-1] / entry - 1)

    # Identification-quality view, independent of any stop. Did price
    # actually break out and follow through?
    #   confirmed -> ran at least the +tp target at some point
    #   fakeout   -> never made meaningful upside (< tp/2) OR rolled over
    #   marginal  -> in between
    if np.isnan(mfe):
        breakout_class = "no_data"
    elif mfe >= tp:
        breakout_class = "confirmed"
    elif mfe < tp / 2 or fwd_ret <= -sl:
        breakout_class = "fakeout"
    else:
        breakout_class = "marginal"

    return {
        "entry_date": entry_ts.date().isoformat(),
        "entry_price": round(entry, 2),
        "outcome": outcome,
        "breakout_class": breakout_class,
        "days_to_resolve": days,
        "fwd_return_%": None if np.isnan(fwd_ret) else round(100 * fwd_ret, 1),
        "max_favorable_%": None if np.isnan(mfe) else round(100 * mfe, 1),
        "max_adverse_%": None if np.isnan(mae) else round(100 * mae, 1),
    }


SUCCESS = {"true"}
FALSE_POS = {"false", "timeout_down"}


def evaluate_ticker(
    df: pd.DataFrame,
    algos: dict,
    cooldown: int = 10,
    horizon: int = 20,
    tp: float = 0.08,
    sl: float = 0.05,
) -> pd.DataFrame:
    rows = []
    for name, fn in algos.items():
        sig = fn(df)
        for ts in dedup_signals(sig, cooldown):
            r = classify_trade(df, ts, horizon, tp, sl)
            if r["outcome"] == "no_data":
                continue
            r["algorithm"] = name
            rows.append(r)
    cols = [
        "algorithm",
        "entry_date",
        "entry_price",
        "outcome",
        "breakout_class",
        "days_to_resolve",
        "fwd_return_%",
        "max_favorable_%",
        "max_adverse_%",
    ]
    return pd.DataFrame(rows, columns=cols)


def summarize(signals: pd.DataFrame) -> pd.DataFrame:
    if signals.empty:
        return pd.DataFrame()
    g = signals.groupby("algorithm")
    out = g.agg(
        signals=("outcome", "size"),
        true=("outcome", lambda s: (s == "true").sum()),
        false=("outcome", lambda s: (s == "false").sum()),
        timeout_up=("outcome", lambda s: (s == "timeout_up").sum()),
        timeout_down=("outcome", lambda s: (s == "timeout_down").sum()),
        avg_fwd_return_pct=("fwd_return_%", "mean"),
    )
    cls = signals.groupby("algorithm")["breakout_class"]
    out["confirmed"] = cls.apply(lambda s: (s == "confirmed").sum())
    out["fakeout"] = cls.apply(lambda s: (s == "fakeout").sum())
    out["tradeable_win_%"] = (100 * out["true"] / out["signals"]).round(1)
    out["stop_whipsaw_%"] = (
        100 * (out["false"] + out["timeout_down"]) / out["signals"]
    ).round(1)
    out["confirmed_%"] = (100 * out["confirmed"] / out["signals"]).round(1)
    out["fakeout_%"] = (100 * out["fakeout"] / out["signals"]).round(1)
    out["avg_fwd_return_pct"] = out["avg_fwd_return_pct"].round(2)
    return out.reset_index()
