# High-recall breakout system — SPY+QQQ, last 3 years

Goal: **minimise missed breakouts** (opportunity cost of a miss >> cost of a false alarm). The system is an OR-union of 8 deliberately loose detectors (see `breakout/recall_system.py`); a soft trend tag is attached but never suppresses a signal.


**Ground truth (independent of the detector):** a day is an opportunity launch if price gains ≥ +20% within 30 trading days *and* it is near the start of the move (not already extended). Launches are clustered so each distinct move counts once. An episode is *caught* if the system fired from 3 bars before to 15 bars after the launch while price was still within +12% of it (i.e. still actionable).


Universe: 502 names with sufficient history. Scored window: 2023-05-15 → 2026-05-15.


## Recall vs. cost, by detector


| detector | episodes | caught | recall_% | signals | false_alarm_% | avg_signals_per_name_yr | avg_lead_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| union | 2711 | 2204 | 81.3 | 30011 | 88.0 | 14.9 | -5.2 |
| fast_donchian | 2711 | 1873 | 69.1 | 22579 | 88.7 | 11.2 | -6.4 |
| donchian_20 | 2711 | 1217 | 44.9 | 16765 | 90.2 | 8.3 | -6.5 |
| trend_continuation | 2711 | 1060 | 39.1 | 12338 | 86.7 | 6.1 | -5.4 |
| six_month_high | 2711 | 629 | 23.2 | 12764 | 91.8 | 6.3 | -5.3 |
| range_expansion | 2711 | 616 | 22.7 | 4478 | 85.6 | 2.2 | -6.8 |
| gap_go | 2711 | 583 | 21.5 | 3043 | 79.1 | 1.5 | -6.6 |
| squeeze_release | 2711 | 332 | 12.2 | 3298 | 89.3 | 1.6 | -7.0 |
| volume_thrust | 2711 | 211 | 7.8 | 1097 | 80.8 | 0.5 | -5.3 |


**Headline:** the union catches **81.3%** of all +20% episodes vs. **69.1%** for the best single detector (`fast_donchian`) — the OR-ensemble is the entire point. Cost: ~14.9 signals/name/yr and a 88.0% false-alarm rate, which is the accepted trade for high recall.


## Where recall is weakest (>=3 episodes)


| ticker | episodes | caught | recall_% | signals | false_alarm_% | signals_per_yr |
| --- | --- | --- | --- | --- | --- | --- |
| BK | 3 | 1 | 33.3 | 78 | 96.2 | 19.3 |
| ELV | 3 | 1 | 33.3 | 48 | 95.8 | 11.9 |
| CDW | 3 | 1 | 33.3 | 45 | 95.6 | 11.2 |
| HUM | 8 | 3 | 37.5 | 43 | 88.4 | 10.7 |
| EA | 5 | 2 | 40.0 | 55 | 94.5 | 13.6 |
| WST | 7 | 3 | 42.9 | 45 | 86.7 | 11.2 |
| MOH | 9 | 4 | 44.4 | 54 | 88.9 | 13.4 |
| EL | 10 | 5 | 50.0 | 50 | 88.0 | 12.4 |
| CHTR | 8 | 4 | 50.0 | 40 | 77.5 | 9.9 |
| UHS | 8 | 4 | 50.0 | 53 | 81.1 | 13.1 |
| WAT | 8 | 4 | 50.0 | 49 | 87.8 | 12.1 |
| BG | 6 | 3 | 50.0 | 63 | 90.5 | 15.6 |


## Live signals on 2026-05-15


39 names firing today. Higher `n_detectors` = more independent triggers agreeing; `trend=up` = above a rising 50-day average.


**Multi-detector signals (n_detectors >= 2):**


| ticker | close | n_detectors | detectors | trend |
| --- | --- | --- | --- | --- |
| ENPH | 52.89 | 6 | fast_donchian+donchian_20+six_month_high+volume_thrust+range_expansion+trend_continuation | weak |
| COST | 1048.95 | 4 | fast_donchian+donchian_20+six_month_high+squeeze_release | up |
| EBAY | 116.13 | 4 | fast_donchian+donchian_20+six_month_high+trend_continuation | up |
| FTNT | 122.78 | 4 | fast_donchian+donchian_20+six_month_high+trend_continuation | up |
| JBHT | 262.21 | 4 | fast_donchian+donchian_20+six_month_high+trend_continuation | up |
| TRGP | 271.99 | 4 | fast_donchian+donchian_20+six_month_high+trend_continuation | up |
| AIZ | 254.61 | 3 | fast_donchian+donchian_20+six_month_high | up |
| CRWD | 594.08 | 3 | fast_donchian+donchian_20+six_month_high | up |
| DDOG | 207.98 | 3 | fast_donchian+donchian_20+six_month_high | up |
| OKE | 92.32 | 3 | fast_donchian+donchian_20+trend_continuation | up |
| PANW | 242.83 | 3 | fast_donchian+donchian_20+six_month_high | up |
| XOM | 157.92 | 3 | fast_donchian+donchian_20+trend_continuation | up |
| KMI | 33.63 | 3 | fast_donchian+donchian_20+trend_continuation | weak |
| ZS | 161.05 | 2 | fast_donchian+donchian_20 | down |
| CSCO | 118.21 | 2 | six_month_high+trend_continuation | up |
| VRSN | 297.57 | 2 | six_month_high+trend_continuation | up |
| WMB | 77.72 | 2 | six_month_high+trend_continuation | up |


_Full list of 39 names in `results/today_signals.csv`._
