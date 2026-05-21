"""Optional earnings-call transcript fetcher.

Inert until BOTH are true:
  1. the environment network policy allowlists the provider domain, and
  2. an API key is set via env var.

Supported providers (first one with a key wins):
  FMP_API_KEY      -> financialmodelingprep.com  (has a transcript endpoint)
  FINNHUB_API_KEY  -> finnhub.io                  (transcript endpoint)

Returns {} (with a reason in `last_reason`) when unavailable, so callers
degrade gracefully to the quantitative recap.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request

last_reason = "not attempted"


def _get(url: str, timeout: int = 20):
    req = urllib.request.Request(url, headers={"User-Agent": "research/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def fetch_transcripts(ticker: str, quarters: int = 4) -> dict[str, str]:
    """{'YYYY Qn': transcript_text} for the most recent `quarters`."""
    global last_reason

    fmp = os.environ.get("FMP_API_KEY")
    finnhub = os.environ.get("FINNHUB_API_KEY")
    if not fmp and not finnhub:
        last_reason = (
            "no transcript API key set (export FMP_API_KEY or "
            "FINNHUB_API_KEY)")
        return {}

    out: dict[str, str] = {}
    try:
        if fmp:
            base = "https://financialmodelingprep.com/api/v3"
            idx = _get(
                f"{base}/earning_call_transcript/{ticker}?apikey={fmp}")
            for item in idx[:quarters]:
                q, y = item.get("quarter"), item.get("year")
                txt = item.get("content")
                if not txt:
                    detail = _get(
                        f"{base}/earning_call_transcript/{ticker}"
                        f"?quarter={q}&year={y}&apikey={fmp}")
                    txt = detail[0]["content"] if detail else ""
                if txt:
                    out[f"{y} Q{q}"] = txt
            last_reason = f"ok (FMP, {len(out)} transcripts)"
            return out

        if finnhub:
            base = "https://finnhub.io/api/v1"
            lst = _get(
                f"{base}/stock/transcripts/list?symbol={ticker}"
                f"&token={finnhub}")
            ids = [t["id"] for t in lst.get("transcripts", [])[:quarters]]
            for tid in ids:
                d = _get(
                    f"{base}/stock/transcripts?id={tid}&token={finnhub}")
                speech = " ".join(
                    s.get("speech", "") if isinstance(s.get("speech"), str)
                    else " ".join(s.get("speech", []))
                    for s in d.get("transcript", []))
                out[d.get("title", tid)] = speech
            last_reason = f"ok (Finnhub, {len(out)} transcripts)"
            return out
    except urllib.error.URLError as e:
        last_reason = (
            f"network blocked or provider unreachable ({e}). Allowlist the "
            "provider domain in the environment network policy.")
        return {}
    except Exception as e:  # noqa: BLE001
        last_reason = f"transcript fetch error: {type(e).__name__}: {e}"
        return {}
    return out


def save_transcripts(ticker: str, out_dir: str, quarters: int = 4) -> list[str]:
    """Persist raw transcripts so the agent can read & summarise them."""
    tx = fetch_transcripts(ticker, quarters)
    paths = []
    if tx:
        os.makedirs(out_dir, exist_ok=True)
        for label, text in tx.items():
            p = os.path.join(
                out_dir, f"{ticker}_{label.replace(' ', '_')}.txt")
            with open(p, "w") as fh:
                fh.write(text)
            paths.append(p)
    return paths
