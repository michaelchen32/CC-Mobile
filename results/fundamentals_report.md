# Fundamental / valuation / earnings dossier

Names that fired in the high-recall screen on the latest bar (2026-07-31). **Source: yfinance only** — the environment blocks all other sites, so literal earnings-call transcript text is not retrievable; the earnings section is a quantitative recap (EPS beat/miss + revenue/margin path) instead. Forward '2026E' = consensus next-fiscal-year (+1y) estimate; TEV/EBITDA & TEV/FCF 26E are estimated as forward revenue x trailing margin (marked _est_). Not investment advice.


## Master table

| ticker | name | sector | n_detectors | trend | rev_growth_TTM_% | net_margin_% | CFO_TTM | FCF_TTM | TEV/Sales_26E | TEV/EBITDA_26E_est | TEV/FCF_26E_est | PE_26E | TEV/Sales_TTM | PE_TTM | L1M_% | L3M_% | L12M_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DXCM | DexCom, Inc. | Healthcare | 7 | up | 13.1 | 20.1 | 1748700032.0 | 1021162496.0 | 5.3 | 18.8 | 25.9 | 26.8 | 6.2 | 33.0 | 21.2 | 40.1 | -6.3 |
| AMZN | Amazon.com, Inc. | Consumer Cyclical | 6 | weak | 19.6 | 17.4 | 161402994688.0 | 22722125824.0 | 3.2 | 14.8 | 109.7 | 26.2 | 3.9 | 21.8 | 12.4 | 2.5 | 18.0 |
| EOG | EOG Resources, Inc. | Energy | 4 | up | 15.6 | 23.3 | 10721000448.0 | 2864250112.0 | 3.2 | 5.9 | 26.1 | 10.1 | 3.5 | 14.6 | 16.5 | 6.6 | 26.9 |
| MTD | Mettler-Toledo International, I | Healthcare | 4 | up | 4.5 | 21.9 | 975166976.0 | 693589632.0 | 6.9 | 22.2 | 40.9 | 27.5 | 7.4 | 31.9 | 8.9 | 10.9 | 11.9 |
| ZBRA | Zebra Technologies Corporation | Technology | 4 | up | 14.3 | 7.5 | 915000000.0 | 559000000.0 | 2.6 | 14.2 | 26.1 | 14.2 | 3.0 | 35.4 | 9.7 | 29.9 | -11.6 |
| EA | Electronic Arts Inc. | Communication Services | 3 | up | 11.9 | 11.8 | 2552999936.0 | 2219124992.0 | 5.9 | 30.0 | 20.1 | 34.2 | 6.8 | 60.0 | 2.1 | 3.8 | 34.8 |
| WY | Weyerhaeuser Company | Real Estate | 3 | up | -0.9 | 6.9 | 547000000.0 | 13625000.0 | 3.0 | 30.0 | 1515.4 | 37.7 | 3.4 | 37.9 | 6.2 | 3.0 | 1.5 |
| CBOE | Cboe Global Markets, Inc. | Financial Services | 3 | weak | 6.5 | 25.8 | 2799699968.0 | 1003075008.0 | 10.3 | 27.7 | 49.3 | 20.4 | 6.4 | 24.2 | 25.2 | 3.6 | 29.0 |
| MSFT | Microsoft Corporation | Technology | 3 | weak | 17.7 | 40.3 | 182934994944.0 | 16363499520.0 | 7.5 | 12.9 | 152.6 | 20.0 | 10.6 | 25.9 | 20.9 | 14.2 | -8.7 |
| CME | CME Group Inc. | Financial Services | 2 | down | 0.8 | 63.4 | 4309000192.0 | 2909012480.0 | 13.3 | 18.8 | 30.9 | 20.7 | 14.5 | 22.7 | 15.9 | -6.5 | 0.2 |
| HII | Huntington Ingalls Industries,  | Industrials | 2 | down | 10.9 | 5.0 | 347000000.0 | -300249984.0 | 1.1 | 12.7 |  | 15.9 | 1.2 | 19.5 | 17.0 | -10.0 | 28.4 |
| BEN | Franklin Resources, Inc. | Financial Services | 2 | up | 14.3 | 8.7 | 277800000.0 | -3226200064.0 | 2.1 | 12.6 |  | 10.8 | 2.2 | 23.0 | -0.6 | 14.1 | 46.7 |
| BMY | Bristol-Myers Squibb Company | Healthcare | 2 | up | 5.7 | 18.9 | 12782000128.0 | 8114375168.0 | 3.5 | 9.1 | 21.2 | 10.1 | 3.4 | 14.4 | 17.0 | 9.0 | 48.9 |
| MHK | Mohawk Industries, Inc. | Consumer Cyclical | 2 | up | 6.8 | 4.2 | 1272800000.0 | 966899968.0 | 0.9 | 6.5 | 10.1 | 12.4 | 0.9 | 16.3 | 2.7 | 16.6 | 5.0 |
| NTAP | NetApp, Inc. | Technology | 2 | up | 12.5 | 18.4 | 2067000064.0 | 1295250048.0 | 4.3 | 15.9 | 23.1 | 18.1 | 4.9 | 28.1 | 14.5 | 61.6 | 73.5 |
| REGN | Regeneron Pharmaceuticals, Inc. | Healthcare | 2 | weak | 16.7 | 27.9 | 4681299968.0 | 3065299968.0 | 3.9 | 12.8 | 19.6 | 15.2 | 4.6 | 18.9 | 22.1 | 8.0 | 38.3 |
| ORCL | Oracle Corporation | Technology | 1 | down | 20.6 | 25.4 | 31977000960.0 | -24536750080.0 | 3.9 | 8.7 |  | 11.9 | 7.6 | 22.3 | -8.5 | -19.3 | -47.6 |
| PDD | PDD Holdings Inc. | Consumer Cyclical | 1 | down | 11.0 | 21.6 | 107866693632.0 | 71642849280.0 | -0.6 | -2.6 | -3.5 | 1.1 | -0.7 | 9.3 | 7.3 | -11.3 | -21.6 |
| CFG | Citizens Financial Group, Inc. | Financial Services | 1 | up | 14.7 | 26.1 |  |  | 3.5 |  |  | 11.0 | 4.3 | 15.6 | 0.4 | 10.9 | 52.9 |
| CVX | Chevron Corporation | Energy | 1 | up | 52.6 | 9.8 | 45320998912.0 |  | 2.1 | 8.6 |  | 15.4 | 2.1 | 18.9 | 18.8 | 2.8 | 33.5 |
| ERIE | Erie Indemnity Company | Financial Services | 1 | up | 2.8 | 14.0 | 697777024.0 | 481207744.0 |  |  |  |  | 3.0 | 22.0 | -2.3 | 11.2 | -30.0 |
| FANG | Diamondback Energy, Inc. | Energy | 1 | up | 4.2 | 2.0 | 8231000064.0 | 1397250048.0 | 4.6 | 6.5 | 47.2 | 11.7 | 5.3 | 209.2 | 18.0 | -0.8 | 37.9 |
| IEX | IDEX Corporation | Industrials | 1 | up | 6.4 | 14.5 | 716700032.0 | 555612480.0 | 4.7 | 17.4 | 30.4 | 24.3 | 5.1 | 33.1 | 2.8 | 6.5 | 42.4 |
| MPC | Marathon Petroleum Corporation | Energy | 1 | up | 8.8 | 3.4 | 9438000128.0 | 3518749952.0 | 0.9 | 12.5 | 36.5 | 11.4 | 1.0 | 20.8 | 19.5 | 27.9 | 88.9 |
| PANW | Palo Alto Networks, Inc. | Technology | 1 | up | 31.1 | 7.9 | 4216999936.0 | 3579375104.0 | 19.5 | 139.5 | 57.8 | 170.1 | 25.4 | 286.1 | -5.7 | 85.0 | 81.3 |
| TDY | Teledyne Technologies Incorpora | Technology | 1 | up | 9.8 | 15.3 | 1271299968.0 | 912675008.0 | 4.6 | 18.6 | 32.4 | 24.6 | 5.0 | 31.7 | -0.9 | 1.5 | 19.1 |
| TRGP | Targa Resources, Inc. | Energy | 1 | up | -10.2 | 12.9 | 3702500096.0 | -318550016.0 | 3.4 | 10.7 |  | 22.6 | 4.7 | 27.6 | 5.4 | 4.4 | 66.0 |
| VLO | Valero Energy Corporation | Energy | 1 | up | 51.7 | 5.4 | 10908000256.0 | 8416374784.0 | 0.8 | 7.7 | 12.3 | 11.4 | 0.7 | 13.1 | 16.6 | 25.0 | 131.1 |
| APA | APA Corporation | Energy | 1 | weak | -11.9 | 18.3 | 4003000064.0 | 1691250048.0 | 2.3 | 3.7 | 11.4 | 9.0 | 2.2 | 8.7 | 17.9 | -7.7 | 98.3 |
| COP | ConocoPhillips | Energy | 1 | weak | -5.3 | 12.3 | 17976000512.0 | 5289124864.0 | 2.5 | 6.2 | 27.6 | 13.4 | 2.8 | 20.4 | 16.7 | -3.5 | 28.8 |
| GOOG | Alphabet Inc. | Communication Services | 1 | weak | 24.2 | 54.8 | 185675005952.0 | 22665000960.0 | 7.0 | 18.1 | 138.3 | 24.2 | 9.6 | 17.9 | -0.3 | -6.6 | 81.2 |
| OXY | Occidental Petroleum Corporatio | Energy | 1 | weak | -8.3 | 22.4 | 9665000448.0 | 3033374976.0 | 3.3 | 6.5 | 23.3 | 14.5 | 3.7 | 77.1 | 19.0 | -5.4 | 31.2 |
| TT | Trane Technologies plc | Industrials | 1 | weak | 10.6 | 13.3 | 3876800000.0 | 3121687552.0 | 4.0 | 20.7 | 28.5 | 26.1 | 4.7 | 33.9 | -6.1 | -7.4 | 6.2 |


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
| 2025-06 | 1.16B | 15.5% | 303.0M | 208.9M |
| 2025-09 | 1.21B | 23.5% | 659.9M | 579.4M |
| 2025-12 | 1.26B | 21.2% | 294.0M | 192.1M |
| 2026-03 | 1.19B | 16.7% | 525.6M | 449.0M |
| 2026-06 | 1.31B | 19.0% | 269.2M | 184.5M |


**2) Valuation:**


- 2026E TEV/Sales: **5.3x**  (TTM 6.2x)
- 2026E TEV/EBITDA _est_: **18.8x**  (TTM 22.1x)
- 2026E TEV/FCF _est_: **25.9x**
- 2026E P/E: **26.8x**  (TTM 33.0x, fwd 26.8x)
- EV 30.94B, 26E rev 5.81B, 26E EPS 3.11x


**3) Performance:**


- L1M 21.2% · L3M 40.1% · L12M -6.3% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, >=5% up-day on >=2x volume, gap-up and held, range expansion (>=2x ATR), uptrend continuation off a dip; 1M 21.2%, 3M 40.1%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 0.61 | 0.7 | 15.11 |
| 2026-04-30 | 0.47 | 0.56 | 18.99 |
| 2026-02-12 | 0.65 | 0.68 | 4.5 |
| 2025-10-30 | 0.57 | 0.61 | 7.51 |


_Highlights:_ revenue +15.6% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (23.1%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## AMZN — Amazon.com, Inc.  (Consumer Cyclical / Internet Retail)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 513.98B | n/a | -0.5% | 7.5% | 46.75B | -16.89B | -3.3% |
| 2023 | 574.78B | 11.8% | 5.3% | 15.6% | 84.95B | 32.22B | 5.6% |
| 2024 | 637.96B | 11.0% | 9.3% | 19.4% | 115.88B | 32.88B | 5.2% |
| 2025 | 716.92B | 12.4% | 10.8% | 23.1% | 139.51B | 7.70B | 1.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 155.67B | 11.0% | 17.02B | -8.00B |
| 2025-06 | 167.70B | 10.8% | 32.52B | 332.0M |
| 2025-09 | 180.17B | 11.8% | 35.52B | 430.0M |
| 2025-12 | 213.39B | 9.9% | 54.46B | 14.94B |
| 2026-03 | 181.52B | 16.7% | 26.03B | -18.17B |
| 2026-06 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **3.2x**  (TTM 3.9x)
- 2026E TEV/EBITDA _est_: **14.8x**  (TTM 17.9x)
- 2026E TEV/FCF _est_: **109.7x**
- 2026E P/E: **26.2x**  (TTM 21.8x, fwd 26.4x)
- EV 3028.69B, 26E rev 942.79B, 26E EPS 10.38x


**3) Performance:**


- L1M 12.4% · L3M 2.5% · L12M 18.0% · -1.2% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, >=5% up-day on >=2x volume, gap-up and held, range expansion (>=2x ATR), uptrend continuation off a dip; 1M 12.4%, 3M 2.5%; at/near 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 1.83 | 5.75 | 215.02 |
| 2026-04-29 | 1.64 | 2.78 | 69.02 |
| 2026-02-05 | 1.95 | 1.95 | 0.22 |
| 2025-10-30 | 1.56 | 1.95 | 25.2 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS all last 4 quarters


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


- 2026E TEV/Sales: **3.2x**  (TTM 3.5x)
- 2026E TEV/EBITDA _est_: **5.9x**  (TTM 6.6x)
- 2026E TEV/FCF _est_: **26.1x**
- 2026E P/E: **10.1x**  (TTM 14.6x, fwd 10.1x)
- EV 83.65B, 26E rev 26.40B, 26E EPS 14.70x


**3) Performance:**


- L1M 16.5% · L3M 6.6% · L12M 26.9% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 16.5%, 3M 6.6%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 3.21 | 3.41 | 6.22 |
| 2026-02-24 | 2.2 | 2.27 | 3.38 |
| 2025-11-06 | 2.45 | 2.71 | 10.77 |
| 2025-08-07 | 2.2 | 2.32 | 5.23 |


_Highlights:_ strong FCF margin (15.3%); beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MTD — Mettler-Toledo International, I  (Healthcare / Diagnostics & Research)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 3.92B | n/a | 22.3% | 31.6% | 859.1M | 737.8M | 18.8% |
| 2023 | 3.79B | -3.4% | 20.8% | 30.9% | 965.9M | 860.6M | 22.7% |
| 2024 | 3.87B | 2.2% | 22.3% | 31.9% | 968.3M | 864.4M | 22.3% |
| 2025 | 4.03B | 4.0% | 21.6% | 30.9% | 955.8M | 848.6M | 21.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 883.7M | 18.5% | 194.4M | 177.2M |
| 2025-06 | 983.2M | 20.6% | 236.4M | 212.5M |
| 2025-09 | 1.03B | 21.1% | 299.4M | 274.9M |
| 2025-12 | 1.13B | 25.3% | 225.6M | 184.1M |
| 2026-03 | 947.1M | 17.9% | 139.8M | 122.4M |
| 2026-06 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **6.9x**  (TTM 7.4x)
- 2026E TEV/EBITDA _est_: **22.2x**  (TTM 23.9x)
- 2026E TEV/FCF _est_: **40.9x**
- 2026E P/E: **27.5x**  (TTM 31.9x, fwd 27.6x)
- EV 30.46B, 26E rev 4.44B, 26E EPS 51.48x


**3) Performance:**


- L1M 8.9% · L3M 10.9% · L12M 11.9% · -6.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, range expansion (>=2x ATR); 1M 8.9%, 3M 10.9%; -6.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 10.81 | 11.46 | 6.06 |
| 2026-05-07 | 8.71 | 8.91 | 2.33 |
| 2026-02-05 | 12.81 | 13.36 | 4.31 |
| 2025-11-06 | 10.66 | 11.15 | 4.64 |


_Highlights:_ revenue growth accelerating; strong FCF margin (21.1%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ZBRA — Zebra Technologies Corporation  (Technology / Communication Equipment)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.78B | n/a | 8.0% | 19.7% | 488.0M | 413.0M | 7.1% |
| 2023 | 4.58B | -20.7% | 6.5% | 14.0% | -4.0M | -91.0M | -2.0% |
| 2024 | 4.98B | 8.7% | 10.6% | 18.2% | 1.01B | 954.0M | 19.2% |
| 2025 | 5.40B | 8.3% | 7.8% | 15.8% | 917.0M | 831.0M | 15.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.31B | 10.4% | 178.0M | 158.0M |
| 2025-06 | 1.29B | 8.7% | 147.0M | 130.0M |
| 2025-09 | 1.32B | 7.7% | 235.0M | 216.0M |
| 2025-12 | 1.48B | 4.7% | 357.0M | 327.0M |
| 2026-03 | 1.50B | 9.0% | 176.0M | 163.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.6x**  (TTM 3.0x)
- 2026E TEV/EBITDA _est_: **14.2x**  (TTM 16.3x)
- 2026E TEV/FCF _est_: **26.1x**
- 2026E P/E: **14.2x**  (TTM 35.4x, fwd 14.2x)
- EV 16.73B, 26E rev 6.39B, 26E EPS 20.71x


**3) Performance:**


- L1M 9.7% · L3M 29.9% · L12M -11.6% · -13.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 9.7%, 3M 29.9%; -13.9% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-12 | 4.25 | 4.75 | 11.88 |
| 2026-02-12 | 4.33 | 4.33 | -0.11 |
| 2025-10-28 | 3.75 | 3.88 | 3.4 |
| 2025-08-05 | 3.33 | 3.61 | 8.45 |


_Highlights:_ strong FCF margin (15.4%); beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## EA — Electronic Arts Inc.  (Communication Services / Electronic Gaming & Multimedia)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2023 | 7.43B | n/a | 10.8% | 25.9% | 1.55B | 1.34B | 18.1% |
| 2024 | 7.56B | 1.8% | 16.8% | 27.1% | 2.31B | 2.12B | 28.0% |
| 2025 | 7.46B | -1.3% | 15.0% | 27.1% | 2.08B | 1.86B | 24.9% |
| 2026 | 7.53B | 0.9% | 11.8% | 20.7% | 2.55B | 2.32B | 30.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.90B | 13.4% | 549.0M | 495.0M |
| 2025-06 | 1.67B | 12.0% | 17.0M | -55.0M |
| 2025-09 | 1.84B | 7.4% | 130.0M | 87.0M |
| 2025-12 | 1.90B | 4.6% | 1.83B | 1.77B |
| 2026-03 | 2.12B | 21.7% | 580.0M | 519.0M |


**2) Valuation:**


- 2026E TEV/Sales: **5.9x**  (TTM 6.8x)
- 2026E TEV/EBITDA _est_: **30.0x**  (TTM 34.7x)
- 2026E TEV/FCF _est_: **20.1x**
- 2026E P/E: **34.2x**  (TTM 60.0x, fwd 21.8x)
- EV 51.50B, 26E rev 8.71B, 26E EPS 6.13x


**3) Performance:**


- L1M 2.1% · L3M 3.8% · L12M 34.8% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 2.1%, 3M 3.8%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 2.36 | 1.59 | -32.35 |
| 2026-02-03 | 1.48 | 0.35 | -76.4 |
| 2025-10-28 | 0.35 | 0.54 | 52.69 |
| 2025-07-29 | 0.13 | 0.25 | 97.53 |


_Highlights:_ revenue growth accelerating; strong FCF margin (30.8%); beat EPS 2/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## WY — Weyerhaeuser Company  (Real Estate / REIT - Specialty)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 10.18B | n/a | 18.5% | 30.0% | 2.83B | 2.36B | 23.2% |
| 2023 | 7.67B | -24.6% | 10.9% | 22.4% | 1.43B | 753.0M | 9.8% |
| 2024 | 7.12B | -7.2% | 5.6% | 16.8% | 1.01B | 341.0M | 4.8% |
| 2025 | 6.91B | -3.1% | 4.7% | 15.1% | 562.0M | -381.0M | -5.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.76B | 4.7% | 70.0M | -23.0M |
| 2025-06 | 1.88B | 4.6% | 396.0M | 284.0M |
| 2025-09 | 1.72B | 4.7% | 210.0M | -376.0M |
| 2025-12 | 1.54B | 4.8% | -114.0M | -266.0M |
| 2026-03 | 1.73B | 9.0% | 52.0M | -60.0M |
| 2026-06 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **3.0x**  (TTM 3.4x)
- 2026E TEV/EBITDA _est_: **30.0x**  (TTM 33.4x)
- 2026E TEV/FCF _est_: **1515.4x**
- 2026E P/E: **37.7x**  (TTM 37.9x, fwd 37.7x)
- EV 22.96B, 26E rev 7.62B, 26E EPS 0.66x


**3) Performance:**


- L1M 6.2% · L3M 3.0% · L12M 1.5% · -6.0% from 12-mo high


**4) Reason for breakout:**


>=5% up-day on >=2x volume, gap-up and held, range expansion (>=2x ATR); 1M 6.2%, 3M 3.0%; -6.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 0.08 | 0.13 | 66.58 |
| 2026-04-30 | 0.05 | 0.11 | 119.91 |
| 2026-01-29 | -0.13 | -0.09 | 30.79 |
| 2025-10-30 | -0.08 | 0.06 | 177.36 |


_Highlights:_ revenue growth accelerating; beat EPS all last 4 quarters


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CBOE — Cboe Global Markets, Inc.  (Financial Services / Financial Data & Stock Exchanges)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 3.96B | n/a | 5.9% | 16.7% | 651.1M | 591.3M | 14.9% |
| 2023 | 3.77B | -4.7% | 20.2% | 33.6% | 1.08B | 1.03B | 27.3% |
| 2024 | 4.09B | 8.5% | 18.7% | 31.0% | 1.10B | 1.04B | 25.4% |
| 2025 | 4.71B | 15.1% | 23.3% | 36.9% | 1.75B | 1.68B | 35.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.20B | 21.0% | 912.9M | 898.2M |
| 2025-06 | 1.17B | 20.0% | 333.7M | 313.4M |
| 2025-09 | 1.14B | 26.3% | 153.9M | 137.9M |
| 2025-12 | 1.20B | 26.0% | 352.1M | 332.1M |
| 2026-03 | 1.27B | 30.3% | 1.96B | 1.94B |
| 2026-06 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **10.3x**  (TTM 6.4x)
- 2026E TEV/EBITDA _est_: **27.7x**  (TTM 17.1x)
- 2026E TEV/FCF _est_: **49.3x**
- 2026E P/E: **20.4x**  (TTM 24.2x, fwd 20.4x)
- EV 30.48B, 26E rev 2.95B, 26E EPS 15.17x


**3) Performance:**


- L1M 25.2% · L3M 3.6% · L12M 29.0% · -15.2% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, range expansion (>=2x ATR); 1M 25.2%, 3M 3.6%; -15.2% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-31 | 3.49 | 3.56 | 2.01 |
| 2026-05-01 | 3.38 | 3.7 | 9.54 |
| 2026-02-06 | 2.95 | 3.06 | 3.76 |
| 2025-10-31 | 2.53 | 2.67 | 5.58 |


_Highlights:_ revenue +15.1% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (35.7%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MSFT — Microsoft Corporation  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2023 | 211.91B | n/a | 34.1% | 49.6% | 87.58B | 59.48B | 28.1% |
| 2024 | 245.12B | 15.7% | 36.0% | 53.7% | 118.55B | 74.07B | 30.2% |
| 2025 | 281.72B | 14.9% | 36.1% | 55.2% | 136.16B | 71.61B | 25.4% |
| 2026 | 331.84B | 17.8% | 40.3% | 62.5% | 182.94B | 66.99B | 20.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-06 | 76.44B | 35.6% | 42.65B | 25.57B |
| 2025-09 | 77.67B | 35.7% | 45.06B | 25.66B |
| 2025-12 | 81.27B | 47.3% | 35.76B | 5.88B |
| 2026-03 | 82.89B | 38.3% | 46.68B | 15.80B |
| 2026-06 | 90.01B | 39.7% | 55.44B | 19.64B |


**2) Valuation:**


- 2026E TEV/Sales: **7.5x**  (TTM 10.6x)
- 2026E TEV/EBITDA _est_: **12.9x**  (TTM 18.0x)
- 2026E TEV/FCF _est_: **152.6x**
- 2026E P/E: **20.0x**  (TTM 25.9x, fwd 20.0x)
- EV 3502.96B, 26E rev 465.58B, 26E EPS 23.28x


**3) Performance:**


- L1M 20.9% · L3M 14.2% · L12M -8.7% · -13.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 20.9%, 3M 14.2%; -13.7% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-29 | 4.24 | 4.74 | 11.81 |
| 2026-04-29 | 4.07 | 4.27 | 4.9 |
| 2026-01-28 | 3.92 | 4.14 | 5.69 |
| 2025-10-29 | 3.66 | 4.13 | 12.73 |


_Highlights:_ revenue +17.8% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (20.2%); beat EPS all last 4 quarters


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
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 1.69B | 60.6% | 1.06B | 1.04B |
| 2025-09 | 1.54B | 59.1% | 968.1M | 949.7M |
| 2025-12 | 1.65B | 71.7% | 1.13B | 1.10B |
| 2026-03 | 1.88B | 61.4% | 1.26B | 1.24B |
| 2026-06 | 1.71B | 61.1% | 947.1M | 923.5M |


**2) Valuation:**


- 2026E TEV/Sales: **13.3x**  (TTM 14.5x)
- 2026E TEV/EBITDA _est_: **18.8x**  (TTM 20.5x)
- 2026E TEV/FCF _est_: **30.9x**
- 2026E P/E: **20.7x**  (TTM 22.7x, fwd 20.7x)
- EV 97.88B, 26E rev 7.36B, 26E EPS 12.94x


**3) Performance:**


- L1M 15.9% · L3M -6.5% · L12M 0.2% · -15.6% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 15.9%, 3M -6.5%; -15.6% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-22 | 2.91 | 2.99 | 2.75 |
| 2026-04-22 | 3.37 | 3.36 | -0.25 |
| 2026-02-04 | 2.74 | 2.77 | 0.99 |
| 2025-10-22 | 2.63 | 2.68 | 1.98 |


_Highlights:_ net margin expanding; strong FCF margin (64.3%); beat EPS 3/4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## HII — Huntington Ingalls Industries,   (Industrials / Aerospace & Defense)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 10.68B | n/a | 5.4% | 11.0% | 766.0M | 482.0M | 4.5% |
| 2023 | 11.45B | 7.3% | 5.9% | 11.3% | 970.0M | 678.0M | 5.9% |
| 2024 | 11.54B | 0.7% | 4.8% | 9.2% | 393.0M | 26.0M | 0.2% |
| 2025 | 12.48B | 8.2% | 4.8% | 9.7% | 1.20B | 794.0M | 6.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 3.08B | 4.9% | 823.0M | 727.0M |
| 2025-09 | 3.19B | 4.5% | 118.0M | 13.0M |
| 2025-12 | 3.48B | 4.6% | 650.0M | 516.0M |
| 2026-03 | 3.10B | 4.8% | -390.0M | -464.0M |
| 2026-06 | 3.42B | 6.1% | -31.0M | -150.0M |


**2) Valuation:**


- 2026E TEV/Sales: **1.1x**  (TTM 1.2x)
- 2026E TEV/EBITDA _est_: **12.7x**  (TTM 13.5x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **15.9x**  (TTM 19.5x, fwd 15.9x)
- EV 15.79B, 26E rev 14.03B, 26E EPS 20.56x


**3) Performance:**


- L1M 17.0% · L3M -10.0% · L12M 28.4% · -27.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 17.0%, 3M -10.0%; -27.7% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 3.82 | 5.27 | 38.02 |
| 2026-05-05 | 3.73 | 3.79 | 1.68 |
| 2026-02-05 | 3.85 | 4.04 | 5.03 |
| 2025-10-30 | 3.4 | 3.68 | 8.31 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## BEN — Franklin Resources, Inc.  (Financial Services / Asset Management)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 8.28B | n/a | 15.6% | 26.7% | 1.96B | 1.87B | 22.6% |
| 2023 | 7.85B | -5.1% | 11.2% | 24.3% | 1.09B | 940.4M | 12.0% |
| 2024 | 8.48B | 8.0% | 5.5% | 16.2% | 971.3M | 794.2M | 9.4% |
| 2025 | 8.77B | 3.5% | 6.0% | 16.1% | 1.07B | 911.6M | 10.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.11B | 7.2% | -50.1M | -87.6M |
| 2025-06 | 2.06B | 4.5% | 1.28B | 1.27B |
| 2025-09 | 2.34B | 5.0% | -20.7M | -51.9M |
| 2025-12 | 2.33B | 11.0% | -255.1M | -255.1M |
| 2026-03 | 2.29B | 11.7% | -27.6M | -27.6M |


**2) Valuation:**


- 2026E TEV/Sales: **2.1x**  (TTM 2.2x)
- 2026E TEV/EBITDA _est_: **12.6x**  (TTM 13.0x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **10.8x**  (TTM 23.0x, fwd 10.8x)
- EV 20.57B, 26E rev 9.60B, 26E EPS 3.12x


**3) Performance:**


- L1M -0.6% · L3M 14.1% · L12M 46.7% · -1.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, uptrend continuation off a dip; 1M -0.6%, 3M 14.1%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-31 | 0.66 | 0.72 | 8.28 |
| 2026-04-28 | 0.55 | 0.71 | 28.64 |
| 2026-01-30 | 0.55 | 0.7 | 27.53 |
| 2025-11-07 | 0.59 | 0.67 | 14.03 |


_Highlights:_ net margin expanding; beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## BMY — Bristol-Myers Squibb Company  (Healthcare / Drug Manufacturers - General)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 46.16B | n/a | 13.7% | 41.6% | 13.07B | 11.95B | 25.9% |
| 2023 | 45.01B | -2.5% | 17.8% | 43.0% | 13.86B | 12.65B | 28.1% |
| 2024 | 48.30B | 7.3% | -18.5% | 6.6% | 15.19B | 13.94B | 28.9% |
| 2025 | 48.20B | -0.2% | 14.6% | 31.6% | 14.16B | 12.85B | 26.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 12.27B | 10.7% | 3.92B | 3.56B |
| 2025-09 | 12.22B | 18.0% | 6.31B | 5.99B |
| 2025-12 | 12.50B | 8.7% | 1.97B | 1.60B |
| 2026-03 | 11.49B | 23.3% | 1.10B | 757.0M |
| 2026-06 | 12.97B | 25.6% | 3.39B | 3.09B |


**2) Valuation:**


- 2026E TEV/Sales: **3.5x**  (TTM 3.4x)
- 2026E TEV/EBITDA _est_: **9.1x**  (TTM 8.8x)
- 2026E TEV/FCF _est_: **21.2x**
- 2026E P/E: **10.1x**  (TTM 14.4x, fwd 10.1x)
- EV 167.40B, 26E rev 47.81B, 26E EPS 6.47x


**3) Performance:**


- L1M 17.0% · L3M 9.0% · L12M 48.9% · 0.0% from 12-mo high


**4) Reason for breakout:**


new 6-month high, uptrend continuation off a dip; 1M 17.0%, 3M 9.0%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 1.6 | 2.04 | 27.74 |
| 2026-04-30 | 1.42 | 1.58 | 11.18 |
| 2026-02-05 | 1.2 | 1.26 | 4.57 |
| 2025-10-30 | 1.52 | 1.63 | 7.55 |


_Highlights:_ net margin expanding; strong FCF margin (26.7%); beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MHK — Mohawk Industries, Inc.  (Consumer Cyclical / Furnishings, Fixtures & Appliances)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 11.74B | n/a | 0.2% | 7.1% | 669.2M | 88.5M | 0.8% |
| 2023 | 11.14B | -5.1% | -4.0% | 3.1% | 1.33B | 716.3M | 6.4% |
| 2024 | 10.84B | -2.7% | 4.7% | 12.3% | 1.13B | 679.5M | 6.3% |
| 2025 | 10.79B | -0.5% | 3.4% | 10.6% | 1.06B | 616.2M | 5.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.53B | 2.9% | 3.7M | -85.4M |
| 2025-06 | 2.80B | 5.2% | 206.3M | 126.1M |
| 2025-09 | 2.76B | 3.9% | 386.6M | 310.3M |
| 2025-12 | 2.70B | 1.6% | 459.6M | 265.2M |
| 2026-03 | 2.73B | 4.3% | 110.1M | 7.8M |
| 2026-06 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **0.9x**  (TTM 0.9x)
- 2026E TEV/EBITDA _est_: **6.5x**  (TTM 6.5x)
- 2026E TEV/FCF _est_: **10.1x**
- 2026E P/E: **12.4x**  (TTM 16.3x, fwd 12.4x)
- EV 9.85B, 26E rev 11.31B, 26E EPS 9.93x


**3) Performance:**


- L1M 2.7% · L3M 16.6% · L12M 5.0% · -11.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 2.7%, 3M 16.6%; -11.9% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 2.58 | 3.67 | 42.04 |
| 2026-04-30 | 1.81 | 1.9 | 4.81 |
| 2026-02-12 | 1.98 | 2.0 | 1.12 |
| 2025-10-23 | 2.64 | 2.67 | 1.16 |


_Highlights:_ revenue growth accelerating; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## NTAP — NetApp, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2023 | 6.36B | n/a | 20.0% | 21.7% | 1.11B | 868.0M | 13.6% |
| 2024 | 6.27B | -1.5% | 15.7% | 25.2% | 1.69B | 1.53B | 24.4% |
| 2025 | 6.57B | 4.9% | 18.0% | 25.7% | 1.51B | 1.34B | 20.4% |
| 2026 | 6.92B | 5.4% | 18.4% | 28.3% | 2.07B | 1.87B | 27.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-04 | 1.73B | 19.6% | 675.0M | 640.0M |
| 2025-07 | 1.56B | 14.9% | 673.0M | 620.0M |
| 2025-10 | 1.71B | 17.9% | 127.0M | 78.0M |
| 2026-01 | 1.71B | 19.5% | 317.0M | 271.0M |
| 2026-04 | 1.95B | 20.7% | 950.0M | 900.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.3x**  (TTM 4.9x)
- 2026E TEV/EBITDA _est_: **15.9x**  (TTM 18.1x)
- 2026E TEV/FCF _est_: **23.1x**
- 2026E P/E: **18.1x**  (TTM 28.1x, fwd 18.1x)
- EV 34.12B, 26E rev 7.89B, 26E EPS 9.84x


**3) Performance:**


- L1M 14.5% · L3M 61.6% · L12M 73.5% · -1.1% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 14.5%, 3M 61.6%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-28 | 2.27 | 2.43 | 7.22 |
| 2026-02-26 | 2.06 | 2.12 | 2.78 |
| 2025-11-25 | 1.88 | 2.05 | 8.76 |
| 2025-08-27 | 1.54 | 1.55 | 0.74 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (27.0%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## REGN — Regeneron Pharmaceuticals, Inc.  (Healthcare / Biotechnology)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 12.17B | n/a | 35.6% | 43.2% | 5.01B | 3.40B | 27.9% |
| 2023 | 13.12B | 7.8% | 30.1% | 35.8% | 4.59B | 3.67B | 28.0% |
| 2024 | 14.20B | 8.3% | 31.1% | 37.4% | 4.42B | 3.54B | 24.9% |
| 2025 | 14.34B | 1.0% | 31.4% | 40.6% | 4.98B | 3.77B | 26.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-06 | 3.68B | 37.9% | 1.14B | 737.6M |
| 2025-09 | 3.75B | 38.9% | 1.62B | 1.37B |
| 2025-12 | 3.88B | 21.7% | 1.17B | 880.0M |
| 2026-03 | 3.61B | 20.2% | 1.08B | 799.4M |
| 2026-06 | 4.29B | 30.2% | 813.0M | 521.8M |


**2) Valuation:**


- 2026E TEV/Sales: **3.9x**  (TTM 4.6x)
- 2026E TEV/EBITDA _est_: **12.8x**  (TTM 15.1x)
- 2026E TEV/FCF _est_: **19.6x**
- 2026E P/E: **15.2x**  (TTM 18.9x, fwd 12.8x)
- EV 70.86B, 26E rev 18.31B, 26E EPS 50.21x


**3) Performance:**


- L1M 22.1% · L3M 8.0% · L12M 38.3% · -5.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 22.1%, 3M 8.0%; -5.9% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 10.21 | 14.29 | 39.99 |
| 2026-04-29 | 8.9 | 9.47 | 6.38 |
| 2026-01-30 | 10.75 | 11.44 | 6.38 |
| 2025-10-28 | 9.64 | 11.83 | 22.66 |


_Highlights:_ net margin expanding; strong FCF margin (26.3%); beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ORCL — Oracle Corporation  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2023 | 49.95B | n/a | 17.0% | 37.5% | 17.16B | 8.47B | 17.0% |
| 2024 | 52.96B | 6.0% | 19.8% | 40.4% | 18.67B | 11.81B | 22.3% |
| 2025 | 57.40B | 8.4% | 21.7% | 41.7% | 20.82B | -394.0M | -0.7% |
| 2026 | 67.36B | 17.3% | 25.4% | 49.7% | 31.98B | -23.69B | -35.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-02 | n/a | n/a | n/a | n/a |
| 2025-05 | 15.90B | 21.5% | 6.16B | -2.92B |
| 2025-08 | 14.93B | 19.6% | 8.14B | -362.0M |
| 2025-11 | 16.06B | 38.2% | 2.07B | -9.97B |
| 2026-02 | 17.19B | 21.6% | 7.15B | -11.48B |
| 2026-05 | 19.18B | 22.4% | 14.62B | -1.87B |


**2) Valuation:**


- 2026E TEV/Sales: **3.9x**  (TTM 7.6x)
- 2026E TEV/EBITDA _est_: **8.7x**  (TTM 16.9x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **11.9x**  (TTM 22.3x, fwd 11.9x)
- EV 515.13B, 26E rev 130.47B, 26E EPS 10.89x


**3) Performance:**


- L1M -8.5% · L3M -19.3% · L12M -47.6% · -60.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -8.5%, 3M -19.3%; -60.0% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-06-10 | 1.96 | 2.11 | 7.52 |
| 2026-03-10 | 1.69 | 1.79 | 5.69 |
| 2025-12-10 | 1.64 | 2.26 | 38.04 |
| 2025-09-09 | 1.48 | 1.47 | -0.62 |


_Highlights:_ revenue +17.3% latest FY; revenue growth accelerating; net margin expanding; beat EPS 3/4 quarters


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## PDD — PDD Holdings Inc.  (Consumer Cyclical / Internet Retail)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 130.56B | n/a | 24.2% | 30.0% | 48.51B | 47.87B | 36.7% |
| 2023 | 247.64B | 89.7% | 24.2% | 29.8% | 94.16B | 93.58B | 37.8% |
| 2024 | 393.84B | 59.0% | 28.5% | 34.4% | 121.93B | 120.96B | 30.7% |
| 2025 | 431.85B | 9.7% | 22.7% | 28.4% | 106.94B | 105.79B | 24.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 95.67B | 15.4% | 15.52B | 15.52B |
| 2025-06 | 103.98B | 29.6% | 21.64B | 21.64B |
| 2025-09 | 108.28B | 27.1% | 45.66B | 45.66B |
| 2025-12 | 123.91B | 18.6% | 24.12B | 22.97B |
| 2026-03 | 106.23B | 11.8% | 16.45B | 16.45B |


**2) Valuation:**


- 2026E TEV/Sales: **-0.6x**  (TTM -0.7x)
- 2026E TEV/EBITDA _est_: **-2.6x**  (TTM -3.2x)
- 2026E TEV/FCF _est_: **-3.5x**
- 2026E P/E: **1.1x**  (TTM 9.3x, fwd 7.2x)
- EV -306.61B, 26E rev 535.72B, 26E EPS 82.59x


**3) Performance:**


- L1M 7.3% · L3M -11.3% · L12M -21.6% · -35.9% from 12-mo high


**4) Reason for breakout:**


volatility-squeeze release; 1M 7.3%, 3M -11.3%; -35.9% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-27 | 16.37 | 9.51 | -41.89 |
| 2026-03-25 | 21.02 | 17.69 | -15.84 |
| 2025-11-18 | 16.57 | 21.08 | 27.22 |
| 2025-08-25 | 14.8 | 22.07 | 49.13 |


_Highlights:_ strong FCF margin (24.5%); beat EPS 2/4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CFG — Citizens Financial Group, Inc.  (Financial Services / Banks - Regional)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 8.02B | n/a | 25.8% | n/a | 4.12B | 3.99B | 49.8% |
| 2023 | 8.22B | 2.5% | 19.6% | n/a | 2.96B | 2.79B | 33.9% |
| 2024 | 7.81B | -5.0% | 19.3% | n/a | 2.00B | 1.88B | 24.1% |
| 2025 | 8.25B | 5.6% | 22.2% | n/a | 2.21B | 2.04B | 24.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.94B | 19.3% | -213.0M | -227.0M |
| 2025-06 | 2.04B | 21.4% | 886.0M | 853.0M |
| 2025-09 | 2.12B | 23.3% | 1.70B | 1.66B |
| 2025-12 | 2.16B | 24.5% | -158.0M | -250.0M |
| 2026-03 | 2.17B | 23.8% | 237.0M | 237.0M |
| 2026-06 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **3.5x**  (TTM 4.3x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **11.0x**  (TTM 15.6x, fwd 11.0x)
- EV 34.88B, 26E rev 9.98B, 26E EPS 6.51x


**3) Performance:**


- L1M 0.4% · L3M 10.9% · L12M 52.9% · -3.1% from 12-mo high


**4) Reason for breakout:**


volatility-squeeze release; 1M 0.4%, 3M 10.9%; -3.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-16 | 1.25 | 1.3 | 4.39 |
| 2026-04-16 | 1.09 | 1.13 | 3.73 |
| 2026-01-21 | 1.11 | 1.13 | 2.24 |
| 2025-10-15 | 1.03 | 1.05 | 2.27 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (24.7%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CVX — Chevron Corporation  (Energy / Oil & Gas Integrated)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 235.72B | n/a | 15.0% | 27.8% | 49.60B | 37.63B | 16.0% |
| 2023 | 196.91B | -16.5% | 10.9% | 24.3% | 35.61B | 19.78B | 10.0% |
| 2024 | 193.41B | -1.8% | 9.1% | 23.7% | 31.49B | 15.04B | 7.8% |
| 2025 | 184.43B | -4.6% | 6.7% | 22.5% | 33.94B | 16.59B | 9.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 46.10B | 7.6% | 5.19B | 1.26B |
| 2025-06 | 44.38B | 5.6% | 8.58B | 4.86B |
| 2025-09 | 48.17B | 7.3% | 9.38B | 4.94B |
| 2025-12 | 45.79B | 6.0% | 10.79B | 5.53B |
| 2026-03 | 47.56B | 4.6% | 2.51B | -1.55B |
| 2026-06 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **2.1x**  (TTM 2.1x)
- 2026E TEV/EBITDA _est_: **8.6x**  (TTM 8.5x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **15.4x**  (TTM 18.9x, fwd 15.4x)
- EV 431.94B, 26E rev 207.32B, 26E EPS 12.78x


**3) Performance:**


- L1M 18.8% · L3M 2.8% · L12M 33.5% · -5.9% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 18.8%, 3M 2.8%; -5.9% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-31 | 5.58 | 6.06 | 8.63 |
| 2026-05-01 | 0.97 | 1.41 | 45.56 |
| 2026-01-30 | 1.44 | 1.52 | 5.2 |
| 2025-10-31 | 1.71 | 1.85 | 8.39 |


_Highlights:_ beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ERIE — Erie Indemnity Company  (Financial Services / Insurance Brokers)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 2.85B | n/a | 10.5% | n/a | 366.2M | 298.9M | 10.5% |
| 2023 | 3.31B | 16.1% | 13.5% | n/a | 381.2M | 288.6M | 8.7% |
| 2024 | 3.86B | 16.7% | 15.5% | n/a | 611.2M | 486.4M | 12.6% |
| 2025 | 4.15B | 7.4% | 13.5% | n/a | 686.7M | 571.0M | 13.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 1.29B | 13.5% | n/a | 157.3M |
| 2025-09 | 1.30B | 14.0% | n/a | 184.4M |
| 2025-12 | 333.5M | 19.0% | n/a | 140.8M |
| 2026-03 | 1.23B | 12.2% | n/a | 54.5M |
| 2026-06 | 1.31B | 13.7% | n/a | 173.4M |


**2) Valuation:**


- 2026E TEV/Sales: **n/a**  (TTM 3.0x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM 14.9x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **n/a**  (TTM 22.0x, fwd 17.3x)
- EV 12.41B, 26E rev 0, 26E EPS n/a


**3) Performance:**


- L1M -2.3% · L3M 11.2% · L12M -30.0% · -33.0% from 12-mo high


**4) Reason for breakout:**


gap-up and held; 1M -2.3%, 3M 11.2%; -33.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 3.35 | 3.45 | 2.92 |
| 2026-04-23 | 3.06 | 2.9 | -5.26 |
| 2026-02-23 | 1.59 | 2.76 | 73.67 |
| 2025-10-30 | 3.37 | 3.49 | 3.5 |


_Highlights:_ beat EPS 3/4 quarters


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
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.03B | 34.9% | 2.35B | 663.0M |
| 2025-06 | 3.65B | 19.1% | 1.68B | -2.31B |
| 2025-09 | 3.91B | 26.1% | 2.38B | 73.0M |
| 2025-12 | 3.34B | -43.6% | 2.34B | 873.0M |
| 2026-03 | 4.21B | 0.6% | 1.83B | 581.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.6x**  (TTM 5.3x)
- 2026E TEV/EBITDA _est_: **6.5x**  (TTM 7.6x)
- 2026E TEV/FCF _est_: **47.2x**
- 2026E P/E: **11.7x**  (TTM 209.2x, fwd 11.7x)
- EV 76.98B, 26E rev 16.88B, 26E EPS 17.36x


**3) Performance:**


- L1M 18.0% · L3M -0.8% · L12M 37.9% · -4.5% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 18.0%, 3M -0.8%; -4.5% from 12-mo high; trend tag: up


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


## IEX — IDEX Corporation  (Industrials / Specialty Industrial Machinery)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 3.18B | n/a | 18.4% | 28.6% | 557.4M | 489.4M | 15.4% |
| 2023 | 3.27B | 2.9% | 18.2% | 29.4% | 716.7M | 626.8M | 19.1% |
| 2024 | 3.27B | -0.2% | 15.4% | 26.3% | 668.1M | 603.0M | 18.4% |
| 2025 | 3.46B | 5.8% | 14.0% | 26.1% | 680.4M | 616.8M | 17.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-06 | 865.4M | 15.2% | 161.7M | 146.9M |
| 2025-09 | 878.7M | 14.5% | 203.5M | 188.7M |
| 2025-12 | 899.1M | 14.3% | 209.5M | 189.8M |
| 2026-03 | 886.9M | 13.5% | 103.7M | 86.0M |
| 2026-06 | 920.6M | 15.6% | 200.0M | 177.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.7x**  (TTM 5.1x)
- 2026E TEV/EBITDA _est_: **17.4x**  (TTM 18.9x)
- 2026E TEV/FCF _est_: **30.4x**
- 2026E P/E: **24.3x**  (TTM 33.1x, fwd 24.3x)
- EV 18.25B, 26E rev 3.88B, 26E EPS 9.46x


**3) Performance:**


- L1M 2.8% · L3M 6.5% · L12M 42.4% · -1.4% from 12-mo high


**4) Reason for breakout:**


volatility-squeeze release; 1M 2.8%, 3M 6.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-29 | 2.11 | 2.32 | 9.93 |
| 2026-04-29 | 1.77 | 2.0 | 12.8 |
| 2026-02-04 | 2.04 | 2.1 | 2.89 |
| 2025-10-29 | 1.93 | 2.03 | 5.17 |


_Highlights:_ revenue growth accelerating; strong FCF margin (17.8%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MPC — Marathon Petroleum Corporation  (Energy / Oil & Gas Refining & Marketing)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 177.45B | n/a | 8.2% | 14.0% | 16.36B | 13.94B | 7.9% |
| 2023 | 148.38B | -16.4% | 6.5% | 12.5% | 14.12B | 12.23B | 8.2% |
| 2024 | 138.86B | -6.4% | 2.5% | 7.6% | 8.66B | 6.13B | 4.4% |
| 2025 | 132.70B | -4.4% | 3.0% | 8.8% | 8.25B | 4.77B | 3.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 31.52B | -0.2% | -64.0M | -727.0M |
| 2025-06 | 33.80B | 3.6% | 2.64B | 1.94B |
| 2025-09 | 34.81B | 3.9% | 2.61B | 1.66B |
| 2025-12 | 32.57B | 4.7% | 3.07B | 1.89B |
| 2026-03 | 34.20B | 1.5% | 1.12B | 208.0M |


**2) Valuation:**


- 2026E TEV/Sales: **0.9x**  (TTM 1.0x)
- 2026E TEV/EBITDA _est_: **12.5x**  (TTM 12.8x)
- 2026E TEV/FCF _est_: **36.5x**
- 2026E P/E: **11.4x**  (TTM 20.8x, fwd 11.4x)
- EV 131.24B, 26E rev 138.95B, 26E EPS 27.77x


**3) Performance:**


- L1M 19.5% · L3M 27.9% · L12M 88.9% · -1.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 19.5%, 3M 27.9%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 0.75 | 1.65 | 120.63 |
| 2026-02-03 | 2.71 | 4.07 | 50.13 |
| 2025-11-04 | 3.16 | 3.01 | -4.86 |
| 2025-08-05 | 3.22 | 3.96 | 22.98 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## PANW — Palo Alto Networks, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 5.50B | n/a | -4.9% | 1.7% | 1.98B | 1.79B | 32.6% |
| 2023 | 6.89B | 25.3% | 6.4% | 12.6% | 2.78B | 2.63B | 38.2% |
| 2024 | 8.03B | 16.5% | 32.1% | 15.9% | 3.26B | 3.10B | 38.6% |
| 2025 | 9.22B | 14.9% | 12.3% | 21.0% | 3.72B | 3.47B | 37.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-01 | n/a | n/a | n/a | n/a |
| 2025-04 | 2.29B | 11.4% | 628.0M | 560.0M |
| 2025-07 | 2.54B | 10.0% | 1.02B | 934.5M |
| 2025-10 | 2.47B | 13.5% | 1.77B | 1.69B |
| 2026-01 | 2.59B | 16.7% | 554.0M | 384.0M |
| 2026-04 | 3.00B | -5.9% | 871.0M | 788.0M |


**2) Valuation:**


- 2026E TEV/Sales: **19.5x**  (TTM 25.4x)
- 2026E TEV/EBITDA _est_: **139.5x**  (TTM 181.6x)
- 2026E TEV/FCF _est_: **57.8x**
- 2026E P/E: **170.1x**  (TTM 286.1x, fwd 80.4x)
- EV 269.46B, 26E rev 13.81B, 26E EPS 1.95x


**3) Performance:**


- L1M -5.7% · L3M 85.0% · L12M 81.3% · -7.5% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -5.7%, 3M 85.0%; -7.5% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-06-02 | 0.8 | 0.85 | 6.62 |
| 2026-02-17 | 0.94 | 1.03 | 9.94 |
| 2025-11-19 | 0.89 | 0.93 | 4.36 |
| 2025-08-18 | 0.89 | 0.95 | 7.31 |


_Highlights:_ strong FCF margin (37.6%); beat EPS all last 4 quarters


_Issues:_ rich valuation (26E P/E 170.1x); high TEV/Sales 26E (19.5x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## TDY — Teledyne Technologies Incorpora  (Technology / Scientific & Technical Instruments)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.46B | n/a | 14.4% | 24.4% | 486.8M | 394.2M | 7.2% |
| 2023 | 5.64B | 3.2% | 15.7% | 24.0% | 836.1M | 721.2M | 12.8% |
| 2024 | 5.67B | 0.6% | 14.4% | 23.0% | 1.19B | 1.11B | 19.5% |
| 2025 | 6.12B | 7.9% | 14.6% | 24.4% | 1.19B | 1.07B | 17.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 1.51B | 13.9% | n/a | 196.3M |
| 2025-09 | 1.54B | 14.3% | n/a | 313.9M |
| 2025-12 | 1.61B | 17.1% | n/a | 339.2M |
| 2026-03 | 1.56B | 14.5% | n/a | 204.3M |
| 2026-06 | 1.66B | 15.1% | 315.2M | 284.7M |


**2) Valuation:**


- 2026E TEV/Sales: **4.6x**  (TTM 5.0x)
- 2026E TEV/EBITDA _est_: **18.6x**  (TTM 20.1x)
- 2026E TEV/FCF _est_: **32.4x**
- 2026E P/E: **24.6x**  (TTM 31.7x, fwd 24.6x)
- EV 32.08B, 26E rev 6.91B, 26E EPS 26.67x


**3) Performance:**


- L1M -0.9% · L3M 1.5% · L12M 19.1% · -4.8% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -0.9%, 3M 1.5%; -4.8% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-22 | 5.79 | 6.28 | 8.41 |
| 2026-04-22 | 5.47 | 5.8 | 5.97 |
| 2026-01-21 | 5.83 | 6.3 | 8.1 |
| 2025-10-22 | 5.47 | 5.57 | 1.8 |


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (17.6%); beat EPS all last 4 quarters


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
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.56B | 5.9% | 954.4M | 162.2M |
| 2025-06 | 4.26B | 14.8% | 858.3M | -47.8M |
| 2025-09 | 4.15B | 11.5% | 599.2M | -72.6M |
| 2025-12 | 4.06B | 13.4% | 1.51B | 542.3M |
| 2026-03 | 4.09B | 11.7% | 739.5M | -160.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.4x**  (TTM 4.7x)
- 2026E TEV/EBITDA _est_: **10.7x**  (TTM 14.8x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **22.6x**  (TTM 27.6x, fwd 22.6x)
- EV 77.20B, 26E rev 22.98B, 26E EPS 11.96x


**3) Performance:**


- L1M 5.4% · L3M 4.4% · L12M 66.0% · -4.9% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 5.4%, 3M 4.4%; -4.9% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-07 | 2.57 | 2.76 | 7.4 |
| 2026-02-19 | 2.4 | 2.69 | 12.12 |
| 2025-11-05 | 2.18 | 2.41 | 10.4 |
| 2025-08-07 | 1.98 | 2.02 | 2.2 |


_Highlights:_ revenue growth accelerating; net margin expanding; beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## VLO — Valero Energy Corporation  (Energy / Oil & Gas Refining & Marketing)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 176.38B | n/a | 6.5% | 10.4% | 12.57B | 10.89B | 6.2% |
| 2023 | 144.77B | -17.9% | 6.1% | 10.4% | 9.23B | 8.32B | 5.7% |
| 2024 | 129.88B | -10.3% | 2.1% | 5.4% | 6.68B | 5.78B | 4.4% |
| 2025 | 122.69B | -5.5% | 1.9% | 5.5% | 5.83B | 5.03B | 4.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 29.89B | 2.4% | 936.0M | 786.0M |
| 2025-09 | 32.17B | 3.4% | 1.88B | 1.70B |
| 2025-12 | 30.37B | 3.7% | 2.06B | 1.84B |
| 2026-03 | 32.38B | 3.9% | 1.39B | 1.23B |
| 2026-06 | 44.48B | 8.4% | 5.58B | 5.35B |


**2) Valuation:**


- 2026E TEV/Sales: **0.8x**  (TTM 0.7x)
- 2026E TEV/EBITDA _est_: **7.7x**  (TTM 7.2x)
- 2026E TEV/FCF _est_: **12.3x**
- 2026E P/E: **11.4x**  (TTM 13.1x, fwd 11.6x)
- EV 96.83B, 26E rev 124.21B, 26E EPS 27.35x


**3) Performance:**


- L1M 16.6% · L3M 25.0% · L12M 131.1% · -0.2% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 16.6%, 3M 25.0%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 10.13 | 12.54 | 23.84 |
| 2026-04-30 | 3.16 | 4.22 | 33.47 |
| 2026-01-29 | 3.27 | 3.82 | 16.95 |
| 2025-10-23 | 3.05 | 3.66 | 19.88 |


_Highlights:_ revenue growth accelerating; beat EPS all last 4 quarters


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
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.64B | 13.2% | 1.10B | 306.0M |
| 2025-06 | 2.18B | 27.7% | 1.18B | 514.0M |
| 2025-09 | 2.12B | 9.7% | 1.46B | 741.0M |
| 2025-12 | 1.99B | 14.0% | 808.0M | 218.0M |
| 2026-03 | 2.33B | 19.2% | 554.0M | 8.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.3x**  (TTM 2.2x)
- 2026E TEV/EBITDA _est_: **3.7x**  (TTM 3.5x)
- 2026E TEV/FCF _est_: **11.4x**
- 2026E P/E: **9.0x**  (TTM 8.7x, fwd 9.0x)
- EV 18.38B, 26E rev 8.00B, 26E EPS 4.12x


**3) Performance:**


- L1M 17.9% · L3M -7.7% · L12M 98.3% · -14.8% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 17.9%, 3M -7.7%; -14.8% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-06 | 1.14 | 1.38 | 20.9 |
| 2026-02-25 | 0.64 | 0.91 | 41.73 |
| 2025-11-05 | 0.79 | 0.93 | 17.59 |
| 2025-08-05 | 0.48 | 0.87 | 79.46 |


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
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 16.52B | 17.2% | 6.12B | 2.74B |
| 2025-06 | 14.00B | 14.1% | 3.48B | 199.0M |
| 2025-09 | 15.03B | 11.5% | 5.88B | 3.01B |
| 2025-12 | 13.39B | 10.8% | 4.32B | 1.29B |
| 2026-03 | 15.76B | 13.9% | 4.29B | 1.35B |


**2) Valuation:**


- 2026E TEV/Sales: **2.5x**  (TTM 2.8x)
- 2026E TEV/EBITDA _est_: **6.2x**  (TTM 7.0x)
- 2026E TEV/FCF _est_: **27.6x**
- 2026E P/E: **13.4x**  (TTM 20.4x, fwd 13.4x)
- EV 163.74B, 26E rev 66.65B, 26E EPS 9.00x


**3) Performance:**


- L1M 16.7% · L3M -3.5% · L12M 28.8% · -9.3% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 16.7%, 3M -3.5%; -9.3% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-04-30 | 1.69 | 1.89 | 11.52 |
| 2026-02-05 | 1.09 | 1.02 | -6.47 |
| 2025-11-06 | 1.41 | 1.61 | 14.05 |
| 2025-08-07 | 1.36 | 1.42 | 4.71 |


_Highlights:_ revenue growth accelerating; beat EPS 3/4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## GOOG — Alphabet Inc.  (Communication Services / Internet Content & Information)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 282.84B | n/a | 21.2% | 30.1% | 91.50B | 60.01B | 21.2% |
| 2023 | 307.39B | 8.7% | 24.0% | 31.9% | 101.75B | 69.50B | 22.6% |
| 2024 | 350.02B | 13.9% | 28.6% | 38.7% | 125.30B | 72.76B | 20.8% |
| 2025 | 402.84B | 15.1% | 32.8% | 44.9% | 164.71B | 73.27B | 18.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 96.43B | 29.2% | 27.75B | 5.30B |
| 2025-09 | 102.35B | 34.2% | 48.41B | 24.46B |
| 2025-12 | 113.83B | 30.3% | 52.40B | 24.55B |
| 2026-03 | 109.90B | 56.9% | 45.79B | 10.12B |
| 2026-06 | 119.80B | 93.7% | 39.07B | -5.86B |


**2) Valuation:**


- 2026E TEV/Sales: **7.0x**  (TTM 9.6x)
- 2026E TEV/EBITDA _est_: **18.1x**  (TTM 24.6x)
- 2026E TEV/FCF _est_: **138.3x**
- 2026E P/E: **24.2x**  (TTM 17.9x, fwd 24.2x)
- EV 4258.17B, 26E rev 605.84B, 26E EPS 14.73x


**3) Performance:**


- L1M -0.3% · L3M -6.6% · L12M 81.2% · -10.6% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -0.3%, 3M -6.6%; -10.6% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-22 | 2.91 | 9.11 | 212.9 |
| 2026-04-29 | 2.63 | 5.11 | 94.3 |
| 2026-02-04 | 2.64 | 2.82 | 6.78 |
| 2025-10-29 | 2.26 | 2.87 | 26.88 |


_Highlights:_ revenue +15.1% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (18.2%); beat EPS all last 4 quarters


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
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 5.70B | 16.4% | 2.15B | 466.0M |
| 2025-06 | 6.41B | 7.1% | 2.96B | 736.0M |
| 2025-09 | 6.62B | 12.5% | 2.79B | 1.02B |
| 2025-12 | 1.75B | 5.8% | 2.63B | 1.88B |
| 2026-03 | 5.23B | 64.0% | 1.28B | -273.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.3x**  (TTM 3.7x)
- 2026E TEV/EBITDA _est_: **6.5x**  (TTM 7.2x)
- 2026E TEV/FCF _est_: **23.3x**
- 2026E P/E: **14.5x**  (TTM 77.1x, fwd 14.5x)
- EV 78.48B, 26E rev 23.47B, 26E EPS 3.93x


**3) Performance:**


- L1M 19.0% · L3M -5.4% · L12M 31.2% · -13.4% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 19.0%, 3M -5.4%; -13.4% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-05-05 | 0.59 | 1.06 | 80.35 |
| 2026-02-18 | 0.17 | 0.31 | 83.77 |
| 2025-11-10 | 0.52 | 0.64 | 22.73 |
| 2025-08-06 | 0.31 | 0.39 | 24.79 |


_Highlights:_ revenue growth accelerating; strong FCF margin (19.0%); beat EPS all last 4 quarters


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## TT — Trane Technologies plc  (Industrials / Building Products & Equipment)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 15.99B | n/a | 11.0% | 17.0% | 1.50B | 1.21B | 7.6% |
| 2023 | 17.68B | 10.5% | 11.4% | 17.8% | 2.39B | 2.09B | 11.8% |
| 2024 | 19.84B | 12.2% | 12.9% | 19.5% | 3.15B | 2.77B | 14.0% |
| 2025 | 21.32B | 7.5% | 13.7% | 20.1% | 3.19B | 2.81B | 13.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | n/a | n/a | n/a | n/a |
| 2025-06 | 5.75B | 15.2% | 692.1M | 602.2M |
| 2025-09 | 5.74B | 14.8% | 1.00B | 935.6M |
| 2025-12 | 5.14B | 11.5% | 1.16B | 1.05B |
| 2026-03 | 4.97B | 11.8% | 626.2M | 546.5M |
| 2026-06 | 6.35B | 14.6% | 1.09B | 1.01B |


**2) Valuation:**


- 2026E TEV/Sales: **4.0x**  (TTM 4.7x)
- 2026E TEV/EBITDA _est_: **20.7x**  (TTM 24.0x)
- 2026E TEV/FCF _est_: **28.5x**
- 2026E P/E: **26.1x**  (TTM 33.9x, fwd 26.1x)
- EV 103.42B, 26E rev 25.79B, 26E EPS 17.40x


**3) Performance:**


- L1M -6.1% · L3M -7.4% · L12M 6.2% · -9.6% from 12-mo high


**4) Reason for breakout:**


gap-up and held; 1M -6.1%, 3M -7.4%; -9.6% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


| Report date | EPS est | EPS reported | Surprise % |
| --- | --- | --- | --- |
| 2026-07-30 | 4.26 | 4.31 | 1.15 |
| 2026-04-30 | 2.53 | 2.63 | 3.94 |
| 2026-01-29 | 2.81 | 2.86 | 1.63 |
| 2025-10-30 | 3.78 | 3.88 | 2.69 |


_Highlights:_ net margin expanding; beat EPS all last 4 quarters


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._
