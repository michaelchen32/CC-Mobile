"""Recall-oriented backtest.

Ground truth ("the opportunities we must not miss") is defined
independently of the detector: a day is an opportunity launch if price
goes on to gain >= `thresh` within `horizon` trading days AND that day is
near the *start* of the move (not already extended). Launches are
clustered so each distinct move counts once.

Recall = fraction of opportunity episodes for which the system produced
at least one *actionable* signal (early enough, before price ran away).
We also report the cost of that recall: false-alarm rate and alert load.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .recall_system import DETECTORS, detect


def opportunities(
    df: pd.DataFrame,
    thresh: float = 0.20,
    horizon: int = 30,
    episode_gap: int = 25,
) -> list[dict]:
    c = df["Close"].to_numpy(float)
    h = df["High"].to_numpy(float)
    low = df["Low"].to_numpy(float)
    n = len(df)
    eps: list[dict] = []
    last_anchor = -(10**9)
    for t in range(20, n - 1):
        end = min(t + horizon, n - 1)
        if end <= t:
            break
        fwd_max = h[t + 1 : end + 1].max()
        fwd_ret = fwd_max / c[t] - 1
        if fwd_ret < thresh:
            continue
        trailing = c[t] / c[max(0, t - 10)] - 1  # not already extended
        base = c[t] <= low[max(0, t - 5) : t].min() * 1.06  # near a base
        if trailing > 0.10 or not base:
            continue
        if t - last_anchor < episode_gap:
            continue
        eps.append(
            {
                "anchor_idx": t,
                "anchor_date": df.index[t],
                "anchor_price": float(c[t]),
                "fwd_max_ret_%": round(100 * fwd_ret, 1),
            }
        )
        last_anchor = t
    return eps


def _dedup(idxs: list[int], cooldown: int) -> list[int]:
    kept, last = [], -(10**9)
    for i in idxs:
        if i - last > cooldown:
            kept.append(i)
            last = i
    return kept


def evaluate(
    df: pd.DataFrame,
    thresh: float = 0.20,
    horizon: int = 30,
    lead_tol: int = 3,
    lag_tol: int = 15,
    max_chase: float = 0.12,
    eval_start: str | None = None,
) -> dict:
    """Per-ticker recall for the union and each individual detector.

    Full df is used for indicator warm-up; only episodes/signals dated on
    or after `eval_start` are scored (so the report covers a clean window
    while 200-day averages etc. are still valid)."""
    eps = opportunities(df, thresh, horizon)
    if eval_start is not None:
        cutoff = pd.Timestamp(eval_start)
        eps = [e for e in eps if e["anchor_date"] >= cutoff]
    d = detect(df)
    if eval_start is not None:
        d = d.copy()
        before = df.index < pd.Timestamp(eval_start)
        d.loc[before, "signal"] = False
        for _n in DETECTORS:
            d.loc[before, _n] = False
    pos = np.arange(len(df))
    close = df["Close"].to_numpy(float)
    years = max((df.index[-1] - df.index[0]).days / 365.25, 0.25)

    def recall_for(mask: pd.Series) -> dict:
        sig_idx = _dedup(list(pos[mask.to_numpy()]), cooldown=3)
        caught = 0
        leads = []
        for e in eps:
            a, ap = e["anchor_idx"], e["anchor_price"]
            for s in sig_idx:
                if a - lead_tol <= s <= a + lag_tol and close[s] <= ap * (
                    1 + max_chase
                ):
                    caught += 1
                    leads.append(a - s)
                    break
        # actionable = signal sits inside some opportunity's entry window
        useful = 0
        for s in sig_idx:
            for e in eps:
                a, ap = e["anchor_idx"], e["anchor_price"]
                if a - lead_tol <= s <= a + lag_tol and close[s] <= ap * (
                    1 + max_chase
                ):
                    useful += 1
                    break
        return {
            "episodes": len(eps),
            "caught": caught,
            "recall_%": round(100 * caught / len(eps), 1) if eps else None,
            "signals": len(sig_idx),
            "false_alarm_%": (
                round(100 * (1 - useful / len(sig_idx)), 1) if sig_idx else None
            ),
            "signals_per_yr": round(len(sig_idx) / years, 1),
            "avg_lead_days": round(float(np.mean(leads)), 1) if leads else None,
        }

    res = {"union": recall_for(d["signal"])}
    for name in DETECTORS:
        res[name] = recall_for(d[name])
    return res


def aggregate(per_ticker: dict[str, dict]) -> pd.DataFrame:
    """Combine per-ticker results into one recall table per detector."""
    keys = ["union"] + DETECTORS
    rows = []
    for k in keys:
        ep = ca = si = us = 0
        leads = []
        spy = []
        for _t, r in per_ticker.items():
            v = r[k]
            ep += v["episodes"]
            ca += v["caught"]
            si += v["signals"]
            if v["false_alarm_%"] is not None:
                us += round(v["signals"] * (1 - v["false_alarm_%"] / 100))
            if v["avg_lead_days"] is not None:
                leads.append(v["avg_lead_days"])
            spy.append(v["signals_per_yr"])
        rows.append(
            {
                "detector": k,
                "episodes": ep,
                "caught": ca,
                "recall_%": round(100 * ca / ep, 1) if ep else None,
                "signals": si,
                "false_alarm_%": round(100 * (1 - us / si), 1) if si else None,
                "avg_signals_per_name_yr": round(float(np.mean(spy)), 1)
                if spy
                else None,
                "avg_lead_days": round(float(np.mean(leads)), 1)
                if leads
                else None,
            }
        )
    df = pd.DataFrame(rows)
    return df.sort_values("recall_%", ascending=False).reset_index(drop=True)
