# PCA factor-loading & crowdedness analysis

Cross-section of 35 semis / AI-silicon / semicap / optical / AI-power /
software / mega-cap / consumer names. PCA on the **correlation matrix of daily
log returns** over the last **20** and **60** trading days, to extract the
dominant factors and gauge crowding (factor concentration / co-movement).

## Run

```bash
python3 -m pip install --user numpy pandas matplotlib
python3 fetch_and_pca.py          # uses data/closes.csv cache if present
REFETCH=1 python3 fetch_and_pca.py # force re-download from Yahoo
```

## Method

- **Data**: Yahoo v8 chart API, adjusted closes (split/div-adjusted), `range=1y`.
- **Universe**: 35 names. `SK Hynix=000660.KS`, `Samsung=005930.KS`; the 2 Korean
  names are forward-filled onto the US trading calendar (33 of 35 are US-listed).
- **Returns**: daily log returns; window = last `W` returns (W = 20, 60).
- **PCA**: eigendecomposition of the Pearson correlation matrix of standardized
  returns. Loadings reported = `eigenvector · sqrt(eigenvalue)` = correlation of
  each name with the PC. PC signs flipped so each PC's loadings sum positive.
- **Crowding gauges**: PC1 variance share, absorption ratio (top ~p/5 PCs),
  mean pairwise correlation, effective # of factors (eigenvalue participation
  ratio), and per-name |PC1 loading|.

## Caveats

1. **20d is rank-deficient** (20 obs < 34 names): the correlation matrix has rank
   ≤ 19, so top eigenvalues / PC1 share / absorption ratio are **upward-biased**.
   Use 60d for *levels*; use 20d for *structure / direction of change*. **Mean
   pairwise correlation** is the robust cross-window crowding comparison.
2. **Non-synchronous closes**: Seoul closes ~13–14h before the US, so Samsung /
   SK Hynix correlations with US names are biased low — they split into their own
   component (PC3 in the 60d window). Their *mutual* correlation stays high.
3. **CBRS (Cerebras)** IPO'd 2026-05-14 (only 11 obs) → excluded from both windows.
4. This is **statistical/return crowding** (factor concentration & co-movement),
   not **positioning crowding** (which needs 13F / short-interest / flow data).

## Outputs (`out/`)

`summary.md`, `loadings_{20,60}d.csv`, `pc1_change_20d_vs_60d.csv`,
`scree.png`, `pc1_loadings_60d.png`, `heatmap_60d.png`, `factor_map_60d.png`.
