"""Stock-price breakout detection algorithms and an evaluation harness."""

# Install the requests-based yfinance transport before any network call so
# the data layer works behind a TLS-re-terminating egress proxy. No-op when
# the default transport already works. See breakout/_session.py.
from . import _session  # noqa: F401,E402
