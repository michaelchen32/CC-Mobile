#!/usr/bin/env python3
"""
Per-sector PCA / crowding: run the same correlation-matrix PCA *within* the
Semiconductor complex and within the SaaS complex, over 20d and 60d windows.

Within-sector PC1 share = how tightly the sector trades as one (crowding);
PC2/PC3 = intra-sector sub-themes (memory vs logic vs equipment; security vs
data/dev vs application). Reads the cached price panel from data/closes.csv.
"""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

HERE   = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, "out", "sector"); os.makedirs(OUTDIR, exist_ok=True)
panel  = pd.read_csv(os.path.join(HERE, "data", "closes.csv"), index_col=0, parse_dates=True)

SEMI = ["MU","SK Hynix","Samsung","SNDK","NVDA","AMD","AVGO","MRVL","CRDO",
        "INTC","QCOM","CBRS","AMAT","LRCX","KLAC"]
SAAS = ["NOW","WDAY","TEAM","HUBS","ADBE","SHOP","CRWD","PANW","DDOG","MDB","U"]

SUB = {**{n:"Memory"   for n in ["MU","SK Hynix","Samsung","SNDK"]},
       **{n:"Logic"    for n in ["NVDA","AMD","AVGO","MRVL","CRDO","INTC","QCOM","CBRS"]},
       **{n:"Equipment"for n in ["AMAT","LRCX","KLAC"]},
       **{n:"Security" for n in ["CRWD","PANW"]},
       **{n:"Data/Dev" for n in ["DDOG","MDB","TEAM","U"]},
       **{n:"App"      for n in ["NOW","WDAY","HUBS","ADBE","SHOP"]}}
COL = {"Memory":"#d62728","Logic":"#1f77b4","Equipment":"#17becf",
       "Security":"#2ca02c","Data/Dev":"#ff7f0e","App":"#9467bd"}

def pca(names, W):
    sub = panel[names].iloc[-(W+1):]
    good = [c for c in sub.columns if sub[c].notna().all()]
    dropped = [c for c in sub.columns if c not in good]
    rets = np.log(sub[good]).diff().iloc[1:]
    Z = (rets - rets.mean())/rets.std(ddof=1)
    C = np.corrcoef(Z.values, rowvar=False)
    w, V = np.linalg.eigh(C); o = np.argsort(w)[::-1]; w, V = w[o], V[:, o]
    wpos = np.clip(w, 0, None); evr = wpos/wpos.sum()
    load = V*np.sqrt(wpos); s = np.sign(load.sum(0)); s[s==0]=1; load*=s
    L = pd.DataFrame(load, index=rets.columns, columns=[f"PC{i+1}" for i in range(load.shape[1])])
    p = C.shape[0]; k = max(1, round(p/5))
    m = dict(W=W, p=p, n=rets.shape[0], pc1=evr[0], pc2=evr[1], pc3=evr[2],
             AR=evr[:k].sum(), k=k, avg_corr=C[np.triu_indices(p,1)].mean(),
             Neff=(wpos.sum()**2)/np.square(wpos).sum(),
             d0=rets.index[0].date(), d1=rets.index[-1].date())
    return dict(evr=evr, L=L, m=m, dropped=dropped)

R = {}
for sec, names in [("Semi", SEMI), ("SaaS", SAAS)]:
    R[sec] = {W: pca(names, W) for W in (20, 60)}

# ---- console + CSV ----------------------------------------------------------
print(f"Panel through {panel.index[-1].date()}\n")
print(f"{'sector':5s} {'win':>4s} {'n':>3s} {'p':>3s}  PC1    PC2    PC3   AR     avg_corr  Neff")
for sec in ("Semi","SaaS"):
    for W in (20,60):
        m = R[sec][W]["m"]
        print(f"{sec:5s} {m['W']:>3d}d {m['n']:>3d} {m['p']:>3d}  "
              f"{m['pc1']*100:4.1f}%  {m['pc2']*100:4.1f}%  {m['pc3']*100:4.1f}%  "
              f"{m['AR']*100:4.1f}%  {m['avg_corr']:+.3f}    {m['Neff']:.1f}   "
              f"[{m['d0']}->{m['d1']}]" + (f"  drop={R[sec][W]['dropped']}" if R[sec][W]['dropped'] else ""))

for sec in ("Semi","SaaS"):
    for W in (60,20):
        L = R[sec][W]["L"][["PC1","PC2","PC3"]].copy()
        L["comm3"] = (L**2).sum(axis=1); L["sub"] = [SUB[i] for i in L.index]
        L = L.sort_values("PC1", ascending=False)
        R[sec][W]["L"].to_csv(os.path.join(OUTDIR, f"{sec.lower()}_loadings_{W}d.csv"))
        print(f"\n----- {sec} {W}d loadings (PC1 sorted, PC1={R[sec][W]['m']['pc1']*100:.0f}%) -----")
        print(L.to_string(float_format=lambda x: f"{x:+.3f}"))

# ---- figures ----------------------------------------------------------------
def scree(sec):
    e20, e60 = R[sec][20]["evr"], R[sec][60]["evr"]
    x = np.arange(1, min(10, len(e60))+1)
    fig, ax = plt.subplots(figsize=(7,4))
    ax.bar(x-0.18, e20[:len(x)]*100, .36, color="#888", label=f"20d (PC1={e20[0]*100:.0f}%)")
    ax.bar(x+0.18, e60[:len(x)]*100, .36, color="#1f77b4", label=f"60d (PC1={e60[0]*100:.0f}%)")
    ax.set_xticks(x); ax.set_xlabel("PC"); ax.set_ylabel("variance explained (%)")
    ax.set_title(f"{sec}: scree (within-sector PCA)"); ax.legend()
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, f"{sec.lower()}_scree.png"), dpi=130); plt.close(fig)

def pc1_bar(sec, W=60):
    L = R[sec][W]["L"]["PC1"].sort_values()
    fig, ax = plt.subplots(figsize=(7, max(3.5, .42*len(L))))
    ax.barh(L.index, L.values, color=[COL[SUB[i]] for i in L.index])
    ax.axvline(0, color="k", lw=.6)
    ax.set_title(f"{sec} — PC1 loading ({W}d), PC1={R[sec][W]['m']['pc1']*100:.0f}% of variance")
    ax.set_xlabel("PC1 loading (corr with sector factor)")
    h = [plt.Rectangle((0,0),1,1,color=COL[s]) for s in COL if any(SUB[i]==s for i in L.index)]
    lab = [s for s in COL if any(SUB[i]==s for i in L.index)]
    ax.legend(h, lab, fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, f"{sec.lower()}_pc1_loadings_{W}d.png"), dpi=130); plt.close(fig)

def heatmap(sec, W=60):
    L = R[sec][W]["L"][["PC1","PC2","PC3"]].sort_values("PC1", ascending=False)
    fig, ax = plt.subplots(figsize=(4.6, max(4, .42*len(L))))
    im = ax.imshow(L.values, cmap="RdBu_r", norm=TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1), aspect="auto")
    ax.set_yticks(range(len(L))); ax.set_yticklabels(L.index, fontsize=8)
    ax.set_xticks(range(3)); ax.set_xticklabels(["PC1","PC2","PC3"])
    for i in range(len(L)):
        for j in range(3):
            ax.text(j, i, f"{L.values[i,j]:+.2f}", ha="center", va="center", fontsize=6.5)
    ax.set_title(f"{sec} loadings ({W}d)"); fig.colorbar(im, ax=ax, shrink=.5)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, f"{sec.lower()}_heatmap_{W}d.png"), dpi=130); plt.close(fig)

def factor_map(sec, W=60):
    L = R[sec][W]["L"]
    fig, ax = plt.subplots(figsize=(7.5, 6))
    for s in COL:
        nm = [i for i in L.index if SUB[i]==s]
        if nm: ax.scatter(L.loc[nm,"PC1"], L.loc[nm,"PC2"], color=COL[s], label=s, s=55)
    for i in L.index:
        ax.annotate(i, (L.loc[i,"PC1"], L.loc[i,"PC2"]), fontsize=8, xytext=(3,3), textcoords="offset points")
    ax.axhline(0, color="k", lw=.5); ax.axvline(0, color="k", lw=.5)
    ax.set_xlabel(f"PC1 ({R[sec][W]['m']['pc1']*100:.0f}%) — sector factor")
    ax.set_ylabel(f"PC2 ({R[sec][W]['m']['pc2']*100:.0f}%) — intra-sector spread")
    ax.set_title(f"{sec}: factor map ({W}d)"); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, f"{sec.lower()}_factor_map_{W}d.png"), dpi=130); plt.close(fig)

for sec in ("Semi","SaaS"):
    scree(sec); pc1_bar(sec); heatmap(sec); factor_map(sec)

# crowding comparison: PC1 share + avg corr, both sectors & windows
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
labels = ["Semi 20d","Semi 60d","SaaS 20d","SaaS 60d"]
pc1 = [R["Semi"][20]["m"]["pc1"], R["Semi"][60]["m"]["pc1"], R["SaaS"][20]["m"]["pc1"], R["SaaS"][60]["m"]["pc1"]]
ac  = [R["Semi"][20]["m"]["avg_corr"], R["Semi"][60]["m"]["avg_corr"], R["SaaS"][20]["m"]["avg_corr"], R["SaaS"][60]["m"]["avg_corr"]]
cols = ["#1f77b4","#1f77b4","#2ca02c","#2ca02c"]
axes[0].bar(labels, [v*100 for v in pc1], color=cols); axes[0].set_title("PC1 variance share (crowding)"); axes[0].set_ylabel("%")
axes[1].bar(labels, ac, color=cols); axes[1].set_title("mean pairwise correlation")
for a in axes:
    for t in a.get_xticklabels(): t.set_rotation(20)
fig.suptitle("Within-sector crowding: Semi vs SaaS")
fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "crowding_compare.png"), dpi=130); plt.close(fig)
print("\nWrote sector figures to", OUTDIR)
