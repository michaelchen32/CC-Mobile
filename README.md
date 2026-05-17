# Stock-price breakout detection

Six well-known breakout algorithms, implemented from scratch on OHLCV data,
plus a harness that scores every signal for follow-through and false
positives.

```
pip install -r requirements.txt
python analyze.py        # writes results/report.md, signals.csv, charts/
```

Outputs land in `results/` (full report `results/report.md`, every
de-duplicated signal in `results/signals.csv`, per-algorithm rollup in
`results/summary_by_algo.csv`, annotated price charts in
`results/charts/`).

## The algorithms (`breakout/algorithms.py`)

| # | Algorithm | Idea | Why it's a standard |
|---|-----------|------|---------------------|
| 1 | **Donchian channel** | Close above the prior 20-day high | The original Turtle Trading entry; the canonical breakout rule |
| 2 | **Darvas box** | Close above a box top confirmed by a 4-day stall under a new high | Nicolas Darvas' 1950s method, still a staple of swing trading |
| 3 | **Bollinger squeeze** | Bandwidth contracts to the bottom quartile of its range, then close clears the upper band | Volatility-contraction-then-expansion; the most cited squeeze pattern |
| 4 | **TTM squeeze** | Bollinger bands sit *inside* Keltner channels (coiled), fire on release with positive momentum | John Carter's squeeze; ubiquitous on trading desks |
| 5 | **Volume-confirmed resistance** | Close clears a horizontal swing-high resistance on ≥1.5× average volume | Textbook S/R breakout; volume is the classic confirmation filter |
| 6 | **52-week-high momentum** | New 252-day closing high while above a rising 50-day average | Driehaus/Minervini momentum; strongest single equity-momentum factor |

## How signals are scored (`breakout/evaluate.py`)

Consecutive signals are de-duplicated (10-bar cooldown). Each surviving
signal is entered at its close and tracked 20 trading days, two ways:

* **Tradeable outcome** — `true` if +8% is hit before a −5% stop, `false`
  if the stop goes first, `timeout_up/down` otherwise. `stop_whipsaw_%`
  counts the bad ones. This measures *tradeability* with a fixed stop.
* **Identification quality** (path-independent) — `confirmed` if price
  later runs ≥ +8%, `fakeout` if it never makes ≥ +4% upside or rolls
  over past −5%, else `marginal`. **`fakeout_%` is the real
  false-positive rate for breakout *detection*** — a tight stop can
  whipsaw out of a genuine breakout, which inflates the tradeable
  false count but not the fakeout count.

## What the study found

Windows: GOOG over calendar 2025; memory (MU, WDC, STX, SNDK) and optics
(COHR, LITE, FN, CIEN, AAOI, POET) over Sep-2025 → May-2026; plus a
15-name QQQ/SPY sample over three years for a false-positive check.

**GOOG 2025** — algorithms cleanly caught the post-Aug-2025 trend leg
(the Donchian/Darvas/momentum signals around $200–$260 all confirmed and
ran 10–20%). The recurring false positive was the **late-Jan-2025
breakout near $205**, which every algorithm flagged and which then
collapsed ~18% on the DeepSeek/AI-capex scare — a textbook fakeout that
*all six* fired on.

**Memory & optics, late-2025 / early-2026** — this was an exceptionally
clean breakout regime (the AI memory + optical-interconnect super-cycle).
Detection false-positive (`fakeout_%`) rates were unusually low:

| Group | best algo | confirmed_% | fakeout_% |
|-------|-----------|------------|-----------|
| Memory | Darvas box | 75% | **12%** |
| Memory | 52-wk momentum | 71% | 16% |
| Optics | 52-wk momentum | 71% | **20%** |
| Optics | volume-resistance | 69% | 21% |

MU ran ≈$120→$800, SNDK ≈$90→$1,200, LITE ≈$170→$1,050; almost every
signal was `confirmed`. Most `false` tags here are *stop whipsaws* on a
real parabola, not failed breakouts — exactly the case the dual scoring
was built to separate.

**Three-year QQQ/SPY false-positive check** — false positives concentrate,
as expected, in **range-bound / declining names**:

* **PYPL**: Darvas 70% fakeout, volume-resistance 67%, Donchian 50%
* **SBUX**: 52-wk momentum 88% fakeout, Darvas 77%, volume-resistance 71%
* Strong trenders (NVDA, META, AVGO) sit at the opposite end with high
  `confirmed_%`.

**Overall, across all ~3,000 de-duplicated signals:**

| algorithm | confirmed_% | fakeout_% |
|-----------|------------|-----------|
| volume_resistance | **56.3** | **29.0** |
| high_52w_momentum | 52.0 | **29.0** |
| ttm_squeeze | 51.7 | 32.5 |
| donchian_20 | 50.4 | 34.2 |
| darvas_box | 49.4 | 32.5 |
| bollinger_squeeze | 47.9 | 34.5 |

Takeaways: (1) **volume-confirmed resistance** and **52-week-high
momentum** were the most reliable identifiers (best confirmed rate,
lowest fakeout rate) — the volume/trend filters do real work. (2) Raw
**Donchian** fires the most often but with more noise. (3) Every
algorithm's false-positive rate is regime-dependent: ~12–25% in a strong
trend (memory/optics 2025-26), 50%+ in chop (PYPL/SBUX). No breakout
detector is reliable without a trend/volume context filter.

*Data via yfinance, auto-adjusted. Educational analysis, not investment
advice; past performance does not predict future results.*
