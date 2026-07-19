# Breakout Screen — Session Handoff / Runbook

A self-contained brief for continuing the stock-breakout screening & analysis
work in a fresh coding session. Covers **methodology, rules, scope, file map,
commands, and data-source caveats**. Drop this into a new session as context.

---

## 0. What this project is

A stock-price **breakout detection** system over the SPY + QQQ universe, plus a
daily-screen workflow that, for every newly-breaking-out name, produces a
research dossier (fundamentals, valuation, performance, breakout reason, and —
when possible — earnings/news context).

- **Repo:** `michaelchen32/CC-Mobile`
- **Working branch:** `claude/wonderful-euler-sxTb3` (develop, commit, and push here)
- **Language/stack:** Python 3.11; `pandas`, `numpy`, `yfinance`, `matplotlib` (see `requirements.txt`)
- **Framing:** educational analysis, **not investment advice** — every brief must carry that disclaimer.

Setup in a fresh container:
```bash
pip install -r requirements.txt
```

---

## 1. File map

```
breakout/
  algorithms.py     # 6 canonical breakout algos (the "study" set)
  recall_system.py  # 8-detector high-recall OR-union (what the DAILY screen uses)
  indicators.py     # sma, ema, atr, true_range, rolling_slope
  data.py           # yfinance OHLCV + on-disk cache (data_cache/); bulk_fetch, get_ohlcv
  evaluate.py       # dedup (10-bar cooldown) + trade classification + scoring
  universe.py       # static SPY + QQQ constituent list (~500 names)
  transcripts.py    # OPTIONAL earnings-transcript fetcher (needs FMP/Finnhub key)
  news.py           # yfinance .news headline fetcher (added; used for driver context)
analyze.py            # historical study runner (GOOG / memory / optics / QQQ-SPY FP study)
daily_screen.py       # daily market-close screen orchestrator  <-- main entry point
collect_fundamentals.py # per-name dossier builder (the 5 info blocks)
run_recall.py         # recall backtest runner
results/              # all outputs (committed)
  screen_history/<date>.csv       # full ranked signal list per day
  daily_screen_latest.md          # standard daily brief
  momentum_brief_<date>.md        # sector-grouped, news-enriched brief (custom)
  news_dossier_<date>.json        # raw per-name headline data (re-usable)
  fundamentals_master.csv / _report.md
  report.md / signals.csv / recall_report.md
```

---

## 2. The 6 canonical algorithms (`breakout/algorithms.py`)

Each takes an OHLCV DataFrame, returns a boolean Series (True on the trigger bar).

| # | Name (`key`) | Rule | Default params |
|---|---|---|---|
| 1 | Donchian (`donchian_20`) | Close > highest high of prior N bars | lookback=20 |
| 2 | Darvas box (`darvas_box`) | Box top = new 60-day high that then stalls `settle_days`; fire when close exceeds confirmed box top | high_lookback=60, settle_days=4 |
| 3 | Bollinger squeeze (`bollinger_squeeze`) | Bandwidth in bottom `squeeze_pct` of trailing range, then close crosses above upper band within `squeeze_window` bars | n=20, k=2.0, bw_lookback=126, squeeze_pct=0.25, squeeze_window=10 |
| 4 | TTM squeeze (`ttm_squeeze`) | BB inside Keltner (coiled) → fire on release with positive momentum | n=20, bb_k=2.0, kc_k=1.5 |
| 5 | Volume-confirmed resistance (`volume_resistance`) | Close clears horizontal swing-high resistance by `buffer` on ≥`vol_mult`× avg volume | pivot_window=10, resistance_lookback=60, vol_mult=1.5, vol_n=20, buffer=0.005 |
| 6 | 52-week-high momentum (`high_52w_momentum`) | New 252-bar closing high while above a rising 50-day MA | lookback=252, trend_n=50, slope_n=50, min_slope=0.0 |

Exposed as `ALGORITHMS = {key: fn}`. These are used by `analyze.py` for the
historical precision/false-positive study — **not** by the daily screen.

---

## 3. The 8-detector high-recall system (`breakout/recall_system.py`)

This is what **`daily_screen.py` actually runs.** Design goal: minimise *missed*
breakouts (a missed multibagger costs more than a false alarm), so it is an
**OR-union** of 8 deliberately loose detectors. Any one firing = a signal.

| Detector | Rule |
|---|---|
| `fast_donchian` | close > prior 10-day high (early base break) |
| `donchian_20` | close > prior 20-day high |
| `six_month_high` | close ≥ prior 126-day high |
| `volume_thrust` | ≥5% up day AND ≥2× 20-day avg vol AND close in top 30% of range |
| `gap_go` | gap up ≥2.5% and holds the open |
| `range_expansion` | true range ≥2× ATR(20) while pushing the 10-day high |
| `squeeze_release` | TTM squeeze (BB inside KC) releases with positive momentum |
| `trend_continuation` | in uptrend (c>SMA50>SMA150), new 5-day high right after a ≥3% dip |

- `n_detectors` = count of detectors firing (higher = stronger confluence).
- **`trend` tag** (`up` / `weak` / `down`) is attached for CONTEXT ONLY — it never suppresses a signal.
  - `up` = close > rising SMA50; `weak` = close > SMA200 but not up; else `down`.
- Recall backtest (3yr, in `results/recall_report.md`): union catches ~81% of
  all +20%/30-day episodes at ~88% false-alarm rate — the accepted cost of high recall.

**Key interpretation rule:** single-detector `gap_go`-only fires (n_det=1) in a
choppy tape are the low-quality / high-false-alarm cohort. Multi-detector
(n_det≥3) base breakouts with `trend=up` are the high-quality signals.

---

## 4. Scoring methodology (`breakout/evaluate.py`)

Used by the historical study (not the daily screen), but it defines the
project's notion of a "real" breakout:

- **Dedup:** 10-bar cooldown (drop signals within 10 bars of a counted one).
- **Entry:** signal-bar close; **horizon:** 20 trading days.
- **Tradeable outcome:** `true` = +8% target hit before −5% stop; `false` =
  stop first; `timeout_up`/`timeout_down` = neither (final close above/below entry).
- **Identification quality (path-independent):** `confirmed` = max favorable
  excursion ≥ +8%; `fakeout` = never made ≥+4% upside OR rolled past −5%;
  `marginal` = in between.
- **`fakeout_%`** = the true false-positive rate for *detection* (a tight stop
  can whipsaw a real breakout, inflating the tradeable-false count but not fakeout).

Overall study result (all ~3,000 dedup signals): `volume_resistance` and
`high_52w_momentum` were the most reliable (confirmed ~56%/52%, fakeout ~29%);
raw Donchian fires most but noisiest. Every detector is regime-dependent
(~12–25% fakeout in strong trends, 50%+ in chop).

---

## 5. Daily-screen workflow (`daily_screen.py`) — the main loop

```bash
python daily_screen.py            # defaults to today
python daily_screen.py 2026-07-09 # backfill/explicit trading day (use for "yesterday's close")
```

What it does:
1. Fetch OHLCV for the full SPY+QQQ universe (`LOOKBACK_DAYS=420`, enough for SMA200 + 126-day warmup).
2. Run `recall_system.todays_signal` on the latest bar for each name.
3. Diff vs the previous snapshot → **NEW** / **DROPPED** names.
4. For each NEW name: earnings recap (EPS beat/miss + revenue/margin path) and rise drivers.
5. Write `results/screen_history/<date>.csv` and `results/daily_screen_latest.md`.

**The standard analysis request = "run the screen for the latest close, identify
NEW additions, and for each new name summarise growth drivers + recent news,
grouped by sector / growth driver."** The established output for that is a
`results/momentum_brief_<date>.md` (see §7).

---

## 6. Per-name dossier — the 5 info blocks (`collect_fundamentals.py`)

The original spec. For each new/target name, collect:

1. **Fundamentals** — revenue growth, net margin, FCF margin; CFO and FCF for last 5 FY and last 8 quarters.
2. **Valuation** — 2026E TEV/Sales, TEV/EBITDA, TEV/FCF, P/E (2026E = consensus +1y estimate; EBITDA/FCF forward = fwd revenue × trailing margin, marked _est_).
3. **Performance** — returns L1M / L3M / L12M (21 / 63 / 252 trading days) + % from 12-mo high.
4. **Reason for breakout** — which detectors fired + trend tag.
5. **Earnings recap** — last 4 reported quarters (EPS est/actual/surprise), highlights vs issues; plus call-transcript summary **when transcripts are available** (see §8).

```bash
# reads results/today_signals.csv (ticker,date,close,n_detectors,detectors,trend)
python collect_fundamentals.py    # -> results/fundamentals_master.csv + _report.md
```

---

## 7. News-enriched momentum brief (the custom deliverable added this session)

For "summarise growth drivers + recent news, grouped by sector":

1. Build `results/today_signals.csv` = the NEW names (diff current vs prior snapshot), sorted by `n_detectors`.
2. For each, pull `sector`/`industry`/`revenueGrowth` via `yfinance.Ticker.info` and recent headlines via `breakout.news.fetch_news(ticker, days=~14, max_items=~5)`.
3. Save raw data to `results/news_dossier_<date>.json`.
4. Write `results/momentum_brief_<date>.md`:
   - Header: total signals, NEW/DROPPED counts, trend-tag distribution.
   - **Group NEW names by sector** (and/or by cross-cutting growth-driver theme).
   - Per name: close, n_det, trend, rev growth TTM, and the **specific catalyst** from the headlines (earnings beat, M&A, upgrade, product, macro).
   - A "cross-sector themes" roll-up and a "top conviction (n_det≥4)" callout.
   - **Conviction caveat:** flag single-detector `gap_go` fires as fragile.
   - Disclaimer footer.

Helper (`breakout/news.py`):
```python
from breakout.news import fetch_news, format_news_block
fetch_news("MU", days=14, max_items=5)  # -> [{title, summary, source, pub}, ...]
```

---

## 8. Scope, conventions & rules

- **Universe:** SPY (S&P 500) ∪ QQQ (Nasdaq-100), ~500 names, static list in `universe.py` (delisted/renamed tickers fail gracefully). Wikipedia constituent sources are network-blocked, hence the bundled list.
- **Data source:** `yfinance` (auto-adjusted OHLCV), cached per-ticker in `data_cache/<TICKER>_<start>_<end>.csv`. Cache key includes the run window, so clear `data_cache/*_<end>.csv` to force a fresh pull for a re-run.
- **"Latest close" / "yesterday's close":** pass the explicit trading date to `daily_screen.py`. On weekends/holidays use the last session (e.g. Friday). Snapshot files are named by that date.
- **Diff semantics:** NEW/DROPPED are vs the previous snapshot in `screen_history/`. If there's a multi-day gap between runs, say so (the diff then reflects the whole gap, not one session).
- **Commit convention:** after each run, `git add results/ && git commit && git push -u origin claude/wonderful-euler-sxTb3`. Descriptive commit messages summarising the day's signals/themes. Do NOT open a PR unless explicitly asked.
- **Disclaimer:** every brief ends with an educational-use / not-investment-advice / past-performance line.
- **Model-identity / secrets:** never write model IDs or keys into committed artifacts.

---

## 9. ⚠️ Data-source caveats (READ FIRST — this is where time gets lost)

1. **yfinance/Yahoo rate-limits shared cloud IPs.** In the Claude Code web
   environment the egress IP is shared, and Yahoo returns **HTTP 429** on the
   `query1/query2.finance.yahoo.com` chart endpoints. This can persist for
   **hours** and blocks the entire screen (mass "possibly delisted; no price
   data found"). It blocked the **2026-07-09** run for 6h+.
   - Diagnose: `curl -sS -o /dev/null -w "%{http_code}\n" "https://query1.finance.yahoo.com/v8/finance/chart/AAPL?range=5d&interval=1d"` — 429 = throttled, 200 = clear.
   - It is IP-level; no endpoint/host trick bypasses it. Only waiting or a keyed vendor helps.
   - Stooq fallback is also blocked (anti-bot PoW + datacenter-IP "Access denied").
2. **Earnings-call transcripts are NOT retrievable via yfinance.** `transcripts.py`
   is inert until an API key is set (`FMP_API_KEY` or `FINNHUB_API_KEY`) AND the
   provider domain is allowlisted in the environment network policy. Without it,
   the earnings section degrades to a quantitative recap.

### Durable fix — switch the data layer to a keyed vendor
Keyed requests meter per-account (not per-IP), so the 429 throttle disappears.

- **FMP (financialmodelingprep.com)** — best single-vendor fit: prices +
  fundamentals + transcripts; free tier (250 calls/day), `transcripts.py`
  already targets it. Env var `FMP_API_KEY`.
- **Finnhub, Tiingo, Polygon, EODHD, Alpaca** — alternatives (see prior analysis).
- **S&P Capital IQ Pro API** — if entitled (user has a CapIQ subscription);
  carries all three incl. transcripts (`IQ_TRANSCRIPT_*`). API access is separate
  from the web seat.

To wire one in: add a provider in `breakout/data.py` that activates when the key
env var is present (fall back to yfinance otherwise), and in the web environment
set Network access → Custom + allowlist the vendor domain, and add the key as an
env var. See https://code.claude.com/docs/en/claude-code-on-the-web.

---

## 10. Run history & analytical continuity

Briefs committed this session (each = `momentum_brief_<date>.md` + `screen_history/<date>.csv`):
`2026-05-22, 05-26, 05-28, 05-29, 06-01, 06-05, 06-09, 06-12, 06-29`.
**Pending / blocked:** `2026-07-09` (Yahoo 429).

Observations worth carrying forward:
- **MU (Micron)** has signalled in nearly every session — the most persistent
  winner (AI-memory super-cycle, rev growth very high post-SanDisk). Good sanity check.
- The screen **whipsaws through regimes** week to week (broad AI → industrials →
  healthcare/defense → mega-cap AI → defensive rotation → AI snap-back …). High
  recall catches every rotation; the cost is noise. `trend=up` ratio among NEW
  names is a useful breadth gauge (high = healthy participation).
- Single-detector `gap_go` fires often fade within 1–2 sessions (dead-cat bounces).

---

## 11. Quick start for the next session

```bash
pip install -r requirements.txt
# If using a keyed vendor, export the key first, e.g.:  export FMP_API_KEY=...
python daily_screen.py <YYYY-MM-DD>          # latest trading day
# then build today_signals.csv (NEW = current-vs-prior snapshot diff), and:
python collect_fundamentals.py               # 5-block dossier  (optional)
# build results/momentum_brief_<date>.md with sector grouping + news (see §7)
git add results/ && git commit -m "..." && git push -u origin claude/wonderful-euler-sxTb3
```
If `daily_screen.py` prints mass "no price data" / the curl probe returns 429 →
Yahoo is throttling the IP (§9). Either wait, retry in a fresh session (may get a
different egress IP), or switch to a keyed vendor.
```
