# Fundamental / valuation / earnings dossier

Names that fired in the high-recall screen on the latest bar (2026-05-15). **Source: yfinance only** — the environment blocks all other sites, so literal earnings-call transcript text is not retrievable; the earnings section is a quantitative recap (EPS beat/miss + revenue/margin path) instead. Forward '2026E' = consensus next-fiscal-year (+1y) estimate; TEV/EBITDA & TEV/FCF 26E are estimated as forward revenue x trailing margin (marked _est_). Not investment advice.


## Master table

| ticker | name | sector | n_detectors | trend | rev_growth_TTM_% | net_margin_% | CFO_TTM | FCF_TTM | TEV/Sales_26E | TEV/EBITDA_26E_est | TEV/FCF_26E_est | PE_26E | TEV/Sales_TTM | PE_TTM | L1M_% | L3M_% | L12M_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENPH | Enphase Energy, Inc. | Technology | 6 | weak | -20.6 | 9.6 | 190996992 | 91614248 | 5.1 | 40.0 | 78.3 | 21.7 | 4.8 | 52.4 | 65.5 | 21.6 | 9.6 |
| COST | Costco Wholesale Corporation | Consumer Defensive | 4 | up | 21.5 | 3.0 | 15011000320 | 6690375168 | 1.4 | 30.5 | 61.4 | 46.5 | 1.6 | 54.6 | 6.4 | 3.1 | 6.4 |
| EBAY | eBay Inc. | Consumer Cyclical | 4 | up | 19.5 | 17.6 | 2172999936 | 1124125056 | 4.3 | 17.5 | 44.5 | 17.2 | 4.7 | 26.8 | 13.9 | 41.4 | 70.3 |
| FTNT | Fortinet, Inc. | Technology | 4 | up | 20.1 | 27.5 | 2804400128 | 1813049984 | 10.1 | 30.4 | 39.6 | 35.8 | 12.3 | 47.6 | 49.0 | 43.5 | 18.9 |
| JBHT | J.B. Hunt Transport Services, I | Industrials | 4 | up | 4.6 | 5.1 | 1627117952 | 829849984 | 1.9 | 14.4 | 27.9 | 28.9 | 2.2 | 40.7 | 10.2 | 18.5 | 79.0 |
| TRGP | Targa Resources, Inc. | Energy | 4 | up | -10.2 | 12.9 | 3702500096 | -318550016 | 3.4 | 10.9 |  | 22.8 | 4.7 | 27.8 | 14.0 | 22.1 | 65.0 |
| AIZ | Assurant, Inc. | Financial Services | 3 | up | 11.3 | 7.6 | 1681799936 | 2029737472 | 0.9 | 7.1 | 5.7 | 11.3 | 1.0 | 13.1 | 13.3 | 17.5 | 31.7 |
| CRWD | CrowdStrike Holdings, Inc. | Technology | 3 | up | 23.3 | -3.4 | 1612349056 | 1604615040 | 20.4 |  | 61.1 | 96.3 | 30.4 |  | 42.1 | 38.3 | 36.3 |
| DDOG | Datadog, Inc. | Technology | 3 | up | 32.2 | 3.7 | 1113216000 | 936726528 | 13.5 | 1428.7 | 52.8 | 73.1 | 19.2 | 519.9 | 68.4 | 66.1 | 74.6 |
| OKE | ONEOK, Inc. | Energy | 3 | up | 19.6 | 10.0 | 5629000192 | 454375008 | 2.4 | 11.4 | 188.9 | 14.9 | 2.6 | 16.5 | 9.6 | 8.5 | 12.5 |
| PANW | Palo Alto Networks, Inc. | Technology | 3 | up | 14.9 | 13.0 | 3974000128 | 2859225088 | 14.3 | 92.2 | 49.5 | 105.7 | 19.6 | 134.9 | 45.4 | 45.5 | 27.2 |
| XOM | Exxon Mobil Corporation | Energy | 3 | up | 2.6 | 7.8 | 47722000384 | 11630499840 | 1.9 | 10.9 | 52.4 | 15.2 | 2.1 | 26.6 | 4.6 | 7.1 | 51.6 |
| KMI | Kinder Morgan, Inc. | Energy | 3 | weak | 13.8 | 18.9 | 6246000128 | 1646875008 | 5.9 | 14.0 | 63.3 | 22.0 | 6.2 | 22.6 | 6.8 | 5.0 | 27.5 |
| ZS | Zscaler, Inc. | Technology | 2 | down | 25.9 | -2.3 | 1114038016 | 1020966656 | 6.1 |  | 17.9 | 35.1 | 8.1 |  | 19.9 | -9.4 | -34.1 |
| CSCO | Cisco Systems, Inc. | Technology | 2 | up | 12.0 | 19.7 | 13025000448 | 9671874560 | 7.1 | 25.3 | 44.4 | 24.9 | 7.9 | 39.4 | 39.9 | 54.7 | 97.3 |
| VRSN | VeriSign, Inc. | Technology | 2 | up | 6.6 | 50.0 | 1072200000 | 807275008 |  |  |  | 28.9 | 16.8 | 32.9 | 8.7 | 36.4 | 9.0 |
| WMB | Williams Companies, Inc. (The) | Energy | 2 | up | 9.0 | 23.1 | 6067999744 | -190250000 | 9.3 | 16.5 |  | 30.0 | 10.5 | 34.1 | 9.7 | 8.3 | 37.9 |
| DXCM | DexCom, Inc. | Healthcare | 1 | down | 15.0 | 19.3 | 1782499968 | 1056637504 | 3.9 | 14.5 | 17.8 | 20.2 | 4.7 | 26.5 | 0.7 | -12.0 | -28.8 |
| IT | Gartner, Inc. | Technology | 1 | down | -1.5 | 11.4 | 1367891968 | 1064192896 | 1.7 | 8.3 | 10.4 | 9.5 | 1.8 | 14.4 | -6.0 | -7.8 | -67.2 |
| LW | Lamb Weston Holdings, Inc. | Consumer Defensive | 1 | down | 2.9 | 4.6 | 978600000 | 596987520 | 1.6 | 8.8 | 17.2 | 14.7 | 1.5 | 20.7 | 1.7 | -10.8 | -11.7 |
| AAPL | Apple Inc. | Technology | 1 | up | 16.6 | 27.2 | 140222005248 | 101090746368 | 8.6 | 24.2 | 38.3 | 31.2 | 9.8 | 36.3 | 14.1 | 17.5 | 42.0 |
| APA | APA Corporation | Energy | 1 | up | -11.9 | 18.3 | 4003000064 | 1691250048 | 2.3 | 3.7 | 11.3 | 9.4 | 2.3 | 9.1 | 3.5 | 40.5 | 123.5 |
| COP | ConocoPhillips | Energy | 1 | up | -5.3 | 12.3 | 17976000512 | 5289124864 | 2.5 | 6.4 | 28.3 | 13.6 | 2.8 | 20.7 | 1.4 | 11.5 | 37.8 |
| CZR | Caesars Entertainment, Inc. | Consumer Cyclical | 1 | up | 2.7 | -4.2 | 1288000000 | 752625024 | 2.6 | 8.4 | 39.2 | 33.0 | 2.7 |  | 0.4 | 53.3 | -9.4 |
| DVN | Devon Energy Corporation | Energy | 1 | up | -0.8 | 14.2 | 6424000000 | 1600499968 | 1.4 | 3.3 | 14.0 | 9.1 | 2.4 | 13.8 | 8.1 | 11.4 | 49.5 |
| EOG | EOG Resources, Inc. | Energy | 1 | up | 15.6 | 23.3 | 10721000448 | 2864250112 | 3.0 | 5.7 | 25.0 | 9.7 | 3.4 | 13.8 | 4.6 | 17.1 | 25.7 |
| FANG | Diamondback Energy, Inc. | Energy | 1 | up | 4.2 | 2.0 | 8231000064 | 1397250048 | 4.6 | 6.5 | 47.1 | 12.0 | 5.3 | 207.7 | 9.7 | 21.7 | 45.2 |
| GL | Globe Life Inc. | Financial Services | 1 | up | 5.4 | 19.4 | 1385442048 | 1317225088 | 2.2 | 8.1 | 10.1 | 9.3 | 2.4 | 10.7 | 3.6 | 7.7 | 31.1 |
| HOLX | Hologic, Inc. | Healthcare | 1 | up | 2.5 | 13.2 | 1097699968 | 848612480 | 3.8 | 11.7 | 18.7 | 20.1 | 4.1 | 31.5 | 0.4 | 1.7 | 23.2 |
| HUM | Humana Inc. | Healthcare | 1 | up | 23.5 | 0.8 | 1844000000 | 1431374976 | 0.2 | 6.9 | 16.3 | 19.9 | 0.2 | 32.6 | 52.0 | 66.6 | 34.5 |
| MO | Altria Group, Inc. | Consumer Defensive | 1 | up | 5.3 | 39.5 | 8894000128 | 8542875136 | 7.0 | 9.0 | 16.6 | 12.5 | 7.0 | 15.3 | 12.6 | 10.5 | 38.9 |
| NTAP | NetApp, Inc. | Technology | 1 | up | 4.4 | 18.1 | 1792000000 | 1116000000 | 3.3 | 12.5 | 19.6 | 14.1 | 3.5 | 20.1 | 15.7 | 17.7 | 22.7 |
| OXY | Occidental Petroleum Corporatio | Energy | 1 | up | -8.3 | 22.4 | 9665000448 | 3033374976 | 3.3 | 6.4 | 22.9 | 16.1 | 3.8 | 80.6 | 4.8 | 30.0 | 39.0 |
| SBUX | Starbucks Corporation | Consumer Cyclical | 1 | up | 8.8 | 3.9 | 4345699840 | -1304087552 | 3.7 | 26.7 |  | 35.3 | 3.8 | 81.5 | 9.2 | 14.6 | 27.6 |
| UNP | Union Pacific Corporation | Industrials | 1 | up | 3.2 | 29.2 | 9520000000 | 4034374912 | 7.0 | 13.8 | 43.2 | 19.8 | 7.7 | 22.3 | 7.8 | 4.3 | 21.3 |
| CINF | Cincinnati Financial Corporatio | Financial Services | 1 | weak | 11.6 | 21.3 | 3457999872 | 2748250112 | 2.0 | 7.0 | 9.3 | 18.1 | 2.0 | 9.5 | 1.9 | 2.8 | 16.4 |
| CME | CME Group Inc. | Financial Services | 1 | weak | 14.4 | 63.3 | 4420400128 | 3030237440 | 14.9 | 21.0 | 33.2 | 23.2 | 16.2 | 25.5 | 0.9 | 1.0 | 16.5 |
| MNST | Monster Beverage Corporation | Consumer Defensive | 1 | weak | 26.9 | 23.1 | 2195563008 | 1684340480 | 8.0 | 24.8 | 41.6 | 34.2 | 9.4 | 42.1 | 15.6 | 6.9 | 42.8 |
| ODFL | Old Dominion Freight Line, Inc. | Industrials | 1 | weak | -2.9 | 18.5 | 1407248000 | 861986240 | 6.8 | 21.8 | 43.1 | 32.9 | 7.7 | 42.4 | -4.9 | 5.3 | 19.2 |


## ENPH — Enphase Energy, Inc.  (Technology / Solar)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 2.33B | n/a | 17.0% | 22.3% | 744.8M | 698.4M | 30.0% |
| 2023 | 2.29B | -1.7% | 19.2% | 26.0% | 696.8M | 586.4M | 25.6% |
| 2024 | 1.33B | -41.9% | 7.7% | 15.8% | 513.7M | 480.1M | 36.1% |
| 2025 | 1.47B | 10.7% | 11.7% | 19.7% | 136.5M | 95.9M | 6.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 356.1M | 8.3% | 48.4M | 33.8M |
| 2025-06 | 363.2M | 10.2% | 26.6M | 18.4M |
| 2025-09 | 410.4M | 16.2% | 13.9M | 5.9M |
| 2025-12 | 343.3M | 11.3% | 47.6M | 37.8M |
| 2026-03 | 282.9M | -2.6% | 102.9M | 83.0M |


**2) Valuation:**


- 2026E TEV/Sales: **5.1x**  (TTM 4.8x)
- 2026E TEV/EBITDA _est_: **40.0x**  (TTM 37.1x)
- 2026E TEV/FCF _est_: **78.3x**
- 2026E P/E: **21.7x**  (TTM 52.4x, fwd 21.7x)
- EV 6.65B, 26E rev 1.30B, 26E EPS 2.44x


**3) Performance:**


- L1M 65.5% · L3M 21.6% · L12M 9.6% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, >=5% up-day on >=2x volume, range expansion (>=2x ATR), uptrend continuation off a dip; 1M 65.5%, 3M 21.6%; at/near 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-28 | 0.45 | 0.47 | 5.46 |
| 2026-02-03 | 0.58 | 0.71 | 21.42 |
| 2025-10-28 | 0.25 | 0.5 | 96.19 |
| 2025-07-22 | 0.22 | 0.28 | 28.82 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## COST — Costco Wholesale Corporation  (Consumer Defensive / Discount Stores)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 226.95B | n/a | 2.6% | 4.4% | 7.39B | 3.50B | 1.5% |
| 2023 | 242.29B | 6.8% | 2.6% | 4.4% | 11.07B | 6.75B | 2.8% |
| 2024 | 254.45B | 5.0% | 2.9% | 4.8% | 11.34B | 6.63B | 2.6% |
| 2025 | 275.24B | 8.2% | 2.9% | 4.9% | 13.34B | 7.84B | 2.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-08 | n/a | n/a | n/a | n/a |
| 2024-11 | n/a | n/a | n/a | n/a |
| 2025-02 | 63.72B | 2.8% | 2.75B | 1.61B |
| 2025-05 | 63.20B | 3.0% | 3.46B | 2.33B |
| 2025-08 | 86.16B | 3.0% | 3.87B | 1.90B |
| 2025-11 | 67.31B | 3.0% | 4.69B | 3.16B |
| 2026-02 | 69.60B | 2.9% | 3.00B | 1.71B |


**2) Valuation:**


- 2026E TEV/Sales: **1.4x**  (TTM 1.6x)
- 2026E TEV/EBITDA _est_: **30.5x**  (TTM 34.4x)
- 2026E TEV/FCF _est_: **61.4x**
- 2026E P/E: **46.5x**  (TTM 54.6x, fwd 46.6x)
- EV 463.38B, 26E rev 323.03B, 26E EPS 22.57x


**3) Performance:**


- L1M 6.4% · L3M 3.1% · L12M 6.4% · -0.2% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, volatility-squeeze release; 1M 6.4%, 3M 3.1%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-03-05 | 4.55 | 4.58 | 0.71 |
| 2025-12-11 | 4.28 | 4.5 | 5.21 |
| 2025-09-25 | 5.8 | 5.87 | 1.13 |
| 2025-05-29 | 4.24 | 4.28 | 0.86 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## EBAY — eBay Inc.  (Consumer Cyclical / Internet Retail)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 9.79B | n/a | -13.0% | -9.4% | 2.25B | 1.80B | 18.4% |
| 2023 | 10.11B | 3.2% | 27.4% | 43.2% | 2.43B | 1.97B | 19.5% |
| 2024 | 10.28B | 1.7% | 19.2% | 27.8% | 2.41B | 1.96B | 19.0% |
| 2025 | 11.10B | 7.9% | 18.3% | 26.7% | 1.96B | 1.43B | 12.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 2.58B | 19.3% | 755.0M | 644.0M |
| 2025-06 | 2.73B | 13.5% | -275.0M | -441.0M |
| 2025-09 | 2.82B | 22.4% | 896.0M | 765.0M |
| 2025-12 | 2.96B | 17.8% | 583.0M | 466.0M |
| 2026-03 | 3.09B | 16.6% | 969.0M | 897.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.3x**  (TTM 4.7x)
- 2026E TEV/EBITDA _est_: **17.5x**  (TTM 19.2x)
- 2026E TEV/FCF _est_: **44.5x**
- 2026E P/E: **17.2x**  (TTM 26.8x, fwd 17.2x)
- EV 54.91B, 26E rev 12.73B, 26E EPS 6.76x


**3) Performance:**


- L1M 13.9% · L3M 41.4% · L12M 70.3% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 13.9%, 3M 41.4%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-29 | 1.58 | 1.66 | 5.03 |
| 2026-02-18 | 1.35 | 1.41 | 4.44 |
| 2025-10-29 | 1.33 | 1.36 | 1.9 |
| 2025-07-30 | 1.3 | 1.37 | 5.63 |


_Highlights:_ revenue growth accelerating; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## FTNT — Fortinet, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 4.42B | n/a | 19.4% | 24.4% | 1.73B | 1.45B | 32.8% |
| 2023 | 5.30B | 20.1% | 21.6% | 27.7% | 1.94B | 1.73B | 32.6% |
| 2024 | 5.96B | 12.3% | 29.3% | 37.0% | 2.26B | 1.88B | 31.6% |
| 2025 | 6.80B | 14.2% | 27.3% | 36.1% | 2.59B | 2.23B | 32.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | 1.66B | 31.7% | 477.6M | 380.0M |
| 2025-03 | 1.54B | 28.1% | 863.3M | 796.8M |
| 2025-06 | 1.63B | 27.0% | 451.9M | 284.1M |
| 2025-09 | 1.72B | 27.5% | 655.2M | 567.5M |
| 2025-12 | 1.91B | 26.6% | 620.2M | 577.4M |


**2) Valuation:**


- 2026E TEV/Sales: **10.1x**  (TTM 12.3x)
- 2026E TEV/EBITDA _est_: **30.4x**  (TTM 36.9x)
- 2026E TEV/FCF _est_: **39.6x**
- 2026E P/E: **35.8x**  (TTM 47.6x, fwd 35.8x)
- EV 87.23B, 26E rev 8.63B, 26E EPS 3.43x


**3) Performance:**


- L1M 49.0% · L3M 43.5% · L12M 18.9% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 49.0%, 3M 43.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-06 | 0.62 | 0.82 | 32.63 |
| 2026-02-05 | 0.74 | 0.81 | 8.95 |
| 2025-11-05 | 0.63 | 0.74 | 16.91 |
| 2025-08-06 | 0.59 | 0.64 | 8.27 |


_Highlights:_ revenue growth accelerating; strong FCF margin (32.7%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## JBHT — J.B. Hunt Transport Services, I  (Industrials / Integrated Freight & Logistics)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 14.81B | n/a | 6.5% | 13.3% | 1.78B | 236.1M | 1.6% |
| 2023 | 12.83B | -13.4% | 5.7% | 13.6% | 1.74B | -117.8M | -0.9% |
| 2024 | 12.09B | -5.8% | 4.7% | 13.2% | 1.48B | 617.8M | 5.1% |
| 2025 | 12.00B | -0.7% | 5.0% | 13.2% | 1.68B | 947.6M | 7.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.92B | 4.0% | 404.2M | 158.4M |
| 2025-06 | 2.93B | 4.4% | 402.1M | 185.6M |
| 2025-09 | 3.05B | 5.6% | 486.4M | 352.4M |
| 2025-12 | 3.10B | 5.8% | 385.6M | 251.3M |
| 2026-03 | 3.06B | 4.6% | 353.0M | 242.8M |


**2) Valuation:**


- 2026E TEV/Sales: **1.9x**  (TTM 2.2x)
- 2026E TEV/EBITDA _est_: **14.4x**  (TTM 16.3x)
- 2026E TEV/FCF _est_: **27.9x**
- 2026E P/E: **28.9x**  (TTM 40.7x, fwd 28.9x)
- EV 26.29B, 26E rev 13.79B, 26E EPS 9.06x


**3) Performance:**


- L1M 10.2% · L3M 18.5% · L12M 79.0% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 10.2%, 3M 18.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-15 | 1.45 | 1.49 | 3.09 |
| 2026-01-15 | 1.82 | 1.9 | 4.62 |
| 2025-10-15 | 1.46 | 1.76 | 20.66 |
| 2025-07-15 | 1.3 | 1.31 | 0.9 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## TRGP — Targa Resources, Inc.  (Energy / Oil & Gas Midstream)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 20.93B | n/a | 5.7% | 15.3% | 2.38B | 1.05B | 5.0% |
| 2023 | 16.06B | -23.3% | 8.4% | 24.7% | 3.21B | 826.2M | 5.1% |
| 2024 | 16.38B | 2.0% | 8.0% | 25.2% | 3.65B | 683.9M | 4.2% |
| 2025 | 17.03B | 3.9% | 11.3% | 28.5% | 3.92B | 584.1M | 3.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.56B | 5.9% | 954.4M | 162.2M |
| 2025-06 | 4.26B | 14.8% | 858.3M | -47.8M |
| 2025-09 | 4.15B | 11.5% | 599.2M | -72.6M |
| 2025-12 | 4.06B | 13.4% | 1.51B | 542.3M |
| 2026-03 | 4.09B | 11.7% | 739.5M | -160.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.4x**  (TTM 4.7x)
- 2026E TEV/EBITDA _est_: **10.9x**  (TTM 14.9x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **22.8x**  (TTM 27.8x, fwd 22.8x)
- EV 77.55B, 26E rev 22.68B, 26E EPS 11.95x


**3) Performance:**


- L1M 14.0% · L3M 22.1% · L12M 65.0% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 14.0%, 3M 22.1%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-07 | 2.48 | 2.21 | -10.91 |
| 2026-02-19 | 2.4 | 2.69 | 12.12 |
| 2025-11-05 | 2.13 | 2.2 | 3.06 |
| 2025-08-07 | 1.98 | 2.02 | 2.2 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## AIZ — Assurant, Inc.  (Financial Services / Insurance - Property & Casualty)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 10.19B | n/a | 2.7% | n/a | 596.9M | 410.6M | 4.0% |
| 2023 | 11.13B | 9.2% | 5.8% | n/a | 1.14B | 935.6M | 8.4% |
| 2024 | 11.88B | 6.7% | 6.4% | n/a | 1.33B | 1.11B | 9.4% |
| 2025 | 12.81B | 7.9% | 6.8% | n/a | 1.83B | 1.60B | 12.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | 3.10B | 6.5% | 102.8M | 34.8M |
| 2025-03 | 3.07B | 4.8% | 392.4M | 339.0M |
| 2025-06 | 3.16B | 7.4% | 265.5M | 205.6M |
| 2025-09 | 3.23B | 8.2% | 505.0M | 442.1M |
| 2025-12 | 3.35B | 6.7% | 671.0M | 611.7M |
| 2026-03 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **0.9x**  (TTM 1.0x)
- 2026E TEV/EBITDA _est_: **7.1x**  (TTM 7.9x)
- 2026E TEV/FCF _est_: **5.7x**
- 2026E P/E: **11.3x**  (TTM 13.1x, fwd 11.3x)
- EV 12.90B, 26E rev 14.65B, 26E EPS 22.48x


**3) Performance:**


- L1M 13.3% · L3M 17.5% · L12M 31.7% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 13.3%, 3M 17.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 5.07 | 5.41 | 6.78 |
| 2026-02-10 | 5.5 | 5.61 | 1.94 |
| 2025-11-04 | 4.36 | 5.17 | 18.63 |
| 2025-08-05 | 4.45 | 5.1 | 14.51 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CRWD — CrowdStrike Holdings, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2023 | 2.24B | n/a | -8.2% | -1.8% | 941.0M | 674.6M | 30.1% |
| 2024 | 3.06B | 36.3% | 2.4% | 9.1% | 1.17B | 929.1M | 30.4% |
| 2025 | 3.95B | 29.4% | -0.4% | 7.6% | 1.38B | 1.07B | 27.0% |
| 2026 | 4.81B | 21.7% | -3.4% | 3.8% | 1.61B | 1.24B | 25.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-01 | 1.06B | -8.7% | 345.7M | 240.8M |
| 2025-04 | 1.10B | -10.0% | 384.1M | 280.9M |
| 2025-07 | 1.17B | -6.6% | 332.8M | 285.0M |
| 2025-10 | 1.23B | -2.8% | 397.5M | 297.4M |
| 2026-01 | 1.31B | 4.5% | 497.9M | 378.1M |


**2) Valuation:**


- 2026E TEV/Sales: **20.4x**  (TTM 30.4x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM -3135.2x)
- 2026E TEV/FCF _est_: **61.1x**
- 2026E P/E: **96.3x**  (TTM n/a, fwd 96.3x)
- EV 146.30B, 26E rev 7.18B, 26E EPS 6.17x


**3) Performance:**


- L1M 42.1% · L3M 38.3% · L12M 36.3% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 42.1%, 3M 38.3%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-03-03 | 1.1 | 1.12 | 1.56 |
| 2025-12-02 | 0.94 | 0.96 | 1.98 |
| 2025-08-27 | 0.83 | 0.93 | 12.05 |
| 2025-06-03 | 0.66 | 0.73 | 10.62 |


_Highlights:_ revenue +21.7% latest FY; strong FCF margin (25.8%); beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating; net margin negative (-3.4%); rich valuation (26E P/E 96.3x); high TEV/Sales 26E (20.4x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DDOG — Datadog, Inc.  (Technology / Software - Application)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 1.68B | n/a | -3.0% | 0.8% | 418.4M | 353.5M | 21.1% |
| 2023 | 2.13B | 27.1% | 2.3% | 5.2% | 660.0M | 597.5M | 28.1% |
| 2024 | 2.68B | 26.1% | 6.8% | 9.9% | 870.6M | 775.1M | 28.9% |
| 2025 | 3.43B | 27.7% | 3.1% | 5.7% | 1.05B | 914.7M | 26.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 761.6M | 3.2% | 271.5M | 244.4M |
| 2025-06 | 826.8M | 0.3% | 200.1M | 165.4M |
| 2025-09 | 885.7M | 3.8% | 251.5M | 214.0M |
| 2025-12 | 953.2M | 4.9% | 327.1M | 291.0M |
| 2026-03 | 1.01B | 5.2% | 334.6M | 289.1M |


**2) Valuation:**


- 2026E TEV/Sales: **13.5x**  (TTM 19.2x)
- 2026E TEV/EBITDA _est_: **1428.7x**  (TTM 2037.0x)
- 2026E TEV/FCF _est_: **52.8x**
- 2026E P/E: **73.1x**  (TTM 519.9x, fwd 73.1x)
- EV 70.56B, 26E rev 5.24B, 26E EPS 2.84x


**3) Performance:**


- L1M 68.4% · L3M 66.1% · L12M 74.6% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 68.4%, 3M 66.1%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-07 | 0.51 | 0.6 | 18.25 |
| 2026-02-10 | 0.55 | 0.59 | 6.33 |
| 2025-11-06 | 0.46 | 0.55 | 20.33 |
| 2025-08-07 | 0.41 | 0.46 | 12.84 |


_Highlights:_ revenue +27.7% latest FY; revenue growth accelerating; strong FCF margin (26.7%); beat EPS all last 4 quarters


_Issues:_ rich valuation (26E P/E 73.1x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## OKE — ONEOK, Inc.  (Energy / Oil & Gas Midstream)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 22.39B | n/a | 7.7% | 15.9% | 2.91B | 1.70B | 7.6% |
| 2023 | 17.68B | -21.0% | 15.0% | 29.0% | 4.42B | 2.83B | 16.0% |
| 2024 | 21.70B | 22.7% | 14.0% | 30.5% | 4.89B | 2.87B | 13.2% |
| 2025 | 33.63B | 55.0% | 10.1% | 23.2% | 5.60B | 2.45B | 7.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 8.04B | 7.9% | 904.0M | 275.0M |
| 2025-06 | 7.89B | 10.7% | 1.52B | 776.0M |
| 2025-09 | 8.63B | 10.9% | 1.62B | 820.0M |
| 2025-12 | 9.06B | 10.8% | 1.55B | 576.0M |
| 2026-03 | 9.62B | 8.0% | 934.0M | 70.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.4x**  (TTM 2.6x)
- 2026E TEV/EBITDA _est_: **11.4x**  (TTM 12.2x)
- 2026E TEV/FCF _est_: **188.9x**
- 2026E P/E: **14.9x**  (TTM 16.5x, fwd 14.9x)
- EV 91.78B, 26E rev 37.63B, 26E EPS 6.20x


**3) Performance:**


- L1M 9.6% · L3M 8.5% · L12M 12.5% · -0.6% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, uptrend continuation off a dip; 1M 9.6%, 3M 8.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-28 | 1.3 | 1.3 | 0.14 |
| 2026-02-23 | 1.49 | 1.55 | 3.85 |
| 2025-10-28 | 1.45 | 1.49 | 2.45 |
| 2025-08-04 | 1.33 | 1.34 | 1.11 |


_Highlights:_ revenue +55.0% latest FY; revenue growth accelerating; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## PANW — Palo Alto Networks, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.50B | n/a | -4.9% | 1.7% | 1.98B | 1.79B | 32.6% |
| 2023 | 6.89B | 25.3% | 6.4% | 12.6% | 2.78B | 2.63B | 38.2% |
| 2024 | 8.03B | 16.5% | 32.1% | 15.9% | 3.26B | 3.10B | 38.6% |
| 2025 | 9.22B | 14.9% | 12.3% | 21.0% | 3.72B | 3.47B | 37.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-10 | n/a | n/a | n/a | n/a |
| 2025-01 | 2.26B | 11.8% | 557.0M | 509.0M |
| 2025-04 | 2.29B | 11.5% | 628.2M | 560.3M |
| 2025-07 | 2.54B | 10.0% | 1.02B | 934.5M |
| 2025-10 | 2.47B | 13.5% | 1.77B | 1.69B |
| 2026-01 | 2.59B | 16.7% | 554.0M | 384.0M |


**2) Valuation:**


- 2026E TEV/Sales: **14.3x**  (TTM 19.6x)
- 2026E TEV/EBITDA _est_: **92.2x**  (TTM 126.3x)
- 2026E TEV/FCF _est_: **49.5x**
- 2026E P/E: **105.7x**  (TTM 134.9x, fwd 61.2x)
- EV 194.07B, 26E rev 13.55B, 26E EPS 2.30x


**3) Performance:**


- L1M 45.4% · L3M 45.5% · L12M 27.2% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 45.4%, 3M 45.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-02-17 | 0.94 | 1.03 | 9.94 |
| 2025-11-19 | 0.89 | 0.93 | 4.36 |
| 2025-08-18 | 0.89 | 0.95 | 7.31 |
| 2025-05-20 | 0.77 | 0.8 | 3.59 |


_Highlights:_ strong FCF margin (37.6%); beat EPS all last 4 quarters


_Issues:_ rich valuation (26E P/E 105.7x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## XOM — Exxon Mobil Corporation  (Energy / Oil & Gas Integrated)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 398.68B | n/a | 14.0% | 25.7% | 76.80B | 58.39B | 14.6% |
| 2023 | 334.70B | -16.0% | 10.8% | 22.2% | 55.37B | 33.45B | 10.0% |
| 2024 | 339.25B | 1.4% | 9.9% | 21.6% | 55.02B | 30.72B | 9.1% |
| 2025 | 323.90B | -4.5% | 8.9% | 21.0% | 51.97B | 23.61B | 7.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 81.06B | 9.5% | 12.95B | 7.05B |
| 2025-06 | 79.48B | 8.9% | 11.55B | 5.27B |
| 2025-09 | 83.33B | 9.1% | 14.79B | 6.06B |
| 2025-12 | 80.04B | 8.1% | 12.68B | 5.23B |
| 2026-03 | 83.16B | 5.0% | 8.71B | 2.23B |


**2) Valuation:**


- 2026E TEV/Sales: **1.9x**  (TTM 2.1x)
- 2026E TEV/EBITDA _est_: **10.9x**  (TTM 12.5x)
- 2026E TEV/FCF _est_: **52.4x**
- 2026E P/E: **15.2x**  (TTM 26.6x, fwd 15.2x)
- EV 700.41B, 26E rev 374.93B, 26E EPS 10.38x


**3) Performance:**


- L1M 4.6% · L3M 7.1% · L12M 51.6% · -7.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, uptrend continuation off a dip; 1M 4.6%, 3M 7.1%; -7.3% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-01 | 0.89 | 1.0 | 12.52 |
| 2026-01-30 | 1.66 | 1.53 | -7.67 |
| 2025-10-31 | 1.79 | 1.76 | -1.59 |
| 2025-08-01 | 1.56 | 1.64 | 4.93 |


_Highlights:_ beat EPS 2/4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## KMI — Kinder Morgan, Inc.  (Energy / Oil & Gas Midstream)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 19.20B | n/a | 13.3% | 32.6% | 4.97B | 3.35B | 17.4% |
| 2023 | 15.33B | -20.1% | 15.6% | 42.5% | 6.49B | 4.17B | 27.2% |
| 2024 | 15.10B | -1.5% | 17.3% | 44.6% | 5.63B | 3.01B | 19.9% |
| 2025 | 16.94B | 12.2% | 18.0% | 42.4% | 5.92B | 2.89B | 17.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.24B | 16.9% | 1.16B | 396.0M |
| 2025-06 | 4.04B | 17.7% | 1.65B | 1.00B |
| 2025-09 | 4.15B | 15.1% | 1.41B | 621.0M |
| 2025-12 | 4.51B | 22.1% | 1.69B | 872.0M |
| 2026-03 | 4.83B | 20.2% | 1.49B | 687.0M |


**2) Valuation:**


- 2026E TEV/Sales: **5.9x**  (TTM 6.2x)
- 2026E TEV/EBITDA _est_: **14.0x**  (TTM 14.6x)
- 2026E TEV/FCF _est_: **63.3x**
- 2026E P/E: **22.0x**  (TTM 22.6x, fwd 22.0x)
- EV 108.21B, 26E rev 18.19B, 26E EPS 1.53x


**3) Performance:**


- L1M 6.8% · L3M 5.0% · L12M 27.5% · -0.4% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, uptrend continuation off a dip; 1M 6.8%, 3M 5.0%; at/near 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-22 | 0.39 | 0.48 | 22.1 |
| 2026-01-21 | 0.36 | 0.45 | 23.85 |
| 2025-10-22 | 0.3 | 0.29 | -2.84 |
| 2025-07-16 | 0.28 | 0.28 | 0.81 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (17.1%); beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ZS — Zscaler, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 1.09B | n/a | -35.8% | -25.4% | 321.9M | 231.3M | 21.2% |
| 2023 | 1.62B | 48.2% | -12.5% | -6.8% | 462.3M | 333.6M | 20.6% |
| 2024 | 2.17B | 34.1% | -2.7% | 3.0% | 779.8M | 585.0M | 27.0% |
| 2025 | 2.67B | 23.3% | -1.6% | 4.0% | 972.5M | 726.7M | 27.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-01 | 647.9M | -1.2% | 179.4M | 143.4M |
| 2025-04 | 678.0M | -0.6% | 211.1M | 119.5M |
| 2025-07 | 719.2M | -2.4% | 250.6M | 171.9M |
| 2025-10 | 788.1M | -1.5% | 448.3M | 413.3M |
| 2026-01 | 815.8M | -4.2% | 204.1M | 169.1M |


**2) Valuation:**


- 2026E TEV/Sales: **6.1x**  (TTM 8.1x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM -356.5x)
- 2026E TEV/FCF _est_: **17.9x**
- 2026E P/E: **35.1x**  (TTM n/a, fwd 35.1x)
- EV 24.25B, 26E rev 3.97B, 26E EPS 4.59x


**3) Performance:**


- L1M 19.9% · L3M -9.4% · L12M -34.1% · -52.1% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 19.9%, 3M -9.4%; -52.1% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-02-26 | 0.9 | 1.01 | 12.56 |
| 2025-11-25 | -0.11 | -0.07 | 36.73 |
| 2025-09-02 | 0.8 | 0.89 | 11.03 |
| 2025-05-29 | 0.76 | 0.84 | 10.78 |


_Highlights:_ revenue +23.3% latest FY; strong FCF margin (27.2%); beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating; net margin negative (-1.6%)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CSCO — Cisco Systems, Inc.  (Technology / Communication Equipment)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 51.56B | n/a | 22.9% | 32.6% | 13.23B | 12.75B | 24.7% |
| 2023 | 57.00B | 10.6% | 22.1% | 30.7% | 19.89B | 19.04B | 33.4% |
| 2024 | 53.80B | -5.6% | 19.2% | 29.3% | 10.88B | 10.21B | 19.0% |
| 2025 | 56.65B | 5.3% | 18.0% | 27.4% | 14.19B | 13.29B | 23.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-01 | 13.99B | 17.4% | 2.24B | 2.03B |
| 2025-04 | 14.15B | 17.6% | 4.06B | 3.80B |
| 2025-07 | 14.67B | 17.4% | 4.23B | 4.02B |
| 2025-10 | 14.88B | 19.2% | 3.21B | 2.89B |
| 2026-01 | 15.35B | 20.7% | 1.82B | 1.54B |


**2) Valuation:**


- 2026E TEV/Sales: **7.1x**  (TTM 7.9x)
- 2026E TEV/EBITDA _est_: **25.3x**  (TTM 28.4x)
- 2026E TEV/FCF _est_: **44.4x**
- 2026E P/E: **24.9x**  (TTM 39.4x, fwd 24.9x)
- EV 481.83B, 26E rev 68.11B, 26E EPS 4.75x


**3) Performance:**


- L1M 39.9% · L3M 54.7% · L12M 97.3% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high, uptrend continuation off a dip; 1M 39.9%, 3M 54.7%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-13 | 1.04 | 1.06 | 2.29 |
| 2026-02-11 | 1.02 | 1.04 | 1.75 |
| 2025-11-12 | 0.98 | 1.0 | 1.82 |
| 2025-08-13 | 0.98 | 0.99 | 1.3 |


_Highlights:_ revenue growth accelerating; strong FCF margin (23.5%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## VRSN — VeriSign, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 1.42B | n/a | 47.3% | 70.3% | 831.1M | 803.7M | 56.4% |
| 2023 | 1.49B | 4.8% | 54.8% | 73.4% | 853.8M | 808.0M | 54.1% |
| 2024 | 1.56B | 4.3% | 50.4% | 72.8% | 902.6M | 874.5M | 56.2% |
| 2025 | 1.66B | 6.4% | 49.8% | 71.0% | 1.09B | 1.07B | 64.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 402.3M | 49.5% | 291.3M | 285.5M |
| 2025-06 | 409.9M | 50.6% | 202.5M | 194.7M |
| 2025-09 | 419.1M | 50.8% | 307.7M | 303.0M |
| 2025-12 | 425.3M | 48.5% | 289.6M | 285.1M |
| 2026-03 | 428.9M | 50.0% | 272.4M | 265.2M |


**2) Valuation:**


- 2026E TEV/Sales: **n/a**  (TTM 16.8x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM 24.2x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **28.9x**  (TTM 32.9x, fwd 27.9x)
- EV 28.32B, 26E rev 0, 26E EPS 10.31x


**3) Performance:**


- L1M 8.7% · L3M 36.4% · L12M 9.0% · -1.8% from 12-mo high


**4) Reason for breakout:**


new 6-month high, uptrend continuation off a dip; 1M 8.7%, 3M 36.4%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-23 | 2.25 | 2.34 | 4.2 |
| 2026-02-05 | 2.29 | 2.23 | -2.44 |
| 2025-10-23 | 2.25 | 2.27 | 0.92 |
| 2025-07-24 | 2.2 | 2.21 | 0.59 |


_Highlights:_ revenue growth accelerating; strong FCF margin (64.5%); beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## WMB — Williams Companies, Inc. (The)  (Energy / Oil & Gas Midstream)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 10.96B | n/a | 18.7% | 52.0% | 4.89B | 2.61B | 23.8% |
| 2023 | 10.91B | -0.5% | 29.1% | 70.7% | 5.94B | 3.37B | 30.9% |
| 2024 | 10.50B | -3.7% | 21.2% | 62.5% | 4.97B | 2.30B | 21.9% |
| 2025 | 11.95B | 13.8% | 21.9% | 62.0% | 5.90B | 899.0M | 7.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.05B | 22.7% | 1.43B | 421.0M |
| 2025-06 | 2.78B | 19.6% | 1.45B | 438.0M |
| 2025-09 | 2.92B | 22.1% | 1.44B | 445.0M |
| 2025-12 | 3.20B | 23.0% | 1.58B | -405.0M |
| 2026-03 | 3.03B | 28.5% | 1.60B | 244.0M |


**2) Valuation:**


- 2026E TEV/Sales: **9.3x**  (TTM 10.5x)
- 2026E TEV/EBITDA _est_: **16.5x**  (TTM 18.6x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **30.0x**  (TTM 34.1x, fwd 30.0x)
- EV 126.61B, 26E rev 13.60B, 26E EPS 2.59x


**3) Performance:**


- L1M 9.7% · L3M 8.3% · L12M 37.9% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high, uptrend continuation off a dip; 1M 9.7%, 3M 8.3%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-04 | 0.62 | 0.73 | 17.2 |
| 2026-02-10 | 0.56 | 0.55 | -1.37 |
| 2025-11-03 | 0.54 | 0.53 | -1.03 |
| 2025-08-04 | 0.49 | 0.46 | -5.99 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS 1/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DXCM — DexCom, Inc.  (Healthcare / Medical Devices)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 2.91B | n/a | 11.7% | 19.4% | 669.5M | 304.7M | 10.5% |
| 2023 | 3.62B | 24.5% | 14.9% | 25.3% | 748.5M | 511.9M | 14.1% |
| 2024 | 4.03B | 11.3% | 14.3% | 23.4% | 989.5M | 630.7M | 15.6% |
| 2025 | 4.66B | 15.6% | 17.9% | 29.1% | 1.44B | 1.08B | 23.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 1.04B | 10.2% | 183.8M | 96.8M |
| 2025-06 | 1.16B | 15.5% | 303.0M | 208.9M |
| 2025-09 | 1.21B | 23.5% | 659.9M | 579.4M |
| 2025-12 | 1.26B | 21.2% | 294.0M | 192.1M |
| 2026-03 | 1.19B | 16.7% | 525.6M | 449.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.9x**  (TTM 4.7x)
- 2026E TEV/EBITDA _est_: **14.5x**  (TTM 17.6x)
- 2026E TEV/FCF _est_: **17.8x**
- 2026E P/E: **20.2x**  (TTM 26.5x, fwd 20.2x)
- EV 22.75B, 26E rev 5.84B, 26E EPS 3.05x


**3) Performance:**


- L1M 0.7% · L3M -12.0% · L12M -28.8% · -31.2% from 12-mo high


**4) Reason for breakout:**


gap-up and held; 1M 0.7%, 3M -12.0%; -31.2% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-30 | 0.47 | 0.56 | 18.99 |
| 2026-02-12 | 0.65 | 0.68 | 4.5 |
| 2025-10-30 | 0.57 | 0.61 | 7.51 |
| 2025-07-30 | 0.44 | 0.48 | 8.25 |


_Highlights:_ revenue +15.6% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (23.1%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## IT — Gartner, Inc.  (Technology / Information Technology Services)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.48B | n/a | 14.8% | 24.6% | 1.10B | 993.4M | 18.1% |
| 2023 | 5.91B | 7.9% | 14.9% | 24.9% | 1.16B | 1.05B | 17.8% |
| 2024 | 6.27B | 6.1% | 20.0% | 27.5% | 1.48B | 1.38B | 22.1% |
| 2025 | 6.50B | 3.7% | 11.2% | 19.9% | 1.29B | 1.18B | 18.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.53B | 13.7% | 313.5M | 287.9M |
| 2025-06 | 1.69B | 14.3% | 383.6M | 347.3M |
| 2025-09 | 1.52B | 2.3% | 298.7M | 269.3M |
| 2025-12 | 1.75B | 13.8% | 294.5M | 270.7M |
| 2026-03 | 1.51B | 14.7% | 391.0M | 370.6M |


**2) Valuation:**


- 2026E TEV/Sales: **1.7x**  (TTM 1.8x)
- 2026E TEV/EBITDA _est_: **8.3x**  (TTM 8.6x)
- 2026E TEV/FCF _est_: **10.4x**
- 2026E P/E: **9.5x**  (TTM 14.4x, fwd 9.5x)
- EV 11.48B, 26E rev 6.74B, 26E EPS 15.34x


**3) Performance:**


- L1M -6.0% · L3M -7.8% · L12M -67.2% · -67.5% from 12-mo high


**4) Reason for breakout:**


gap-up and held; 1M -6.0%, 3M -7.8%; -67.5% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 2.72 | 3.18 | 16.75 |
| 2026-02-03 | 3.51 | 3.94 | 12.21 |
| 2025-11-04 | 2.12 | 0.47 | -77.88 |
| 2025-08-05 | 3.31 | 3.53 | 6.8 |


_Highlights:_ strong FCF margin (18.1%); beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## LW — Lamb Weston Holdings, Inc.  (Consumer Defensive / Packaged Foods)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 4.10B | n/a | 4.9% | 15.5% | 418.6M | 128.5M | 3.1% |
| 2023 | 5.35B | 30.5% | 18.9% | 20.7% | 761.7M | 107.7M | 2.0% |
| 2024 | 6.47B | 20.9% | 11.2% | 21.2% | 798.2M | -131.3M | -2.0% |
| 2025 | 6.45B | -0.3% | 5.5% | 16.6% | 868.3M | 230.1M | 3.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-11 | n/a | n/a | n/a | n/a |
| 2025-02 | 1.52B | 9.6% | 56.0M | -19.8M |
| 2025-05 | 1.68B | 7.2% | 383.0M | 295.2M |
| 2025-08 | 1.66B | 3.9% | 352.0M | 274.4M |
| 2025-11 | 1.62B | 3.8% | 178.4M | 101.0M |
| 2026-02 | 1.56B | 3.5% | 65.2M | -36.3M |


**2) Valuation:**


- 2026E TEV/Sales: **1.6x**  (TTM 1.5x)
- 2026E TEV/EBITDA _est_: **8.8x**  (TTM 8.6x)
- 2026E TEV/FCF _est_: **17.2x**
- 2026E P/E: **14.7x**  (TTM 20.7x, fwd 14.7x)
- EV 10.05B, 26E rev 6.37B, 26E EPS 3.00x


**3) Performance:**


- L1M 1.7% · L3M -10.8% · L12M -11.7% · -32.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M 1.7%, 3M -10.8%; -32.3% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-01 | 0.61 | 0.72 | 17.42 |
| 2025-12-19 | 0.65 | 0.69 | 6.36 |
| 2025-09-30 | 0.53 | 0.74 | 38.71 |
| 2025-07-23 | 0.63 | 0.87 | 38.23 |


_Highlights:_ beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## AAPL — Apple Inc.  (Technology / Consumer Electronics)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 394.33B | n/a | 25.3% | 33.1% | 122.15B | 111.44B | 28.3% |
| 2023 | 383.29B | -2.8% | 25.3% | 32.8% | 110.54B | 99.58B | 26.0% |
| 2024 | 391.04B | 2.0% | 24.0% | 34.4% | 118.25B | 108.81B | 27.8% |
| 2025 | 416.16B | 6.4% | 26.9% | 34.8% | 111.48B | 98.77B | 23.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 95.36B | 26.0% | 23.95B | 20.88B |
| 2025-06 | 94.04B | 24.9% | 27.87B | 24.41B |
| 2025-09 | 102.47B | 26.8% | 29.73B | 26.49B |
| 2025-12 | 143.76B | 29.3% | 53.92B | 51.55B |
| 2026-03 | 111.18B | 26.6% | 28.70B | 26.73B |


**2) Valuation:**


- 2026E TEV/Sales: **8.6x**  (TTM 9.8x)
- 2026E TEV/EBITDA _est_: **24.2x**  (TTM 27.7x)
- 2026E TEV/FCF _est_: **38.3x**
- 2026E P/E: **31.2x**  (TTM 36.3x, fwd 31.3x)
- EV 4425.79B, 26E rev 516.63B, 26E EPS 9.63x


**3) Performance:**


- L1M 14.1% · L3M 17.5% · L12M 42.0% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 14.1%, 3M 17.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-30 | 1.94 | 2.01 | 3.46 |
| 2026-01-29 | 2.67 | 2.84 | 6.25 |
| 2025-10-30 | 1.77 | 1.85 | 4.52 |
| 2025-07-31 | 1.43 | 1.57 | 9.48 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (23.7%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## APA — APA Corporation  (Energy / Oil & Gas E&P)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 11.07B | n/a | 32.5% | 65.7% | 4.94B | 2.54B | 23.0% |
| 2023 | 8.28B | -25.2% | 34.5% | 57.4% | 3.13B | 772.0M | 9.3% |
| 2024 | 9.74B | 17.6% | 8.3% | 42.9% | 3.62B | 709.0M | 7.3% |
| 2025 | 8.92B | -8.4% | 16.1% | 60.2% | 4.54B | 1.78B | 19.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | 2.71B | 13.1% | 1.04B | 342.0M |
| 2025-03 | 2.64B | 13.2% | 1.10B | 306.0M |
| 2025-06 | 2.18B | 27.7% | 1.18B | 514.0M |
| 2025-09 | 2.12B | 9.7% | 1.46B | 741.0M |
| 2025-12 | 1.99B | 14.0% | 808.0M | 218.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.3x**  (TTM 2.3x)
- 2026E TEV/EBITDA _est_: **3.7x**  (TTM 3.6x)
- 2026E TEV/FCF _est_: **11.3x**
- 2026E P/E: **9.4x**  (TTM 9.1x, fwd 9.4x)
- EV 18.96B, 26E rev 8.28B, 26E EPS 4.15x


**3) Performance:**


- L1M 3.5% · L3M 40.5% · L12M 123.5% · -11.6% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 3.5%, 3M 40.5%; -11.6% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-06 | 1.14 | 1.38 | 20.9 |
| 2026-02-25 | 0.64 | 0.91 | 41.73 |
| 2025-11-05 | 0.79 | 0.93 | 17.59 |
| 2025-08-05 | 0.52 | 1.67 | 220.64 |


_Highlights:_ net margin expanding; strong FCF margin (19.9%); beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## COP — ConocoPhillips  (Energy / Oil & Gas E&P)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 78.49B | n/a | 23.8% | 47.3% | 28.31B | 18.16B | 23.1% |
| 2023 | 56.14B | -28.5% | 19.5% | 45.9% | 19.96B | 8.72B | 15.5% |
| 2024 | 54.74B | -2.5% | 16.9% | 44.6% | 20.12B | 8.01B | 14.6% |
| 2025 | 58.94B | 7.7% | 13.6% | 43.4% | 19.80B | 7.24B | 12.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 16.52B | 17.2% | 6.12B | 2.74B |
| 2025-06 | 14.00B | 14.1% | 3.48B | 199.0M |
| 2025-09 | 15.03B | 11.5% | 5.88B | 3.01B |
| 2025-12 | 13.39B | 10.8% | 4.32B | 1.29B |
| 2026-03 | 15.76B | 13.9% | 4.29B | 1.35B |


**2) Valuation:**


- 2026E TEV/Sales: **2.5x**  (TTM 2.8x)
- 2026E TEV/EBITDA _est_: **6.4x**  (TTM 7.1x)
- 2026E TEV/FCF _est_: **28.3x**
- 2026E P/E: **13.6x**  (TTM 20.7x, fwd 13.7x)
- EV 166.10B, 26E rev 65.94B, 26E EPS 8.98x


**3) Performance:**


- L1M 1.4% · L3M 11.5% · L12M 37.8% · -7.8% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 1.4%, 3M 11.5%; -7.8% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-30 | 1.69 | 1.89 | 11.55 |
| 2026-02-05 | 1.09 | 1.02 | -6.47 |
| 2025-11-06 | 1.41 | 1.61 | 14.05 |
| 2025-08-07 | 1.36 | 1.42 | 4.71 |


_Highlights:_ revenue growth accelerating; beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CZR — Caesars Entertainment, Inc.  (Consumer Cyclical / Resorts & Casinos)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 10.82B | n/a | -8.3% | 27.0% | 975.0M | 12.0M | 0.1% |
| 2023 | 11.53B | 6.5% | 6.8% | 30.8% | 1.81B | 515.0M | 4.5% |
| 2024 | 11.24B | -2.5% | -2.5% | 31.8% | 1.07B | -236.0M | -2.1% |
| 2025 | 11.49B | 2.1% | -4.4% | 28.7% | 1.30B | 493.0M | 4.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.79B | -4.1% | 218.0M | -5.0M |
| 2025-06 | 2.91B | -2.8% | 462.0M | 232.0M |
| 2025-09 | 2.87B | -1.9% | 318.0M | 122.0M |
| 2025-12 | 2.92B | -8.6% | 304.0M | 144.0M |
| 2026-03 | 2.87B | -3.4% | 204.0M | -6.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.6x**  (TTM 2.7x)
- 2026E TEV/EBITDA _est_: **8.4x**  (TTM 8.9x)
- 2026E TEV/FCF _est_: **39.2x**
- 2026E P/E: **33.0x**  (TTM n/a, fwd 33.0x)
- EV 30.97B, 26E rev 12.13B, 26E EPS 0.84x


**3) Performance:**


- L1M 0.4% · L3M 53.3% · L12M -9.4% · -11.8% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 0.4%, 3M 53.3%; -11.8% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-28 | -0.24 | -0.48 | -97.94 |
| 2026-02-17 | -0.22 | -0.27 | -21.02 |
| 2025-10-28 | 0.08 | -0.26 | -411.71 |
| 2025-07-29 | 0.05 | -0.39 | -886.77 |


_Highlights:_ revenue growth accelerating


_Issues:_ net margin negative (-4.4%); missed EPS all last 4 quarters


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DVN — Devon Energy Corporation  (Energy / Oil & Gas E&P)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 19.17B | n/a | 31.4% | 54.1% | 8.53B | 3.40B | 17.8% |
| 2023 | 15.26B | -20.4% | 24.6% | 49.5% | 6.54B | 2.60B | 17.0% |
| 2024 | 15.94B | 4.5% | 18.1% | 46.2% | 6.60B | -853.0M | -5.4% |
| 2025 | 17.19B | 7.8% | 15.4% | 44.0% | 6.71B | 2.80B | 16.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | 4.40B | 14.5% | 1.66B | 622.0M |
| 2025-03 | 4.45B | 11.1% | 1.94B | 1.00B |
| 2025-06 | 4.28B | 21.0% | 1.54B | 573.0M |
| 2025-09 | 4.33B | 15.9% | 1.69B | 623.0M |
| 2025-12 | 4.12B | 13.6% | 1.53B | 601.0M |


**2) Valuation:**


- 2026E TEV/Sales: **1.4x**  (TTM 2.4x)
- 2026E TEV/EBITDA _est_: **3.3x**  (TTM 5.6x)
- 2026E TEV/FCF _est_: **14.0x**
- 2026E P/E: **9.1x**  (TTM 13.8x, fwd 9.4x)
- EV 37.69B, 26E rev 26.99B, 26E EPS 5.43x


**3) Performance:**


- L1M 8.1% · L3M 11.4% · L12M 49.5% · -5.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 8.1%, 3M 11.4%; -5.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 1.09 | 1.04 | -4.91 |
| 2026-02-17 | 0.83 | 0.82 | -0.81 |
| 2025-11-05 | 0.94 | 1.04 | 10.56 |
| 2025-08-05 | 0.86 | 0.84 | -2.84 |


_Highlights:_ revenue growth accelerating; strong FCF margin (16.3%); beat EPS 1/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## EOG — EOG Resources, Inc.  (Energy / Oil & Gas E&P)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 29.49B | n/a | 26.3% | 46.2% | 11.09B | 6.09B | 20.7% |
| 2023 | 23.18B | -21.4% | 32.8% | 57.5% | 11.34B | 5.16B | 22.2% |
| 2024 | 23.38B | 0.8% | 27.4% | 53.3% | 12.14B | 5.77B | 24.7% |
| 2025 | 22.58B | -3.4% | 22.1% | 49.0% | 10.04B | 3.45B | 15.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 5.84B | 25.0% | 2.29B | 806.0M |
| 2025-06 | 5.36B | 25.1% | 2.03B | 239.0M |
| 2025-09 | 5.73B | 25.7% | 3.11B | 1.45B |
| 2025-12 | 5.65B | 12.4% | 2.61B | 957.0M |
| 2026-03 | 6.76B | 29.3% | 2.97B | 1.32B |


**2) Valuation:**


- 2026E TEV/Sales: **3.0x**  (TTM 3.4x)
- 2026E TEV/EBITDA _est_: **5.7x**  (TTM 6.3x)
- 2026E TEV/FCF _est_: **25.0x**
- 2026E P/E: **9.7x**  (TTM 13.8x, fwd 9.7x)
- EV 79.16B, 26E rev 26.09B, 26E EPS 14.41x


**3) Performance:**


- L1M 4.6% · L3M 17.1% · L12M 25.7% · -5.7% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 4.6%, 3M 17.1%; -5.7% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 3.21 | 3.41 | 6.22 |
| 2026-02-24 | 2.2 | 2.27 | 3.38 |
| 2025-11-06 | 2.49 | 2.7 | 8.47 |
| 2025-08-07 | 2.18 | 2.46 | 13.03 |


_Highlights:_ strong FCF margin (15.3%); beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## FANG — Diamondback Energy, Inc.  (Energy / Oil & Gas E&P)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 9.57B | n/a | 45.8% | 75.6% | 6.33B | 2.71B | 28.4% |
| 2023 | 8.34B | -12.8% | 37.7% | 74.0% | 5.92B | 1.21B | 14.5% |
| 2024 | 11.02B | 32.2% | 30.3% | 69.3% | 6.41B | -5.37B | -48.8% |
| 2025 | 14.93B | 35.4% | 11.1% | 48.1% | 8.76B | -703.0M | -4.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.03B | 34.9% | 2.35B | 663.0M |
| 2025-06 | 3.65B | 19.1% | 1.68B | -2.31B |
| 2025-09 | 3.91B | 26.1% | 2.38B | 73.0M |
| 2025-12 | 3.34B | -43.6% | 2.34B | 873.0M |
| 2026-03 | 4.21B | 0.6% | 1.83B | 581.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.6x**  (TTM 5.3x)
- 2026E TEV/EBITDA _est_: **6.5x**  (TTM 7.6x)
- 2026E TEV/FCF _est_: **47.1x**
- 2026E P/E: **12.0x**  (TTM 207.7x, fwd 12.0x)
- EV 77.16B, 26E rev 16.95B, 26E EPS 16.99x


**3) Performance:**


- L1M 9.7% · L3M 21.7% · L12M 45.2% · -4.2% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 9.7%, 3M 21.7%; -4.2% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-04 | 3.75 | 4.23 | 12.78 |
| 2026-02-23 | 2.0 | 1.74 | -13.16 |
| 2025-11-03 | 2.94 | 3.08 | 4.59 |
| 2025-08-04 | 2.72 | 2.67 | -2.01 |


_Highlights:_ revenue +35.4% latest FY; revenue growth accelerating; beat EPS 2/4 quarters


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## GL — Globe Life Inc.  (Financial Services / Insurance - Life)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.23B | n/a | 17.1% | n/a | 1.42B | 1.39B | 26.7% |
| 2023 | 5.45B | 4.2% | 17.8% | n/a | 1.48B | 1.43B | 26.3% |
| 2024 | 5.78B | 6.1% | 18.5% | n/a | 1.40B | 1.33B | 23.0% |
| 2025 | 5.99B | 3.7% | 19.4% | n/a | 1.40B | 1.25B | 20.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | 1.47B | 17.4% | 336.9M | 321.9M |
| 2025-03 | 1.48B | 17.2% | 431.9M | 420.1M |
| 2025-06 | 1.48B | 17.1% | 307.9M | 295.0M |
| 2025-09 | 1.51B | 25.6% | 306.0M | 208.7M |
| 2025-12 | 1.52B | 17.5% | 350.6M | 330.1M |
| 2026-03 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **2.2x**  (TTM 2.4x)
- 2026E TEV/EBITDA _est_: **8.1x**  (TTM 9.1x)
- 2026E TEV/FCF _est_: **10.1x**
- 2026E P/E: **9.3x**  (TTM 10.7x, fwd 9.3x)
- EV 14.86B, 26E rev 6.79B, 26E EPS 16.62x


**3) Performance:**


- L1M 3.6% · L3M 7.7% · L12M 31.1% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 3.6%, 3M 7.7%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-22 | 3.48 | 3.43 | -1.35 |
| 2026-02-04 | 3.4 | 3.29 | -3.2 |
| 2025-10-22 | 4.54 | 4.81 | 5.9 |
| 2025-07-23 | 3.25 | 3.27 | 0.76 |


_Highlights:_ net margin expanding; strong FCF margin (20.9%); beat EPS 2/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## HOLX — Hologic, Inc.  (Healthcare / Medical Instruments & Supplies)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 4.86B | n/a | 26.8% | 43.5% | 2.13B | 2.00B | 41.1% |
| 2023 | 4.03B | -17.1% | 11.3% | 27.6% | 1.05B | 901.0M | 22.4% |
| 2024 | 4.03B | -0.0% | 19.6% | 32.2% | 1.29B | 1.15B | 28.4% |
| 2025 | 4.10B | 1.7% | 13.8% | 26.8% | 1.06B | 904.7M | 22.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | 1.02B | 19.7% | 189.3M | 142.3M |
| 2025-03 | 1.01B | -1.7% | 169.4M | 129.2M |
| 2025-06 | 1.02B | 19.0% | 343.3M | 308.5M |
| 2025-09 | 1.05B | 17.8% | 355.1M | 324.7M |
| 2025-12 | 1.05B | 17.1% | 229.9M | 194.8M |


**2) Valuation:**


- 2026E TEV/Sales: **3.8x**  (TTM 4.1x)
- 2026E TEV/EBITDA _est_: **11.7x**  (TTM 12.7x)
- 2026E TEV/FCF _est_: **18.7x**
- 2026E P/E: **20.1x**  (TTM 31.5x, fwd 15.7x)
- EV 17.12B, 26E rev 4.46B, 26E EPS 3.78x


**3) Performance:**


- L1M 0.4% · L3M 1.7% · L12M 23.2% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 0.4%, 3M 1.7%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-01-29 | 1.1 | 1.04 | -5.43 |
| 2025-11-03 | 1.1 | 1.13 | 2.65 |
| 2025-07-30 | 1.05 | 1.08 | 2.74 |
| 2025-05-01 | 1.02 | 1.03 | 1.37 |


_Highlights:_ revenue growth accelerating; strong FCF margin (22.1%); beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## HUM — Humana Inc.  (Healthcare / Healthcare Plans)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 92.87B | n/a | 3.0% | n/a | 4.59B | 3.45B | 3.7% |
| 2023 | 106.37B | 14.5% | 2.3% | n/a | 3.98B | 2.98B | 2.8% |
| 2024 | 117.76B | 10.7% | 1.0% | n/a | 2.97B | 2.39B | 2.0% |
| 2025 | 129.66B | 10.1% | 0.9% | n/a | 921.0M | 375.0M | 0.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 32.11B | 3.9% | 331.0M | 236.0M |
| 2025-06 | 32.39B | 1.7% | 1.27B | 1.16B |
| 2025-09 | 32.65B | 0.6% | 971.0M | 836.0M |
| 2025-12 | 32.52B | -2.4% | -1.65B | -1.85B |
| 2026-03 | 39.65B | 3.0% | 1.25B | 1.13B |


**2) Valuation:**


- 2026E TEV/Sales: **0.2x**  (TTM 0.2x)
- 2026E TEV/EBITDA _est_: **6.9x**  (TTM 8.7x)
- 2026E TEV/FCF _est_: **16.3x**
- 2026E P/E: **19.9x**  (TTM 32.6x, fwd 19.9x)
- EV 29.11B, 26E rev 170.93B, 26E EPS 15.34x


**3) Performance:**


- L1M 52.0% · L3M 66.6% · L12M 34.5% · -1.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 52.0%, 3M 66.6%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-29 | 10.2 | 10.31 | 1.05 |
| 2026-02-11 | -3.99 | -3.96 | 0.68 |
| 2025-11-05 | 2.83 | 3.24 | 14.64 |
| 2025-07-29 | 5.87 | 6.27 | 6.86 |


_Highlights:_ beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MO — Altria Group, Inc.  (Consumer Defensive / Tobacco)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 20.69B | n/a | 27.9% | 42.3% | 8.26B | 8.05B | 38.9% |
| 2023 | 20.50B | -0.9% | 39.7% | 60.2% | 9.29B | 9.09B | 44.3% |
| 2024 | 20.44B | -0.3% | 55.1% | 73.7% | 8.75B | 8.61B | 42.1% |
| 2025 | 20.14B | -1.5% | 34.5% | 53.8% | 9.29B | 9.07B | 45.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.52B | 23.8% | 2.72B | 2.68B |
| 2025-06 | 5.29B | 45.0% | 205.0M | 173.0M |
| 2025-09 | 5.25B | 45.2% | 3.09B | 3.04B |
| 2025-12 | 5.08B | 22.0% | 3.27B | 3.18B |
| 2026-03 | 4.76B | 45.9% | 2.32B | 2.23B |


**2) Valuation:**


- 2026E TEV/Sales: **7.0x**  (TTM 7.0x)
- 2026E TEV/EBITDA _est_: **9.0x**  (TTM 9.1x)
- 2026E TEV/FCF _est_: **16.6x**
- 2026E P/E: **12.5x**  (TTM 15.3x, fwd 12.5x)
- EV 143.17B, 26E rev 20.60B, 26E EPS 5.87x


**3) Performance:**


- L1M 12.6% · L3M 10.5% · L12M 38.9% · -2.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 12.6%, 3M 10.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-30 | 1.25 | 1.32 | 5.92 |
| 2026-01-29 | 1.32 | 1.3 | -1.33 |
| 2025-10-30 | 1.44 | 1.41 | -1.83 |
| 2025-07-30 | 1.38 | 1.44 | 3.99 |


_Highlights:_ strong FCF margin (45.1%); beat EPS 2/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## NTAP — NetApp, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 6.32B | n/a | 14.8% | 21.6% | 1.21B | 985.0M | 15.6% |
| 2023 | 6.36B | 0.7% | 20.0% | 21.7% | 1.11B | 868.0M | 13.6% |
| 2024 | 6.27B | -1.5% | 15.7% | 25.2% | 1.69B | 1.53B | 24.4% |
| 2025 | 6.57B | 4.9% | 18.0% | 25.7% | 1.51B | 1.34B | 20.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-10 | n/a | n/a | n/a | n/a |
| 2025-01 | 1.64B | 18.2% | 385.0M | 338.0M |
| 2025-04 | 1.73B | 19.6% | 675.0M | 640.0M |
| 2025-07 | 1.56B | 14.9% | 673.0M | 620.0M |
| 2025-10 | 1.71B | 17.9% | 127.0M | 78.0M |
| 2026-01 | 1.71B | 19.5% | 317.0M | 271.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.3x**  (TTM 3.5x)
- 2026E TEV/EBITDA _est_: **12.5x**  (TTM 13.4x)
- 2026E TEV/FCF _est_: **19.6x**
- 2026E P/E: **14.1x**  (TTM 20.1x, fwd 14.1x)
- EV 23.38B, 26E rev 7.19B, 26E EPS 8.53x


**3) Performance:**


- L1M 15.7% · L3M 17.7% · L12M 22.7% · -3.7% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 15.7%, 3M 17.7%; -3.7% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-02-26 | 2.06 | 2.12 | 2.78 |
| 2025-11-25 | 1.88 | 2.05 | 8.76 |
| 2025-08-27 | 1.14 | 1.15 | 0.8 |
| 2025-05-29 | 1.9 | 1.93 | 1.76 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (20.4%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## OXY — Occidental Petroleum Corporatio  (Energy / Oil & Gas E&P)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 36.63B | n/a | 36.3% | 60.3% | 16.81B | 12.31B | 33.6% |
| 2023 | 23.16B | -36.8% | 20.3% | 50.3% | 12.31B | 6.61B | 28.6% |
| 2024 | 22.02B | -4.9% | 13.9% | 51.7% | 11.44B | 5.18B | 23.5% |
| 2025 | 21.59B | -1.9% | 10.8% | 54.0% | 10.53B | 4.11B | 19.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 5.70B | 16.4% | 2.15B | 466.0M |
| 2025-06 | 6.41B | 7.1% | 2.96B | 736.0M |
| 2025-09 | 6.62B | 12.5% | 2.79B | 1.02B |
| 2025-12 | 1.75B | 5.8% | 2.63B | 1.88B |
| 2026-03 | 5.23B | 64.0% | 1.28B | -273.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.3x**  (TTM 3.8x)
- 2026E TEV/EBITDA _est_: **6.4x**  (TTM 7.5x)
- 2026E TEV/FCF _est_: **22.9x**
- 2026E P/E: **16.1x**  (TTM 80.6x, fwd 16.1x)
- EV 81.02B, 26E rev 24.66B, 26E EPS 3.71x


**3) Performance:**


- L1M 4.8% · L3M 30.0% · L12M 39.0% · -10.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 4.8%, 3M 30.0%; -10.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 0.59 | 1.06 | 80.35 |
| 2026-02-18 | 0.18 | 0.31 | 76.86 |
| 2025-11-10 | 0.52 | 0.64 | 22.73 |
| 2025-08-06 | 0.31 | 0.39 | 24.79 |


_Highlights:_ revenue growth accelerating; strong FCF margin (19.0%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## SBUX — Starbucks Corporation  (Consumer Cyclical / Restaurants)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 32.25B | n/a | 10.2% | 19.4% | 4.40B | 2.56B | 7.9% |
| 2023 | 35.98B | 11.6% | 11.5% | 20.6% | 6.01B | 3.68B | 10.2% |
| 2024 | 36.18B | 0.6% | 10.4% | 19.7% | 6.10B | 3.32B | 9.2% |
| 2025 | 37.18B | 2.8% | 5.0% | 13.0% | 4.75B | 2.44B | 6.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 8.76B | 4.4% | 292.0M | -297.2M |
| 2025-06 | 9.46B | 5.9% | 1.00B | 434.3M |
| 2025-09 | 9.57B | 1.4% | 1.38B | 925.8M |
| 2025-12 | 9.92B | 3.0% | 1.60B | 1.27B |
| 2026-03 | 9.53B | 5.4% | 364.5M | 91.8M |


**2) Valuation:**


- 2026E TEV/Sales: **3.7x**  (TTM 3.8x)
- 2026E TEV/EBITDA _est_: **26.7x**  (TTM 26.8x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **35.3x**  (TTM 81.5x, fwd 35.3x)
- EV 144.45B, 26E rev 38.61B, 26E EPS 3.03x


**3) Performance:**


- L1M 9.2% · L3M 14.6% · L12M 27.6% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 9.2%, 3M 14.6%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-28 | 0.44 | 0.5 | 14.51 |
| 2026-01-28 | 0.57 | 0.26 | -54.31 |
| 2025-10-29 | 0.52 | 0.12 | -76.79 |
| 2025-07-29 | 0.65 | 0.49 | -24.99 |


_Highlights:_ revenue growth accelerating; beat EPS 1/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## UNP — Union Pacific Corporation  (Industrials / Railroads)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 24.88B | n/a | 28.1% | 50.6% | 9.36B | 5.74B | 23.1% |
| 2023 | 24.12B | -3.0% | 26.4% | 49.3% | 8.38B | 4.77B | 19.8% |
| 2024 | 24.25B | 0.5% | 27.8% | 51.4% | 9.35B | 5.89B | 24.3% |
| 2025 | 24.51B | 1.1% | 29.1% | 52.8% | 9.29B | 5.50B | 22.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 6.03B | 27.0% | 2.21B | 1.30B |
| 2025-06 | 6.15B | 30.5% | 2.33B | 1.40B |
| 2025-09 | 6.24B | 28.6% | 2.52B | 1.57B |
| 2025-12 | 6.08B | 30.4% | 2.23B | 1.23B |
| 2026-03 | 6.22B | 27.4% | 2.44B | 1.50B |


**2) Valuation:**


- 2026E TEV/Sales: **7.0x**  (TTM 7.7x)
- 2026E TEV/EBITDA _est_: **13.8x**  (TTM 15.2x)
- 2026E TEV/FCF _est_: **43.2x**
- 2026E P/E: **19.8x**  (TTM 22.3x, fwd 19.8x)
- EV 191.11B, 26E rev 27.11B, 26E EPS 13.69x


**3) Performance:**


- L1M 7.8% · L3M 4.3% · L12M 21.3% · -0.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M 7.8%, 3M 4.3%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-23 | 2.86 | 2.93 | 2.42 |
| 2026-01-27 | 2.86 | 3.11 | 8.76 |
| 2025-10-23 | 2.98 | 3.01 | 1.14 |
| 2025-07-24 | 2.91 | 3.03 | 4.18 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (22.4%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CINF — Cincinnati Financial Corporatio  (Financial Services / Insurance - Property & Casualty)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 6.56B | n/a | -7.4% | n/a | 2.05B | 2.04B | 31.0% |
| 2023 | 10.01B | 52.6% | 18.4% | n/a | 2.05B | 2.03B | 20.3% |
| 2024 | 11.34B | 13.2% | 20.2% | n/a | 2.65B | 2.63B | 23.2% |
| 2025 | 12.63B | 11.4% | 18.9% | n/a | 3.11B | 3.09B | 24.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 2.57B | -3.5% | 310.0M | 307.0M |
| 2025-06 | 3.25B | 21.1% | 741.0M | 737.0M |
| 2025-09 | 3.73B | 30.1% | 1.11B | 1.11B |
| 2025-12 | 3.09B | 21.9% | 947.0M | 939.0M |
| 2026-03 | 2.86B | 9.6% | 656.0M | 654.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.0x**  (TTM 2.0x)
- 2026E TEV/EBITDA _est_: **7.0x**  (TTM 7.0x)
- 2026E TEV/FCF _est_: **9.3x**
- 2026E P/E: **18.1x**  (TTM 9.5x, fwd 18.1x)
- EV 25.37B, 26E rev 12.83B, 26E EPS 9.18x


**3) Performance:**


- L1M 1.9% · L3M 2.8% · L12M 16.4% · -3.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M 1.9%, 3M 2.8%; -3.0% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-27 | 1.94 | 2.1 | 8.24 |
| 2026-02-09 | 2.89 | 3.37 | 16.6 |
| 2025-10-27 | 2.06 | 2.85 | 38.43 |
| 2025-07-28 | 1.39 | 1.97 | 42.0 |


_Highlights:_ strong FCF margin (24.5%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CME — CME Group Inc.  (Financial Services / Financial Data & Stock Exchanges)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.02B | n/a | 53.6% | 80.0% | 3.06B | 2.97B | 59.1% |
| 2023 | 5.58B | 11.1% | 57.8% | 83.6% | 3.45B | 3.38B | 60.5% |
| 2024 | 6.13B | 9.9% | 57.5% | 82.2% | 3.69B | 3.60B | 58.7% |
| 2025 | 6.52B | 6.4% | 62.5% | 89.5% | 4.28B | 4.19B | 64.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 1.64B | 58.2% | 1.12B | 1.10B |
| 2025-06 | 1.69B | 60.6% | 1.06B | 1.04B |
| 2025-09 | 1.54B | 59.1% | 968.1M | 949.7M |
| 2025-12 | 1.65B | 71.7% | 1.13B | 1.10B |
| 2026-03 | 1.88B | 61.4% | 1.26B | 1.24B |


**2) Valuation:**


- 2026E TEV/Sales: **14.9x**  (TTM 16.2x)
- 2026E TEV/EBITDA _est_: **21.0x**  (TTM 22.9x)
- 2026E TEV/FCF _est_: **33.2x**
- 2026E P/E: **23.2x**  (TTM 25.5x, fwd 23.2x)
- EV 109.52B, 26E rev 7.34B, 26E EPS 12.87x


**3) Performance:**


- L1M 0.9% · L3M 1.0% · L12M 16.5% · -6.3% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 0.9%, 3M 1.0%; -6.3% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-22 | 3.29 | 3.18 | -3.34 |
| 2026-02-04 | 2.63 | 3.24 | 23.19 |
| 2025-10-22 | 2.63 | 2.68 | 1.98 |
| 2025-07-23 | 2.8 | 2.81 | 0.34 |


_Highlights:_ net margin expanding; strong FCF margin (64.3%); beat EPS 3/4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MNST — Monster Beverage Corporation  (Consumer Defensive / Beverages - Non-Alcoholic)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 6.31B | n/a | 18.9% | 26.1% | 887.7M | 675.5M | 10.7% |
| 2023 | 7.14B | 13.1% | 22.8% | 28.3% | 1.72B | 1.48B | 20.8% |
| 2024 | 7.49B | 4.9% | 20.1% | 26.8% | 1.93B | 1.62B | 21.6% |
| 2025 | 8.29B | 10.7% | 23.0% | 30.5% | 2.10B | 1.94B | 23.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | 1.81B | 14.9% | 461.7M | 349.5M |
| 2025-03 | 1.85B | 23.9% | 507.6M | 473.2M |
| 2025-06 | 2.11B | 23.1% | 466.0M | 424.6M |
| 2025-09 | 2.20B | 23.9% | 745.1M | 697.2M |
| 2025-12 | 2.13B | 21.1% | 379.4M | 345.7M |


**2) Valuation:**


- 2026E TEV/Sales: **8.0x**  (TTM 9.4x)
- 2026E TEV/EBITDA _est_: **24.8x**  (TTM 29.2x)
- 2026E TEV/FCF _est_: **41.6x**
- 2026E P/E: **34.2x**  (TTM 42.1x, fwd 33.8x)
- EV 82.28B, 26E rev 10.32B, 26E EPS 2.55x


**3) Performance:**


- L1M 15.6% · L3M 6.9% · L12M 42.8% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 15.6%, 3M 6.9%; at/near 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-07 | 0.53 | 0.57 | 8.33 |
| 2026-02-26 | 0.49 | 0.5 | 2.66 |
| 2025-11-06 | 0.49 | 0.53 | 9.22 |
| 2025-08-07 | 0.48 | 0.51 | 6.73 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (23.4%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ODFL — Old Dominion Freight Line, Inc.  (Industrials / Trucking)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 6.26B | n/a | 22.0% | 33.8% | 1.69B | 916.4M | 14.6% |
| 2023 | 5.87B | -6.3% | 21.1% | 33.6% | 1.57B | 811.8M | 13.8% |
| 2024 | 5.81B | -0.9% | 20.4% | 32.7% | 1.66B | 888.0M | 15.3% |
| 2025 | 5.50B | -5.5% | 18.6% | 31.4% | 1.37B | 955.1M | 17.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | 1.39B | 19.0% | 401.1M | 230.1M |
| 2025-03 | 1.37B | 18.5% | 336.5M | 248.4M |
| 2025-06 | 1.41B | 19.1% | 285.8M | 98.7M |
| 2025-09 | 1.41B | 19.3% | 437.5M | 343.5M |
| 2025-12 | 1.31B | 17.6% | 310.3M | 264.5M |
| 2026-03 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **6.8x**  (TTM 7.7x)
- 2026E TEV/EBITDA _est_: **21.8x**  (TTM 24.6x)
- 2026E TEV/FCF _est_: **43.1x**
- 2026E P/E: **32.9x**  (TTM 42.4x, fwd 32.9x)
- EV 41.99B, 26E rev 6.16B, 26E EPS 6.17x


**3) Performance:**


- L1M -4.9% · L3M 5.3% · L12M 19.2% · -9.5% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -4.9%, 3M 5.3%; -9.5% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-29 | 1.05 | 1.14 | 8.46 |
| 2026-02-04 | 1.06 | 1.09 | 2.89 |
| 2025-10-29 | 1.22 | 1.28 | 5.15 |
| 2025-07-30 | 1.29 | 1.27 | -1.21 |


_Highlights:_ strong FCF margin (17.4%); beat EPS 3/4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._
