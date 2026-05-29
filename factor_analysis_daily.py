#!/usr/bin/env python3
"""
Statistical factor analysis + crowdedness for the 30-name large-cap
20-trading-day momentum basket, using ACTUAL daily returns over the
last 20 and 60 trading days (source: Yahoo Finance daily adj-close).

Outputs:
  1. Factor exposures: per-stock + equal-weight-basket OLS on factor-ETF
     daily returns (market, momentum, quality, low-vol, size, growth/value,
     semis/AI, spec-growth, crypto, duration), with R^2 and t-stats.
  2. Crowdedness: average pairwise return correlation, PCA of the 30-name
     return matrix (variance share of PC1, participation ratio / effective
     number of independent bets), for both windows.
"""
import json, time, sys
import urllib.request
import numpy as np
import pandas as pd

STOCKS = ["RKLB","ASTS","UMC","ALAB","MU","SNOW","HUT","DDOG","ARM","STRL",
          "FLEX","SMTC","SMCI","GH","AAON","IONQ","DELL","FTNT","RIOT","APLD",
          "DOCN","CRWD","CIFR","QBTS","AMD","FSLR","PANW","IREN","F","PL"]

# factor-proxy ETFs
FACTORS = {
 "MKT":"SPY", "Mom":"MTUM", "Qual":"QUAL", "LowVol":"USMV", "Size":"IWM",
 "Growth":"IWF", "Value":"IWD", "Semis":"SMH", "Spec":"ARKK",
 "Crypto":"IBIT", "Duration":"TLT",
}

UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch(sym, rng="6mo"):
    url=(f"https://query2.finance.yahoo.com/v8/finance/chart/{sym}"
         f"?range={rng}&interval=1d&events=div%2Csplit")
    for attempt in range(5):
        try:
            req=urllib.request.Request(url, headers=UA)
            j=json.load(urllib.request.urlopen(req, timeout=30))
            r=j["chart"]["result"][0]
            ts=r["timestamp"]
            q=r["indicators"]["quote"][0]["close"]
            adj=r["indicators"].get("adjclose",[{}])[0].get("adjclose", q)
            s=pd.Series(adj, index=pd.to_datetime(ts, unit="s").normalize(), name=sym)
            return s.dropna()
        except Exception as e:
            time.sleep(1.5*(attempt+1))
    print(f"  !! failed {sym}: {e}", file=sys.stderr)
    return None

print("Downloading daily series (Yahoo)...", file=sys.stderr)
series={}
for sym in STOCKS+list(FACTORS.values()):
    s=fetch(sym)
    if s is not None and len(s)>62: series[sym]=s
    time.sleep(0.35)
px=pd.DataFrame(series).sort_index().ffill().dropna(how="any")
rets=px.pct_change().dropna()
print(f"Aligned panel: {rets.shape[0]} daily returns x {rets.shape[1]} symbols, "
      f"last date {rets.index[-1].date()}", file=sys.stderr)

stocks=[s for s in STOCKS if s in rets.columns]
fac_cols={k:v for k,v in FACTORS.items() if v in rets.columns}

def ols(y, Xdf):
    X=np.column_stack([np.ones(len(Xdf)), Xdf.values])
    beta,_,_,_=np.linalg.lstsq(X,y.values,rcond=None)
    resid=y.values-X@beta
    n,k=X.shape
    dof=max(n-k,1)
    s2=(resid@resid)/dof
    cov=s2*np.linalg.pinv(X.T@X)
    se=np.sqrt(np.diag(cov))
    t=beta/np.where(se==0,np.nan,se)
    sst=((y.values-y.values.mean())**2).sum()
    r2=1-(resid@resid)/sst if sst>0 else np.nan
    return beta,t,r2

def analyze(window, label):
    rw=rets.iloc[-window:]
    print("\n"+"#"*72)
    print(f"#  WINDOW: last {window} trading days ({label})  "
          f"[{rw.index[0].date()} -> {rw.index[-1].date()}, n={len(rw)} obs]")
    print("#"*72)

    # ---- equal-weight basket factor regression ----
    bask=rw[stocks].mean(axis=1)
    # parsimonious factor set sized to dof
    core = ["MKT","Semis","Spec","Crypto","Duration"] if window>=40 else ["MKT","Semis","Spec"]
    Xcols=[fac_cols[k] for k in core if k in fac_cols]
    Xdf=rw[Xcols]
    beta,t,r2=ols(bask, Xdf)
    print(f"\n[A] EQUAL-WEIGHT BASKET multi-factor OLS   (R^2 = {r2:.2f})")
    print(f"     {'factor':<12}{'beta':>8}{'t-stat':>8}")
    names=["alpha"]+[k for k in core if k in fac_cols]
    for nm,b,tt in zip(names,beta,t):
        star="*" if abs(tt)>=2 else " "
        print(f"     {nm:<12}{b:>8.2f}{tt:>8.1f} {star}")

    # ---- univariate factor correlation of basket (robust driver signal) ----
    print(f"\n[B] BASKET return correlation with each factor (univariate driver):")
    cors=[(k, np.corrcoef(bask, rw[v])[0,1]) for k,v in fac_cols.items()]
    for k,c in sorted(cors,key=lambda x:-abs(x[1])):
        print(f"     {k:<12}{c:+.2f}")

    # ---- per-stock market beta + R^2 dispersion ----
    spy=rw[fac_cols["MKT"]]
    betas={};r2s={}
    for s in stocks:
        b,_,rr=ols(rw[s], spy.to_frame())
        betas[s]=b[1]; r2s[s]=rr
    bser=pd.Series(betas); rser=pd.Series(r2s)
    print(f"\n[C] Per-stock MARKET (SPY) beta: mean {bser.mean():.2f}, "
          f"median {bser.median():.2f}, range {bser.min():.2f}-{bser.max():.2f}")
    print(f"    avg single-stock R^2 vs market: {rser.mean():.2f} "
          f"(low => idiosyncratic/theme-driven, not market-driven)")

    # ---- CROWDEDNESS: correlation + PCA ----
    C=rw[stocks].corr().values
    n=len(stocks)
    offdiag=C[np.triu_indices(n,1)]
    eig=np.sort(np.linalg.eigvalsh(C))[::-1]
    pc1=eig[0]/eig.sum(); pc2=eig[1]/eig.sum()
    pr=(eig.sum()**2)/(eig**2).sum()   # participation ratio = eff. # bets
    print(f"\n[D] CROWDEDNESS / co-movement ({n} names)")
    print(f"     avg pairwise correlation : {offdiag.mean():+.2f}  "
          f"(median {np.median(offdiag):+.2f})")
    print(f"     PC1 variance share       : {pc1*100:.0f}%   "
          f"(single common factor)")
    print(f"     PC1+PC2 variance share   : {(pc1+pc2)*100:.0f}%")
    print(f"     participation ratio      : {pr:.1f} of {n}  "
          f"(effective independent bets)")
    return bask, offdiag.mean(), pc1, pr

r20=analyze(20,"~1 month")
r60=analyze(60,"~3 months")

print("\n"+"="*72)
print("SUMMARY: 20d vs 60d")
print("="*72)
print(f"{'metric':<28}{'20d':>10}{'60d':>10}")
print(f"{'avg pairwise corr':<28}{r20[1]:>10.2f}{r60[1]:>10.2f}")
print(f"{'PC1 variance share':<28}{r20[2]*100:>9.0f}%{r60[2]*100:>9.0f}%")
print(f"{'eff. # independent bets':<28}{r20[3]:>10.1f}{r60[3]:>10.1f}")
