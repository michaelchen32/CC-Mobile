# US Large-Cap Breakout Screen — 2026-07-17

*Universe:* all US-listed stocks with market cap > $10bn (885 names; OHLCV resolved for 885).  
*Method:* the 6 canonical breakout algorithms — Donchian-20, Darvas box, Bollinger squeeze, TTM squeeze, volume-confirmed resistance, and 52-week-high momentum. Any algorithm firing = a signal; `n_det` = how many of the six agree. Trend tag is context only.  
*Reliability note (from the historical study):* **volume resistance** and **52w-high momentum** are the most reliable filters; raw **Donchian-20** fires most often but is the noisiest.  
*Signals this session:* **85** (trend mix — up 64, weak 15, down 6).

## Top conviction (n_det ≥ 3)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Detectors |
|---|---|--:|--:|--:|:--:|:--:|---|
| **ADM** | Archer-Daniels-Midland Company C | $41bn | 85.90 | +3.5% | 4 | up | Donchian-20, Darvas box, Bollinger squeeze, 52w-high momentum |
| **TRV** | The Travelers Companies, Inc. Co | $78bn | 368.98 | +9.2% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |
| **SUN** | Sunoco LP Common Units represent | $15bn | 74.00 | +2.7% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |
| **EG** | Everest Group, Ltd. Common Stock | $15bn | 382.57 | +2.5% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |
| **CTRE** | CareTrust REIT, Inc. Common Stoc | $10bn | 42.88 | +2.2% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |
| **PM** | Philip Morris International Inc  | $301bn | 192.98 | +1.6% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |
| **MO** | Altria Group, Inc. | $124bn | 74.21 | +1.6% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |
| **OHI** | Omega Healthcare Investors, Inc. | $15bn | 50.21 | +0.7% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |
| **FRT** | Federal Realty Investment Trust  | $11bn | 126.02 | +0.5% | 3 | up | Donchian-20, volume resistance, 52w-high momentum |
| **KIM** | Kimco Realty Corporation (HC) Co | $18bn | 26.12 | +0.3% | 3 | up | Donchian-20, Darvas box, 52w-high momentum |

## Signals by sector

### Energy (22)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| SUN | Sunoco LP Common Units represe | $15bn | 74.00 | +2.7% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · +106% rev |
| VG | Venture Global, Inc. Class A c | $34bn | 13.80 | +8.9% | 2 | up | Donchian-20, Bollinger squeeze · +59% rev |
| VLO | Valero Energy Corporation Comm | $92bn | 309.65 | +3.1% | 2 | up | Donchian-20, 52w-high momentum · +7% rev |
| PSX | Phillips 66 Common Stock | $83bn | 206.86 | +2.8% | 2 | up | Donchian-20, 52w-high momentum · +7% rev |
| PR | Permian Resources Corporation  | $17bn | 20.21 | +2.5% | 2 | weak | Donchian-20, Bollinger squeeze · +1% rev |
| MPC | Marathon Petroleum Corporation | $91bn | 312.60 | +2.2% | 2 | up | Donchian-20, 52w-high momentum · +9% rev |
| DINO | HF Sinclair Corporation Common | $16bn | 88.59 | +2.0% | 2 | up | Donchian-20, 52w-high momentum · +12% rev |
| XOM | ExxonMobil Holdings Corporatio | $611bn | 147.36 | +1.0% | 2 | weak | Donchian-20, Bollinger squeeze · +3% rev |
| TRGP | Targa Resources, Inc. Common S | $61bn | 282.91 | +0.9% | 2 | up | Donchian-20, 52w-high momentum · -10% rev |
| PBA | Pembina Pipeline Corp. Ordinar | $30bn | 51.29 | +0.7% | 2 | up | Donchian-20, 52w-high momentum · -8% rev |
| EQNR | Equinor ASA | $93bn | 37.37 | +4.9% | 1 | weak | Donchian-20 · -5% rev |
| SU | Suncor Energy  Inc. Common Sto | $74bn | 62.43 | +2.9% | 1 | weak | Donchian-20 · +18% rev |
| FANG | Diamondback Energy, Inc. Commo | $55bn | 195.54 | +2.9% | 1 | weak | Donchian-20 · +4% rev |
| CNQ | Canadian Natural Resources Lim | $92bn | 43.89 | +2.4% | 1 | weak | Donchian-20 · -1% rev |
| OVV | Ovintiv Inc. (DE) | $16bn | 57.79 | +2.4% | 1 | weak | Donchian-20 · +8% rev |
| BP | BP p.l.c. Common Stock | $110bn | 41.90 | +2.0% | 1 | weak | Donchian-20 · +12% rev |
| CVX | Chevron Corporation Common Sto | $373bn | 187.38 | +1.9% | 1 | weak | Donchian-20 · +2% rev |
| EOG | EOG Resources, Inc. Common Sto | $75bn | 139.89 | +1.8% | 1 | weak | Donchian-20 · +16% rev |
| COP | ConocoPhillips Common Stock | $140bn | 114.71 | +1.7% | 1 | weak | Donchian-20 · -5% rev |
| VNOM | Viper Energy, Inc. Class A Com | $16bn | 44.38 | +0.7% | 1 | weak | Donchian-20 · +109% rev |
| PAA | Plains All American Pipeline,  | $17bn | 23.87 | +0.5% | 1 | up | Donchian-20 · +9% rev |
| ENB | Enbridge Inc Common Stock | $124bn | 56.71 | +0.4% | 1 | up | Donchian-20 · +21% rev |

### Financial Services (14)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| TRV | The Travelers Companies, Inc.  | $78bn | 368.98 | +9.2% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · +0% rev |
| EG | Everest Group, Ltd. Common Sto | $15bn | 382.57 | +2.5% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · -5% rev |
| AFL | AFLAC Incorporated Common Stoc | $63bn | 124.72 | +1.4% | 2 | up | Donchian-20, 52w-high momentum · +28% rev |
| RGA | Reinsurance Group of America,  | $16bn | 241.79 | +0.8% | 2 | up | Donchian-20, 52w-high momentum · +24% rev |
| PRU | Prudential Financial, Inc. Com | $41bn | 119.07 | +0.7% | 2 | up | Donchian-20, 52w-high momentum · +15% rev |
| CM | Canadian Imperial Bank of Comm | $111bn | 121.24 | +0.4% | 2 | up | Donchian-20, 52w-high momentum · +15% rev |
| GL | Globe Life Inc. Common Stock | $14bn | 184.76 | +0.1% | 2 | up | Donchian-20, 52w-high momentum · +5% rev |
| MFC | Manulife Financial Corporation | $72bn | 43.39 | +0.1% | 2 | up | Donchian-20, 52w-high momentum · +12% rev |
| AIG | American International Group,  | $43bn | 80.50 | +3.2% | 1 | up | volume resistance · +1% rev |
| PFG | Principal Financial Group Inc  | $25bn | 113.95 | +0.7% | 1 | up | 52w-high momentum · -4% rev |
| MET | MetLife, Inc. Common Stock | $60bn | 94.00 | +0.3% | 1 | up | 52w-high momentum · +3% rev |
| SLF | Sun Life Financial Inc. Common | $46bn | 81.78 | +0.2% | 1 | up | 52w-high momentum · +0% rev |
| HSBC | HSBC Holdings, plc. Common Sto | $346bn | 100.61 | +0.1% | 1 | up | 52w-high momentum · +3% rev |
| EWBC | East West Bancorp, Inc. Common | $18bn | 134.52 | -1.2% | 1 | up | TTM squeeze · +14% rev |

### Real Estate (13)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| CTRE | CareTrust REIT, Inc. Common St | $10bn | 42.88 | +2.2% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · +3% rev |
| OHI | Omega Healthcare Investors, In | $15bn | 50.21 | +0.7% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · +14% rev |
| FRT | Federal Realty Investment Trus | $11bn | 126.02 | +0.5% | 3 | up | Donchian-20, volume resistance, 52w-high momentum · +10% rev |
| KIM | Kimco Realty Corporation (HC)  | $18bn | 26.12 | +0.3% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · +4% rev |
| VTR | Ventas, Inc. Common Stock | $47bn | 96.10 | +1.1% | 2 | up | Donchian-20, 52w-high momentum · +22% rev |
| AHR | American Healthcare REIT, Inc. | $11bn | 57.16 | +1.0% | 2 | up | Donchian-20, 52w-high momentum · +21% rev |
| WPC | W. P. Carey Inc. REIT | $17bn | 75.86 | +1.0% | 2 | up | Donchian-20, 52w-high momentum · +9% rev |
| DOC | Healthpeak Properties, Inc. Co | $16bn | 22.51 | +0.8% | 2 | up | Donchian-20, 52w-high momentum · +7% rev |
| WELL | Welltower Inc. Common Stock | $172bn | 243.25 | +0.7% | 2 | up | Donchian-20, 52w-high momentum · +38% rev |
| REG | Regency Centers Corporation Co | $15bn | 82.68 | +0.4% | 2 | up | Donchian-20, 52w-high momentum · +10% rev |
| LINE | Lineage, Inc. Common Stock | $10bn | 44.59 | +0.7% | 1 | up | 52w-high momentum · +0% rev |
| SPG | Simon Property Group, Inc. Com | $74bn | 228.70 | +0.1% | 1 | up | 52w-high momentum · +19% rev |
| SUI | Sun Communities, Inc. Common S | $15bn | 121.46 | -0.4% | 1 | down | TTM squeeze · +9% rev |

### Consumer Cyclical (7)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| FIVE | Five Below, Inc. Common Stock | $11bn | 202.63 | +2.5% | 2 | weak | Donchian-20, Bollinger squeeze · +32% rev |
| SN | SharkNinja, Inc. Ordinary Shar | $22bn | 154.53 | +0.2% | 2 | up | Donchian-20, 52w-high momentum · +16% rev |
| MUSA | Murphy USA Inc. Common Stock | $11bn | 618.57 | +3.3% | 1 | up | Donchian-20 · +7% rev |
| AS | Amer Sports, Inc. Ordinary Sha | $20bn | 36.44 | +1.1% | 1 | up | TTM squeeze · +32% rev |
| GIL | Gildan Activewear, Inc. Class  | $10bn | 54.08 | +0.9% | 1 | down | TTM squeeze · +64% rev |
| CCK | Crown Holdings, Inc. | $13bn | 117.21 | +0.2% | 1 | up | Donchian-20 · +13% rev |
| BBY | Best Buy Co., Inc. Common Stoc | $18bn | 85.41 | +0.1% | 1 | up | 52w-high momentum · +2% rev |

### Industrials (7)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| CP | Canadian Pacific Kansas City L | $84bn | 93.71 | +0.9% | 2 | up | Donchian-20, 52w-high momentum · -2% rev |
| UNP | Union Pacific Corporation Comm | $179bn | 301.75 | +0.8% | 2 | up | Donchian-20, 52w-high momentum · +3% rev |
| CNI | Canadian National Railway Comp | $78bn | 129.03 | +0.6% | 2 | up | Donchian-20, 52w-high momentum · -0% rev |
| NSC | Norfolk Southern Corporation C | $76bn | 340.16 | +0.6% | 2 | up | Donchian-20, 52w-high momentum · +0% rev |
| UPS | United Parcel Service, Inc. Co | $100bn | 117.72 | +0.5% | 2 | up | Donchian-20, 52w-high momentum · -2% rev |
| EXPD | Expeditors International of Wa | $24bn | 182.80 | +0.5% | 2 | up | Donchian-20, 52w-high momentum · +4% rev |
| CHRW | C.H. Robinson Worldwide, Inc.  | $25bn | 208.50 | +1.3% | 1 | up | 52w-high momentum · -1% rev |

### Healthcare (6)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| TECH | Bio-Techne Corp Common Stock | $11bn | 72.12 | +0.5% | 2 | up | Donchian-20, 52w-high momentum · -2% rev |
| DVA | DaVita Inc. Common Stock | $15bn | 236.97 | +1.3% | 1 | up | 52w-high momentum · +6% rev |
| SNY | Sanofi ADS | $109bn | 44.66 | +1.0% | 1 | up | Donchian-20 · +6% rev |
| CVS | CVS Health Corporation Common  | $137bn | 107.47 | +0.9% | 1 | up | 52w-high momentum · +6% rev |
| BMY | Bristol-Myers Squibb Company C | $124bn | 60.74 | +0.4% | 1 | up | Donchian-20 · +3% rev |
| IDXX | IDEXX Laboratories, Inc. Commo | $45bn | 567.44 | -1.5% | 1 | down | TTM squeeze · +14% rev |

### Consumer Defensive (5)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| ADM | Archer-Daniels-Midland Company | $41bn | 85.90 | +3.5% | 4 | up | Donchian-20, Darvas box, Bollinger squeeze, 52w-high momentum · +2% rev |
| PM | Philip Morris International In | $301bn | 192.98 | +1.6% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · +9% rev |
| MO | Altria Group, Inc. | $124bn | 74.21 | +1.6% | 3 | up | Donchian-20, Darvas box, 52w-high momentum · +5% rev |
| DAR | Darling Ingredients Inc. Commo | $10bn | 63.10 | +3.1% | 1 | weak | Donchian-20 · +12% rev |
| SFD | Smithfield Foods, Inc. Common  | $10bn | 25.77 | +0.6% | 1 | weak | TTM squeeze · +1% rev |

### Communication Services (5)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| EA | Electronic Arts Inc. Common St | $52bn | 208.90 | +0.5% | 2 | up | Donchian-20, 52w-high momentum · +12% rev |
| ROKU | Roku, Inc. Class A Common Stoc | $21bn | 144.43 | +0.4% | 2 | up | Donchian-20, 52w-high momentum · +22% rev |
| TIGO | Millicom International Cellula | $16bn | 98.34 | +2.9% | 1 | up | 52w-high momentum · +45% rev |
| FOXA | Fox Corporation Class A Common | $24bn | 57.62 | +1.4% | 1 | down | Donchian-20 · -9% rev |
| FOX | Fox Corporation Class B Common | $22bn | 51.63 | +1.1% | 1 | down | Donchian-20 · -9% rev |

### Technology (3)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| PANW | Palo Alto Networks, Inc. Commo | $292bn | 358.68 | +1.3% | 1 | up | 52w-high momentum · +31% rev |
| ADBE | Adobe Inc. Common Stock | $94bn | 237.25 | +0.8% | 1 | down | Donchian-20 · +13% rev |
| AAPL | Apple Inc. Common Stock | $4.90T | 333.74 | +0.1% | 1 | up | 52w-high momentum · +17% rev |

### Utilities (2)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| EMA | Emera Incorporated Common Shar | $17bn | 55.11 | +0.9% | 2 | up | Donchian-20, 52w-high momentum · +5% rev |
| FTS | Fortis Inc. Common Shares | $30bn | 58.78 | +0.2% | 2 | up | Donchian-20, 52w-high momentum · +2% rev |

### Basic Materials (1)

| Ticker | Company | Mkt cap | Close | Day | n_det | Trend | Signal |
|---|---|--:|--:|--:|:--:|:--:|---|
| CTVA | Corteva, Inc. Common Stock | $58bn | 87.30 | +0.8% | 1 | up | 52w-high momentum · +11% rev |

## Fragility flag

20 single-algorithm **raw Donchian-20-only** fires (the noisiest cohort per the study — treat as low-conviction):

`EQNR`, `MUSA`, `DAR`, `SU`, `FANG`, `CNQ`, `OVV`, `BP`, `CVX`, `EOG`, `COP`, `FOXA`, `FOX`, `SNY`, `ADBE`, `VNOM`, `PAA`, `ENB`, `BMY`, `CCK`

---

**Disclaimer.** Educational analysis only — **not investment advice**. Breakout detection is a high-recall/high-false-alarm screen; a signal is a starting point for research, not a recommendation. Prices are auto-adjusted OHLCV from Yahoo Finance and may contain errors. Past performance does not guarantee future results.
