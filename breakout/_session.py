"""Force yfinance onto a plain ``requests`` transport.

Some managed execution environments route outbound HTTPS through a proxy
that re-terminates TLS. yfinance's default ``curl_cffi`` transport performs
browser TLS-impersonation (a spoofed JA3 fingerprint) that such a proxy
resets mid-handshake, so every Yahoo call fails with ``curl (35) Recv
failure: Connection reset by peer``. A standard ``requests`` session
negotiates ordinary TLS and tunnels through cleanly.

Importing this module (done once from ``breakout/__init__``) installs a
shared ``requests`` session as the default for ``yf.download()`` and
``yf.Ticker(...)``. It is a no-op when yfinance or requests are missing, and
never overrides a session a caller passed explicitly, so it is harmless in
environments where the default transport already works.
"""
from __future__ import annotations

_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def install() -> None:
    try:
        import requests
        import yfinance as yf
    except Exception:  # noqa: BLE001 - libraries absent; nothing to patch
        return

    if getattr(yf, "_ccr_session_installed", False):
        return

    sess = requests.Session()
    sess.headers.update({"User-Agent": _UA})

    _orig_download = yf.download

    def _download(*args, **kwargs):
        if not kwargs.get("session"):
            kwargs["session"] = sess
        return _orig_download(*args, **kwargs)

    yf.download = _download

    _orig_ticker_init = yf.Ticker.__init__

    def _ticker_init(self, ticker, *args, **kwargs):
        if not kwargs.get("session"):
            kwargs["session"] = sess
        return _orig_ticker_init(self, ticker, *args, **kwargs)

    yf.Ticker.__init__ = _ticker_init
    yf._ccr_session_installed = True


install()
