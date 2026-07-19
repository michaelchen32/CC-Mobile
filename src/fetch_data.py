"""
Fetch ~30 years of S&P 500 (^GSPC) daily bars from Yahoo Finance and cache
them to data/gspc.csv (the input consumed by src/hmm_regime.py).

Note: this hits Yahoo's public chart API directly with urllib rather than the
`yfinance` package -- same underlying data source, no extra dependency. A
browser User-Agent header is required or Yahoo returns HTTP 429.

Run:  python3 src/fetch_data.py
"""

import csv
import datetime
import json
import time
import urllib.request

SYMBOL = "%5EGSPC"          # ^GSPC (S&P 500 index)
PERIOD1 = 802483200         # 1995-06-07  (~30y history)
PERIOD2 = 1815091200        # far-future bound -> grabs the latest available bar
OUT = "data/gspc.csv"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def fetch(retries=6):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{SYMBOL}"
           f"?period1={PERIOD1}&period2={PERIOD2}&interval=1d&events=div")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    last_err = None
    for attempt in range(retries):
        try:
            return json.load(urllib.request.urlopen(req, timeout=25))
        except Exception as e:          # 429 / transient network -> back off
            last_err = e
            print(f"retry {attempt}: {str(e)[:100]}")
            time.sleep(4)
    raise RuntimeError(f"failed to fetch data: {last_err}")


def main():
    data = fetch()
    r = data["chart"]["result"][0]
    ts = r["timestamp"]
    q = r["indicators"]["quote"][0]
    adj = r["indicators"].get("adjclose", [{}])[0].get("adjclose")

    rows = []
    for i, t in enumerate(ts):
        c = q["close"][i]
        if c is None:
            continue
        a = adj[i] if adj else c
        rows.append((datetime.date.fromtimestamp(t).isoformat(),
                     c, a, q["open"][i], q["high"][i], q["low"][i], q["volume"][i]))

    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "close", "adjclose", "open", "high", "low", "volume"])
        w.writerows(rows)

    first, last = rows[0], rows[-1]
    wd = datetime.date.fromisoformat(last[0]).strftime("%A")
    print(f"wrote {OUT}: {len(rows)} rows, {first[0]} .. {last[0]} ({wd}), "
          f"last close {last[1]:,.2f}")


if __name__ == "__main__":
    main()
