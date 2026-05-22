# Momentum-stock screen — 2026-05-22 (NEW entrants only, trend=up)

**Run:** `python daily_screen.py` on the high-recall 8-detector union over the SPY+QQQ universe (502 names).
**Today's tape:** 119 total signals, **86 NEW** vs the 2026-05-21 baseline, 12 dropped.
**Filtered for momentum** (`trend=up`, i.e. above a rising 50-day average and 50dma > 150dma): **49 NEW names**.
**Note:** transcripts skipped per instructions. Drivers below are inferred from the numbers (revenue growth, returns, detector mix) + standard sector context, **not** verified against management commentary.

---

## By sector

### Technology — 20 names · the largest single bucket

The bulk of today's NEW momentum cohort. Three sub-drivers overlap:

- **AI infrastructure / datacenter compute** — HPE (n_det=5, +47% L3M), NTAP (6, +18% L3M), CSCO (4, +55% L3M), ANET (2). HPQ and NTAP are the *highest-detector* names today (n=6 each) — both classic enterprise-IT names whose hardware franchises got re-rated as the AI capex cycle widened beyond pure GPUs into storage / networking / commercial PCs. CSCO's +55% L3M / +97% L12M is the standout — Splunk integration + AI-networking attach.
- **Semiconductors (broad cycle)** — AMD (+105% L3M, +260% L12M), MPWR, AMAT, NXPI, TXN, ON, QCOM, GLW (+314% L12M!), SNPS, SWKS, SMCI, INTC. Even legacy/turnaround names (INTC +132% L3M, +405% L12M; SMCI +33% L1M) are pulling in. SNPS revenue +66% TTM reflects the Ansys deal closing. **Caveat:** at +300–400% L12M (INTC, GLW), most of the upside is now reflected — these signals are momentum-extension, not bottom fishing.
- **Software / security** — CRWD (+38% L3M, beat consensus on the rebound), FTNT (+49% L1M with rev +20% TTM), FFIV (+32% L3M).

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| NTAP | 139.36 | 6 | 4.4% | +16% | +18% | +23% | NetApp |
| HPQ | 25.24 | 6 | 6.9% | +6% | +10% | -24% | HP Inc. |
| HPE | 37.58 | 5 | 18.4% | +28% | +47% | +90% | HP Enterprise |
| CSCO | 120.41 | 4 | 12.0% | +40% | +55% | +97% | Cisco |
| FTNT | 133.93 | 4 | 20.1% | +49% | +44% | +19% | Fortinet |
| NXPI | 316.47 | 4 | 12.2% | +36% | +20% | +41% | NXP Semis |
| SNPS | 524.74 | 4 | 65.5% | +14% | +15% | -3% | Synopsys |
| SWKS | 82.42 | 4 | -1.0% | +17% | +12% | -1% | Skyworks |
| CRWD | 663.46 | 3 | 23.3% | +42% | +38% | +36% | CrowdStrike |
| FFIV | 393.63 | 3 | 11.0% | +18% | +32% | +29% | F5 |
| AMD | 467.51 | 2 | 37.8% | +52% | +105% | +260% | AMD |
| TXN | 309.21 | 2 | 18.6% | +36% | +35% | +66% | Texas Instruments |
| ANET | 154.03 | 2 | 35.1% | -12% | +0% | +45% | Arista |
| INTC | 119.84 | 1 | 7.2% | +59% | +133% | +405% | Intel |
| ON | 116.20 | 1 | 4.7% | +42% | +57% | +150% | onsemi |
| QCOM | 238.16 | 1 | -3.5% | +50% | +44% | +35% | Qualcomm |
| GLW | 194.05 | 1 | 20.0% | +16% | +44% | +314% | Corning |
| MPWR | 1589.81 | 1 | 26.1% | +11% | +33% | +113% | Monolithic Power |
| AMAT | 432.16 | 1 | 11.4% | +12% | +23% | +153% | Applied Materials |
| SMCI | 35.58 | 1 | 122.7% | +33% | +16% | -15% | Super Micro |

### Real Estate — 8 names · rate-sensitive

Almost a clean sweep of the major REIT sub-sectors at once — usually a sign of a rate-driven bid rather than name-specific catalysts. Industrial (PLD, n=4) leads; coastal apartments (ESS, n=3), single-family rental (INVH), strip centers (KIM), open-air (CPT, UDR, DOC), datacenter (EQIX) all firing. The L1M numbers are mostly +5–13% on stocks that were flat or down on L12M (CPT, UDR, INVH, ESS) — a **catch-up trade in a beaten-down sub-sector** rather than fundamental acceleration. EQIX is the cleanest fundamental story (rev +12% TTM, datacenter demand).

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| PLD | 145.90 | 4 | 8.3% | -1% | +2% | +35% | Prologis |
| ESS | 276.70 | 3 | 6.4% | +8% | +8% | -0% | Essex |
| INVH | 29.29 | 2 | 9.2% | +6% | +5% | -13% | Invitation Homes |
| UDR | 38.01 | 2 | 4.2% | +9% | +3% | -2% | UDR |
| KIM | 24.11 | 2 | 4.0% | -3% | +2% | +14% | Kimco |
| CPT | 107.47 | 2 | -0.5% | +5% | +0% | -3% | Camden |
| DOC | 19.73 | 1 | 7.1% | +13% | +17% | +22% | Healthpeak |
| EQIX | 1079.79 | 1 | 12.1% | -3% | +15% | +29% | Equinix |

### Financial Services — 5 names · capital markets + custody

A diversifying set: **trust/custody banks** (BK n=4, NTRS) where fee income + securities-lending balances are at cycle highs; **regional banks** (FITB rev +33% TTM is the outlier — likely benefitted from yield-curve normalization; TFC); **bulge bracket** (GS) where deal/IB activity has been re-accelerating. The fact that the trust banks and GS are *both* firing suggests a capital-markets-up regime tape.

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| BK | 138.98 | 4 | 13.4% | +1% | +15% | +56% | BNY Mellon |
| GS | 996.73 | 2 | 14.5% | +5% | +5% | +58% | Goldman |
| NTRS | 167.77 | 1 | 13.9% | +5% | +13% | +58% | Northern Trust |
| TFC | 48.38 | 1 | 5.2% | -4% | -9% | +19% | Truist |
| FITB | 49.48 | 1 | 33.0% | -4% | -10% | +25% | Fifth Third |

### Consumer Cyclical — 4 names · idiosyncratic, not a sector theme

Mixed bag. **ROST** (n=6, the highest-conviction signal today) — off-price retail, which structurally outperforms when the consumer trades down; classic post-earnings gap-and-go (gap_go + range_expansion both fired). **F** at a new 6-month high suggests the auto-trade rotation. **CZR / MGM** gaming — CZR +53% L3M is the regional-gaming-recovery thesis.

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| ROST | 234.81 | 6 | 12.2% | -4% | +9% | +43% | Ross Stores |
| CZR | 28.47 | 2 | 2.7% | +0% | +53% | -9% | Caesars |
| F | 14.93 | 2 | 6.4% | +9% | -4% | +32% | Ford |
| MGM | 38.40 | 1 | 4.2% | -4% | +8% | +6% | MGM |

### Industrials — 3 names · electrification beneficiaries

All three connect to the **power/grid-electrification + datacenter capex** theme — ETN (electrical components into datacenter & grid), ROK (factory automation + grid-side controls), GNRC (backup power / standby gensets, +27% L1M; +105% L12M is the biggest L12M in the entire cohort outside semis).

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| GNRC | 270.14 | 2 | 12.4% | +27% | +18% | +105% | Generac |
| ROK | 452.29 | 1 | 11.9% | +11% | +14% | +48% | Rockwell |
| ETN | 391.35 | 1 | 16.8% | +2% | +3% | +23% | Eaton |

### Basic Materials — 3 names · steel up, chemicals flat

Heterogeneous. **NUE** rev +21% TTM, +97% L12M — the genuine momentum story (steel cycle + tariff tailwind). **IFF / EMN** are *recovery* breakouts — both have negative revenue growth TTM but L1M positive; mean-reversion off year-long underperformance, not a fundamental acceleration.

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| NUE | 232.00 | 1 | 21.3% | +18% | +24% | +97% | Nucor |
| IFF | 75.28 | 1 | -3.6% | +6% | -8% | +0% | IFF |
| EMN | 74.12 | 1 | -4.9% | -2% | -10% | -7% | Eastman |

### Healthcare — 2 names

**WST** is the clean story (pharma packaging/devices, rev +21% TTM, GLP-1 vial demand). **BIIB** is more of a re-base after years of underperformance — note rev +1.9% TTM, L1M +3%; this is a low-conviction technical signal, not a fundamental acceleration.

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| WST | 316.42 | 1 | 21.0% | +12% | +21% | +47% | West Pharma |
| BIIB | 193.76 | 1 | 1.9% | +3% | -1% | +53% | Biogen |

### Energy — 2 names · oil services + midstream catch-up

Both **catch-up** moves. SLB (oil services) and TRGP (gas midstream) — services bounced after underperforming E&Ps in the prior leg.

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| SLB | 57.28 | 1 | 2.7% | +5% | +12% | +74% | SLB |
| TRGP | 276.75 | 1 | -10.2% | +16% | +20% | +77% | Targa Resources |

### Utilities — 2 names · AI-power demand

LNT and EVRG — both regulated utilities. Utilities firing in a "momentum" screen at all is unusual — likely tied to the **datacenter power-load story** (utilities serving AI-build geographies have been re-rated this cycle). Returns modest (+21% / +31% L12M) so not extended.

| ticker | close | n_det | rev TTM | L1M | L3M | L12M | name |
|---|---|---|---|---|---|---|---|
| LNT | 73.95 | 1 | 5.0% | -2% | +0% | +21% | Alliant |
| EVRG | 83.94 | 1 | 5.0% | +3% | +3% | +31% | Evergy |

---

## Cross-sector themes (recap)

| Theme | Names |
|---|---|
| **AI / datacenter capex** (semis, networking, storage, power, REIT) | AMD, NVDA-adjacent (MPWR, NXPI, AMAT, TXN, ON, GLW, ANET), CSCO, HPE, NTAP, FTNT, CRWD, FFIV, EQIX, ETN, ROK, LNT, EVRG |
| **Rate-sensitive REIT bid** (catch-up) | PLD, ESS, INVH, UDR, KIM, CPT, DOC |
| **Capital markets / custody** | GS, BK, NTRS, FITB |
| **Consumer / retail rotation** | ROST, F, CZR, MGM |
| **Cyclical recovery / mean reversion** | INTC, QCOM, SMCI, IFF, EMN, TRGP, SLB |
| **Health / specialty industrials with secular tailwind** | WST, GNRC, NUE |

## Detector context

Of the 49 momentum names:
- **`trend_continuation`** fired on 25 — these are re-entries off a dip inside an existing uptrend (least surprising; trend already established)
- **`fast_donchian` + `donchian_20`** (classic 10/20-day high break) fired on 19 — broader-base breakouts
- **`six_month_high`** fired on 16 — meaningful resistance taken out
- **`gap_go` / `range_expansion`** fired on 7 — explicit catalyst-driven moves (post-earnings, etc.)

Top-6 most-multi-detector names (best technical confluence): **HPQ, NTAP, ROST** (6), **HPE** (5), **BK, CSCO, FTNT, NXPI, PLD, SNPS, SWKS** (4).

## Dropped vs 2026-05-21

12 names that fired yesterday no longer signal: AMT, AZN, COO, D, DLR, ES, IT, MET, MU, SYY, WBD, WSM. Most likely just signal-cooldown after their breakout day.

---

*Educational analysis based on yfinance data + the project's high-recall breakout detector. Not investment advice. Drivers are inferred — not verified against earnings-call transcripts (skipped per instructions). Past performance does not predict future results.*
