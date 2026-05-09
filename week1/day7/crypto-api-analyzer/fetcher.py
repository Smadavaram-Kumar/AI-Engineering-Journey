"""
fetcher.py — Pulls live crypto data from CoinGecko's public API.

The /coins/markets endpoint returns the top N coins by market cap with
~25 useful fields (price, volume, % change over various windows, etc.)
No API key required for this endpoint.
"""

import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"


def fetch_top_coins(limit: int = 50, currency: str = "usd") -> list[dict]:
    """
    Fetch the top N cryptocurrencies by market cap.

    Args:
        limit: how many coins to fetch (1–250)
        currency: target currency (usd, inr, eur, ...)

    Returns:
        A list of dicts — one per coin — straight from the API.

    Raises:
        requests.exceptions.RequestException: if the API call fails.
    """
    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "price_change_percentage": "1h,24h,7d",
    }

    print(f"📡 Fetching top {limit} coins from CoinGecko...")
    response = requests.get(COINGECKO_URL, params=params, timeout=30)
    response.raise_for_status()         # raises HTTPError if 4xx/5xx

    data = response.json()
    print(f"✅ Got {len(data)} coins")
    return data


if __name__ == "__main__":
    # Quick test — runs only when you do `python fetcher.py`
    coins = fetch_top_coins(limit=5)
    for coin in coins:
        print(f"{coin['symbol'].upper():6s}  ${coin['current_price']:>12,.2f}")