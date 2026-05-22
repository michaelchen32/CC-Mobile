"""Collect fundamentals / valuation / performance / earnings for the names
that fired in results/today_signals.csv.

Data source: yfinance only (the environment's network policy blocks every
other site, including earnings-transcript providers). Literal call
transcript TEXT is therefore NOT retrievable; in its place this builds a
quantitative earnings recap (EPS beat/miss history + revenue/margin
trajectory) and flags highlights vs. issues from the numbers.

Outputs:
  results/fundamentals_master.csv   one row per name, key metrics
  results/fundamentals_report.md    per-name detail (the 5 requested blocks)
"""
from __future__ import annotations

import os
import time

import numpy as np
import pandas as pd
import yfinance as yf

from breakout.data import _cache_path

RESULTS = os.path.join(os.path.dirname(__file__), "results")
PRICE_START, PRICE_END = "2022-05-01", "2026-05-18"


def _row(stmt: pd.DataFrame, names: list[str]) -> pd.Series | None:
    if stmt is None or stmt.empty:
        return None
    for n in names:
        if n in stmt.index:
            return stmt.loc[n]
    return None


def _m(x) -> str:
    """Human money formatting."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "n/a"
    x = float(x)
    a = abs(x)
    if a >= 1e9:
        return f"{x/1e9:.2f}B"
    if a >= 1e6:
        return f"{x/1e6:.1f}M"
    return f"{x:,.0f}"


def _pct(x, d: int = 1) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "n/a"
    return f"{100*float(x):.{d}f}%"


def _x(x, d: int = 1) -> str:
    if x is None or (isinstance(x, float) and (np.isnan(x) or np.isinf(x))):
        return "n/a"
    return f"{float(x):.{d}f}x"


def perf(ticker: str) -> dict:
    p = _cache_path(ticker, PRICE_START, PRICE_END)
    if not os.path.exists(p):
        return {}
    px = pd.read_csv(p, index_col=0, parse_dates=True)["Close"].dropna()
    if px.empty:
        return {}

    def ret(n: int):
        if len(px) <= n:
            return None
        return px.iloc[-1] / px.iloc[-1 - n] - 1

    last = px.index[-1]
    hi12 = px.iloc[-252:].max() if len(px) >= 30 else px.max()
    return {
        "last_date": last.date().isoformat(),
        "L1M_%": ret(21),
        "L3M_%": ret(63),
        "L12M_%": ret(252),
        "pct_from_12m_high_%": px.iloc[-1] / hi12 - 1,
    }


def annual_series(t: yf.Ticker) -> pd.DataFrame:
    fin, cf = t.financials, t.cashflow
    rev = _row(fin, ["Total Revenue"])
    ni = _row(fin, ["Net Income", "Net Income Common Stockholders"])
    eb = _row(fin, ["EBITDA", "Normalized EBITDA"])
    cfo = _row(cf, ["Operating Cash Flow",
                    "Cash Flow From Continuing Operating Activities"])
    fcf = _row(cf, ["Free Cash Flow"])
    capex = _row(cf, ["Capital Expenditure"])
    if rev is None:
        return pd.DataFrame()
    cols = list(rev.index)[:5]
    rows = {}
    for c in cols:
        yr = pd.Timestamp(c).year
        r = float(rev.get(c, np.nan))
        n = float(ni.get(c, np.nan)) if ni is not None else np.nan
        e = float(eb.get(c, np.nan)) if eb is not None else np.nan
        o = float(cfo.get(c, np.nan)) if cfo is not None else np.nan
        f = float(fcf.get(c, np.nan)) if fcf is not None else np.nan
        cx = float(capex.get(c, np.nan)) if capex is not None else np.nan
        rows[yr] = {
            "Revenue": r,
            "Rev_growth": np.nan,
            "Net_margin": n / r if r else np.nan,
            "EBITDA_margin": e / r if r else np.nan,
            "CFO": o,
            "FCF": f if not np.isnan(f) else (o + cx if not np.isnan(o) and not np.isnan(cx) else np.nan),
            "FCF_margin": (f / r) if (r and not np.isnan(f)) else np.nan,
        }
    df = pd.DataFrame(rows).T.sort_index()
    df["Rev_growth"] = df["Revenue"].pct_change()
    return df


def quarterly_series(t: yf.Ticker) -> pd.DataFrame:
    qf, qc = t.quarterly_financials, t.quarterly_cashflow
    rev = _row(qf, ["Total Revenue"])
    ni = _row(qf, ["Net Income", "Net Income Common Stockholders"])
    cfo = _row(qc, ["Operating Cash Flow",
                    "Cash Flow From Continuing Operating Activities"])
    fcf = _row(qc, ["Free Cash Flow"])
    if rev is None:
        return pd.DataFrame()
    cols = list(rev.index)[:8]
    rows = {}
    for c in cols:
        key = pd.Timestamp(c).strftime("%Y-%m")
        r = float(rev.get(c, np.nan))
        rows[key] = {
            "Revenue": r,
            "Net_margin": (float(ni.get(c, np.nan)) / r)
            if (ni is not None and r) else np.nan,
            "CFO": float(cfo.get(c, np.nan)) if cfo is not None else np.nan,
            "FCF": float(fcf.get(c, np.nan)) if fcf is not None else np.nan,
        }
    return pd.DataFrame(rows).T.iloc[::-1]


def valuation(t: yf.Ticker, info: dict) -> dict:
    ev = info.get("enterpriseValue")
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    fwd_rev = fwd_eps = np.nan
    try:
        re = t.revenue_estimate
        if re is not None and "+1y" in re.index:
            fwd_rev = float(re.loc["+1y", "avg"])
    except Exception:  # noqa: BLE001
        pass
    try:
        ee = t.earnings_estimate
        if ee is not None and "+1y" in ee.index:
            fwd_eps = float(ee.loc["+1y", "avg"])
    except Exception:  # noqa: BLE001
        pass

    trail_rev = info.get("totalRevenue")
    eb_margin = (info.get("ebitda") / trail_rev) if (
        info.get("ebitda") and trail_rev) else np.nan
    fcf_margin = (info.get("freeCashflow") / trail_rev) if (
        info.get("freeCashflow") and trail_rev) else np.nan

    def safe_div(a, b):
        try:
            return a / b if a and b and b > 0 else np.nan
        except Exception:  # noqa: BLE001
            return np.nan

    fwd_ebitda = fwd_rev * eb_margin if not np.isnan(fwd_rev) and not np.isnan(eb_margin) else np.nan
    fwd_fcf = fwd_rev * fcf_margin if not np.isnan(fwd_rev) and not np.isnan(fcf_margin) else np.nan
    return {
        "EV": ev,
        "fwd_rev_26E": fwd_rev,
        "fwd_eps_26E": fwd_eps,
        "TEV/Sales_26E": safe_div(ev, fwd_rev),
        "TEV/EBITDA_26E_est": safe_div(ev, fwd_ebitda),
        "TEV/FCF_26E_est": safe_div(ev, fwd_fcf),
        "PE_26E": safe_div(price, fwd_eps),
        "TEV/Sales_TTM": info.get("enterpriseToRevenue"),
        "TEV/EBITDA_TTM": info.get("enterpriseToEbitda"),
        "PE_TTM": info.get("trailingPE"),
        "PE_fwd_info": info.get("forwardPE"),
    }


def earnings_recap(t: yf.Ticker) -> pd.DataFrame:
    try:
        ed = t.get_earnings_dates(limit=16)
    except Exception:  # noqa: BLE001
        return pd.DataFrame()
    if ed is None or ed.empty:
        return pd.DataFrame()
    ed = ed.dropna(subset=["Reported EPS"]).head(4)
    out = ed[["EPS Estimate", "Reported EPS", "Surprise(%)"]].copy()
    out.index = [pd.Timestamp(i).date().isoformat() for i in out.index]
    return out


def diagnose(ann: pd.DataFrame, eps: pd.DataFrame, val: dict) -> tuple[list, list]:
    hi, iss = [], []
    if not ann.empty and len(ann) >= 2:
        g = ann["Rev_growth"].dropna()
        if not g.empty:
            if g.iloc[-1] > 0.15:
                hi.append(f"revenue +{_pct(g.iloc[-1])} latest FY")
            if len(g) >= 2 and g.iloc[-1] > g.iloc[-2]:
                hi.append("revenue growth accelerating")
            if len(g) >= 2 and g.iloc[-1] < g.iloc[-2] - 0.03:
                iss.append("revenue growth decelerating")
        nm = ann["Net_margin"].dropna()
        if not nm.empty:
            if nm.iloc[-1] < 0:
                iss.append(f"net margin negative ({_pct(nm.iloc[-1])})")
            elif len(nm) >= 2 and nm.iloc[-1] > nm.iloc[-2]:
                hi.append("net margin expanding")
        fm = ann["FCF_margin"].dropna()
        if not fm.empty:
            if fm.iloc[-1] < 0:
                iss.append("negative free cash flow")
            elif fm.iloc[-1] > 0.15:
                hi.append(f"strong FCF margin ({_pct(fm.iloc[-1])})")
    if not eps.empty:
        beats = (eps["Surprise(%)"] > 0).sum()
        if beats == len(eps):
            hi.append(f"beat EPS all last {len(eps)} quarters")
        elif beats == 0:
            iss.append(f"missed EPS all last {len(eps)} quarters")
        else:
            hi.append(f"beat EPS {beats}/{len(eps)} quarters")
    pe = val.get("PE_26E")
    if pe and not np.isnan(pe) and pe > 60:
        iss.append(f"rich valuation (26E P/E {_x(pe)})")
    ts = val.get("TEV/Sales_26E")
    if ts and not np.isnan(ts) and ts > 15:
        iss.append(f"high TEV/Sales 26E ({_x(ts)})")
    return hi or ["no standout positives in the numbers"], iss or ["none flagged from the numbers"]


def breakout_reason(row: pd.Series, pf: dict) -> str:
    bits = []
    dets = row["detectors"].split("+")
    name_map = {
        "fast_donchian": "10-day-high break",
        "donchian_20": "20-day-high break",
        "six_month_high": "new 6-month high",
        "volume_thrust": ">=5% up-day on >=2x volume",
        "gap_go": "gap-up and held",
        "range_expansion": "range expansion (>=2x ATR)",
        "squeeze_release": "volatility-squeeze release",
        "trend_continuation": "uptrend continuation off a dip",
    }
    bits.append(", ".join(name_map.get(d, d) for d in dets))
    if pf.get("L1M_%") is not None:
        bits.append(f"1M {_pct(pf['L1M_%'])}, 3M {_pct(pf.get('L3M_%'))}")
    if pf.get("pct_from_12m_high_%") is not None:
        v = pf["pct_from_12m_high_%"]
        bits.append("at/near 12-mo high" if v > -0.02
                     else f"{_pct(v)} from 12-mo high")
    bits.append(f"trend tag: {row['trend']}")
    return "; ".join(bits)


def fetch(ticker: str, retries: int = 3):
    for a in range(retries):
        try:
            t = yf.Ticker(ticker)
            info = t.info
            if not info or info.get("enterpriseValue") is None and info.get(
                "marketCap") is None:
                raise ValueError("empty info")
            return t, info
        except Exception:  # noqa: BLE001
            time.sleep(2 ** a)
    return None, None


def main() -> None:
    sig = pd.read_csv(os.path.join(RESULTS, "today_signals.csv"))
    tickers = sig["ticker"].tolist()
    print(f"Collecting fundamentals for {len(tickers)} names...")

    master, rep = [], []
    rep.append("# Fundamental / valuation / earnings dossier\n")
    rep.append(
        "Names that fired in the high-recall screen on the latest bar "
        f"({sig['date'].iloc[0]}). **Source: yfinance only** — the "
        "environment blocks all other sites, so literal earnings-call "
        "transcript text is not retrievable; the earnings section is a "
        "quantitative recap (EPS beat/miss + revenue/margin path) instead. "
        "Forward '2026E' = consensus next-fiscal-year (+1y) estimate; "
        "TEV/EBITDA & TEV/FCF 26E are estimated as forward revenue x "
        "trailing margin (marked _est_). Not investment advice.\n")

    for i, tk in enumerate(tickers, 1):
        row = sig[sig["ticker"] == tk].iloc[0]
        print(f"[{i}/{len(tickers)}] {tk}")
        t, info = fetch(tk)
        if t is None:
            rep.append(f"\n## {tk}\n_data unavailable_\n")
            continue
        try:
            ann = annual_series(t)
        except Exception:  # noqa: BLE001
            ann = pd.DataFrame()
        try:
            qtr = quarterly_series(t)
        except Exception:  # noqa: BLE001
            qtr = pd.DataFrame()
        pf = perf(tk)
        val = valuation(t, info)
        eps = earnings_recap(t)
        hi, iss = diagnose(ann, eps, val)

        master.append({
            "ticker": tk,
            "name": info.get("shortName"),
            "sector": info.get("sector"),
            "n_detectors": row["n_detectors"],
            "trend": row["trend"],
            "rev_growth_TTM_%": info.get("revenueGrowth"),
            "net_margin_%": info.get("profitMargins"),
            "CFO_TTM": info.get("operatingCashflow"),
            "FCF_TTM": info.get("freeCashflow"),
            "TEV/Sales_26E": val["TEV/Sales_26E"],
            "TEV/EBITDA_26E_est": val["TEV/EBITDA_26E_est"],
            "TEV/FCF_26E_est": val["TEV/FCF_26E_est"],
            "PE_26E": val["PE_26E"],
            "TEV/Sales_TTM": val["TEV/Sales_TTM"],
            "PE_TTM": val["PE_TTM"],
            "L1M_%": pf.get("L1M_%"),
            "L3M_%": pf.get("L3M_%"),
            "L12M_%": pf.get("L12M_%"),
        })

        rep.append(f"\n## {tk} — {info.get('shortName','')}  "
                   f"({info.get('sector','?')} / {info.get('industry','?')})\n")

        rep.append("\n**1) Fundamentals (annual, up to 5 FY):**\n\n")
        if ann.empty:
            rep.append("_n/a_\n")
        else:
            lines = ["| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |",
                     "| --- | --- | --- | --- | --- | --- | --- | --- |"]
            for yr, r in ann.iterrows():
                lines.append(f"| {yr} | {_m(r.Revenue)} | {_pct(r.Rev_growth)} "
                             f"| {_pct(r.Net_margin)} | {_pct(r.EBITDA_margin)} "
                             f"| {_m(r.CFO)} | {_m(r.FCF)} | {_pct(r.FCF_margin)} |")
            rep.append("\n".join(lines) + "\n")
        rep.append("\n**Quarterly (up to 8 q, newest last):**\n\n")
        if qtr.empty:
            rep.append("_n/a_\n")
        else:
            lines = ["| Qtr | Revenue | Net margin | CFO | FCF |",
                     "| --- | --- | --- | --- | --- |"]
            for q, r in qtr.iterrows():
                lines.append(f"| {q} | {_m(r.Revenue)} | {_pct(r.Net_margin)} "
                             f"| {_m(r.CFO)} | {_m(r.FCF)} |")
            rep.append("\n".join(lines) + "\n")

        rep.append("\n**2) Valuation:**\n\n")
        rep.append(
            f"- 2026E TEV/Sales: **{_x(val['TEV/Sales_26E'])}**  "
            f"(TTM {_x(val['TEV/Sales_TTM'])})\n"
            f"- 2026E TEV/EBITDA _est_: **{_x(val['TEV/EBITDA_26E_est'])}**  "
            f"(TTM {_x(val['TEV/EBITDA_TTM'])})\n"
            f"- 2026E TEV/FCF _est_: **{_x(val['TEV/FCF_26E_est'])}**\n"
            f"- 2026E P/E: **{_x(val['PE_26E'])}**  "
            f"(TTM {_x(val['PE_TTM'])}, fwd {_x(val['PE_fwd_info'])})\n"
            f"- EV {_m(val['EV'])}, 26E rev {_m(val['fwd_rev_26E'])}, "
            f"26E EPS {_x(val['fwd_eps_26E'],2)}\n")

        rep.append("\n**3) Performance:**\n\n")
        rep.append(
            f"- L1M {_pct(pf.get('L1M_%'))} · L3M {_pct(pf.get('L3M_%'))} · "
            f"L12M {_pct(pf.get('L12M_%'))} · "
            f"{_pct(pf.get('pct_from_12m_high_%'))} from 12-mo high\n")

        rep.append("\n**4) Reason for breakout:**\n\n")
        rep.append(f"{breakout_reason(row, pf)}\n")

        rep.append("\n**5) Earnings recap, last 4 reported quarters:**\n\n")
        if eps.empty:
            rep.append("_EPS history n/a_\n")
        else:
            lines = ["| Report date | EPS est | EPS reported | Surprise % |",
                     "| --- | --- | --- | --- |"]
            for d, r in eps.iterrows():
                lines.append(f"| {d} | {r['EPS Estimate']} | "
                             f"{r['Reported EPS']} | {r['Surprise(%)']} |")
            rep.append("\n".join(lines) + "\n")
        rep.append(f"\n_Highlights:_ {'; '.join(hi)}\n")
        rep.append(f"\n_Issues:_ {'; '.join(iss)}\n")
        rep.append(
            "\n_Note: call-transcript narrative not retrievable in this "
            "environment (network limited to the price/data provider)._\n")

    mdf = pd.DataFrame(master)
    for c in ["rev_growth_TTM_%", "net_margin_%", "L1M_%", "L3M_%", "L12M_%"]:
        mdf[c] = (100 * mdf[c]).round(1)
    for c in ["TEV/Sales_26E", "TEV/EBITDA_26E_est", "TEV/FCF_26E_est",
              "PE_26E", "TEV/Sales_TTM", "PE_TTM"]:
        mdf[c] = mdf[c].round(1)
    mdf.to_csv(os.path.join(RESULTS, "fundamentals_master.csv"), index=False)

    hdr = ("\n## Master table\n\n"
           + "| " + " | ".join(mdf.columns) + " |\n"
           + "| " + " | ".join(["---"] * len(mdf.columns)) + " |\n")
    for _, r in mdf.iterrows():
        hdr += "| " + " | ".join(
            "" if pd.isna(v) else str(v) for v in r) + " |\n"
    rep.insert(2, hdr)

    with open(os.path.join(RESULTS, "fundamentals_report.md"), "w") as fh:
        fh.write("\n".join(rep))
    print(f"\nDone. {len(master)} names. Artifacts in {RESULTS}/")


if __name__ == "__main__":
    main()
