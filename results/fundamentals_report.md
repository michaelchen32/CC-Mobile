# Fundamental / valuation / earnings dossier

Names that fired in the high-recall screen on the latest bar (2026-05-22). **Source: yfinance only** — the environment blocks all other sites, so literal earnings-call transcript text is not retrievable; the earnings section is a quantitative recap (EPS beat/miss + revenue/margin path) instead. Forward '2026E' = consensus next-fiscal-year (+1y) estimate; TEV/EBITDA & TEV/FCF 26E are estimated as forward revenue x trailing margin (marked _est_). Not investment advice.


## Master table

| ticker | name | sector | n_detectors | trend | rev_growth_TTM_% | net_margin_% | CFO_TTM | FCF_TTM | TEV/Sales_26E | TEV/EBITDA_26E_est | TEV/FCF_26E_est | PE_26E | TEV/Sales_TTM | PE_TTM | L1M_% | L3M_% | L12M_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ROST | Ross Stores, Inc. | Consumer Cyclical | 6 | up | 12.2 | 9.4 | 3026883072.0 | 1636926336.0 | 2.7 | 19.2 | 37.6 | 28.3 | 3.1 | 35.1 | -4.2 | 8.5 | 42.6 |
| HPE | Hewlett Packard Enterprise Comp | Technology | 5 | up | 18.4 | -0.3 | 4487000064.0 | 2551500032.0 | 1.4 | 10.5 | 20.1 | 13.7 | 1.7 |  | 27.8 | 46.8 | 90.1 |
| HPQ | HP Inc. | Technology | 5 | up | 6.9 | 4.5 | 3705999872.0 | 2825374976.0 | 0.5 | 6.2 | 9.7 | 8.5 | 0.5 | 9.6 | 5.5 | 9.8 | -23.7 |
| NTAP | NetApp, Inc. | Technology | 5 | up | 4.4 | 18.1 | 1792000000.0 | 1116000000.0 | 3.4 | 12.9 | 20.2 | 16.3 | 3.6 | 23.3 | 15.7 | 17.7 | 22.7 |
| BK | The Bank of New York Mellon Cor | Financial Services | 4 | up | 13.4 | 28.7 | 3304999936.0 |  | -3.0 |  |  | 14.2 | -3.2 | 17.0 | 0.5 | 15.1 | 56.4 |
| CSCO | Cisco Systems, Inc. | Technology | 4 | up | 12.0 | 19.7 | 13025000448.0 | 9288375296.0 | 7.0 | 25.2 | 46.1 | 25.3 | 7.9 | 40.1 | 39.9 | 54.7 | 97.3 |
| FTNT | Fortinet, Inc. | Technology | 4 | up | 20.1 | 27.5 | 2804400128.0 | 1813049984.0 | 10.7 | 32.1 | 41.8 | 38.9 | 13.0 | 51.7 | 49.0 | 43.5 | 18.9 |
| GS | Goldman Sachs Group, Inc. (The) | Financial Services | 4 | up | 14.5 | 29.4 | -39792001024.0 |  | 0.2 |  |  | 15.3 | 0.2 | 18.3 | 5.4 | 5.3 | 58.3 |
| NXPI | NXP Semiconductors N.V. | Technology | 4 | up | 12.2 | 21.0 | 3048000000.0 | 3119000064.0 | 5.4 | 14.2 | 21.9 | 17.7 | 6.7 | 29.9 | 36.4 | 19.9 | 40.6 |
| SNPS | Synopsys, Inc. | Technology | 4 | up | 65.5 | 13.8 | 2442895104.0 | 3096222464.0 | 9.9 | 48.9 | 25.5 | 31.1 | 13.1 | 81.6 | 13.9 | 14.9 | -2.9 |
| TXN | Texas Instruments Incorporated | Technology | 4 | up | 18.6 | 29.1 | 7824000000.0 | 1068249984.0 | 12.1 | 25.6 | 208.0 | 35.4 | 15.2 | 53.8 | 36.4 | 34.5 | 66.1 |
| CRWD | CrowdStrike Holdings, Inc. | Technology | 3 | up | 23.3 | -3.4 | 1612349056.0 | 1604615040.0 | 22.3 |  | 66.8 | 109.0 | 33.3 |  | 42.1 | 38.3 | 36.3 |
| FFIV | F5, Inc. | Technology | 3 | up | 11.0 | 22.0 | 1015414976.0 | 759182528.0 | 5.9 | 21.0 | 25.0 | 22.4 | 6.3 | 32.2 | 17.7 | 32.4 | 28.8 |
| SWKS | Skyworks Solutions, Inc. | Technology | 3 | up | -1.0 | 8.9 | 960000000.0 | 687837504.0 | 2.7 | 12.0 | 15.8 | 15.6 | 2.7 | 33.4 | 16.7 | 11.7 | -1.0 |
| DGX | Quest Diagnostics Incorporated | Healthcare | 3 | weak | 9.2 | 9.1 | 1850000000.0 | 947875008.0 | 2.3 | 11.4 | 26.8 | 16.9 | 2.5 | 21.8 | -2.5 | -9.4 | 10.1 |
| BAX | Baxter International Inc. | Healthcare | 2 | down | 2.9 | -9.7 | 1251000064.0 | 900875008.0 | 1.5 | 8.9 | 18.9 | 9.6 | 1.5 |  | -4.6 | -12.5 | -42.2 |
| BBY | Best Buy Co., Inc. | Consumer Cyclical | 2 | down | -1.0 | 2.6 | 1962000000.0 | 842499968.0 | 0.4 | 5.7 | 17.6 | 8.8 | 0.4 | 12.3 | -13.0 | -13.2 | -19.0 |
| COR | Cencora, Inc. | Healthcare | 2 | down | 3.8 | 0.8 | 2276133888.0 | -318246112.0 | 0.2 | 11.2 |  | 13.9 | 0.2 | 21.1 | -19.9 | -28.4 | -6.8 |
| EL | Estee Lauder Companies, Inc. (T | Consumer Defensive | 2 | down | 4.6 | -1.7 | 1798000000.0 | 1807624960.0 | 2.2 | 14.1 | 18.3 | 27.2 | 2.3 |  | 6.6 | -25.6 | 27.2 |
| MMM | 3M Company | Industrials | 2 | down | 1.3 | 11.1 | 2959000064.0 | 2322374912.0 | 3.3 | 13.4 | 35.9 | 16.2 | 3.5 | 29.6 | -2.9 | -14.9 | 0.7 |
| AMD | Advanced Micro Devices, Inc. | Technology | 2 | up | 37.8 | 13.4 | 9724999680.0 | 7173374976.0 | 9.5 | 48.1 | 49.8 | 36.1 | 19.3 | 155.5 | 52.4 | 104.6 | 260.3 |
| ANET | Arista Networks, Inc. | Technology | 2 | up | 35.1 | 38.3 | 5423699968.0 | 4362237440.0 | 12.2 | 28.0 | 27.2 | 34.6 | 18.0 | 52.9 | -11.8 | 0.3 | 44.5 |
| CZR | Caesars Entertainment, Inc. | Consumer Cyclical | 2 | up | 2.7 | -4.2 | 1288000000.0 | 752625024.0 | 2.6 | 8.4 | 39.2 | 33.6 | 2.7 |  | 0.4 | 53.3 | -9.4 |
| GNRC | Generac Holdlings Inc. | Industrials | 2 | up | 12.4 | 4.4 | 499111008.0 | 115297624.0 | 2.8 | 23.1 | 105.6 | 24.1 | 3.6 | 83.1 | 27.1 | 17.5 | 105.2 |
| KIM | Kimco Realty Corporation (HC) | Real Estate | 2 | up | 4.0 | 28.5 | 1139187968.0 | 838712128.0 | 10.8 | 17.8 | 27.8 | 28.1 | 11.3 | 27.7 | -3.2 | 2.4 | 14.3 |
| PLD | Prologis, Inc. | Real Estate | 2 | up | 8.3 | 39.6 | 5135817216.0 | 4854310400.0 | 18.8 | 26.9 | 36.4 | 42.8 | 18.5 | 36.5 | -1.2 | 1.9 | 35.1 |
| ABBV | AbbVie Inc. | Healthcare | 2 | weak | 12.4 | 5.8 | 21223999488.0 | 20811624448.0 | 6.1 | 12.8 | 18.4 | 13.4 | 7.0 | 106.5 | 0.7 | -8.4 | 22.4 |
| CL | Colgate-Palmolive Company | Consumer Defensive | 2 | weak | 8.4 | 10.0 | 4344999936.0 | 3319500032.0 | 3.6 | 15.1 | 22.4 | 22.5 | 3.8 | 35.3 | 6.0 | -8.3 | 3.2 |
| DXCM | DexCom, Inc. | Healthcare | 2 | weak | 15.0 | 19.3 | 1782499968.0 | 1056637504.0 | 4.6 | 17.1 | 20.9 | 23.9 | 5.5 | 31.3 | 0.7 | -12.0 | -28.8 |
| EW | Edwards Lifesciences Corporatio | Healthcare | 2 | weak | 16.7 | 17.4 | 1358599936.0 | 902137472.0 | 6.1 | 20.1 | 42.4 | 25.3 | 7.1 | 46.0 | 2.9 | 7.3 | 6.0 |
| JNJ | Johnson & Johnson | Healthcare | 2 | weak | 9.9 | 21.8 | 22869999616.0 | 12511375360.0 | 5.5 | 15.5 | 42.4 | 18.5 | 6.1 | 27.2 | -3.3 | -6.4 | 59.2 |
| BSX | Boston Scientific Corporation | Healthcare | 1 | down | 11.6 | 17.3 | 4341000192.0 | 2807124992.0 | 4.0 | 15.1 | 29.5 | 15.4 | 4.6 | 24.2 | -16.9 | -29.5 | -48.8 |
| DECK | Deckers Outdoor Corporation | Consumer Cyclical | 1 | down | 7.1 | 19.3 | 1013121024.0 | 758731904.0 | 2.2 | 8.7 | 15.6 | 14.0 | 2.4 | 14.7 | -13.6 | -19.2 | -26.5 |
| GPN | Global Payments Inc. | Industrials | 1 | down | 63.1 | -8.0 | 1812647040.0 | 7124387840.0 | 2.9 | 6.6 | 3.6 | 4.5 | 4.3 | 26.9 | -4.6 | -1.0 | -17.7 |
| LH | Labcorp Holdings Inc. | Healthcare | 1 | down | 5.8 | 6.7 | 1813500032.0 | 1142537472.0 | 1.8 | 11.1 | 21.9 | 13.4 | 1.9 | 23.1 | -6.0 | -11.2 | 4.4 |
| PEG | Public Service Enterprise Group | Utilities | 1 | down | 19.4 | 17.7 | 3520000000.0 | -171750000.0 | 4.8 | 12.9 |  | 17.0 | 4.9 | 17.6 | -6.8 | -10.8 | 2.1 |
| VST | Vistra Corp. | Utilities | 1 | down | 43.4 | 11.5 | 4670000128.0 | 476875008.0 | 2.9 | 8.2 | 116.2 | 14.2 | 3.7 | 26.3 | -15.6 | -18.4 | -9.3 |
| WRB | W.R. Berkley Corporation | Financial Services | 1 | down | 4.0 | 12.6 | 3506656000.0 | 3222230528.0 | 1.9 | 11.1 | 8.9 | 14.0 | 1.7 | 14.3 | 0.3 | -4.5 | -3.9 |
| AMAT | Applied Materials, Inc. | Technology | 1 | up | 11.4 | 29.3 | 7992999936.0 | 3154374912.0 | 8.1 | 25.3 | 74.5 | 27.0 | 11.6 | 41.0 | 12.0 | 23.2 | 153.0 |
| C | Citigroup, Inc. | Financial Services | 1 | up | 15.9 | 20.4 | -30797000704.0 |  | 0.0 |  |  | 10.1 | 0.0 | 15.5 | -4.1 | 11.9 | 67.6 |
| CAT | Caterpillar, Inc. | Industrials | 1 | up | 22.2 | 13.3 | 12320000000.0 | 3776624896.0 | 5.3 | 25.6 | 98.6 | 29.8 | 6.2 | 44.3 | 15.2 | 15.0 | 156.8 |
| CFG | Citizens Financial Group, Inc. | Financial Services | 1 | up | 13.8 | 25.0 | 2660999936.0 |  | 2.8 |  |  | 9.9 | 3.5 | 15.0 | -4.8 | -5.8 | 51.1 |
| DOC | Healthpeak Properties, Inc. | Real Estate | 1 | up | 7.1 | 7.7 | 1233410944.0 | 1109761536.0 | 8.2 | 15.3 | 21.3 | 146.4 | 8.5 | 61.8 | 13.4 | 17.3 | 22.4 |
| EMN | Eastman Chemical Company | Basic Materials | 1 | up | -4.9 | 4.6 | 1000000000.0 | 434000000.0 | 1.4 | 8.9 | 27.9 | 10.6 | 1.5 | 21.4 | -2.4 | -9.5 | -7.1 |
| ESS | Essex Property Trust, Inc. | Real Estate | 1 | up | 6.4 | 29.1 | 1080088960.0 | 983003264.0 | 12.3 | 18.9 | 24.6 | 46.6 | 12.5 | 31.0 | 7.7 | 7.5 | -0.3 |
| ETN | Eaton Corporation, PLC | Industrials | 1 | up | 16.8 | 14.0 | 4741000192.0 | 2646500096.0 | 4.8 | 21.5 | 51.5 | 24.9 | 5.9 | 38.2 | 2.0 | 3.2 | 22.8 |
| F | Ford Motor Company | Consumer Cyclical | 1 | up | 6.4 | -3.2 | 18919000064.0 | -2247500032.0 | 1.1 | 27.1 |  | 8.1 | 1.0 |  | 9.1 | -3.9 | 32.0 |
| FITB | Fifth Third Bancorp | Financial Services | 1 | up | 33.0 | 24.1 | 2175000064.0 |  | 4.4 |  |  | 10.2 | 6.8 | 16.7 | -4.4 | -9.6 | 24.6 |
| GEV | GE Vernova Inc. | Industrials | 1 | up | 16.3 | 23.8 | 9013999616.0 | 9315624960.0 | 5.3 | 61.3 | 22.5 | 43.3 | 7.0 | 30.7 | 7.2 | 30.9 | 142.9 |
| GLW | Corning Incorporated | Technology | 1 | up | 20.0 | 11.1 | 2905999872.0 | 612000000.0 | 7.7 | 32.1 | 205.0 | 46.0 | 10.7 | 94.0 | 15.5 | 44.0 | 314.2 |
| INTC | Intel Corporation | Technology | 1 | up | 7.2 | -5.9 | 9980000256.0 | -8301250048.0 | 9.5 | 36.2 |  | 78.1 | 11.6 |  | 58.8 | 132.5 | 405.4 |
| INVH | Invitation Homes Inc. | Real Estate | 1 | up | 9.2 | 21.0 | 1198760960.0 | 1021075392.0 | 9.0 | 16.7 | 24.4 | 43.9 | 9.4 | 30.7 | 6.3 | 4.7 | -13.0 |
| KEY | KeyCorp | Financial Services | 1 | up | 11.8 | 27.0 | 2286000128.0 |  | 4.8 |  |  | 10.1 | 5.7 | 13.3 | -2.9 | -2.1 | 32.6 |
| LNT | Alliant Energy Corporation | Utilities | 1 | up | 5.0 | 18.6 | 1288000000.0 | -1202625024.0 | 6.5 | 15.4 |  | 20.1 | 6.9 | 23.3 | -1.8 | 0.3 | 20.9 |
| MCHP | Microchip Technology Incorporat | Technology | 1 | up | 35.1 | 4.9 |  |  | 7.7 | 29.2 |  | 23.1 | 11.6 | 429.7 | 22.1 | 20.2 | 59.4 |
| MGM | MGM Resorts International | Consumer Cyclical | 1 | up | 4.2 | 1.0 | 2550087936.0 | 528360256.0 | 2.2 | 17.2 | 74.1 | 17.4 | 2.2 | 53.0 | -3.9 | 8.3 | 5.8 |
| MPWR | Monolithic Power Systems, Inc. | Technology | 1 | up | 26.1 | 23.0 | 832067968.0 | 491719136.0 | 16.7 | 57.5 | 100.3 | 52.4 | 25.5 | 113.8 | 10.5 | 32.6 | 112.7 |
| NTRS | Northern Trust Corporation | Financial Services | 1 | up | 13.9 | 22.4 | 2463699968.0 |  | 4.1 |  |  | 14.3 | 4.5 | 17.6 | 4.5 | 12.6 | 57.9 |
| NUE | Nucor Corporation | Basic Materials | 1 | up | 21.3 | 6.8 | 3756000000.0 | -384100000.0 | 1.5 | 10.2 |  | 14.7 | 1.7 | 23.0 | 18.3 | 24.3 | 96.8 |
| ON | ON Semiconductor Corporation | Technology | 1 | up | 4.7 | 9.5 | 1396600064.0 | 1282174976.0 | 6.1 | 18.1 | 28.9 | 27.4 | 7.2 | 85.8 | 41.5 | 56.6 | 150.2 |
| PNC | PNC Financial Services Group, I | Financial Services | 1 | up | 13.8 | 31.3 | 6821000192.0 |  | 5.5 |  |  | 10.5 | 6.4 | 12.8 | -3.3 | -6.5 | 23.7 |
| QCOM | QUALCOMM Incorporated | Technology | 1 | up | -3.5 | 22.3 | 14284999680.0 | 9589624832.0 | 5.4 | 18.6 | 25.2 | 22.4 | 5.2 | 25.7 | 49.8 | 44.1 | 34.8 |
| ROK | Rockwell Automation, Inc. | Industrials | 1 | up | 11.9 | 12.4 | 1535000064.0 | 974499968.0 | 5.6 | 24.9 | 50.4 | 31.2 | 6.0 | 47.0 | 11.4 | 14.2 | 48.1 |
| STT | State Street Corporation | Financial Services | 1 | up | -2.8 | 21.3 | -2640999936.0 |  |  |  |  | 11.2 |  | 15.7 | 7.7 | 20.2 | 60.8 |
| TFC | Truist Financial Corporation | Financial Services | 1 | up | 5.2 | 29.6 | 5672000000.0 |  | 4.1 |  |  | 9.4 | 4.8 | 12.0 | -4.0 | -8.6 | 19.1 |
| WST | West Pharmaceutical Services, I | Healthcare | 1 | up | 21.0 | 16.8 | 715299968.0 | 275662496.0 | 6.3 | 23.2 | 73.1 | 33.2 | 6.9 | 42.3 | 12.3 | 21.0 | 47.0 |
| ACGL | Arch Capital Group Ltd. | Financial Services | 1 | weak | -3.3 | 24.6 | 5902000128.0 | 5276125184.0 | 2.0 | 6.7 | 7.5 | 9.7 | 1.7 | 7.4 | -3.2 | -4.5 | 3.4 |
| AEE | Ameren Corporation | Utilities | 1 | weak | 3.7 | 17.8 | 3343000064.0 | -1869374976.0 | 5.3 | 11.8 |  | 19.0 | 6.1 | 20.0 | -5.3 | -3.5 | 15.2 |
| AMGN | Amgen Inc. | Healthcare | 1 | weak | 5.8 | 21.0 | 10755999744.0 | 7436624896.0 | 5.9 | 12.9 | 29.4 | 14.4 | 6.1 | 23.6 | -5.9 | -10.9 | 29.3 |
| CMS | CMS Energy Corporation | Utilities | 1 | weak | 11.6 | 12.5 | 1940000000.0 | -2156000000.0 | 4.6 | 13.2 |  | 17.9 | 4.8 | 20.6 | -7.6 | -5.2 | 7.3 |
| CNP | CenterPoint Energy, Inc (Holdin | Utilities | 1 | weak | 1.9 | 11.4 | 2358000128.0 | -4945375232.0 | 4.9 | 12.6 |  | 20.5 | 5.4 | 26.2 | -3.9 | -1.8 | 16.2 |
| DRI | Darden Restaurants, Inc. | Consumer Cyclical | 1 | weak | 5.9 | 8.7 | 1735000064.0 | 678150016.0 | 2.2 | 14.1 | 41.9 | 17.8 | 2.4 | 21.3 | -0.4 | -6.7 | -2.7 |
| DTE | DTE Energy Company | Utilities | 1 | weak | 15.8 | 7.7 | 3295000064.0 | -2188124928.0 | 3.4 | 15.9 |  | 17.4 | 3.4 | 23.9 | -4.9 | -2.8 | 8.9 |
| DUK | Duke Energy Corporation (Holdin | Utilities | 1 | weak | 11.3 | 15.7 | 11665000448.0 | -2246500096.0 | 5.4 | 10.7 |  | 17.5 | 5.8 | 19.3 | -5.2 | -4.8 | 12.3 |
| FE | FirstEnergy Corp. | Utilities | 1 | weak | 11.6 | 6.9 | 3211000064.0 | -1835124992.0 | 3.4 | 10.0 |  | 15.7 | 3.6 | 25.1 | -12.5 | -11.6 | 10.8 |
| HSIC | Henry Schein, Inc. | Healthcare | 1 | weak | 6.3 | 3.0 | 578000000.0 | 290124992.0 | 0.9 | 12.1 | 43.8 | 12.5 | 1.0 | 22.4 | -5.8 | -7.0 | 3.8 |
| L | Loews Corporation | Financial Services | 1 | weak | 1.4 | 8.8 | 2615000064.0 | 2084000000.0 |  |  |  |  | 1.4 | 14.0 | -3.7 | -2.7 | 21.4 |
| MTB | M&T Bank Corporation | Financial Services | 1 | weak | 5.7 | 31.5 | 3380000000.0 |  | 3.5 |  |  | 10.2 | 3.9 | 12.0 | -5.6 | -9.8 | 13.8 |
| PNW | Pinnacle West Capital Corporati | Utilities | 1 | weak | 11.4 | 12.0 | 1638496000.0 | -831102848.0 | 4.6 | 11.9 |  | 18.1 | 5.0 | 19.1 | -4.7 | -0.1 | 15.9 |
| REG | Regency Centers Corporation | Real Estate | 1 | weak | 10.0 | 33.1 | 819390016.0 | 574623104.0 | 11.8 | 18.5 | 33.8 | 31.0 | 12.1 | 27.0 | -4.5 | 0.8 | 9.7 |
| RF | Regions Financial Corporation | Financial Services | 1 | weak | 7.3 | 31.0 | 1982000000.0 |  | 3.4 |  |  | 9.8 | 3.9 | 11.6 | -4.5 | -9.5 | 23.8 |
| TXT | Textron Inc. | Industrials | 1 | weak | 11.8 | 6.2 | 1319000064.0 | 622374976.0 | 1.1 | 10.2 | 27.7 | 12.6 | 1.2 | 17.5 | -1.7 | -9.5 | 18.1 |
| UPS | United Parcel Service, Inc. | Industrials | 1 | weak | -1.6 | 5.9 | 8355999744.0 | 4625500160.0 | 1.1 | 8.5 | 21.7 | 12.5 | 1.2 | 16.2 | -5.8 | -15.9 | 6.1 |
| VZ | Verizon Communications Inc. | Communication Services | 1 | weak | 2.9 | 12.5 | 37339000832.0 | 19608500224.0 | 2.7 | 7.4 | 19.4 | 9.2 | 2.8 | 11.8 | -0.9 | -4.0 | 16.9 |
| WEC | WEC Energy Group, Inc. | Utilities | 1 | weak | 9.0 | 16.2 | 3435200000.0 | -2067012480.0 | 5.5 | 14.0 |  | 18.8 | 5.9 | 22.7 | -5.4 | -4.9 | 10.4 |


## ROST — Ross Stores, Inc.  (Consumer Cyclical / Apparel Retail)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2023 | 18.70B | n/a | 8.1% | 13.2% | 1.69B | 1.04B | 5.5% |
| 2024 | 20.38B | 9.0% | 9.2% | 14.6% | 2.51B | 1.75B | 8.6% |
| 2025 | 21.13B | 3.7% | 9.9% | 15.5% | 2.36B | 1.64B | 7.7% |
| 2026 | 22.75B | 7.7% | 9.4% | 14.9% | 3.03B | 2.21B | 9.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-01 | 5.91B | 9.9% | 882.6M | 676.6M |
| 2025-04 | 4.98B | 9.6% | 409.7M | 202.3M |
| 2025-07 | 5.53B | 9.2% | 668.4M | 466.6M |
| 2025-10 | 5.60B | 9.1% | 827.1M | 617.8M |
| 2026-01 | 6.64B | 9.7% | 1.12B | 920.8M |


**2) Valuation:**


- 2026E TEV/Sales: **2.7x**  (TTM 3.1x)
- 2026E TEV/EBITDA _est_: **19.2x**  (TTM 22.0x)
- 2026E TEV/FCF _est_: **37.6x**
- 2026E P/E: **28.3x**  (TTM 35.1x, fwd 28.3x)
- EV 70.63B, 26E rev 26.08B, 26E EPS 8.19x


**3) Performance:**


- L1M -4.2% · L3M 8.5% · L12M 42.6% · -7.1% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, gap-up and held, range expansion (>=2x ATR), uptrend continuation off a dip; 1M -4.2%, 3M 8.5%; -7.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## HPE — Hewlett Packard Enterprise Comp  (Technology / Communication Equipment)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 28.50B | n/a | 3.0% | 16.5% | 4.59B | 1.47B | 5.2% |
| 2023 | 29.14B | 2.2% | 7.0% | 17.4% | 4.43B | 1.60B | 5.5% |
| 2024 | 30.13B | 3.4% | 8.6% | 16.8% | 4.34B | 1.97B | 6.6% |
| 2025 | 34.30B | 13.8% | 0.2% | 12.8% | 2.92B | 627.0M | 1.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-10 | n/a | n/a | n/a | n/a |
| 2025-01 | 7.85B | 8.0% | -390.0M | -918.0M |
| 2025-04 | 7.63B | -13.8% | -461.0M | -1.01B |
| 2025-07 | 9.14B | 3.3% | 1.30B | 729.0M |
| 2025-10 | 9.68B | 1.8% | 2.46B | 1.82B |
| 2026-01 | 9.30B | 4.9% | 1.18B | 609.0M |


**2) Valuation:**


- 2026E TEV/Sales: **1.4x**  (TTM 1.7x)
- 2026E TEV/EBITDA _est_: **10.5x**  (TTM 12.7x)
- 2026E TEV/FCF _est_: **20.1x**
- 2026E P/E: **13.7x**  (TTM n/a, fwd 13.7x)
- EV 61.95B, 26E rev 43.11B, 26E EPS 2.73x


**3) Performance:**


- L1M 27.8% · L3M 46.8% · L12M 90.1% · -3.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, range expansion (>=2x ATR), uptrend continuation off a dip; 1M 27.8%, 3M 46.8%; -3.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## HPQ — HP Inc.  (Technology / Computer Hardware)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 62.91B | n/a | 5.0% | 8.7% | 4.46B | 3.70B | 5.9% |
| 2023 | 53.72B | -14.6% | 6.1% | 8.3% | 3.57B | 2.98B | 5.5% |
| 2024 | 53.56B | -0.3% | 5.2% | 8.8% | 3.75B | 3.16B | 5.9% |
| 2025 | 55.30B | 3.2% | 4.6% | 7.5% | 3.70B | 2.80B | 5.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-10 | n/a | n/a | n/a | n/a |
| 2025-01 | 13.50B | 4.2% | 374.0M | 72.0M |
| 2025-04 | 13.22B | 3.1% | 38.0M | -145.0M |
| 2025-07 | 13.93B | 5.5% | 1.66B | 1.45B |
| 2025-10 | 14.64B | 5.4% | 1.62B | 1.43B |
| 2026-01 | 14.44B | 3.8% | 383.0M | 150.0M |


**2) Valuation:**


- 2026E TEV/Sales: **0.5x**  (TTM 0.5x)
- 2026E TEV/EBITDA _est_: **6.2x**  (TTM 6.2x)
- 2026E TEV/FCF _est_: **9.7x**
- 2026E P/E: **8.5x**  (TTM 9.6x, fwd 8.5x)
- EV 27.81B, 26E rev 56.83B, 26E EPS 2.98x


**3) Performance:**


- L1M 5.5% · L3M 9.8% · L12M -23.7% · -26.4% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, gap-up and held, range expansion (>=2x ATR); 1M 5.5%, 3M 9.8%; -26.4% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


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


- 2026E TEV/Sales: **3.4x**  (TTM 3.6x)
- 2026E TEV/EBITDA _est_: **12.9x**  (TTM 13.8x)
- 2026E TEV/FCF _est_: **20.2x**
- 2026E P/E: **16.3x**  (TTM 23.3x, fwd 16.3x)
- EV 24.18B, 26E rev 7.19B, 26E EPS 8.53x


**3) Performance:**


- L1M 15.7% · L3M 17.7% · L12M 22.7% · -3.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, range expansion (>=2x ATR), uptrend continuation off a dip; 1M 15.7%, 3M 17.7%; -3.7% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (20.4%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## BK — The Bank of New York Mellon Cor  (Financial Services / Banks - Diversified)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 16.19B | n/a | 15.8% | n/a | 15.07B | 13.72B | 84.8% |
| 2023 | 17.34B | 7.2% | 19.0% | n/a | 5.91B | 4.69B | 27.1% |
| 2024 | 18.26B | 5.3% | 24.8% | n/a | 687.0M | -782.0M | -4.3% |
| 2025 | 19.76B | 8.2% | 28.1% | n/a | 6.73B | 5.18B | 26.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 4.69B | 26.0% | 412.0M | 92.0M |
| 2025-06 | 4.96B | 28.7% | 2.20B | 1.84B |
| 2025-09 | 5.00B | 28.9% | -1.06B | -1.50B |
| 2025-12 | 5.11B | 28.6% | 5.18B | 4.75B |
| 2026-03 | 5.34B | 30.6% | -3.01B | -3.63B |


**2) Valuation:**


- 2026E TEV/Sales: **-3.0x**  (TTM -3.2x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **14.2x**  (TTM 17.0x, fwd 14.2x)
- EV -66.08B, 26E rev 22.31B, 26E EPS 9.64x


**3) Performance:**


- L1M 0.5% · L3M 15.1% · L12M 56.4% · -1.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, volatility-squeeze release; 1M 0.5%, 3M 15.1%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (26.2%)


_Issues:_ none flagged from the numbers


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
| 2025-04 | 14.15B | 17.6% | 4.06B | 3.80B |
| 2025-07 | 14.67B | 17.4% | 4.23B | 4.02B |
| 2025-10 | 14.88B | 19.2% | 3.21B | 2.89B |
| 2026-01 | 15.35B | 20.7% | 1.82B | 1.54B |
| 2026-04 | 15.84B | 21.3% | 3.76B | 3.34B |


**2) Valuation:**


- 2026E TEV/Sales: **7.0x**  (TTM 7.9x)
- 2026E TEV/EBITDA _est_: **25.2x**  (TTM 28.4x)
- 2026E TEV/FCF _est_: **46.1x**
- 2026E P/E: **25.3x**  (TTM 40.1x, fwd 25.3x)
- EV 482.24B, 26E rev 68.49B, 26E EPS 4.77x


**3) Performance:**


- L1M 39.9% · L3M 54.7% · L12M 97.3% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 39.9%, 3M 54.7%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (23.5%)


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
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.54B | 28.1% | 863.3M | 796.8M |
| 2025-06 | 1.63B | 27.0% | 451.9M | 284.1M |
| 2025-09 | 1.72B | 27.5% | 655.2M | 567.5M |
| 2025-12 | 1.91B | 26.6% | 620.2M | 577.4M |
| 2026-03 | 1.85B | 28.9% | 1.08B | 1.01B |


**2) Valuation:**


- 2026E TEV/Sales: **10.7x**  (TTM 13.0x)
- 2026E TEV/EBITDA _est_: **32.1x**  (TTM 39.0x)
- 2026E TEV/FCF _est_: **41.8x**
- 2026E P/E: **38.9x**  (TTM 51.7x, fwd 38.9x)
- EV 92.12B, 26E rev 8.63B, 26E EPS 3.43x


**3) Performance:**


- L1M 49.0% · L3M 43.5% · L12M 18.9% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 49.0%, 3M 43.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (32.7%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## GS — Goldman Sachs Group, Inc. (The)  (Financial Services / Capital Markets)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 47.37B | n/a | 23.8% | n/a | 8.71B | 4.96B | 10.5% |
| 2023 | 46.25B | -2.3% | 18.4% | n/a | -12.59B | -14.90B | -32.2% |
| 2024 | 53.51B | 15.7% | 26.7% | n/a | -13.21B | -15.30B | -28.6% |
| 2025 | 58.28B | 8.9% | 29.5% | n/a | -45.15B | -47.22B | -81.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 15.06B | 31.5% | -37.23B | -37.73B |
| 2025-06 | 14.58B | 25.5% | 5.67B | 5.20B |
| 2025-09 | 15.18B | 27.0% | 2.68B | 2.12B |
| 2025-12 | 13.45B | 34.3% | -16.28B | -16.81B |
| 2026-03 | 17.23B | 32.7% | -31.87B | -32.43B |


**2) Valuation:**


- 2026E TEV/Sales: **0.2x**  (TTM 0.2x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **15.3x**  (TTM 18.3x, fwd 15.3x)
- EV 15.10B, 26E rev 66.84B, 26E EPS 65.40x


**3) Performance:**


- L1M 5.4% · L3M 5.3% · L12M 58.3% · -2.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 5.4%, 3M 5.3%; -2.3% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ net margin expanding


_Issues:_ revenue growth decelerating; negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## NXPI — NXP Semiconductors N.V.  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 13.21B | n/a | 21.1% | 38.2% | 3.90B | 2.67B | 20.2% |
| 2023 | 13.28B | 0.5% | 21.1% | 36.9% | 3.51B | 2.51B | 18.9% |
| 2024 | 12.61B | -5.0% | 19.9% | 35.1% | 2.78B | 1.91B | 15.1% |
| 2025 | 12.27B | -2.7% | 16.5% | 32.3% | 2.82B | 2.28B | 18.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.83B | 17.3% | 565.0M | 401.0M |
| 2025-06 | 2.93B | 15.2% | 779.0M | 659.0M |
| 2025-09 | 3.17B | 19.9% | 585.0M | 485.0M |
| 2025-12 | 3.33B | 13.6% | 891.0M | 738.0M |
| 2026-03 | 3.18B | 35.3% | 793.0M | 672.0M |


**2) Valuation:**


- 2026E TEV/Sales: **5.4x**  (TTM 6.7x)
- 2026E TEV/EBITDA _est_: **14.2x**  (TTM 17.5x)
- 2026E TEV/FCF _est_: **21.9x**
- 2026E P/E: **17.7x**  (TTM 29.9x, fwd 17.7x)
- EV 83.95B, 26E rev 15.53B, 26E EPS 17.63x


**3) Performance:**


- L1M 36.4% · L3M 19.9% · L12M 40.6% · -4.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 36.4%, 3M 19.9%; -4.7% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (18.6%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## SNPS — Synopsys, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 4.62B | n/a | 21.3% | 28.9% | 1.74B | 1.60B | 34.7% |
| 2023 | 5.32B | 15.2% | 23.1% | 29.2% | 1.70B | 1.51B | 28.4% |
| 2024 | 6.13B | 15.2% | 36.9% | 30.1% | 1.41B | 1.27B | 20.7% |
| 2025 | 7.05B | 15.1% | 18.9% | 35.4% | 1.52B | 1.35B | 19.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-10 | n/a | n/a | n/a | n/a |
| 2025-01 | 1.46B | 20.3% | -67.5M | -108.2M |
| 2025-04 | 1.60B | 21.5% | 275.4M | 219.8M |
| 2025-07 | 1.74B | 13.9% | 671.0M | 632.4M |
| 2025-10 | 2.25B | 19.9% | 639.7M | 605.2M |
| 2026-01 | 2.41B | 2.7% | 856.8M | 821.5M |


**2) Valuation:**


- 2026E TEV/Sales: **9.9x**  (TTM 13.1x)
- 2026E TEV/EBITDA _est_: **48.9x**  (TTM 65.1x)
- 2026E TEV/FCF _est_: **25.5x**
- 2026E P/E: **31.1x**  (TTM 81.6x, fwd 31.1x)
- EV 105.21B, 26E rev 10.66B, 26E EPS 17.05x


**3) Performance:**


- L1M 13.9% · L3M 14.9% · L12M -2.9% · -22.1% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, range expansion (>=2x ATR), uptrend continuation off a dip; 1M 13.9%, 3M 14.9%; -22.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +15.1% latest FY; strong FCF margin (19.1%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## TXN — Texas Instruments Incorporated  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 20.03B | n/a | 43.7% | 56.0% | 8.72B | 5.92B | 29.6% |
| 2023 | 17.52B | -12.5% | 37.2% | 51.4% | 6.42B | 1.35B | 7.7% |
| 2024 | 15.64B | -10.7% | 30.7% | 48.2% | 6.32B | 1.50B | 9.6% |
| 2025 | 17.68B | 13.0% | 28.3% | 46.7% | 7.15B | 2.60B | 14.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.07B | 29.0% | 849.0M | -274.0M |
| 2025-06 | 4.45B | 29.1% | 1.86B | 555.0M |
| 2025-09 | 4.74B | 28.8% | 2.19B | 993.0M |
| 2025-12 | 4.42B | 26.3% | 2.25B | 1.33B |
| 2026-03 | 4.83B | 32.0% | 1.52B | 844.0M |


**2) Valuation:**


- 2026E TEV/Sales: **12.1x**  (TTM 15.2x)
- 2026E TEV/EBITDA _est_: **25.6x**  (TTM 32.4x)
- 2026E TEV/FCF _est_: **208.0x**
- 2026E P/E: **35.4x**  (TTM 53.8x, fwd 33.5x)
- EV 280.51B, 26E rev 23.28B, 26E EPS 8.91x


**3) Performance:**


- L1M 36.4% · L3M 34.5% · L12M 66.1% · -1.8% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high, uptrend continuation off a dip; 1M 36.4%, 3M 34.5%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


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


- 2026E TEV/Sales: **22.3x**  (TTM 33.3x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM -3429.5x)
- 2026E TEV/FCF _est_: **66.8x**
- 2026E P/E: **109.0x**  (TTM n/a, fwd 109.0x)
- EV 160.03B, 26E rev 7.18B, 26E EPS 6.16x


**3) Performance:**


- L1M 42.1% · L3M 38.3% · L12M 36.3% · 0.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 42.1%, 3M 38.3%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +21.7% latest FY; strong FCF margin (25.8%)


_Issues:_ revenue growth decelerating; net margin negative (-3.4%); rich valuation (26E P/E 109.0x); high TEV/Sales 26E (22.3x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## FFIV — F5, Inc.  (Technology / Software - Infrastructure)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 2.70B | n/a | 12.0% | 19.6% | 442.6M | 409.0M | 15.2% |
| 2023 | 2.81B | 4.4% | 14.0% | 23.1% | 653.4M | 599.2M | 21.3% |
| 2024 | 2.82B | 0.1% | 20.1% | 27.5% | 792.4M | 762.0M | 27.1% |
| 2025 | 3.09B | 9.7% | 22.4% | 28.6% | 949.7M | 906.4M | 29.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 731.1M | 19.9% | 256.6M | 246.1M |
| 2025-06 | 780.4M | 24.3% | 282.2M | 273.7M |
| 2025-09 | 810.1M | 23.5% | 208.1M | 191.9M |
| 2025-12 | 822.5M | 21.9% | 159.2M | 149.5M |
| 2026-03 | 811.7M | 18.2% | 365.9M | 347.6M |


**2) Valuation:**


- 2026E TEV/Sales: **5.9x**  (TTM 6.3x)
- 2026E TEV/EBITDA _est_: **21.0x**  (TTM 22.7x)
- 2026E TEV/FCF _est_: **25.0x**
- 2026E P/E: **22.4x**  (TTM 32.2x, fwd 22.4x)
- EV 20.47B, 26E rev 3.48B, 26E EPS 17.48x


**3) Performance:**


- L1M 17.7% · L3M 32.4% · L12M 28.8% · -0.6% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 17.7%, 3M 32.4%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (29.4%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## SWKS — Skyworks Solutions, Inc.  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.49B | n/a | 23.2% | 40.4% | 1.42B | 914.9M | 16.7% |
| 2023 | 4.77B | -13.0% | 20.6% | 36.8% | 1.86B | 1.62B | 34.0% |
| 2024 | 4.18B | -12.5% | 14.3% | 26.8% | 1.82B | 1.64B | 39.3% |
| 2025 | 4.09B | -2.2% | 11.7% | 24.9% | 1.30B | 1.08B | 26.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 953.2M | 7.2% | 409.4M | 363.3M |
| 2025-06 | 965.0M | 10.9% | 314.2M | 246.0M |
| 2025-09 | 1.10B | 12.9% | 200.0M | 138.2M |
| 2025-12 | 1.04B | 7.6% | 395.5M | 324.8M |
| 2026-03 | 943.7M | 3.8% | 50.3M | -37.5M |


**2) Valuation:**


- 2026E TEV/Sales: **2.7x**  (TTM 2.7x)
- 2026E TEV/EBITDA _est_: **12.0x**  (TTM 11.9x)
- 2026E TEV/FCF _est_: **15.8x**
- 2026E P/E: **15.6x**  (TTM 33.4x, fwd 15.6x)
- EV 10.83B, 26E rev 4.02B, 26E EPS 5.15x


**3) Performance:**


- L1M 16.7% · L3M 11.7% · L12M -1.0% · -15.5% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break, new 6-month high; 1M 16.7%, 3M 11.7%; -15.5% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (26.3%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DGX — Quest Diagnostics Incorporated  (Healthcare / Diagnostics & Research)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 9.88B | n/a | 9.6% | 18.4% | 1.72B | 1.31B | 13.3% |
| 2023 | 9.25B | -6.4% | 9.2% | 18.7% | 1.27B | 864.0M | 9.3% |
| 2024 | 9.87B | 6.7% | 8.8% | 19.2% | 1.33B | 909.0M | 9.2% |
| 2025 | 11.04B | 11.8% | 9.0% | 19.6% | 1.89B | 1.36B | 12.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 2.65B | 8.3% | 314.0M | 197.0M |
| 2025-06 | 2.76B | 10.2% | 544.0M | 436.0M |
| 2025-09 | 2.82B | 8.7% | 563.0M | 419.0M |
| 2025-12 | 2.81B | 8.7% | 465.0M | 307.0M |
| 2026-03 | 2.90B | 8.7% | 278.0M | 164.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.3x**  (TTM 2.5x)
- 2026E TEV/EBITDA _est_: **11.4x**  (TTM 12.5x)
- 2026E TEV/FCF _est_: **26.8x**
- 2026E P/E: **16.9x**  (TTM 21.8x, fwd 16.9x)
- EV 27.85B, 26E rev 12.38B, 26E EPS 11.67x


**3) Performance:**


- L1M -2.5% · L3M -9.4% · L12M 10.1% · -11.6% from 12-mo high


**4) Reason for breakout:**


10-day-high break, volatility-squeeze release, uptrend continuation off a dip; 1M -2.5%, 3M -9.4%; -11.6% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## BAX — Baxter International Inc.  (Healthcare / Medical Instruments & Supplies)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 10.06B | n/a | -24.2% | -17.5% | 1.21B | 576.0M | 5.7% |
| 2023 | 10.36B | 3.0% | 25.6% | 16.7% | 1.73B | 1.29B | 12.5% |
| 2024 | 10.64B | 2.7% | -6.1% | 10.5% | 1.02B | 559.0M | 5.3% |
| 2025 | 11.24B | 5.7% | -8.5% | 6.8% | 845.0M | 323.0M | 2.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.62B | 4.8% | -193.0M | -315.0M |
| 2025-06 | 2.81B | 3.2% | 217.0M | 68.0M |
| 2025-09 | 2.83B | -1.6% | 237.0M | 126.0M |
| 2025-12 | 2.97B | -37.9% | 584.0M | 444.0M |
| 2026-03 | 2.70B | -0.6% | 213.0M | 76.0M |


**2) Valuation:**


- 2026E TEV/Sales: **1.5x**  (TTM 1.5x)
- 2026E TEV/EBITDA _est_: **8.9x**  (TTM 9.2x)
- 2026E TEV/FCF _est_: **18.9x**
- 2026E P/E: **9.6x**  (TTM n/a, fwd 9.6x)
- EV 17.47B, 26E rev 11.59B, 26E EPS 2.01x


**3) Performance:**


- L1M -4.6% · L3M -12.5% · L12M -42.2% · -45.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M -4.6%, 3M -12.5%; -45.0% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ net margin negative (-8.5%)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## BBY — Best Buy Co., Inc.  (Consumer Cyclical / Specialty Retail)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2023 | 46.30B | n/a | 3.1% | 5.9% | 1.82B | 894.0M | 1.9% |
| 2024 | 43.45B | -6.1% | 2.9% | 6.0% | 1.47B | 675.0M | 1.6% |
| 2025 | 41.53B | -4.4% | 2.2% | 5.3% | 2.10B | 1.39B | 3.4% |
| 2026 | 41.69B | 0.4% | 2.6% | 5.5% | 1.96B | 1.26B | 3.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-10 | n/a | n/a | n/a | n/a |
| 2025-01 | 13.95B | 0.8% | 1.54B | 1.36B |
| 2025-04 | 8.77B | 2.3% | 34.0M | -132.0M |
| 2025-07 | 9.44B | 2.0% | 749.0M | 574.0M |
| 2025-10 | 9.67B | 1.4% | -99.0M | -287.0M |
| 2026-01 | 13.81B | 3.9% | 1.28B | 1.10B |


**2) Valuation:**


- 2026E TEV/Sales: **0.4x**  (TTM 0.4x)
- 2026E TEV/EBITDA _est_: **5.7x**  (TTM 5.8x)
- 2026E TEV/FCF _est_: **17.6x**
- 2026E P/E: **8.8x**  (TTM 12.3x, fwd 8.8x)
- EV 15.03B, 26E rev 42.37B, 26E EPS 7.00x


**3) Performance:**


- L1M -13.0% · L3M -13.2% · L12M -19.0% · -31.1% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M -13.0%, 3M -13.2%; -31.1% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## COR — Cencora, Inc.  (Healthcare / Medical Distribution)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 238.59B | n/a | 0.7% | 1.3% | 2.70B | 2.21B | 0.9% |
| 2023 | 262.17B | 9.9% | 0.7% | 1.3% | 3.91B | 3.45B | 1.3% |
| 2024 | 293.96B | 12.1% | 0.5% | 1.1% | 3.48B | 3.00B | 1.0% |
| 2025 | 321.33B | 9.3% | 0.5% | 1.2% | 3.88B | 3.21B | 1.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 75.45B | 1.0% | 3.35B | 3.22B |
| 2025-06 | 80.66B | 0.9% | 109.2M | -74.0M |
| 2025-09 | 83.73B | -0.4% | 3.13B | 2.88B |
| 2025-12 | 85.93B | 0.7% | -2.31B | -2.42B |
| 2026-03 | 78.36B | 2.1% | 1.34B | 1.17B |


**2) Valuation:**


- 2026E TEV/Sales: **0.2x**  (TTM 0.2x)
- 2026E TEV/EBITDA _est_: **11.2x**  (TTM 12.2x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **13.9x**  (TTM 21.1x, fwd 13.9x)
- EV 64.75B, 26E rev 358.99B, 26E EPS 19.78x


**3) Performance:**


- L1M -19.9% · L3M -28.4% · L12M -6.8% · -31.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break, gap-up and held; 1M -19.9%, 3M -28.4%; -31.0% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## EL — Estee Lauder Companies, Inc. (T  (Consumer Defensive / Household & Personal Products)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 17.74B | n/a | 13.5% | 22.2% | 3.04B | 2.00B | 11.3% |
| 2023 | 15.91B | -10.3% | 6.3% | 15.1% | 1.73B | -1.56B | -9.8% |
| 2024 | 15.61B | -1.9% | 2.5% | 12.7% | 2.36B | 1.44B | 9.2% |
| 2025 | 14.33B | -8.2% | -7.9% | 1.0% | 1.27B | 670.0M | 4.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.55B | 4.5% | 284.0M | 162.0M |
| 2025-06 | 3.41B | -16.0% | 601.0M | 394.0M |
| 2025-09 | 3.48B | 1.4% | -340.0M | -436.0M |
| 2025-12 | 4.23B | 3.8% | 1.12B | 1.02B |
| 2026-03 | 3.71B | 2.4% | 412.0M | 310.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.2x**  (TTM 2.3x)
- 2026E TEV/EBITDA _est_: **14.1x**  (TTM 14.8x)
- 2026E TEV/FCF _est_: **18.3x**
- 2026E P/E: **27.2x**  (TTM n/a, fwd 27.2x)
- EV 34.72B, 26E rev 15.55B, 26E EPS 3.18x


**3) Performance:**


- L1M 6.6% · L3M -25.6% · L12M 27.2% · -32.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, range expansion (>=2x ATR); 1M 6.6%, 3M -25.6%; -32.7% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ revenue growth decelerating; net margin negative (-7.9%)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MMM — 3M Company  (Industrials / Conglomerates)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 26.16B | n/a | 22.1% | 24.8% | 5.59B | 3.84B | 14.7% |
| 2023 | 24.61B | -5.9% | -28.4% | -33.9% | 6.68B | 5.07B | 20.6% |
| 2024 | 24.57B | -0.1% | 17.0% | 30.0% | 1.82B | 638.0M | 2.6% |
| 2025 | 24.95B | 1.5% | 13.0% | 25.9% | 2.31B | 1.40B | 5.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 5.95B | 18.7% | -79.0M | -315.0M |
| 2025-06 | 6.34B | 11.4% | -954.0M | -1.16B |
| 2025-09 | 6.52B | 12.8% | 1.76B | 1.54B |
| 2025-12 | 6.13B | 9.4% | 1.58B | 1.33B |
| 2026-03 | 6.03B | 10.8% | 574.0M | 349.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.3x**  (TTM 3.5x)
- 2026E TEV/EBITDA _est_: **13.4x**  (TTM 13.8x)
- 2026E TEV/FCF _est_: **35.9x**
- 2026E P/E: **16.2x**  (TTM 29.6x, fwd 16.2x)
- EV 86.43B, 26E rev 25.92B, 26E EPS 9.46x


**3) Performance:**


- L1M -2.9% · L3M -14.9% · L12M 0.7% · -15.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M -2.9%, 3M -14.9%; -15.9% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## AMD — Advanced Micro Devices, Inc.  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 23.60B | n/a | 5.6% | 23.4% | 3.56B | 3.12B | 13.2% |
| 2023 | 22.68B | -3.9% | 3.8% | 17.9% | 1.67B | 1.12B | 4.9% |
| 2024 | 25.79B | 13.7% | 6.4% | 20.0% | 3.04B | 2.40B | 9.3% |
| 2025 | 34.64B | 34.3% | 12.5% | 21.0% | 7.71B | 6.74B | 19.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 7.44B | 9.5% | 939.0M | 727.0M |
| 2025-06 | 7.68B | 11.3% | 2.01B | 1.73B |
| 2025-09 | 9.25B | 13.4% | 2.16B | 1.90B |
| 2025-12 | 10.27B | 14.7% | 2.60B | 2.38B |
| 2026-03 | 10.25B | 13.5% | 2.96B | 2.57B |


**2) Valuation:**


- 2026E TEV/Sales: **9.5x**  (TTM 19.3x)
- 2026E TEV/EBITDA _est_: **48.1x**  (TTM 97.5x)
- 2026E TEV/FCF _est_: **49.8x**
- 2026E P/E: **36.1x**  (TTM 155.5x, fwd 36.1x)
- EV 724.63B, 26E rev 75.98B, 26E EPS 12.96x


**3) Performance:**


- L1M 52.4% · L3M 104.6% · L12M 260.3% · -7.6% from 12-mo high


**4) Reason for breakout:**


new 6-month high, uptrend continuation off a dip; 1M 52.4%, 3M 104.6%; -7.6% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +34.3% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (19.4%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ANET — Arista Networks, Inc.  (Technology / Computer Hardware)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 4.38B | n/a | 30.9% | 36.3% | 492.8M | 448.2M | 10.2% |
| 2023 | 5.86B | 33.8% | 35.6% | 39.7% | 2.03B | 2.00B | 34.1% |
| 2024 | 7.00B | 19.5% | 40.7% | 42.9% | 3.71B | 3.68B | 52.5% |
| 2025 | 9.01B | 28.6% | 39.0% | 43.6% | 4.37B | 4.25B | 47.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.00B | 40.6% | 641.7M | 613.3M |
| 2025-06 | 2.20B | 40.3% | 1.20B | 1.18B |
| 2025-09 | 2.31B | 37.0% | 1.27B | 1.24B |
| 2025-12 | 2.49B | 38.4% | 1.26B | 1.22B |
| 2026-03 | 2.71B | 37.8% | 1.69B | 1.64B |


**2) Valuation:**


- 2026E TEV/Sales: **12.2x**  (TTM 18.0x)
- 2026E TEV/EBITDA _est_: **28.0x**  (TTM 41.2x)
- 2026E TEV/FCF _est_: **27.2x**
- 2026E P/E: **34.6x**  (TTM 52.9x, fwd 34.6x)
- EV 174.75B, 26E rev 14.32B, 26E EPS 4.45x


**3) Performance:**


- L1M -11.8% · L3M 0.3% · L12M 44.5% · -20.1% from 12-mo high


**4) Reason for breakout:**


10-day-high break, uptrend continuation off a dip; 1M -11.8%, 3M 0.3%; -20.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +28.6% latest FY; revenue growth accelerating; strong FCF margin (47.2%)


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
- 2026E P/E: **33.6x**  (TTM n/a, fwd 33.6x)
- EV 30.99B, 26E rev 12.13B, 26E EPS 0.84x


**3) Performance:**


- L1M 0.4% · L3M 53.3% · L12M -9.4% · -11.8% from 12-mo high


**4) Reason for breakout:**


10-day-high break, uptrend continuation off a dip; 1M 0.4%, 3M 53.3%; -11.8% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ net margin negative (-4.4%)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## GNRC — Generac Holdlings Inc.  (Industrials / Specialty Industrial Machinery)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 4.56B | n/a | 7.7% | 15.8% | 58.5M | -27.7M | -0.6% |
| 2023 | 4.02B | -11.9% | 5.0% | 13.8% | 521.7M | 392.6M | 9.8% |
| 2024 | 4.30B | 6.8% | 7.6% | 15.6% | 741.3M | 604.6M | 14.1% |
| 2025 | 4.21B | -2.0% | 3.8% | 11.0% | 438.0M | 268.1M | 6.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 942.1M | 4.7% | 58.2M | 27.2M |
| 2025-06 | 1.06B | 7.0% | 72.2M | 14.5M |
| 2025-09 | 1.11B | 5.9% | 118.4M | 96.5M |
| 2025-12 | 1.09B | -2.2% | 189.3M | 129.9M |
| 2026-03 | 1.06B | 6.9% | 119.3M | 89.9M |


**2) Valuation:**


- 2026E TEV/Sales: **2.8x**  (TTM 3.6x)
- 2026E TEV/EBITDA _est_: **23.1x**  (TTM 29.8x)
- 2026E TEV/FCF _est_: **105.6x**
- 2026E P/E: **24.1x**  (TTM 83.1x, fwd 24.1x)
- EV 15.72B, 26E rev 5.58B, 26E EPS 11.04x


**3) Performance:**


- L1M 27.1% · L3M 17.5% · L12M 105.2% · -4.6% from 12-mo high


**4) Reason for breakout:**


gap-up and held, uptrend continuation off a dip; 1M 27.1%, 3M 17.5%; -4.6% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## KIM — Kimco Realty Corporation (HC)  (Real Estate / REIT - Retail)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 1.73B | n/a | 7.3% | 44.9% | 861.1M | 861.1M | 49.8% |
| 2023 | 1.78B | 3.2% | 36.7% | 78.6% | 1.07B | 1.07B | 60.1% |
| 2024 | 2.04B | 14.2% | 20.2% | 62.0% | 1.01B | 1.01B | 49.4% |
| 2025 | 2.14B | 5.1% | 27.3% | 67.8% | 1.12B | 1.12B | 52.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | n/a | n/a | 223.8M | 223.8M |
| 2025-06 | n/a | n/a | 305.4M | 305.4M |
| 2025-09 | n/a | n/a | 332.4M | 332.4M |
| 2025-12 | n/a | n/a | 258.4M | 258.4M |
| 2026-03 | 558.0M | 29.6% | 243.0M | 243.0M |


**2) Valuation:**


- 2026E TEV/Sales: **10.8x**  (TTM 11.3x)
- 2026E TEV/EBITDA _est_: **17.8x**  (TTM 18.7x)
- 2026E TEV/FCF _est_: **27.8x**
- 2026E P/E: **28.1x**  (TTM 27.7x, fwd 28.1x)
- EV 24.52B, 26E rev 2.27B, 26E EPS 0.86x


**3) Performance:**


- L1M -3.2% · L3M 2.4% · L12M 14.3% · -4.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break, uptrend continuation off a dip; 1M -3.2%, 3M 2.4%; -4.9% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ net margin expanding; strong FCF margin (52.3%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## PLD — Prologis, Inc.  (Real Estate / REIT - Industrial)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 5.97B | n/a | 56.3% | 97.0% | 4.13B | 4.13B | 69.1% |
| 2023 | 8.02B | 34.3% | 38.1% | 81.9% | 5.37B | 5.37B | 67.0% |
| 2024 | 8.20B | 2.2% | 45.5% | 91.8% | 4.91B | 4.91B | 59.9% |
| 2025 | 8.79B | 7.2% | 37.9% | 83.8% | 5.01B | 5.01B | 57.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.14B | 27.7% | 1.16B | 1.16B |
| 2025-06 | 2.18B | 26.2% | 1.24B | 1.24B |
| 2025-09 | 2.21B | 34.5% | 1.45B | 1.45B |
| 2025-12 | 2.25B | 62.1% | 1.16B | 1.16B |
| 2026-03 | 2.30B | 42.7% | 1.29B | 1.29B |


**2) Valuation:**


- 2026E TEV/Sales: **18.8x**  (TTM 18.5x)
- 2026E TEV/EBITDA _est_: **26.9x**  (TTM 26.5x)
- 2026E TEV/FCF _est_: **36.4x**
- 2026E P/E: **42.8x**  (TTM 36.5x, fwd 42.8x)
- EV 173.79B, 26E rev 9.23B, 26E EPS 3.40x


**3) Performance:**


- L1M -1.2% · L3M 1.9% · L12M 35.1% · -3.1% from 12-mo high


**4) Reason for breakout:**


new 6-month high, volatility-squeeze release; 1M -1.2%, 3M 1.9%; -3.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (57.0%)


_Issues:_ high TEV/Sales 26E (18.8x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ABBV — AbbVie Inc.  (Healthcare / Drug Manufacturers - General)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 58.05B | n/a | 20.4% | 41.6% | 24.94B | 24.25B | 41.8% |
| 2023 | 54.32B | -6.4% | 9.0% | 31.6% | 22.84B | 22.06B | 40.6% |
| 2024 | 56.33B | 3.7% | 7.6% | 26.5% | 18.81B | 17.83B | 31.7% |
| 2025 | 61.16B | 8.6% | 6.9% | 28.8% | 19.03B | 17.82B | 29.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 13.34B | 9.6% | 1.64B | 1.40B |
| 2025-06 | 15.42B | 6.1% | 5.15B | 4.88B |
| 2025-09 | 15.78B | 1.2% | 7.02B | 6.64B |
| 2025-12 | 16.62B | 10.9% | 5.22B | 4.89B |
| 2026-03 | 15.00B | 4.6% | 3.83B | 3.56B |


**2) Valuation:**


- 2026E TEV/Sales: **6.1x**  (TTM 7.0x)
- 2026E TEV/EBITDA _est_: **12.8x**  (TTM 14.8x)
- 2026E TEV/FCF _est_: **18.4x**
- 2026E P/E: **13.4x**  (TTM 106.5x, fwd 13.4x)
- EV 442.54B, 26E rev 72.64B, 26E EPS 16.23x


**3) Performance:**


- L1M 0.7% · L3M -8.4% · L12M 22.4% · -11.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 0.7%, 3M -8.4%; -11.9% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (29.1%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CL — Colgate-Palmolive Company  (Consumer Defensive / Household & Personal Products)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 17.97B | n/a | 9.9% | 18.8% | 2.56B | 1.86B | 10.4% |
| 2023 | 19.46B | 8.3% | 11.8% | 21.8% | 3.75B | 3.04B | 15.6% |
| 2024 | 20.10B | 3.3% | 14.4% | 24.1% | 4.11B | 3.55B | 17.6% |
| 2025 | 20.38B | 1.4% | 10.5% | 19.4% | 4.20B | 3.63B | 17.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.91B | 14.1% | 600.0M | 476.0M |
| 2025-06 | 5.11B | 14.5% | 884.0M | 776.0M |
| 2025-09 | 5.13B | 14.3% | 1.26B | 1.11B |
| 2025-12 | 5.23B | -0.7% | 1.45B | 1.28B |
| 2026-03 | 5.32B | 12.1% | 747.0M | 609.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.6x**  (TTM 3.8x)
- 2026E TEV/EBITDA _est_: **15.1x**  (TTM 16.1x)
- 2026E TEV/FCF _est_: **22.4x**
- 2026E P/E: **22.5x**  (TTM 35.3x, fwd 22.5x)
- EV 79.26B, 26E rev 22.14B, 26E EPS 4.04x


**3) Performance:**


- L1M 6.0% · L3M -8.3% · L12M 3.2% · -10.6% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 6.0%, 3M -8.3%; -10.6% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (17.8%)


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


- 2026E TEV/Sales: **4.6x**  (TTM 5.5x)
- 2026E TEV/EBITDA _est_: **17.1x**  (TTM 20.7x)
- 2026E TEV/FCF _est_: **20.9x**
- 2026E P/E: **23.9x**  (TTM 31.3x, fwd 23.9x)
- EV 26.71B, 26E rev 5.83B, 26E EPS 3.05x


**3) Performance:**


- L1M 0.7% · L3M -12.0% · L12M -28.8% · -31.2% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M 0.7%, 3M -12.0%; -31.2% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +15.6% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (23.1%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## EW — Edwards Lifesciences Corporatio  (Healthcare / Medical Devices)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 4.46B | n/a | 34.1% | 37.6% | 1.22B | 953.4M | 21.4% |
| 2023 | 5.01B | 12.2% | 28.0% | 30.6% | 895.8M | 629.5M | 12.6% |
| 2024 | 5.44B | 8.6% | 76.7% | 31.7% | 542.3M | 259.9M | 4.8% |
| 2025 | 6.07B | 11.5% | 17.7% | 23.9% | 1.60B | 1.33B | 22.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.41B | 25.3% | 280.4M | 224.4M |
| 2025-06 | 1.53B | 21.5% | 290.2M | 240.9M |
| 2025-09 | 1.55B | 18.7% | 573.7M | 516.2M |
| 2025-12 | 1.57B | 5.8% | 450.9M | 353.5M |
| 2026-03 | 1.65B | 23.1% | 43.8M | -21.1M |


**2) Valuation:**


- 2026E TEV/Sales: **6.1x**  (TTM 7.1x)
- 2026E TEV/EBITDA _est_: **20.1x**  (TTM 23.6x)
- 2026E TEV/FCF _est_: **42.4x**
- 2026E P/E: **25.3x**  (TTM 46.0x, fwd 25.3x)
- EV 44.94B, 26E rev 7.41B, 26E EPS 3.36x


**3) Performance:**


- L1M 2.9% · L3M 7.3% · L12M 6.0% · -6.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break, volatility-squeeze release; 1M 2.9%, 3M 7.3%; -6.7% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (22.0%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## JNJ — Johnson & Johnson  (Healthcare / Drug Manufacturers - General)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 79.99B | n/a | 22.4% | 33.3% | 21.19B | 17.18B | 21.5% |
| 2023 | 85.16B | 6.5% | 41.3% | 27.4% | 22.79B | 17.78B | 20.9% |
| 2024 | 88.82B | 4.3% | 15.8% | 27.9% | 24.27B | 18.06B | 20.3% |
| 2025 | 94.19B | 6.0% | 28.5% | 43.6% | 24.53B | 19.31B | 20.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 21.89B | 50.2% | 4.17B | 3.37B |
| 2025-06 | 23.74B | 23.3% | 3.88B | 2.48B |
| 2025-09 | 23.99B | 21.5% | 9.17B | 8.00B |
| 2025-12 | 24.56B | 20.8% | 7.31B | 5.47B |
| 2026-03 | 24.06B | 21.8% | 2.51B | 1.47B |


**2) Valuation:**


- 2026E TEV/Sales: **5.5x**  (TTM 6.1x)
- 2026E TEV/EBITDA _est_: **15.5x**  (TTM 17.2x)
- 2026E TEV/FCF _est_: **42.4x**
- 2026E P/E: **18.5x**  (TTM 27.2x, fwd 18.5x)
- EV 590.76B, 26E rev 107.23B, 26E EPS 12.71x


**3) Performance:**


- L1M -3.3% · L3M -6.4% · L12M 59.2% · -8.8% from 12-mo high


**4) Reason for breakout:**


10-day-high break, 20-day-high break; 1M -3.3%, 3M -6.4%; -8.8% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (20.5%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## BSX — Boston Scientific Corporation  (Healthcare / Medical Devices)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 12.68B | n/a | 5.5% | 21.7% | 1.53B | 914.0M | 7.2% |
| 2023 | 14.24B | 12.3% | 11.2% | 24.2% | 2.50B | 1.70B | 12.0% |
| 2024 | 16.75B | 17.6% | 11.1% | 23.0% | 3.44B | 2.37B | 14.1% |
| 2025 | 20.07B | 19.9% | 14.4% | 25.4% | 4.53B | 3.40B | 17.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.66B | 14.5% | 541.0M | 277.0M |
| 2025-06 | 5.06B | 15.7% | 1.29B | 1.10B |
| 2025-09 | 5.07B | 14.9% | 1.34B | 1.09B |
| 2025-12 | 5.29B | 12.7% | 1.36B | 939.0M |
| 2026-03 | 5.20B | 25.8% | 348.0M | 171.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.0x**  (TTM 4.6x)
- 2026E TEV/EBITDA _est_: **15.1x**  (TTM 17.2x)
- 2026E TEV/FCF _est_: **29.5x**
- 2026E P/E: **15.4x**  (TTM 24.2x, fwd 15.4x)
- EV 94.76B, 26E rev 23.57B, 26E EPS 3.76x


**3) Performance:**


- L1M -16.9% · L3M -29.5% · L12M -48.8% · -51.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -16.9%, 3M -29.5%; -51.3% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +19.9% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (17.0%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DECK — Deckers Outdoor Corporation  (Consumer Cyclical / Footwear & Accessories)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 3.15B | n/a | 14.3% | 19.4% | 172.4M | 121.3M | 3.9% |
| 2023 | 3.63B | 15.1% | 14.2% | 19.8% | 537.4M | 456.4M | 12.6% |
| 2024 | 4.29B | 18.2% | 17.7% | 24.2% | 1.03B | 943.8M | 22.0% |
| 2025 | 4.99B | 16.3% | 19.4% | 26.4% | 1.04B | 958.4M | 19.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | 1.83B | 25.0% | 1.10B | 1.07B |
| 2025-03 | 1.02B | 14.8% | -73.0M | -89.4M |
| 2025-06 | 964.5M | 14.4% | 36.1M | 12.2M |
| 2025-09 | 1.43B | 18.7% | 8.1M | -13.9M |
| 2025-12 | 1.96B | 24.6% | 1.04B | 1.02B |


**2) Valuation:**


- 2026E TEV/Sales: **2.2x**  (TTM 2.4x)
- 2026E TEV/EBITDA _est_: **8.7x**  (TTM 9.4x)
- 2026E TEV/FCF _est_: **15.6x**
- 2026E P/E: **14.0x**  (TTM 14.7x, fwd 12.7x)
- EV 12.82B, 26E rev 5.81B, 26E EPS 7.38x


**3) Performance:**


- L1M -13.6% · L3M -19.2% · L12M -26.5% · -27.4% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -13.6%, 3M -19.2%; -27.4% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +16.3% latest FY; net margin expanding; strong FCF margin (19.2%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## GPN — Global Payments Inc.  (Industrials / Specialty Business Services)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 8.98B | n/a | 1.2% | 26.0% | 2.24B | 1.63B | 18.1% |
| 2023 | 7.38B | -17.8% | 13.4% | 43.4% | 2.55B | 1.89B | 25.6% |
| 2024 | 7.74B | 4.8% | 20.3% | 51.6% | 3.06B | 2.38B | 30.8% |
| 2025 | 7.71B | -0.4% | 18.2% | 43.2% | 2.66B | 2.04B | 26.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.82B | 16.8% | 555.1M | 427.5M |
| 2025-06 | 1.96B | 12.3% | 817.5M | 665.4M |
| 2025-09 | 2.01B | 31.6% | 768.7M | 598.9M |
| 2025-12 | 1.93B | 11.3% | 515.2M | 347.0M |
| 2026-03 | 2.97B | -60.6% | -288.8M | -550.2M |


**2) Valuation:**


- 2026E TEV/Sales: **2.9x**  (TTM 4.3x)
- 2026E TEV/EBITDA _est_: **6.6x**  (TTM 9.8x)
- 2026E TEV/FCF _est_: **3.6x**
- 2026E P/E: **4.5x**  (TTM 26.9x, fwd 4.5x)
- EV 38.46B, 26E rev 13.14B, 26E EPS 16.26x


**3) Performance:**


- L1M -4.6% · L3M -1.0% · L12M -17.7% · -24.2% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -4.6%, 3M -1.0%; -24.2% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (26.5%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## LH — Labcorp Holdings Inc.  (Healthcare / Diagnostics & Research)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 11.86B | n/a | 10.8% | 16.5% | 1.96B | 1.53B | 12.9% |
| 2023 | 12.16B | 2.5% | 3.4% | 11.1% | 1.33B | 874.1M | 7.2% |
| 2024 | 13.01B | 7.0% | 5.7% | 13.9% | 1.59B | 1.10B | 8.4% |
| 2025 | 13.95B | 7.2% | 6.3% | 14.4% | 1.64B | 1.21B | 8.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.35B | 6.4% | 18.5M | -107.5M |
| 2025-06 | 3.53B | 6.7% | 620.6M | 542.7M |
| 2025-09 | 3.56B | 7.3% | 387.2M | 280.5M |
| 2025-12 | 3.52B | 4.7% | 614.2M | 490.3M |
| 2026-03 | 3.54B | 7.9% | 191.5M | 70.5M |


**2) Valuation:**


- 2026E TEV/Sales: **1.8x**  (TTM 1.9x)
- 2026E TEV/EBITDA _est_: **11.1x**  (TTM 12.1x)
- 2026E TEV/FCF _est_: **21.9x**
- 2026E P/E: **13.4x**  (TTM 23.1x, fwd 13.4x)
- EV 27.30B, 26E rev 15.42B, 26E EPS 19.44x


**3) Performance:**


- L1M -6.0% · L3M -11.2% · L12M 4.4% · -13.5% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -6.0%, 3M -11.2%; -13.5% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## PEG — Public Service Enterprise Group  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 9.80B | n/a | 10.5% | 29.1% | 1.50B | -1.39B | -14.1% |
| 2023 | 11.24B | 14.7% | 22.8% | 45.3% | 3.81B | 481.0M | 4.3% |
| 2024 | 10.29B | -8.4% | 17.2% | 39.3% | 2.13B | -1.25B | -12.1% |
| 2025 | 12.17B | 18.3% | 17.3% | 39.4% | 3.30B | 26.0M | 0.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.22B | 18.3% | 1.05B | 421.0M |
| 2025-06 | 2.81B | 20.9% | 478.0M | -309.0M |
| 2025-09 | 3.23B | 19.3% | 1.05B | 322.0M |
| 2025-12 | 2.92B | 10.8% | 721.0M | -408.0M |
| 2026-03 | 3.85B | 19.3% | 1.27B | 578.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.8x**  (TTM 4.9x)
- 2026E TEV/EBITDA _est_: **12.9x**  (TTM 13.2x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **17.0x**  (TTM 17.6x, fwd 17.0x)
- EV 63.10B, 26E rev 13.02B, 26E EPS 4.70x


**3) Performance:**


- L1M -6.8% · L3M -10.8% · L12M 2.1% · -13.2% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -6.8%, 3M -10.8%; -13.2% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +18.3% latest FY; revenue growth accelerating; net margin expanding


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## VST — Vistra Corp.  (Utilities / Utilities - Independent Power Producers)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 13.73B | n/a | -8.9% | 7.6% | 485.0M | -816.0M | -5.9% |
| 2023 | 14.78B | 7.7% | 10.1% | 30.9% | 5.45B | 3.78B | 25.6% |
| 2024 | 17.22B | 16.5% | 15.4% | 40.4% | 4.56B | 2.48B | 14.4% |
| 2025 | 17.74B | 3.0% | 5.3% | 28.5% | 4.07B | 1.32B | 7.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.93B | -6.8% | 599.0M | -169.0M |
| 2025-06 | 4.25B | 7.7% | 572.0M | -118.0M |
| 2025-09 | 4.97B | 13.1% | 1.47B | 1.01B |
| 2025-12 | 4.58B | 5.1% | 1.43B | 596.0M |
| 2026-03 | 5.64B | 18.2% | 1.20B | 316.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.9x**  (TTM 3.7x)
- 2026E TEV/EBITDA _est_: **8.2x**  (TTM 10.6x)
- 2026E TEV/FCF _est_: **116.2x**
- 2026E P/E: **14.2x**  (TTM 26.3x, fwd 14.4x)
- EV 72.02B, 26E rev 25.27B, 26E EPS 11.11x


**3) Performance:**


- L1M -15.6% · L3M -18.4% · L12M -9.3% · -35.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -15.6%, 3M -18.4%; -35.7% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## WRB — W.R. Berkley Corporation  (Financial Services / Insurance - Property & Casualty)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 11.22B | n/a | 12.3% | n/a | 2.57B | 2.52B | 22.4% |
| 2023 | 12.11B | 8.0% | 11.4% | n/a | 2.93B | 2.88B | 23.7% |
| 2024 | 13.69B | 13.0% | 12.8% | n/a | 3.68B | 3.57B | 26.1% |
| 2025 | 14.64B | 6.9% | 12.2% | n/a | 3.58B | 3.41B | 23.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 3.53B | 11.8% | 743.8M | 727.6M |
| 2025-06 | 3.62B | 11.1% | 703.8M | 683.2M |
| 2025-09 | 3.78B | 13.5% | 1.14B | 1.12B |
| 2025-12 | 3.72B | 12.1% | 995.1M | 878.9M |
| 2026-03 | 3.71B | 13.9% | 667.9M | 667.9M |


**2) Valuation:**


- 2026E TEV/Sales: **1.9x**  (TTM 1.7x)
- 2026E TEV/EBITDA _est_: **11.1x**  (TTM 10.1x)
- 2026E TEV/FCF _est_: **8.9x**
- 2026E P/E: **14.0x**  (TTM 14.3x, fwd 14.0x)
- EV 25.95B, 26E rev 13.46B, 26E EPS 4.83x


**3) Performance:**


- L1M 0.3% · L3M -4.5% · L12M -3.9% · -13.8% from 12-mo high


**4) Reason for breakout:**


volatility-squeeze release; 1M 0.3%, 3M -4.5%; -13.8% from 12-mo high; trend tag: down


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (23.3%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## AMAT — Applied Materials, Inc.  (Technology / Semiconductor Equipment & Materials)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 25.79B | n/a | 25.3% | 32.1% | 5.40B | 4.61B | 17.9% |
| 2023 | 26.52B | 2.8% | 25.9% | 31.9% | 8.70B | 7.59B | 28.6% |
| 2024 | 27.18B | 2.5% | 26.4% | 32.3% | 8.68B | 7.49B | 27.6% |
| 2025 | 28.37B | 4.4% | 24.7% | 35.2% | 7.96B | 5.70B | 20.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-01 | 7.17B | 16.5% | 925.0M | 544.0M |
| 2025-04 | 7.10B | 30.1% | 1.57B | 1.06B |
| 2025-07 | 7.30B | 24.4% | 2.63B | 2.05B |
| 2025-10 | 6.80B | 27.9% | 2.83B | 2.04B |
| 2026-01 | 7.01B | 28.9% | 1.69B | 1.04B |
| 2026-04 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **8.1x**  (TTM 11.6x)
- 2026E TEV/EBITDA _est_: **25.3x**  (TTM 36.4x)
- 2026E TEV/FCF _est_: **74.5x**
- 2026E P/E: **27.0x**  (TTM 41.0x, fwd 27.0x)
- EV 337.54B, 26E rev 41.68B, 26E EPS 16.13x


**3) Performance:**


- L1M 12.0% · L3M 23.2% · L12M 153.0% · -1.6% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 12.0%, 3M 23.2%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (20.1%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## C — Citigroup, Inc.  (Financial Services / Banks - Diversified)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 74.48B | n/a | 19.9% | n/a | 25.07B | 19.44B | 26.1% |
| 2023 | 78.09B | 4.8% | 11.8% | n/a | -73.42B | -80.00B | -102.4% |
| 2024 | 80.67B | 3.3% | 15.7% | n/a | -19.67B | -26.17B | -32.4% |
| 2025 | 85.21B | 5.6% | 16.8% | n/a | -67.63B | -74.15B | -87.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 21.60B | 18.8% | -58.71B | -60.23B |
| 2025-06 | 21.66B | 18.6% | -36.58B | -38.33B |
| 2025-09 | 22.09B | 17.0% | 1.10B | -517.0M |
| 2025-12 | 19.67B | 12.6% | 26.55B | 24.92B |
| 2026-03 | 24.66B | 23.5% | -21.87B | -23.29B |


**2) Valuation:**


- 2026E TEV/Sales: **0.0x**  (TTM 0.0x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **10.1x**  (TTM 15.5x, fwd 10.1x)
- EV 3.74B, 26E rev 96.74B, 26E EPS 12.50x


**3) Performance:**


- L1M -4.1% · L3M 11.9% · L12M 67.6% · -6.8% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -4.1%, 3M 11.9%; -6.8% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CAT — Caterpillar, Inc.  (Industrials / Farm & Heavy Construction Machinery)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 59.43B | n/a | 11.3% | 19.2% | 7.77B | 5.17B | 8.7% |
| 2023 | 67.06B | 12.8% | 15.4% | 23.4% | 12.88B | 9.79B | 14.6% |
| 2024 | 64.81B | -3.4% | 16.7% | 24.7% | 12.04B | 8.82B | 13.6% |
| 2025 | 67.59B | 4.3% | 13.1% | 21.2% | 11.74B | 7.45B | 11.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 14.25B | 14.1% | 1.29B | 371.0M |
| 2025-06 | 16.57B | 13.2% | 3.12B | 2.17B |
| 2025-09 | 17.64B | 13.0% | 3.74B | 2.67B |
| 2025-12 | 19.13B | 12.6% | 3.59B | 2.25B |
| 2026-03 | 17.41B | 14.6% | 1.87B | 819.0M |


**2) Valuation:**


- 2026E TEV/Sales: **5.3x**  (TTM 6.2x)
- 2026E TEV/EBITDA _est_: **25.6x**  (TTM 30.1x)
- 2026E TEV/FCF _est_: **98.6x**
- 2026E P/E: **29.8x**  (TTM 44.3x, fwd 29.8x)
- EV 438.64B, 26E rev 83.35B, 26E EPS 29.81x


**3) Performance:**


- L1M 15.2% · L3M 15.0% · L12M 156.8% · -4.2% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 15.2%, 3M 15.0%; -4.2% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ none flagged from the numbers


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
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.94B | 19.3% | -213.0M | -227.0M |
| 2025-06 | 2.04B | 21.4% | 886.0M | 853.0M |
| 2025-09 | 2.12B | 23.3% | 1.70B | 1.66B |
| 2025-12 | 2.16B | 24.5% | -158.0M | -250.0M |
| 2026-03 | 2.17B | 23.8% | 237.0M | 237.0M |


**2) Valuation:**


- 2026E TEV/Sales: **2.8x**  (TTM 3.5x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **9.9x**  (TTM 15.0x, fwd 9.9x)
- EV 27.81B, 26E rev 9.92B, 26E EPS 6.39x


**3) Performance:**


- L1M -4.8% · L3M -5.8% · L12M 51.1% · -10.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -4.8%, 3M -5.8%; -10.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (24.7%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DOC — Healthpeak Properties, Inc.  (Real Estate / REIT - Healthcare Facilities)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 2.06B | n/a | 24.3% | 67.5% | 900.3M | 900.3M | 43.7% |
| 2023 | 2.18B | 5.8% | 14.0% | 58.0% | 956.2M | 956.2M | 43.8% |
| 2024 | 2.70B | 23.8% | 9.0% | 59.6% | 1.07B | 1.07B | 39.6% |
| 2025 | 2.82B | 4.5% | 2.5% | 58.4% | 1.25B | 1.25B | 44.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 702.9M | 6.1% | 279.4M | 279.4M |
| 2025-06 | 694.3M | 4.6% | 363.5M | 363.5M |
| 2025-09 | 705.9M | -16.6% | 315.0M | 315.0M |
| 2025-12 | 719.4M | 15.8% | 294.1M | 294.1M |
| 2026-03 | 753.0M | 25.7% | 260.9M | 260.9M |


**2) Valuation:**


- 2026E TEV/Sales: **8.2x**  (TTM 8.5x)
- 2026E TEV/EBITDA _est_: **15.3x**  (TTM 15.7x)
- 2026E TEV/FCF _est_: **21.3x**
- 2026E P/E: **146.4x**  (TTM 61.8x, fwd 146.4x)
- EV 24.31B, 26E rev 2.95B, 26E EPS 0.14x


**3) Performance:**


- L1M 13.4% · L3M 17.3% · L12M 22.4% · -2.1% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 13.4%, 3M 17.3%; -2.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (44.4%)


_Issues:_ revenue growth decelerating; rich valuation (26E P/E 146.4x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## EMN — Eastman Chemical Company  (Basic Materials / Specialty Chemicals)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 10.58B | n/a | 7.5% | 15.5% | 975.0M | 364.0M | 3.4% |
| 2023 | 9.21B | -12.9% | 9.7% | 19.5% | 1.37B | 546.0M | 5.9% |
| 2024 | 9.38B | 1.9% | 9.6% | 19.2% | 1.29B | 688.0M | 7.3% |
| 2025 | 8.75B | -6.7% | 5.4% | 14.9% | 970.0M | 424.0M | 4.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.29B | 7.9% | -167.0M | -314.0M |
| 2025-06 | 2.29B | 6.1% | 233.0M | 83.0M |
| 2025-09 | 2.20B | 2.1% | 402.0M | 265.0M |
| 2025-12 | 1.97B | 5.3% | 502.0M | 390.0M |
| 2026-03 | 2.18B | 4.9% | -137.0M | -240.0M |


**2) Valuation:**


- 2026E TEV/Sales: **1.4x**  (TTM 1.5x)
- 2026E TEV/EBITDA _est_: **8.9x**  (TTM 9.7x)
- 2026E TEV/FCF _est_: **27.9x**
- 2026E P/E: **10.6x**  (TTM 21.4x, fwd 10.6x)
- EV 13.23B, 26E rev 9.42B, 26E EPS 7.01x


**3) Performance:**


- L1M -2.4% · L3M -9.5% · L12M -7.1% · -11.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -2.4%, 3M -9.5%; -11.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ESS — Essex Property Trust, Inc.  (Real Estate / REIT - Residential)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 1.61B | n/a | 25.4% | 74.4% | 975.6M | 812.5M | 50.6% |
| 2023 | 1.67B | 3.9% | 24.3% | 71.4% | 980.1M | 839.7M | 50.3% |
| 2024 | 1.77B | 6.3% | 41.8% | 91.7% | 1.07B | 931.9M | 52.5% |
| 2025 | 1.89B | 6.4% | 35.5% | 83.1% | 1.07B | 934.1M | 49.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 464.6M | 43.7% | 281.5M | 253.6M |
| 2025-06 | 469.8M | 47.1% | 216.1M | 179.6M |
| 2025-09 | 473.3M | 34.8% | 342.6M | 306.2M |
| 2025-12 | 479.6M | 16.8% | 234.2M | 194.7M |
| 2026-03 | 484.8M | 21.9% | 287.2M | 267.4M |


**2) Valuation:**


- 2026E TEV/Sales: **12.3x**  (TTM 12.5x)
- 2026E TEV/EBITDA _est_: **18.9x**  (TTM 19.2x)
- 2026E TEV/FCF _est_: **24.6x**
- 2026E P/E: **46.6x**  (TTM 31.0x, fwd 46.6x)
- EV 24.60B, 26E rev 2.00B, 26E EPS 5.92x


**3) Performance:**


- L1M 7.7% · L3M 7.5% · L12M -0.3% · -5.9% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 7.7%, 3M 7.5%; -5.9% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (49.5%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ETN — Eaton Corporation, PLC  (Industrials / Specialty Industrial Machinery)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 20.75B | n/a | 11.9% | 19.3% | 2.53B | 1.94B | 9.3% |
| 2023 | 23.20B | 11.8% | 13.9% | 21.1% | 3.62B | 2.87B | 12.4% |
| 2024 | 24.88B | 7.3% | 15.3% | 22.6% | 4.33B | 3.52B | 14.1% |
| 2025 | 27.45B | 10.3% | 14.9% | 22.5% | 4.47B | 3.55B | 12.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 6.38B | 15.1% | 238.0M | 91.0M |
| 2025-06 | 7.03B | 14.0% | 918.0M | 716.0M |
| 2025-09 | 6.99B | 14.5% | 1.35B | 1.17B |
| 2025-12 | 7.05B | 16.0% | 1.97B | 1.57B |
| 2026-03 | 7.45B | 11.6% | 507.0M | 314.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.8x**  (TTM 5.9x)
- 2026E TEV/EBITDA _est_: **21.5x**  (TTM 26.7x)
- 2026E TEV/FCF _est_: **51.5x**
- 2026E P/E: **24.9x**  (TTM 38.2x, fwd 24.9x)
- EV 169.27B, 26E rev 35.41B, 26E EPS 15.72x


**3) Performance:**


- L1M 2.0% · L3M 3.2% · L12M 22.8% · -7.5% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 2.0%, 3M 3.2%; -7.5% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## F — Ford Motor Company  (Consumer Cyclical / Auto Manufacturers)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 158.06B | n/a | -1.3% | 3.0% | 6.85B | -13.0M | -0.0% |
| 2023 | 176.19B | 11.5% | 2.5% | 6.7% | 14.92B | 6.68B | 3.8% |
| 2024 | 184.99B | 5.0% | 3.2% | 7.7% | 15.42B | 6.74B | 3.6% |
| 2025 | 187.27B | 1.2% | -4.4% | 1.9% | 21.28B | 12.47B | 6.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 40.66B | 1.2% | 3.68B | 1.86B |
| 2025-06 | 50.18B | -0.1% | 6.32B | 4.23B |
| 2025-09 | 50.53B | 4.8% | 7.40B | 5.28B |
| 2025-12 | 45.89B | -24.1% | 3.88B | 1.10B |
| 2026-03 | 43.25B | 5.9% | 1.32B | -1.06B |


**2) Valuation:**


- 2026E TEV/Sales: **1.1x**  (TTM 1.0x)
- 2026E TEV/EBITDA _est_: **27.1x**  (TTM 25.4x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **8.1x**  (TTM n/a, fwd 8.1x)
- EV 192.23B, 26E rev 177.79B, 26E EPS 1.83x


**3) Performance:**


- L1M 9.1% · L3M -3.9% · L12M 32.0% · -7.5% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 9.1%, 3M -3.9%; -7.5% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ revenue growth decelerating; net margin negative (-4.4%)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## FITB — Fifth Third Bancorp  (Financial Services / Banks - Regional)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 8.10B | n/a | 30.2% | n/a | 6.43B | 5.74B | 70.9% |
| 2023 | 8.43B | 4.0% | 27.9% | n/a | 4.51B | 3.99B | 47.4% |
| 2024 | 8.27B | -1.8% | 28.0% | n/a | 2.82B | 2.41B | 29.1% |
| 2025 | 8.82B | 6.6% | 28.6% | n/a | 4.51B | 3.81B | 43.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.11B | 24.4% | 1.23B | 1.12B |
| 2025-06 | 2.22B | 28.3% | 1.31B | 1.10B |
| 2025-09 | 2.28B | 28.5% | 1.05B | 833.0M |
| 2025-12 | 2.21B | 33.1% | 929.0M | 754.0M |
| 2026-03 | 2.75B | 6.0% | -1.11B | -1.25B |


**2) Valuation:**


- 2026E TEV/Sales: **4.4x**  (TTM 6.8x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **10.2x**  (TTM 16.7x, fwd 10.1x)
- EV 61.20B, 26E rev 13.82B, 26E EPS 4.87x


**3) Performance:**


- L1M -4.4% · L3M -9.6% · L12M 24.6% · -13.3% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -4.4%, 3M -9.6%; -13.3% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (43.1%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## GEV — GE Vernova Inc.  (Industrials / Specialty Industrial Machinery)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 29.65B | n/a | -9.2% | -1.8% | -114.0M | -627.0M | -2.1% |
| 2023 | 33.24B | 12.1% | -1.3% | 2.8% | 1.19B | 442.0M | 1.3% |
| 2024 | 34.94B | 5.1% | 4.4% | 4.7% | 2.58B | 1.70B | 4.9% |
| 2025 | 38.07B | 9.0% | 12.8% | 5.9% | 4.99B | 3.71B | 9.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 8.03B | 3.2% | 1.16B | 975.0M |
| 2025-06 | 9.11B | 5.6% | 367.0M | 194.0M |
| 2025-09 | 9.97B | 4.5% | 980.0M | 733.0M |
| 2025-12 | 10.96B | 33.4% | 2.48B | 1.81B |
| 2026-03 | 9.34B | 50.8% | 5.19B | 4.79B |


**2) Valuation:**


- 2026E TEV/Sales: **5.3x**  (TTM 7.0x)
- 2026E TEV/EBITDA _est_: **61.3x**  (TTM 80.7x)
- 2026E TEV/FCF _est_: **22.5x**
- 2026E P/E: **43.3x**  (TTM 30.7x, fwd 42.9x)
- EV 275.62B, 26E rev 51.87B, 26E EPS 24.29x


**3) Performance:**


- L1M 7.2% · L3M 30.9% · L12M 142.9% · -8.7% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 7.2%, 3M 30.9%; -8.7% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## GLW — Corning Incorporated  (Technology / Electronic Components)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 14.19B | n/a | 9.3% | 25.0% | 2.62B | 1.01B | 7.1% |
| 2023 | 12.59B | -11.3% | 4.6% | 20.0% | 2.00B | 615.0M | 4.9% |
| 2024 | 13.12B | 4.2% | 3.9% | 19.0% | 1.94B | 974.0M | 7.4% |
| 2025 | 15.63B | 19.1% | 10.2% | 23.9% | 2.69B | 1.41B | 9.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 3.45B | 4.5% | 151.0M | -57.0M |
| 2025-06 | 3.86B | 12.1% | 708.0M | 400.0M |
| 2025-09 | 4.10B | 10.5% | 784.0M | 450.0M |
| 2025-12 | 4.21B | 12.8% | 1.05B | 620.0M |
| 2026-03 | 4.14B | 9.0% | 362.0M | 30.0M |


**2) Valuation:**


- 2026E TEV/Sales: **7.7x**  (TTM 10.7x)
- 2026E TEV/EBITDA _est_: **32.1x**  (TTM 44.5x)
- 2026E TEV/FCF _est_: **205.0x**
- 2026E P/E: **46.0x**  (TTM 94.0x, fwd 46.0x)
- EV 173.85B, 26E rev 22.62B, 26E EPS 4.22x


**3) Performance:**


- L1M 15.5% · L3M 44.0% · L12M 314.2% · -7.9% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 15.5%, 3M 44.0%; -7.9% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +19.1% latest FY; revenue growth accelerating; net margin expanding


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## INTC — Intel Corporation  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 63.05B | n/a | 12.7% | 33.8% | 15.43B | -9.41B | -14.9% |
| 2023 | 54.23B | -14.0% | 3.1% | 20.7% | 11.47B | -14.28B | -26.3% |
| 2024 | 53.10B | -2.1% | -35.3% | 2.3% | 8.29B | -15.66B | -29.5% |
| 2025 | 52.85B | -0.5% | -0.5% | 27.2% | 9.70B | -4.95B | -9.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 12.67B | -6.5% | 813.0M | -4.37B |
| 2025-06 | 12.86B | -22.7% | 2.05B | -1.50B |
| 2025-09 | 13.65B | 29.8% | 2.55B | 121.0M |
| 2025-12 | 13.67B | -4.3% | 4.29B | 800.0M |
| 2026-03 | 13.58B | -27.5% | 1.10B | -2.54B |


**2) Valuation:**


- 2026E TEV/Sales: **9.5x**  (TTM 11.6x)
- 2026E TEV/EBITDA _est_: **36.2x**  (TTM 43.8x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **78.1x**  (TTM n/a, fwd 78.1x)
- EV 621.42B, 26E rev 65.09B, 26E EPS 1.54x


**3) Performance:**


- L1M 58.8% · L3M 132.5% · L12M 405.4% · -16.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 58.8%, 3M 132.5%; -16.0% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ net margin negative (-0.5%); negative free cash flow; rich valuation (26E P/E 78.1x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## INVH — Invitation Homes Inc.  (Real Estate / REIT - Residential)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 2.24B | n/a | 17.1% | 59.3% | 1.02B | 815.5M | 36.4% |
| 2023 | 2.43B | 8.7% | 21.4% | 62.9% | 1.11B | 886.0M | 36.4% |
| 2024 | 2.62B | 7.7% | 17.3% | 58.6% | 1.08B | 862.4M | 32.9% |
| 2025 | 2.73B | 4.2% | 21.5% | 61.9% | 1.21B | 963.5M | 35.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 674.5M | 24.6% | 300.5M | 249.6M |
| 2025-06 | 681.4M | 20.7% | 382.5M | 322.5M |
| 2025-09 | 688.2M | 19.9% | 394.6M | 321.5M |
| 2025-12 | 685.2M | 21.1% | 128.7M | 69.9M |
| 2026-03 | 734.1M | 21.9% | 293.0M | 236.0M |


**2) Valuation:**


- 2026E TEV/Sales: **9.0x**  (TTM 9.4x)
- 2026E TEV/EBITDA _est_: **16.7x**  (TTM 17.4x)
- 2026E TEV/FCF _est_: **24.4x**
- 2026E P/E: **43.9x**  (TTM 30.7x, fwd 43.9x)
- EV 26.00B, 26E rev 2.90B, 26E EPS 0.66x


**3) Performance:**


- L1M 6.3% · L3M 4.7% · L12M -13.0% · -15.4% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 6.3%, 3M 4.7%; -15.4% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ net margin expanding; strong FCF margin (35.3%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## KEY — KeyCorp  (Financial Services / Banks - Regional)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 7.03B | n/a | 27.3% | n/a | 4.47B | 4.36B | 62.1% |
| 2023 | 6.21B | -11.5% | 15.6% | n/a | 2.90B | 2.76B | 44.4% |
| 2024 | 4.40B | -29.3% | -3.7% | n/a | 664.0M | 599.0M | 13.6% |
| 2025 | 7.29B | 65.7% | 25.1% | n/a | 2.21B | 2.10B | 28.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.72B | 23.5% | -140.0M | -150.0M |
| 2025-06 | 1.78B | 23.8% | 1.23B | 1.21B |
| 2025-09 | 1.84B | 26.5% | 396.0M | 367.0M |
| 2025-12 | 1.94B | 26.3% | 718.0M | 673.0M |
| 2026-03 | 1.91B | 27.3% | -62.0M | -74.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.8x**  (TTM 5.7x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **10.1x**  (TTM 13.3x, fwd 10.1x)
- EV 41.17B, 26E rev 8.59B, 26E EPS 2.15x


**3) Performance:**


- L1M -2.9% · L3M -2.1% · L12M 32.6% · -8.5% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -2.9%, 3M -2.1%; -8.5% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +65.7% latest FY; revenue growth accelerating; net margin expanding; strong FCF margin (28.8%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## LNT — Alliant Energy Corporation  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 4.21B | n/a | 16.3% | 40.5% | 486.0M | 486.0M | 11.6% |
| 2023 | 4.03B | -4.2% | 17.5% | 43.5% | 867.0M | 867.0M | 21.5% |
| 2024 | 3.98B | -1.1% | 17.3% | 44.6% | 1.17B | 1.17B | 29.3% |
| 2025 | 4.36B | 9.6% | 18.6% | 45.7% | 1.17B | 1.17B | 26.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.13B | 18.9% | 249.0M | 249.0M |
| 2025-06 | 961.0M | 18.1% | 243.0M | 243.0M |
| 2025-09 | 1.21B | 23.2% | 408.0M | 408.0M |
| 2025-12 | 1.06B | 13.3% | 269.0M | 269.0M |
| 2026-03 | 1.18B | 18.9% | 368.0M | 368.0M |


**2) Valuation:**


- 2026E TEV/Sales: **6.5x**  (TTM 6.9x)
- 2026E TEV/EBITDA _est_: **15.4x**  (TTM 16.5x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **20.1x**  (TTM 23.3x, fwd 20.1x)
- EV 30.65B, 26E rev 4.75B, 26E EPS 3.69x


**3) Performance:**


- L1M -1.8% · L3M 0.3% · L12M 20.9% · -4.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -1.8%, 3M 0.3%; -4.3% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (26.8%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MCHP — Microchip Technology Incorporat  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 6.82B | n/a | 18.8% | 42.1% | 2.84B | 2.47B | 36.3% |
| 2023 | 8.44B | 23.7% | 26.5% | 48.6% | 3.62B | 3.13B | 37.1% |
| 2024 | 7.63B | -9.5% | 25.0% | 45.0% | 2.89B | 2.61B | 34.2% |
| 2025 | 4.40B | -42.3% | -0.0% | 23.6% | 898.1M | 772.1M | 17.5% |
| 2026 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | 1.03B | -5.2% | 271.5M | 253.4M |
| 2025-03 | 970.5M | -15.9% | 205.9M | 191.7M |
| 2025-06 | 1.08B | -1.7% | 275.6M | 257.7M |
| 2025-09 | 1.14B | 3.7% | 88.1M | 51.6M |
| 2025-12 | 1.19B | 5.3% | 341.4M | 318.9M |
| 2026-03 | n/a | n/a | n/a | n/a |


**2) Valuation:**


- 2026E TEV/Sales: **7.7x**  (TTM 11.6x)
- 2026E TEV/EBITDA _est_: **29.2x**  (TTM 44.1x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **23.1x**  (TTM 429.7x, fwd 23.1x)
- EV 54.59B, 26E rev 7.11B, 26E EPS 4.09x


**3) Performance:**


- L1M 22.1% · L3M 20.2% · L12M 59.4% · -8.8% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 22.1%, 3M 20.2%; -8.8% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (17.5%)


_Issues:_ revenue growth decelerating; net margin negative (-0.0%)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MGM — MGM Resorts International  (Consumer Cyclical / Resorts & Casinos)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 13.13B | n/a | 11.2% | 37.9% | 1.76B | 991.4M | 7.6% |
| 2023 | 16.16B | 23.1% | 7.1% | 17.0% | 2.69B | 1.76B | 10.9% |
| 2024 | 17.24B | 6.7% | 4.3% | 13.9% | 2.36B | 1.21B | 7.0% |
| 2025 | 17.54B | 1.7% | 1.2% | 9.8% | 2.53B | 1.46B | 8.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.28B | 3.5% | 547.1M | 319.0M |
| 2025-06 | 4.40B | 1.1% | 645.9M | 377.4M |
| 2025-09 | 4.25B | -6.7% | 681.4M | 405.4M |
| 2025-12 | 4.61B | 6.4% | 655.0M | 358.5M |
| 2026-03 | 4.45B | 2.8% | 567.8M | 413.1M |


**2) Valuation:**


- 2026E TEV/Sales: **2.2x**  (TTM 2.2x)
- 2026E TEV/EBITDA _est_: **17.2x**  (TTM 17.5x)
- 2026E TEV/FCF _est_: **74.1x**
- 2026E P/E: **17.4x**  (TTM 53.0x, fwd 17.4x)
- EV 39.72B, 26E rev 17.97B, 26E EPS 2.23x


**3) Performance:**


- L1M -3.9% · L3M 8.3% · L12M 5.8% · -8.8% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -3.9%, 3M 8.3%; -8.8% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MPWR — Monolithic Power Systems, Inc.  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 1.79B | n/a | 24.4% | 31.4% | 246.7M | 187.8M | 10.5% |
| 2023 | 1.82B | 1.5% | 23.5% | 28.7% | 638.2M | 580.6M | 31.9% |
| 2024 | 2.21B | 21.2% | 72.1% | 26.1% | 788.4M | 624.1M | 28.3% |
| 2025 | 2.79B | 26.4% | 22.3% | 28.0% | 838.2M | 663.3M | 23.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 637.6M | 21.2% | 256.4M | 216.0M |
| 2025-06 | 664.6M | 20.1% | 237.6M | 187.5M |
| 2025-09 | 737.2M | 24.2% | 239.3M | 196.2M |
| 2025-12 | 751.2M | 23.4% | 104.9M | 63.5M |
| 2026-03 | 804.2M | 24.0% | 250.3M | 179.4M |


**2) Valuation:**


- 2026E TEV/Sales: **16.7x**  (TTM 25.5x)
- 2026E TEV/EBITDA _est_: **57.5x**  (TTM 87.9x)
- 2026E TEV/FCF _est_: **100.3x**
- 2026E P/E: **52.4x**  (TTM 113.8x, fwd 52.4x)
- EV 75.36B, 26E rev 4.52B, 26E EPS 30.16x


**3) Performance:**


- L1M 10.5% · L3M 32.6% · L12M 112.7% · -6.7% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 10.5%, 3M 32.6%; -6.7% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +26.4% latest FY; revenue growth accelerating; strong FCF margin (23.8%)


_Issues:_ high TEV/Sales 26E (16.7x)


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## NTRS — Northern Trust Corporation  (Financial Services / Asset Management)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 6.76B | n/a | 19.8% | n/a | 2.39B | 1.67B | 24.7% |
| 2023 | 6.77B | 0.2% | 16.3% | n/a | 2.63B | 1.95B | 28.8% |
| 2024 | 8.29B | 22.4% | 24.5% | n/a | -486.0M | -1.23B | -14.9% |
| 2025 | 8.09B | -2.5% | 21.5% | n/a | 5.53B | 4.76B | 58.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 1.94B | 20.2% | 2.75B | 2.57B |
| 2025-06 | 2.00B | 21.1% | 1.87B | 1.65B |
| 2025-09 | 2.03B | 22.6% | 525.8M | 357.5M |
| 2025-12 | 2.12B | 21.9% | 388.4M | 183.5M |
| 2026-03 | 2.21B | 23.8% | -320.0M | -539.5M |


**2) Valuation:**


- 2026E TEV/Sales: **4.1x**  (TTM 4.5x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **14.3x**  (TTM 17.6x, fwd 14.2x)
- EV 37.42B, 26E rev 9.16B, 26E EPS 11.76x


**3) Performance:**


- L1M 4.5% · L3M 12.6% · L12M 57.9% · -4.6% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M 4.5%, 3M 12.6%; -4.6% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (58.9%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## NUE — Nucor Corporation  (Basic Materials / Steel)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 41.51B | n/a | 18.3% | 27.9% | 10.07B | 8.12B | 19.6% |
| 2023 | 34.71B | -16.4% | 13.0% | 22.1% | 7.11B | 4.90B | 14.1% |
| 2024 | 30.73B | -11.5% | 6.6% | 14.6% | 3.98B | 806.0M | 2.6% |
| 2025 | 32.49B | 5.7% | 5.4% | 13.0% | 3.23B | -188.0M | -0.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2025-03 | 7.83B | 2.0% | 364.0M | -495.0M |
| 2025-06 | 8.46B | 7.1% | 732.0M | -222.0M |
| 2025-09 | 8.52B | 7.1% | 1.34B | 532.0M |
| 2025-12 | 7.69B | 4.9% | 799.0M | -3.0M |
| 2026-03 | 9.50B | 7.8% | 886.0M | 225.0M |


**2) Valuation:**


- 2026E TEV/Sales: **1.5x**  (TTM 1.7x)
- 2026E TEV/EBITDA _est_: **10.2x**  (TTM 11.6x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **14.7x**  (TTM 23.0x, fwd 14.7x)
- EV 57.31B, 26E rev 38.79B, 26E EPS 15.79x


**3) Performance:**


- L1M 18.3% · L3M 24.3% · L12M 96.8% · -3.1% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 18.3%, 3M 24.3%; -3.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ON — ON Semiconductor Corporation  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 8.33B | n/a | 22.8% | 36.1% | 2.63B | 1.60B | 19.2% |
| 2023 | 8.25B | -0.9% | 26.5% | 39.0% | 1.98B | 438.4M | 5.3% |
| 2024 | 7.08B | -14.2% | 22.2% | 35.9% | 1.91B | 1.21B | 17.1% |
| 2025 | 6.00B | -15.3% | 2.0% | 14.8% | 1.76B | 1.42B | 23.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.45B | -33.6% | 602.3M | 454.7M |
| 2025-06 | 1.47B | 11.6% | 184.3M | 106.1M |
| 2025-09 | 1.55B | 16.4% | 418.7M | 372.4M |
| 2025-12 | 1.53B | 11.9% | 554.5M | 485.4M |
| 2026-03 | 1.51B | -2.2% | 239.1M | 217.2M |


**2) Valuation:**


- 2026E TEV/Sales: **6.1x**  (TTM 7.2x)
- 2026E TEV/EBITDA _est_: **18.1x**  (TTM 21.4x)
- 2026E TEV/FCF _est_: **28.9x**
- 2026E P/E: **27.4x**  (TTM 85.8x, fwd 27.4x)
- EV 43.82B, 26E rev 7.17B, 26E EPS 4.25x


**3) Performance:**


- L1M 41.5% · L3M 56.6% · L12M 150.2% · -4.4% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 41.5%, 3M 56.6%; -4.4% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (23.7%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## PNC — PNC Financial Services Group, I  (Financial Services / Banks - Regional)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 21.11B | n/a | 28.6% | n/a | 9.08B | 9.08B | 43.0% |
| 2023 | 21.51B | 1.9% | 25.9% | n/a | 10.11B | 10.11B | 47.0% |
| 2024 | 20.81B | -3.3% | 28.3% | n/a | 7.88B | 7.88B | 37.9% |
| 2025 | 23.08B | 10.9% | 30.1% | n/a | 4.38B | 4.38B | 19.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 5.45B | 27.2% | -509.0M | -509.0M |
| 2025-06 | 5.66B | 28.7% | 1.48B | 1.48B |
| 2025-09 | 5.90B | 30.6% | 2.66B | 2.66B |
| 2025-12 | 6.07B | 33.3% | 757.0M | 757.0M |
| 2026-03 | 6.16B | 28.6% | 1.93B | 1.93B |


**2) Valuation:**


- 2026E TEV/Sales: **5.5x**  (TTM 6.4x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **10.5x**  (TTM 12.8x, fwd 10.5x)
- EV 148.18B, 26E rev 27.08B, 26E EPS 21.03x


**3) Performance:**


- L1M -3.3% · L3M -6.5% · L12M 23.7% · -11.5% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -3.3%, 3M -6.5%; -11.5% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (19.0%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## QCOM — QUALCOMM Incorporated  (Technology / Semiconductors)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 44.20B | n/a | 29.3% | 39.0% | 9.10B | 6.83B | 15.5% |
| 2023 | 35.82B | -19.0% | 20.2% | 27.8% | 11.30B | 9.85B | 27.5% |
| 2024 | 38.96B | 8.8% | 26.0% | 32.7% | 12.20B | 11.16B | 28.6% |
| 2025 | 44.28B | 13.7% | 12.5% | 33.7% | 14.01B | 12.82B | 28.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 10.98B | 25.6% | 2.55B | 2.34B |
| 2025-06 | 10.37B | 25.7% | 2.88B | 2.58B |
| 2025-09 | 11.27B | -27.7% | 4.00B | 3.59B |
| 2025-12 | 12.25B | 24.5% | 4.96B | 4.42B |
| 2026-03 | 10.60B | 69.5% | 2.45B | 1.92B |


**2) Valuation:**


- 2026E TEV/Sales: **5.4x**  (TTM 5.2x)
- 2026E TEV/EBITDA _est_: **18.6x**  (TTM 17.7x)
- 2026E TEV/FCF _est_: **25.2x**
- 2026E P/E: **22.4x**  (TTM 25.7x, fwd 22.4x)
- EV 230.41B, 26E rev 42.46B, 26E EPS 10.64x


**3) Performance:**


- L1M 49.8% · L3M 44.1% · L12M 34.8% · -15.2% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 49.8%, 3M 44.1%; -15.2% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (28.9%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ROK — Rockwell Automation, Inc.  (Industrials / Specialty Industrial Machinery)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 7.76B | n/a | 12.0% | 18.5% | 823.1M | 682.0M | 8.8% |
| 2023 | 9.06B | 16.7% | 15.3% | 22.0% | 1.37B | 1.21B | 13.4% |
| 2024 | 8.26B | -8.8% | 11.5% | 19.0% | 864.0M | 639.0M | 7.7% |
| 2025 | 8.34B | 0.9% | 10.4% | 16.8% | 1.54B | 1.36B | 16.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.00B | 12.4% | 199.0M | 171.0M |
| 2025-06 | 2.14B | 13.8% | 527.0M | 489.0M |
| 2025-09 | 2.32B | 6.0% | 454.0M | 405.0M |
| 2025-12 | 2.10B | 14.5% | 234.0M | 170.0M |
| 2026-03 | 2.24B | 15.7% | 320.0M | 275.0M |


**2) Valuation:**


- 2026E TEV/Sales: **5.6x**  (TTM 6.0x)
- 2026E TEV/EBITDA _est_: **24.9x**  (TTM 26.8x)
- 2026E TEV/FCF _est_: **50.4x**
- 2026E P/E: **31.2x**  (TTM 47.0x, fwd 31.2x)
- EV 52.67B, 26E rev 9.44B, 26E EPS 14.51x


**3) Performance:**


- L1M 11.4% · L3M 14.2% · L12M 48.1% · -2.3% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 11.4%, 3M 14.2%; -2.3% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (16.3%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## STT — State Street Corporation  (Financial Services / Asset Management)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 12.12B | n/a | 22.9% | n/a | 11.95B | 11.22B | 92.5% |
| 2023 | 11.95B | -1.5% | 16.3% | n/a | 690.0M | -126.0M | -1.1% |
| 2024 | 12.92B | 8.2% | 20.8% | n/a | -13.21B | -14.14B | -109.4% |
| 2025 | 13.96B | 8.1% | 21.1% | n/a | 11.90B | 10.84B | 77.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.28B | 19.6% | 2.40B | 2.17B |
| 2025-06 | 3.47B | 20.0% | -8.44B | -8.76B |
| 2025-09 | 3.54B | 24.3% | 7.90B | 7.66B |
| 2025-12 | 3.67B | 20.4% | 10.04B | 9.78B |
| 2026-03 | 3.80B | 20.1% | -12.14B | -12.41B |


**2) Valuation:**


- 2026E TEV/Sales: **n/a**  (TTM n/a)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **11.2x**  (TTM 15.7x, fwd 11.2x)
- EV n/a, 26E rev 15.82B, 26E EPS 13.82x


**3) Performance:**


- L1M 7.7% · L3M 20.2% · L12M 60.8% · -0.8% from 12-mo high


**4) Reason for breakout:**


new 6-month high; 1M 7.7%, 3M 20.2%; at/near 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ net margin expanding; strong FCF margin (77.6%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## TFC — Truist Financial Corporation  (Financial Services / Banks - Regional)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 19.97B | n/a | 31.3% | n/a | 11.08B | 11.08B | 55.5% |
| 2023 | 20.02B | 0.2% | -5.4% | n/a | 8.63B | 8.63B | 43.1% |
| 2024 | 13.28B | -33.7% | 36.3% | n/a | 2.16B | 2.16B | 16.3% |
| 2025 | 20.32B | 53.0% | 26.1% | n/a | 5.74B | 5.74B | 28.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.90B | 25.7% | 746.0M | 746.0M |
| 2025-06 | 4.99B | 24.9% | 914.0M | 914.0M |
| 2025-09 | 5.19B | 28.0% | 1.50B | 1.50B |
| 2025-12 | 5.25B | 25.8% | 2.58B | 2.58B |
| 2026-03 | 5.15B | 28.7% | 679.0M | 679.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.1x**  (TTM 4.8x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **9.4x**  (TTM 12.0x, fwd 9.4x)
- EV 89.94B, 26E rev 22.20B, 26E EPS 5.13x


**3) Performance:**


- L1M -4.0% · L3M -8.6% · L12M 19.1% · -14.1% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -4.0%, 3M -8.6%; -14.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +53.0% latest FY; revenue growth accelerating; strong FCF margin (28.2%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## WST — West Pharmaceutical Services, I  (Healthcare / Medical Instruments & Supplies)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 2.89B | n/a | 20.3% | 28.0% | 724.0M | 439.4M | 15.2% |
| 2023 | 2.95B | 2.2% | 20.1% | 28.6% | 776.5M | 414.5M | 14.1% |
| 2024 | 2.89B | -1.9% | 17.0% | 25.7% | 653.4M | 276.4M | 9.6% |
| 2025 | 3.07B | 6.3% | 16.1% | 25.1% | 754.8M | 468.9M | 15.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 698.0M | 12.9% | 129.4M | 58.1M |
| 2025-06 | 766.5M | 17.2% | 177.1M | 101.9M |
| 2025-09 | 804.6M | 17.4% | 197.2M | 133.9M |
| 2025-12 | 805.0M | 16.4% | 251.1M | 175.0M |
| 2026-03 | 844.9M | 16.4% | 89.9M | 47.2M |


**2) Valuation:**


- 2026E TEV/Sales: **6.3x**  (TTM 6.9x)
- 2026E TEV/EBITDA _est_: **23.2x**  (TTM 25.4x)
- 2026E TEV/FCF _est_: **73.1x**
- 2026E P/E: **33.2x**  (TTM 42.3x, fwd 33.2x)
- EV 22.13B, 26E rev 3.54B, 26E EPS 9.55x


**3) Performance:**


- L1M 12.3% · L3M 21.0% · L12M 47.0% · -7.1% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M 12.3%, 3M 21.0%; -7.1% from 12-mo high; trend tag: up


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; strong FCF margin (15.3%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## ACGL — Arch Capital Group Ltd.  (Financial Services / Insurance - Diversified)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 9.61B | n/a | 15.4% | n/a | 3.82B | 3.77B | 39.2% |
| 2023 | 13.30B | 38.3% | 33.4% | n/a | 5.75B | 5.70B | 42.8% |
| 2024 | 16.93B | 27.3% | 25.5% | n/a | 6.67B | 6.62B | 39.1% |
| 2025 | 19.29B | 14.0% | 22.8% | n/a | 6.17B | 6.13B | 31.8% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 4.59B | 12.5% | 1.46B | 1.45B |
| 2025-06 | 4.96B | 24.9% | 1.12B | 1.11B |
| 2025-09 | 4.98B | 27.1% | 2.19B | 2.17B |
| 2025-12 | 4.76B | 26.0% | 1.40B | 1.39B |
| 2026-03 | 4.38B | 23.9% | 1.19B | 1.18B |


**2) Valuation:**


- 2026E TEV/Sales: **2.0x**  (TTM 1.7x)
- 2026E TEV/EBITDA _est_: **6.7x**  (TTM 5.7x)
- 2026E TEV/FCF _est_: **7.5x**
- 2026E P/E: **9.7x**  (TTM 7.4x, fwd 9.7x)
- EV 33.39B, 26E rev 16.66B, 26E EPS 9.90x


**3) Performance:**


- L1M -3.2% · L3M -4.5% · L12M 3.4% · -7.8% from 12-mo high


**4) Reason for breakout:**


volatility-squeeze release; 1M -3.2%, 3M -4.5%; -7.8% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ strong FCF margin (31.8%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## AEE — Ameren Corporation  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 7.96B | n/a | 13.5% | 39.4% | 2.26B | -1.12B | -14.0% |
| 2023 | 7.50B | -5.7% | 15.4% | 44.7% | 2.56B | -1.21B | -16.1% |
| 2024 | 7.62B | 1.6% | 15.5% | 45.2% | 2.76B | -1.65B | -21.6% |
| 2025 | 8.80B | 15.4% | 16.5% | 44.8% | 3.35B | -821.0M | -9.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.10B | 13.8% | 431.0M | -651.0M |
| 2025-06 | 2.22B | 12.4% | 862.0M | -205.0M |
| 2025-09 | 2.70B | 23.7% | 1.10B | 115.0M |
| 2025-12 | 1.78B | 14.1% | 956.0M | -80.0M |
| 2026-03 | 2.18B | 16.4% | 421.0M | -1.18B |


**2) Valuation:**


- 2026E TEV/Sales: **5.3x**  (TTM 6.1x)
- 2026E TEV/EBITDA _est_: **11.8x**  (TTM 13.5x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **19.0x**  (TTM 20.0x, fwd 19.2x)
- EV 51.82B, 26E rev 9.80B, 26E EPS 5.84x


**3) Performance:**


- L1M -5.3% · L3M -3.5% · L12M 15.2% · -7.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -5.3%, 3M -3.5%; -7.0% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +15.4% latest FY; revenue growth accelerating; net margin expanding


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## AMGN — Amgen Inc.  (Healthcare / Drug Manufacturers - General)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 26.32B | n/a | 24.9% | 46.2% | 9.72B | 8.79B | 33.4% |
| 2023 | 28.19B | 7.1% | 23.8% | 52.5% | 8.47B | 7.36B | 26.1% |
| 2024 | 33.42B | 18.6% | 12.2% | 40.0% | 11.49B | 10.39B | 31.1% |
| 2025 | 36.75B | 10.0% | 21.0% | 46.0% | 9.96B | 8.10B | 22.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 8.15B | 21.2% | 1.39B | 980.0M |
| 2025-06 | 9.18B | 15.6% | 2.28B | 1.91B |
| 2025-09 | 9.56B | 33.7% | 4.68B | 4.25B |
| 2025-12 | 9.87B | 13.5% | 1.60B | 961.0M |
| 2026-03 | 8.62B | 21.1% | 2.19B | 1.48B |


**2) Valuation:**


- 2026E TEV/Sales: **5.9x**  (TTM 6.1x)
- 2026E TEV/EBITDA _est_: **12.9x**  (TTM 13.4x)
- 2026E TEV/FCF _est_: **29.4x**
- 2026E P/E: **14.4x**  (TTM 23.6x, fwd 14.4x)
- EV 227.39B, 26E rev 38.75B, 26E EPS 23.48x


**3) Performance:**


- L1M -5.9% · L3M -10.9% · L12M 29.3% · -15.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -5.9%, 3M -10.9%; -15.3% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ net margin expanding; strong FCF margin (22.0%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CMS — CMS Energy Corporation  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 8.60B | n/a | 9.7% | 29.6% | 855.0M | -1.63B | -18.9% |
| 2023 | 7.46B | -13.2% | 11.9% | 37.2% | 2.31B | -1.08B | -14.4% |
| 2024 | 7.51B | 0.7% | 13.3% | 40.9% | 2.37B | -808.0M | -10.8% |
| 2025 | 8.54B | 13.6% | 12.5% | 39.3% | 2.23B | -1.80B | -21.1% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.45B | 12.4% | 1.03B | 231.0M |
| 2025-06 | 1.84B | 10.9% | 383.0M | -697.0M |
| 2025-09 | 2.02B | 13.7% | 343.0M | -703.0M |
| 2025-12 | 2.23B | 12.9% | 478.0M | -634.0M |
| 2026-03 | 2.73B | 12.5% | 736.0M | -257.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.6x**  (TTM 4.8x)
- 2026E TEV/EBITDA _est_: **13.2x**  (TTM 13.9x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **17.9x**  (TTM 20.6x, fwd 17.9x)
- EV 42.46B, 26E rev 9.30B, 26E EPS 4.17x


**3) Performance:**


- L1M -7.6% · L3M -5.2% · L12M 7.3% · -9.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -7.6%, 3M -5.2%; -9.7% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## CNP — CenterPoint Energy, Inc (Holdin  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 9.32B | n/a | 11.3% | 34.6% | 1.81B | -2.61B | -28.0% |
| 2023 | 8.70B | -6.7% | 10.5% | 36.7% | 3.88B | -524.0M | -6.0% |
| 2024 | 8.64B | -0.6% | 11.8% | 40.4% | 2.14B | -2.37B | -27.5% |
| 2025 | 9.36B | 8.3% | 11.2% | 39.3% | 2.49B | -2.38B | -25.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.92B | 10.2% | 410.0M | -628.0M |
| 2025-06 | 1.94B | 10.2% | 560.0M | -569.0M |
| 2025-09 | 1.99B | 14.7% | 742.0M | -480.0M |
| 2025-12 | 2.50B | 10.5% | 774.0M | -707.0M |
| 2026-03 | 2.98B | 10.6% | 282.0M | -916.0M |


**2) Valuation:**


- 2026E TEV/Sales: **4.9x**  (TTM 5.4x)
- 2026E TEV/EBITDA _est_: **12.6x**  (TTM 14.0x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **20.5x**  (TTM 26.2x, fwd 20.5x)
- EV 51.27B, 26E rev 10.46B, 26E EPS 2.08x


**3) Performance:**


- L1M -3.9% · L3M -1.8% · L12M 16.2% · -5.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -3.9%, 3M -1.8%; -5.9% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DRI — Darden Restaurants, Inc.  (Consumer Cyclical / Restaurants)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 9.63B | n/a | 9.9% | 15.9% | 1.26B | 853.6M | 8.9% |
| 2023 | 10.49B | 8.9% | 9.4% | 15.2% | 1.55B | 951.3M | 9.1% |
| 2024 | 11.39B | 8.6% | 9.0% | 15.6% | 1.61B | 983.6M | 8.6% |
| 2025 | 12.08B | 6.0% | 8.7% | 15.6% | 1.70B | 1.03B | 8.5% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-11 | n/a | n/a | n/a | n/a |
| 2025-02 | 3.16B | 10.2% | 580.3M | 417.1M |
| 2025-05 | 3.27B | 9.3% | 456.4M | 275.0M |
| 2025-08 | 3.04B | 8.5% | 342.5M | 162.9M |
| 2025-11 | 3.10B | 7.6% | 320.4M | 112.0M |
| 2026-02 | 3.35B | 9.2% | 615.7M | 444.3M |


**2) Valuation:**


- 2026E TEV/Sales: **2.2x**  (TTM 2.4x)
- 2026E TEV/EBITDA _est_: **14.1x**  (TTM 15.2x)
- 2026E TEV/FCF _est_: **41.9x**
- 2026E P/E: **17.8x**  (TTM 21.3x, fwd 17.8x)
- EV 30.49B, 26E rev 13.71B, 26E EPS 11.37x


**3) Performance:**


- L1M -0.4% · L3M -6.7% · L12M -2.7% · -10.6% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -0.4%, 3M -6.7%; -10.6% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DTE — DTE Energy Company  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 19.23B | n/a | 5.6% | 16.9% | 1.98B | -1.40B | -7.3% |
| 2023 | 12.74B | -33.7% | 11.0% | 31.1% | 3.22B | -714.0M | -5.6% |
| 2024 | 12.46B | -2.3% | 11.3% | 32.5% | 3.64B | -824.0M | -6.6% |
| 2025 | 15.81B | 26.9% | 9.2% | 28.1% | 3.41B | -1.02B | -6.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.44B | 10.0% | 1.02B | 147.0M |
| 2025-06 | 3.42B | 6.7% | 709.0M | -262.0M |
| 2025-09 | 3.53B | 11.9% | 632.0M | -590.0M |
| 2025-12 | 4.43B | 8.3% | 1.05B | -315.0M |
| 2026-03 | 5.14B | 4.8% | 906.0M | -323.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.4x**  (TTM 3.4x)
- 2026E TEV/EBITDA _est_: **15.9x**  (TTM 16.0x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **17.4x**  (TTM 23.9x, fwd 17.4x)
- EV 56.64B, 26E rev 16.58B, 26E EPS 8.35x


**3) Performance:**


- L1M -4.9% · L3M -2.8% · L12M 8.9% · -7.9% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -4.9%, 3M -2.8%; -7.9% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue +26.9% latest FY; revenue growth accelerating


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## DUK — Duke Energy Corporation (Holdin  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 28.77B | n/a | 8.9% | 43.0% | 5.93B | -5.44B | -18.9% |
| 2023 | 29.06B | 1.0% | 9.8% | 47.7% | 9.88B | -2.73B | -9.4% |
| 2024 | 30.36B | 4.5% | 14.9% | 49.4% | 12.33B | 48.0M | 0.2% |
| 2025 | 32.24B | 6.2% | 15.4% | 52.9% | 12.33B | -1.69B | -5.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 8.25B | 16.7% | 2.18B | -971.0M |
| 2025-06 | 7.51B | 13.1% | 2.86B | -417.0M |
| 2025-09 | 8.54B | 16.6% | 3.63B | 179.0M |
| 2025-12 | 7.94B | 14.9% | 3.66B | -485.0M |
| 2026-03 | 9.18B | 16.9% | 1.51B | -2.58B |


**2) Valuation:**


- 2026E TEV/Sales: **5.4x**  (TTM 5.8x)
- 2026E TEV/EBITDA _est_: **10.7x**  (TTM 11.5x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **17.5x**  (TTM 19.3x, fwd 17.5x)
- EV 189.25B, 26E rev 35.12B, 26E EPS 7.17x


**3) Performance:**


- L1M -5.2% · L3M -4.8% · L12M 12.3% · -8.6% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -5.2%, 3M -4.8%; -8.6% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## FE — FirstEnergy Corp.  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 12.46B | n/a | 3.3% | 30.3% | 2.68B | -165.0M | -1.3% |
| 2023 | 12.87B | 3.3% | 8.6% | 30.7% | 1.39B | -1.97B | -15.3% |
| 2024 | 13.47B | 4.7% | 7.3% | 30.4% | 2.89B | -1.14B | -8.5% |
| 2025 | 15.09B | 12.0% | 6.8% | 28.2% | 3.70B | -1.00B | -6.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.77B | 9.6% | 637.0M | -368.0M |
| 2025-06 | 3.38B | 7.9% | 1.08B | -136.0M |
| 2025-09 | 4.15B | 10.6% | 845.0M | -471.0M |
| 2025-12 | 3.80B | -1.3% | 1.14B | -30.0M |
| 2026-03 | 4.20B | 9.6% | 148.0M | -1.11B |


**2) Valuation:**


- 2026E TEV/Sales: **3.4x**  (TTM 3.6x)
- 2026E TEV/EBITDA _est_: **10.0x**  (TTM 10.8x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **15.7x**  (TTM 25.1x, fwd 15.7x)
- EV 55.78B, 26E rev 16.49B, 26E EPS 2.95x


**3) Performance:**


- L1M -12.5% · L3M -11.6% · L12M 10.8% · -14.7% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -12.5%, 3M -11.6%; -14.7% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## HSIC — Henry Schein, Inc.  (Healthcare / Medical Distribution)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 12.65B | n/a | 4.3% | 7.5% | 602.0M | 474.0M | 3.7% |
| 2023 | 12.34B | -2.4% | 3.4% | 6.9% | 500.0M | 313.0M | 2.5% |
| 2024 | 12.67B | 2.7% | 3.1% | 7.2% | 848.0M | 661.0M | 5.2% |
| 2025 | 13.18B | 4.0% | 3.0% | 7.3% | 712.0M | 521.0M | 4.0% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.17B | 3.5% | 37.0M | -6.0M |
| 2025-06 | 3.24B | 2.7% | 120.0M | 74.0M |
| 2025-09 | 3.34B | 3.0% | 174.0M | 129.0M |
| 2025-12 | 3.44B | 2.9% | 381.0M | 324.0M |
| 2026-03 | 3.37B | 3.2% | -97.0M | -136.0M |


**2) Valuation:**


- 2026E TEV/Sales: **0.9x**  (TTM 1.0x)
- 2026E TEV/EBITDA _est_: **12.1x**  (TTM 12.9x)
- 2026E TEV/FCF _est_: **43.8x**
- 2026E P/E: **12.5x**  (TTM 22.4x, fwd 12.5x)
- EV 13.54B, 26E rev 14.26B, 26E EPS 5.91x


**3) Performance:**


- L1M -5.8% · L3M -7.0% · L12M 3.8% · -12.8% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -5.8%, 3M -7.0%; -12.8% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## L — Loews Corporation  (Financial Services / Insurance - Property & Casualty)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 14.05B | n/a | 5.9% | n/a | 3.31B | 2.65B | 18.9% |
| 2023 | 15.68B | 11.6% | 9.1% | n/a | 3.91B | 3.22B | 20.5% |
| 2024 | 17.24B | 10.0% | 8.2% | n/a | 3.02B | 2.39B | 13.9% |
| 2025 | 18.18B | 5.4% | 9.2% | n/a | 3.28B | 2.70B | 14.9% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 4.44B | 8.3% | 736.0M | 638.0M |
| 2025-06 | 4.47B | 8.7% | 1.01B | 872.0M |
| 2025-09 | 4.60B | 10.9% | 920.0M | 764.0M |
| 2025-12 | 4.66B | 8.6% | 617.0M | 426.0M |
| 2026-03 | 4.50B | 7.5% | 72.0M | -132.0M |


**2) Valuation:**


- 2026E TEV/Sales: **n/a**  (TTM 1.4x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM 8.1x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **n/a**  (TTM 14.0x, fwd 37.9x)
- EV 25.78B, 26E rev 0, 26E EPS n/a


**3) Performance:**


- L1M -3.7% · L3M -2.7% · L12M 21.4% · -6.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -3.7%, 3M -2.7%; -6.0% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ net margin expanding


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## MTB — M&T Bank Corporation  (Financial Services / Banks - Regional)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 8.01B | n/a | 24.9% | n/a | 4.57B | 4.36B | 54.4% |
| 2023 | 9.40B | 17.3% | 29.2% | n/a | 3.90B | 3.65B | 38.8% |
| 2024 | 9.23B | -1.8% | 28.0% | n/a | 3.61B | 3.39B | 36.8% |
| 2025 | 9.63B | 4.3% | 29.6% | n/a | 3.00B | 2.86B | 29.7% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 2.31B | 25.3% | 635.0M | 610.0M |
| 2025-06 | 2.39B | 30.0% | 844.0M | 818.0M |
| 2025-09 | 2.49B | 31.8% | 1.00B | 965.0M |
| 2025-12 | 2.44B | 31.1% | 523.0M | 467.0M |
| 2026-03 | 2.41B | 27.6% | 1.01B | 916.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.5x**  (TTM 3.9x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **10.2x**  (TTM 12.0x, fwd 10.2x)
- EV 36.32B, 26E rev 10.33B, 26E EPS 20.85x


**3) Performance:**


- L1M -5.6% · L3M -9.8% · L12M 13.8% · -13.3% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -5.6%, 3M -9.8%; -13.3% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (29.7%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## PNW — Pinnacle West Capital Corporati  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 4.32B | n/a | 11.2% | 38.1% | 1.24B | -466.0M | -10.8% |
| 2023 | 4.70B | 8.6% | 10.7% | 37.9% | 1.21B | -638.7M | -13.6% |
| 2024 | 5.12B | 9.1% | 11.9% | 40.4% | 1.61B | -639.4M | -12.5% |
| 2025 | 5.34B | 4.2% | 11.5% | 39.9% | 1.81B | -819.5M | -15.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 1.03B | -0.4% | 401.9M | -220.7M |
| 2025-06 | 1.36B | 14.2% | 261.4M | -448.1M |
| 2025-09 | 1.82B | 22.7% | 665.0M | 42.0M |
| 2025-12 | 1.13B | 1.4% | 476.8M | -192.7M |
| 2026-03 | 1.15B | 2.9% | 235.3M | -393.1M |


**2) Valuation:**


- 2026E TEV/Sales: **4.6x**  (TTM 5.0x)
- 2026E TEV/EBITDA _est_: **11.9x**  (TTM 12.9x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **18.1x**  (TTM 19.1x, fwd 18.4x)
- EV 27.52B, 26E rev 5.94B, 26E EPS 5.66x


**3) Performance:**


- L1M -4.7% · L3M -0.1% · L12M 15.9% · -5.0% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -4.7%, 3M -0.1%; -5.0% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ revenue growth decelerating; negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## REG — Regency Centers Corporation  (Real Estate / REIT - Retail)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 1.22B | n/a | 39.4% | 77.9% | 655.8M | 655.8M | 53.6% |
| 2023 | 1.32B | 8.0% | 27.6% | 66.3% | 719.6M | 719.6M | 54.4% |
| 2024 | 1.45B | 9.9% | 27.5% | 68.3% | 790.2M | 790.2M | 54.4% |
| 2025 | 1.55B | 6.9% | 34.0% | 74.2% | 827.7M | 827.7M | 53.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 380.9M | 28.8% | 161.0M | 161.0M |
| 2025-06 | 380.8M | 27.8% | 244.0M | 244.0M |
| 2025-09 | 387.6M | 28.2% | 218.7M | 218.7M |
| 2025-12 | 404.2M | 50.1% | 203.9M | 203.9M |
| 2026-03 | 412.5M | 31.2% | 152.7M | 152.7M |


**2) Valuation:**


- 2026E TEV/Sales: **11.8x**  (TTM 12.1x)
- 2026E TEV/EBITDA _est_: **18.5x**  (TTM 18.9x)
- 2026E TEV/FCF _est_: **33.8x**
- 2026E P/E: **31.0x**  (TTM 27.0x, fwd 31.0x)
- EV 19.90B, 26E rev 1.69B, 26E EPS 2.53x


**3) Performance:**


- L1M -4.5% · L3M 0.8% · L12M 9.7% · -6.2% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -4.5%, 3M 0.8%; -6.2% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ net margin expanding; strong FCF margin (53.3%)


_Issues:_ revenue growth decelerating


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## RF — Regions Financial Corporation  (Financial Services / Banks - Regional)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 7.17B | n/a | 31.3% | n/a | 3.10B | 2.81B | 39.3% |
| 2023 | 7.58B | 5.7% | 27.4% | n/a | 2.31B | 2.15B | 28.4% |
| 2024 | 7.08B | -6.5% | 26.7% | n/a | 1.60B | 1.45B | 20.5% |
| 2025 | 7.53B | 6.3% | 28.6% | n/a | 2.18B | 2.15B | 28.6% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 1.78B | 27.5% | 1.07B | 1.06B |
| 2025-06 | 1.91B | 29.6% | 573.0M | 559.0M |
| 2025-09 | 1.92B | 29.7% | 861.0M | 853.0M |
| 2025-12 | 1.92B | 27.8% | -319.0M | -322.0M |
| 2026-03 | 1.87B | 29.8% | 867.0M | 863.0M |


**2) Valuation:**


- 2026E TEV/Sales: **3.4x**  (TTM 3.9x)
- 2026E TEV/EBITDA _est_: **n/a**  (TTM n/a)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **9.8x**  (TTM 11.6x, fwd 9.8x)
- EV 27.97B, 26E rev 8.20B, 26E EPS 2.85x


**3) Performance:**


- L1M -4.5% · L3M -9.5% · L12M 23.8% · -13.0% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -4.5%, 3M -9.5%; -13.0% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding; strong FCF margin (28.6%)


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## TXT — Textron Inc.  (Industrials / Aerospace & Defense)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 2022 | 12.87B | n/a | 6.7% | 11.8% | 1.49B | 1.13B | 8.8% |
| 2023 | 13.68B | 6.3% | 6.7% | 11.4% | 1.27B | 864.0M | 6.3% |
| 2024 | 13.70B | 0.1% | 6.0% | 10.4% | 1.01B | 650.0M | 4.7% |
| 2025 | 14.80B | 8.0% | 6.2% | 11.2% | 1.31B | 929.0M | 6.3% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2024-09 | n/a | n/a | n/a | n/a |
| 2024-12 | n/a | n/a | n/a | n/a |
| 2025-03 | 3.31B | 6.3% | -124.0M | -180.0M |
| 2025-06 | 3.72B | 6.6% | 387.0M | 309.0M |
| 2025-09 | 3.60B | 6.5% | 349.0M | 273.0M |
| 2025-12 | 4.17B | 5.6% | 700.0M | 527.0M |
| 2026-03 | 3.69B | 6.0% | -117.0M | -250.0M |


**2) Valuation:**


- 2026E TEV/Sales: **1.1x**  (TTM 1.2x)
- 2026E TEV/EBITDA _est_: **10.2x**  (TTM 10.9x)
- 2026E TEV/FCF _est_: **27.7x**
- 2026E P/E: **12.6x**  (TTM 17.5x, fwd 12.6x)
- EV 18.40B, 26E rev 16.20B, 26E EPS 7.30x


**3) Performance:**


- L1M -1.7% · L3M -9.5% · L12M 18.1% · -11.9% from 12-mo high


**4) Reason for breakout:**


uptrend continuation off a dip; 1M -1.7%, 3M -9.5%; -11.9% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating; net margin expanding


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## UPS — United Parcel Service, Inc.  (Industrials / Integrated Freight & Logistics)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 100.34B | n/a | 11.5% | 18.7% | 14.10B | 9.34B | 9.3% |
| 2023 | 90.96B | -9.3% | 7.4% | 14.0% | 10.24B | 5.08B | 5.6% |
| 2024 | 91.07B | 0.1% | 6.3% | 13.1% | 10.12B | 6.21B | 6.8% |
| 2025 | 88.66B | -2.6% | 6.3% | 13.5% | 8.45B | 4.76B | 5.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 21.55B | 5.5% | 2.32B | 1.44B |
| 2025-06 | 21.22B | 6.0% | 348.0M | -775.0M |
| 2025-09 | 21.41B | 6.1% | 2.48B | 1.51B |
| 2025-12 | 24.48B | 7.3% | 3.30B | 2.59B |
| 2026-03 | 21.20B | 4.1% | 2.22B | 1.19B |


**2) Valuation:**


- 2026E TEV/Sales: **1.1x**  (TTM 1.2x)
- 2026E TEV/EBITDA _est_: **8.5x**  (TTM 9.0x)
- 2026E TEV/FCF _est_: **21.7x**
- 2026E P/E: **12.5x**  (TTM 16.2x, fwd 12.5x)
- EV 106.40B, 26E rev 93.62B, 26E EPS 8.00x


**3) Performance:**


- L1M -5.8% · L3M -15.9% · L12M 6.1% · -16.4% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -5.8%, 3M -15.9%; -16.4% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ no standout positives in the numbers


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## VZ — Verizon Communications Inc.  (Communication Services / Telecom Services)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 136.84B | n/a | 15.5% | 35.8% | 37.14B | 10.40B | 7.6% |
| 2023 | 133.97B | -2.1% | 8.7% | 30.0% | 37.48B | 12.91B | 9.6% |
| 2024 | 134.79B | 0.6% | 13.0% | 35.3% | 36.91B | 18.92B | 14.0% |
| 2025 | 138.19B | 2.5% | 12.4% | 34.5% | 37.14B | 19.68B | 14.2% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 33.48B | 14.6% | 7.78B | 3.52B |
| 2025-06 | 34.50B | 14.5% | 8.97B | 5.05B |
| 2025-09 | 33.82B | 14.6% | 11.27B | 6.85B |
| 2025-12 | 36.38B | 6.4% | 9.11B | 4.26B |
| 2026-03 | 34.44B | 14.6% | 7.98B | 3.70B |


**2) Valuation:**


- 2026E TEV/Sales: **2.7x**  (TTM 2.8x)
- 2026E TEV/EBITDA _est_: **7.4x**  (TTM 7.7x)
- 2026E TEV/FCF _est_: **19.4x**
- 2026E P/E: **9.2x**  (TTM 11.8x, fwd 9.2x)
- EV 395.39B, 26E rev 144.91B, 26E EPS 5.27x


**3) Performance:**


- L1M -0.9% · L3M -4.0% · L12M 16.9% · -8.4% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -0.9%, 3M -4.0%; -8.4% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ none flagged from the numbers


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._


## WEC — WEC Energy Group, Inc.  (Utilities / Utilities - Regulated Electric)


**1) Fundamentals (annual, up to 5 FY):**


| FY | Revenue | Rev growth | Net margin | EBITDA mgn | CFO | FCF | FCF margin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022 | 9.60B | n/a | 14.7% | 35.1% | 2.06B | -254.2M | -2.6% |
| 2023 | 8.89B | -7.3% | 15.0% | 39.7% | 3.02B | 525.5M | 5.9% |
| 2024 | 8.60B | -3.3% | 17.8% | 45.5% | 3.21B | 430.7M | 5.0% |
| 2025 | 9.80B | 14.0% | 15.9% | 41.3% | 3.38B | -1.02B | -10.4% |


**Quarterly (up to 8 q, newest last):**


| Qtr | Revenue | Net margin | CFO | FCF |
| --- | --- | --- | --- | --- |
| 2025-03 | 3.15B | 23.0% | 1.16B | 461.5M |
| 2025-06 | 2.01B | 12.2% | 853.3M | 23.9M |
| 2025-09 | 2.10B | 12.9% | 938.9M | -625.7M |
| 2025-12 | 2.54B | 12.5% | 424.6M | -878.4M |
| 2026-03 | 3.43B | 23.4% | 1.22B | 400.5M |


**2) Valuation:**


- 2026E TEV/Sales: **5.5x**  (TTM 5.9x)
- 2026E TEV/EBITDA _est_: **14.0x**  (TTM 15.1x)
- 2026E TEV/FCF _est_: **n/a**
- 2026E P/E: **18.8x**  (TTM 22.7x, fwd 18.9x)
- EV 59.23B, 26E rev 10.84B, 26E EPS 6.01x


**3) Performance:**


- L1M -5.4% · L3M -4.9% · L12M 10.4% · -7.3% from 12-mo high


**4) Reason for breakout:**


10-day-high break; 1M -5.4%, 3M -4.9%; -7.3% from 12-mo high; trend tag: weak


**5) Earnings recap, last 4 reported quarters:**


_EPS history n/a_


_Highlights:_ revenue growth accelerating


_Issues:_ negative free cash flow


_Note: call-transcript narrative not retrievable in this environment (network limited to the price/data provider)._
