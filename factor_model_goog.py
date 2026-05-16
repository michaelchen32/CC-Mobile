"""
Factor model for GOOG, daily returns, ~5 years ending Friday 2026-05-15.

Two complementary fits:
  (A) Carhart 4-factor (Mkt-RF, SMB, HML, MOM) from Ken French data
      -> richest factor attribution. NOTE: FF factors publish with a lag,
         the series ends 2026-03-31, so this fit stops there.
  (B) Single market-factor model with a market factor we build ourselves
      from the S&P 500 and the 13-week T-bill -> can be carried all the
      way through Friday's close, so the residual's *current* position
      reflects Friday's actual price.

The residual is then modeled as a mean-reverting OU / AR(1) process
(Avellaneda-Lee style) to locate where the idiosyncratic component sits.
"""
import numpy as np
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
from scipy import stats as ss
import zipfile

END = pd.Timestamp("2026-05-15")              # Friday's close
START = END - pd.DateOffset(years=5)


def _read_ff_zip(path, colnames):
    with zipfile.ZipFile(path) as z:
        raw = z.read(z.namelist()[0]).decode("latin-1").splitlines()
    rows = [[p.strip() for p in ln.split(",")] for ln in raw
            if ln.strip()[:8].isdigit() and len(ln.strip().split(",")[0].strip()) == 8]
    df = pd.DataFrame(rows).iloc[:, : len(colnames) + 1]
    df.columns = ["Date"] + colnames
    df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
    return df.set_index("Date").astype(float)


def ou_sscore(resid, asof):
    """AR(1) on cumulative residual -> OU params + current s-score."""
    Xc = resid.cumsum()
    Xc.name = "X"
    x_lag = Xc.shift(1).dropna()
    x_cur = Xc.loc[x_lag.index]
    ar = sm.OLS(x_cur, sm.add_constant(x_lag)).fit()
    a, b = ar.params["const"], ar.params["X"]
    z = ar.resid
    kappa = -np.log(b) * 252
    m = a / (1.0 - b)
    sig_eq = np.sqrt(z.var() / (1.0 - b * b))
    halflife = np.log(2) / (-np.log(b))
    s = (Xc.iloc[-1] - m) / sig_eq
    return dict(b=b, kappa=kappa, halflife=halflife, m=m, sig_eq=sig_eq,
                cum=Xc.iloc[-1], s=s, asof=asof)


# ---- prices ---------------------------------------------------------------
dl = yf.download(["GOOG", "^GSPC", "^IRX"],
                 start=START - pd.Timedelta(days=10),
                 end=END + pd.Timedelta(days=1),
                 progress=False, auto_adjust=True)["Close"]
goog_ret = dl["GOOG"].pct_change().dropna() * 100.0
mkt_ret = dl["^GSPC"].pct_change().dropna() * 100.0
rf_daily = (dl["^IRX"] / 100.0 / 252.0).reindex(mkt_ret.index).ffill()
fri_close = float(dl["GOOG"].loc[:END].iloc[-1])
fri_date = dl["GOOG"].loc[:END].index[-1].date()

# =========================================================================
# (A) Carhart 4-factor  (ends 2026-03-31, FF publication lag)
# =========================================================================
ff = _read_ff_zip("/tmp/ff.zip", ["Mkt-RF", "SMB", "HML", "RF"])
mom = _read_ff_zip("/tmp/mom.zip", ["MOM"])
fac = ff.join(mom).dropna()
A = pd.DataFrame({"GOOG": goog_ret}).join(fac, how="inner").loc[START:END].dropna()
A["EXC"] = A["GOOG"] - A["RF"]
mA = sm.OLS(A["EXC"], sm.add_constant(A[["Mkt-RF", "SMB", "HML", "MOM"]])).fit()

print("=" * 66)
print("(A) GOOG  Carhart 4-factor  | daily excess returns")
print(f"    {A.index[0].date()} -> {A.index[-1].date()}  ({len(A)} obs)"
      "   [FF factors end 03-31]")
print("=" * 66)
print(mA.summary().tables[1])
print(f"R^2 = {mA.rsquared:.3f}   adj R^2 = {mA.rsquared_adj:.3f}")
print(f"Annualized alpha = {mA.params['const']*252:+.2f}%  "
      f"(daily {mA.params['const']:+.4f}%, p={mA.pvalues['const']:.2f})")
eA = mA.resid
print(f"\nCarhart residual: daily sd {eA.std():.3f}%  | "
      f"annualized idio vol {eA.std()*np.sqrt(252):.1f}%  | "
      f"skew {ss.skew(eA):+.2f}  exc-kurt {ss.kurtosis(eA):+.2f}")
oA = ou_sscore(eA, A.index[-1].date())
print(f"OU half-life {oA['halflife']:.1f}d | s-score {oA['s']:+.2f} "
      f"(as of {oA['asof']}, NOT Friday)")

# =========================================================================
# (B) Self-built market factor -> carried through Friday's close
# =========================================================================
B = pd.DataFrame({"GOOG": goog_ret, "MKT": mkt_ret, "RF": rf_daily}
                 ).loc[START:END].dropna()
B["y"] = B["GOOG"] - B["RF"]
B["x"] = B["MKT"] - B["RF"]
mB = sm.OLS(B["y"], sm.add_constant(B["x"])).fit()
eB = mB.resid

print("\n" + "=" * 66)
print("(B) GOOG  market-factor model (S&P500 - 13wk T-bill)  | through Fri")
print(f"    {B.index[0].date()} -> {B.index[-1].date()}  ({len(B)} obs)")
print("=" * 66)
beta = mB.params["x"]
print(f"beta(mkt)        : {beta:.3f}  (t={mB.tvalues['x']:.1f})")
print(f"alpha (daily)    : {mB.params['const']:+.4f}%  "
      f"-> annualized {mB.params['const']*252:+.2f}%  "
      f"(p={mB.pvalues['const']:.2f})")
print(f"R^2              : {mB.rsquared:.3f}")
print("-" * 66)
print("RESIDUAL distribution (idiosyncratic daily return, %)")
print(f"  mean           : {eB.mean():.2e}  (~0 by construction)")
print(f"  daily std      : {eB.std():.4f}%")
print(f"  annualized idio: {eB.std()*np.sqrt(252):.2f}%")
print(f"  skew / exc-kurt: {ss.skew(eB):+.3f} / {ss.kurtosis(eB):+.3f}")
print(f"  min / max      : {eB.min():+.2f}% / {eB.max():+.2f}%")
jb = ss.jarque_bera(eB)
print(f"  Jarque-Bera    : stat={jb[0]:.0f}, p={jb[1]:.2g} "
      "(fat-tailed; normality rejected)")

oB = ou_sscore(eB, B.index[-1].date())
print("-" * 66)
print(f"WHERE IT SITS  (OU on cumulative residual, as of {oB['asof']} = Friday)")
print(f"  AR(1) b        : {oB['b']:.4f}")
print(f"  mean-rev kappa : {oB['kappa']:.1f} /yr")
print(f"  half-life      : {oB['halflife']:.1f} trading days")
print(f"  equilibrium m  : {oB['m']:+.3f}")
print(f"  equilib. stdev : {oB['sig_eq']:.3f}")
print(f"  cum resid now  : {oB['cum']:+.3f}")
print(f"  last-day resid : {eB.iloc[-1]:+.3f}%  "
      f"({eB.iloc[-1]/eB.std():+.2f}sigma)")
print(f"\n  >>> s-SCORE    : {oB['s']:+.2f}")
s = oB["s"]
if s > 1.25:
    v = "RICH  vs factor-fair-value  (idio over-extended, mean-revert DOWN)"
elif s < -1.25:
    v = "CHEAP vs factor-fair-value  (idio depressed, mean-revert UP)"
else:
    v = "NEUTRAL — within ~1sigma of factor-implied fair value"
print(f"  >>> {v}")
print(f"\nGOOG Friday close ({fri_date}): ${fri_close:.2f}")
print("=" * 66)
