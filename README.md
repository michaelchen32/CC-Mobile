# US Large-Cap Breakout Screen

A breakout-detection screen over **all US-listed stocks with market cap >$10bn**
(~885 names). Clean-room implementation: universe construction, data access,
breakout detection, and a ranked narrative brief.

> Educational analysis only — **not investment advice**.

## Quick start

```bash
pip install -r requirements.txt
python run_screen.py 2026-07-17      # explicit trading session (latest close)
python run_screen.py                 # today
```

Outputs land in `results/`:
- `screen_<date>.csv` — ranked signal table
- `breakout_brief_<date>.md` — narrative brief (sector-grouped, conviction tiers)

## How it works

```
screener/
  data.py        # OHLCV via yfinance over a plain requests.Session (see below)
  universe.py    # Nasdaq screener API -> filter market cap >$10bn
  detectors.py   # 8-detector high-recall breakout union + trend tag
  screen.py      # orchestrator: universe -> fetch -> detect -> enrich -> rank
run_screen.py    # entry point + brief writer
```

### Data access (the important bit)

Modern **yfinance (>=1.5) uses `curl_cffi` with a browser-impersonated TLS
fingerprint by default.** Behind an intercepting HTTPS proxy that re-terminates
TLS, that impersonated handshake gets reset (`curl (35) Recv failure: Connection
reset by peer`), so every request dies. Naked `curl` to the Yahoo chart endpoint
fails differently — HTTP 429, because it sends no cookie/crumb.

**The fix:** hand yfinance a plain `requests.Session`. It is proxy-aware, trusts
the environment CA bundle, performs yfinance's normal cookie+crumb handshake, and
avoids the impersonated TLS the proxy rejects. See `screener/data.py`.

### Universe

Pulled live from the Nasdaq stock screener API (every NYSE/Nasdaq/AMEX name with
a market-cap figure), filtered to >$10bn, with warrants/units/rights/preferreds
dropped and symbols normalised for yfinance (`BRK/B` → `BRK-B`).

### The 6 canonical breakout algorithms

Each algorithm returns a boolean series (True on the trigger bar); the screen
evaluates the latest bar. Any algorithm firing = a signal; `n_detectors` = how
many of the six agree. The `trend` tag (`up`/`weak`/`down`) is context only.

| # | Algorithm | Rule | Params |
|---|---|---|---|
| 1 | `donchian_20` | close > highest high of prior N bars | lookback=20 |
| 2 | `darvas_box` | break above a confirmed 60-day-high box top (stalls 4 days) | high_lookback=60, settle=4 |
| 3 | `bollinger_squeeze` | bandwidth in bottom 25% of 126-day range, then close crosses above upper band within 10 bars | n=20, k=2 |
| 4 | `ttm_squeeze` | BB inside Keltner (coiled) → fire on release with positive momentum | n=20, bb_k=2, kc_k=1.5 |
| 5 | `volume_resistance` | close clears a horizontal swing-high by 0.5% on ≥1.5× avg volume | pivot=10, lookback=60 |
| 6 | `high_52w_momentum` | new 252-bar closing high above a rising 50-day MA | lookback=252, trend=50 |

**Reliability (from the historical study):** `volume_resistance` and
`high_52w_momentum` are the most reliable filters (highest confirmed, lowest
fakeout); raw `donchian_20` fires most often but is the noisiest. Multi-algorithm
(`n_det≥3`) breakouts with `trend=up` are the high-quality signals; single-algorithm
`donchian_20`-only fires are the low-conviction cohort.

## Caveats

- Prices are auto-adjusted OHLCV from Yahoo Finance; occasional bad ticks happen.
- Sector/revenue-growth enrichment is best-effort via `Ticker.get_info()` and
  degrades to `Unknown` on failure.
- High recall means high false-alarm rate by design — a signal is a research
  starting point, not a recommendation.
