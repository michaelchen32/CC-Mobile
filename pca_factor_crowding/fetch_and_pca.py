#!/usr/bin/env python3
"""
PCA factor-loading & crowdedness analysis across a semis / AI / datacenter /
software / consumer basket, using daily closing data over the last 20 and 60
trading days.

Data source: Yahoo Finance v8 chart API (adjusted closes -> handles splits).
PCA is run on the *correlation* matrix of daily log returns so that high-vol
names do not dominate purely by scale.

Crowding gauges:
  - PC1 variance share      (higher  = more one-factor / crowded)
  - Absorption ratio (AR)   (Kritzman-Li; first ~p/5 PCs)
  - mean pairwise corr      (directly tied to PC1 share)
  - effective # of factors  (participation ratio of eigenvalues; lower = crowded)
  - per-name |PC1 loading|  (who is most crowded into the dominant factor)
"""
import json, time, os, math, urllib.request, datetime as dt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

HERE   = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, "out");  os.makedirs(OUTDIR,  exist_ok=True)
DATADIR= os.path.join(HERE, "data"); os.makedirs(DATADIR, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# (display, yahoo symbol, sector bucket)
TICKERS = [
    ("MU","MU","Memory/HBM"), ("SK Hynix","000660.KS","Memory/HBM"),
    ("Samsung","005930.KS","Memory/HBM"), ("SNDK","SNDK","Memory/HBM"),
    ("NVDA","NVDA","Compute/AI-silicon"), ("AMD","AMD","Compute/AI-silicon"),
    ("AVGO","AVGO","Compute/AI-silicon"), ("MRVL","MRVL","Compute/AI-silicon"),
    ("CRDO","CRDO","Compute/AI-silicon"), ("INTC","INTC","Compute/AI-silicon"),
    ("QCOM","QCOM","Compute/AI-silicon"), ("CBRS","CBRS","Compute/AI-silicon"),
    ("AMAT","AMAT","Semicap"), ("LRCX","LRCX","Semicap"), ("KLAC","KLAC","Semicap"),
    ("LITE","LITE","Optical/Net"), ("COHR","COHR","Optical/Net"), ("AAOI","AAOI","Optical/Net"),
    ("VRT","VRT","AI-power/DC"), ("BE","BE","AI-power/DC"), ("ENPH","ENPH","AI-power/DC"),
    ("CRWD","CRWD","Software/Sec"), ("DDOG","DDOG","Software/Sec"), ("PANW","PANW","Software/Sec"),
    ("WDAY","WDAY","Software/Sec"), ("TEAM","TEAM","Software/Sec"), ("NOW","NOW","Software/Sec"),
    ("HUBS","HUBS","Software/Sec"), ("SHOP","SHOP","Software/Sec"), ("ADBE","ADBE","Software/Sec"),
    ("MDB","MDB","Software/Sec"), ("U","U","Software/Sec"), ("CDNS","CDNS","EDA"),
    ("AMZN","AMZN","Mega-cap"), ("GOOG","GOOG","Mega-cap"), ("TSLA","TSLA","Mega-cap"),
    ("DELL","DELL","Mega-cap"), ("UBER","UBER","Mega-cap"),
    ("IONQ","IONQ","Quantum"),
    ("NKE","NKE","Consumer"), ("LULU","LULU","Consumer"), ("AS","AS","Consumer"),
]
SECTORS = {d: s for d, _, s in TICKERS}
SECTOR_COLORS = {
    "Memory/HBM":"#d62728", "Compute/AI-silicon":"#1f77b4", "Semicap":"#17becf",
    "Optical/Net":"#9467bd", "AI-power/DC":"#ff7f0e", "Software/Sec":"#2ca02c",
    "Mega-cap":"#8c564b", "Quantum":"#e377c2", "Consumer":"#7f7f7f", "EDA":"#bcbd22",
}

def fetch(sym, rng="1y"):
    hosts = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]
    last = None
    for attempt in range(4):
        host = hosts[attempt % 2]
        url = (f"https://{host}/v8/finance/chart/{sym}"
               f"?range={rng}&interval=1d&events=div,splits")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
            res = data["chart"]["result"][0]
            ts  = res["timestamp"]
            ind = res["indicators"]
            close = ind["quote"][0]["close"]
            adj = None
            if ind.get("adjclose"):
                adj = ind["adjclose"][0].get("adjclose")
            px = adj if adj is not None else close
            dates = [dt.datetime.fromtimestamp(t, dt.timezone.utc).date() for t in ts]
            s = pd.Series(px, index=pd.to_datetime(dates), dtype="float64")
            s = s[~s.index.duplicated(keep="last")].sort_index()
            return s
        except Exception as e:
            last = e
            time.sleep(2 ** attempt)
    print(f"  !! FAILED {sym}: {last}")
    return None

# ---- download (cached) ------------------------------------------------------
CACHE = os.path.join(DATADIR, "closes.csv")
failed = []
if os.path.exists(CACHE) and os.environ.get("REFETCH") != "1":
    print("Loading cached closes:", CACHE)
    panel = pd.read_csv(CACHE, index_col=0, parse_dates=True)
else:
    print("Fetching daily closes from Yahoo ...")
    series = {}
    for disp, sym, sec in TICKERS:
        s = fetch(sym)
        if s is None or s.dropna().shape[0] < 5:
            failed.append(disp); print(f"  {disp:10s} {sym:12s}  -- no/short data"); continue
        sd = s.dropna()
        series[disp] = s
        print(f"  {disp:10s} {sym:12s} n={sd.shape[0]:4d}  "
              f"first={sd.index[0].date()} last={sd.index[-1].date()}  px={sd.iloc[-1]:.2f}")
        time.sleep(0.35)
    # US trading calendar from a core liquid name; ffill the 2 Korean names onto it
    ref = series["NVDA"].index
    panel = pd.DataFrame(series).reindex(ref).ffill()
    panel.index.name = "date"
    panel.to_csv(CACHE)

print(f"\nPanel: {panel.shape[1]} names x {panel.shape[0]} US sessions, "
      f"{panel.index[0].date()} -> {panel.index[-1].date()}")
if failed: print("Dropped (no data):", failed)

# ---- PCA --------------------------------------------------------------------
def pca_window(panel, W):
    sub = panel.iloc[-(W + 1):]
    good = [c for c in sub.columns if sub[c].notna().all()]
    dropped = [c for c in sub.columns if c not in good]
    sub = sub[good]
    rets = np.log(sub).diff().iloc[1:]                 # W daily log returns
    Z = (rets - rets.mean()) / rets.std(ddof=1)
    C = np.corrcoef(Z.values, rowvar=False)
    w, V = np.linalg.eigh(C)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    wpos = np.clip(w, 0, None)
    evr  = wpos / wpos.sum()
    load = V * np.sqrt(wpos)                            # corr(asset, PC)
    signs = np.sign(load.sum(axis=0)); signs[signs == 0] = 1
    load *= signs
    loadings = pd.DataFrame(load, index=rets.columns,
                            columns=[f"PC{i+1}" for i in range(load.shape[1])])
    p = C.shape[0]
    k = max(1, round(p / 5))
    metrics = dict(
        W=W, p=p, n_obs=rets.shape[0],
        pc1=evr[0], pc2=evr[1], pc3=evr[2],
        AR_k=k, AR=evr[:k].sum(),
        avg_corr=C[np.triu_indices(p, 1)].mean(),
        med_corr=np.median(C[np.triu_indices(p, 1)]),
        Neff=(wpos.sum()**2) / (np.square(wpos).sum()),
        date0=rets.index[0].date(), date1=rets.index[-1].date(),
    )
    return dict(rets=rets, C=C, w=w, evr=evr, loadings=loadings,
                dropped=dropped, metrics=metrics)

R = {W: pca_window(panel, W) for W in (20, 60)}

# ---- console summary --------------------------------------------------------
def fmt(m):
    return (f"window={m['W']:>2}d  n_obs={m['n_obs']:>2}  assets={m['p']:>2}  "
            f"PC1={m['pc1']*100:5.1f}%  PC2={m['pc2']*100:4.1f}%  PC3={m['pc3']*100:4.1f}%  "
            f"AR(top{m['AR_k']})={m['AR']*100:5.1f}%  avg_corr={m['avg_corr']:.3f}  "
            f"Neff={m['Neff']:.1f}  [{m['date0']}->{m['date1']}]")

print("\n================  CROWDING METRICS  ================")
for W in (20, 60):
    print(fmt(R[W]["metrics"]))
    if R[W]["dropped"]:
        print(f"   dropped (insufficient history in {W}d window): {R[W]['dropped']}")

# Per-name PC1 / PC2 / PC3 + communality(3), ranked by |PC1| in the 60d window
def table(W):
    L = R[W]["loadings"][["PC1", "PC2", "PC3"]].copy()
    L["comm3"] = (L**2).sum(axis=1)
    L["sector"] = [SECTORS[i] for i in L.index]
    return L.sort_values("PC1", ascending=False)

for W in (60, 20):
    t = table(W)
    R[W]["loadings"].to_csv(os.path.join(OUTDIR, f"loadings_{W}d.csv"))
    print(f"\n----- {W}d loadings (sorted by PC1) -----")
    print(t.to_string(float_format=lambda x: f"{x:+.3f}"))

# Change in crowding contribution between the two windows (common names)
common = R[20]["loadings"].index.intersection(R[60]["loadings"].index)
chg = pd.DataFrame({
    "PC1_60d": R[60]["loadings"].loc[common, "PC1"],
    "PC1_20d": R[20]["loadings"].loc[common, "PC1"],
})
chg["delta"] = chg["PC1_20d"].abs() - chg["PC1_60d"].abs()
chg["sector"] = [SECTORS[i] for i in chg.index]
chg = chg.sort_values("delta", ascending=False)
chg.to_csv(os.path.join(OUTDIR, "pc1_change_20d_vs_60d.csv"))
print("\n----- |PC1 loading| change: 20d - 60d (crowding IN at top, OUT at bottom) -----")
print(chg.to_string(float_format=lambda x: f"{x:+.3f}"))

# ---- markdown summary -------------------------------------------------------
with open(os.path.join(OUTDIR, "summary.md"), "w") as f:
    f.write("# PCA factor / crowding summary\n\n")
    f.write(f"Panel: {panel.shape[1]} names, US calendar {panel.index[0].date()} -> {panel.index[-1].date()}.\n\n")
    f.write("| window | n_obs | assets | PC1 | PC2 | PC3 | AR(top k) | avg corr | N_eff |\n")
    f.write("|---|---|---|---|---|---|---|---|---|\n")
    for W in (20, 60):
        m = R[W]["metrics"]
        f.write(f"| {m['W']}d | {m['n_obs']} | {m['p']} | {m['pc1']*100:.1f}% | "
                f"{m['pc2']*100:.1f}% | {m['pc3']*100:.1f}% | {m['AR']*100:.1f}% (k={m['AR_k']}) | "
                f"{m['avg_corr']:.3f} | {m['Neff']:.1f} |\n")
    f.write("\n## 60d loadings (sorted by PC1)\n\n```\n")
    f.write(table(60).to_string(float_format=lambda x: f"{x:+.3f}"))
    f.write("\n```\n\n## 20d loadings (sorted by PC1)\n\n```\n")
    f.write(table(20).to_string(float_format=lambda x: f"{x:+.3f}"))
    f.write("\n```\n")

# ---- plots ------------------------------------------------------------------
def scree():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    x = np.arange(1, 13)
    for W, c in [(20, "#888"), (60, "#1f77b4")]:
        ax.bar(x + (0.18 if W == 60 else -0.18), R[W]["evr"][:12] * 100, width=0.36,
               color=c, label=f"{W}d (PC1={R[W]['evr'][0]*100:.0f}%)")
    ax.set_xticks(x); ax.set_xlabel("principal component"); ax.set_ylabel("variance explained (%)")
    ax.set_title("Scree: variance explained by PC — 20d vs 60d")
    ax.legend(); fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "scree.png"), dpi=130); plt.close(fig)

def pc1_bar(W=60):
    L = R[W]["loadings"]["PC1"].sort_values()
    cols = [SECTOR_COLORS[SECTORS[i]] for i in L.index]
    fig, ax = plt.subplots(figsize=(8, 11))
    ax.barh(L.index, L.values, color=cols)
    ax.axvline(0, color="k", lw=.6)
    ax.set_title(f"PC1 loading by name ({W}d)  —  PC1={R[W]['evr'][0]*100:.0f}% of variance\n"
                 "(higher = more crowded into the dominant factor)")
    ax.set_xlabel("PC1 loading  (corr with PC1)")
    handles = [plt.Rectangle((0,0),1,1,color=c) for c in SECTOR_COLORS.values()]
    ax.legend(handles, SECTOR_COLORS.keys(), fontsize=7, ncol=2, loc="lower right")
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, f"pc1_loadings_{W}d.png"), dpi=130); plt.close(fig)

def heatmap(W=60):
    L = R[W]["loadings"][["PC1","PC2","PC3"]].sort_values("PC1", ascending=False)
    fig, ax = plt.subplots(figsize=(5.6, 12))
    norm = TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1)
    im = ax.imshow(L.values, cmap="RdBu_r", norm=norm, aspect="auto")
    ax.set_yticks(range(len(L))); ax.set_yticklabels(L.index, fontsize=8)
    ax.set_xticks(range(3)); ax.set_xticklabels(["PC1","PC2","PC3"])
    for i in range(len(L)):
        for j in range(3):
            ax.text(j, i, f"{L.values[i,j]:+.2f}", ha="center", va="center",
                    fontsize=6, color="k")
    ax.set_title(f"Loadings heatmap ({W}d)")
    fig.colorbar(im, ax=ax, shrink=.5, label="loading")
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, f"heatmap_{W}d.png"), dpi=130); plt.close(fig)

def scatter(W=60):
    L = R[W]["loadings"]
    fig, ax = plt.subplots(figsize=(9, 7.5))
    for sec, c in SECTOR_COLORS.items():
        names = [i for i in L.index if SECTORS[i] == sec]
        if names:
            ax.scatter(L.loc[names,"PC1"], L.loc[names,"PC2"], color=c, label=sec, s=45)
    for i in L.index:
        ax.annotate(i, (L.loc[i,"PC1"], L.loc[i,"PC2"]), fontsize=7,
                    xytext=(3,3), textcoords="offset points")
    ax.axhline(0, color="k", lw=.5); ax.axvline(0, color="k", lw=.5)
    ax.set_xlabel(f"PC1 ({R[W]['evr'][0]*100:.0f}%)  — common 'beta' factor")
    ax.set_ylabel(f"PC2 ({R[W]['evr'][1]*100:.0f}%)  — style/sub-theme spread")
    ax.set_title(f"Factor map: PC1 vs PC2 ({W}d)")
    ax.legend(fontsize=7); fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, f"factor_map_{W}d.png"), dpi=130); plt.close(fig)

scree(); pc1_bar(60); heatmap(60); scatter(60)
print("\nWrote CSVs + PNGs to", OUTDIR)
