"""
analyzer.py — Loads API data into a DataFrame and computes summary stats.
"""

import pandas as pd


def build_dataframe(raw: list[dict]) -> pd.DataFrame:
    """Turn the raw API response into a clean DataFrame."""
    df = pd.DataFrame(raw)

    # Pick only the columns we care about (the API returns 25+ fields)
    keep = [
        "id", "symbol", "name",
        "current_price", "market_cap", "total_volume",
        "price_change_percentage_24h",
        "price_change_percentage_7d_in_currency",
        "market_cap_rank",
    ]
    df = df[keep].copy()

    # Tidy up: uppercase symbol, rename for readability
    df["symbol"] = df["symbol"].str.upper()
    df = df.rename(columns={
        "price_change_percentage_24h": "change_24h",
        "price_change_percentage_7d_in_currency": "change_7d",
        "market_cap_rank": "rank",
    })

    return df


def compute_stats(df: pd.DataFrame) -> dict:
    """Compute the summary statistics required by the project brief."""
    return {
        "total_coins":     len(df),
        "avg_price":       float(df["current_price"].mean()),
        "max_price":       float(df["current_price"].max()),
        "min_price":       float(df["current_price"].min()),
        "median_price":    float(df["current_price"].median()),
        "total_market_cap":float(df["market_cap"].sum()),
        "biggest_gainer_24h": {
            "symbol":  df.loc[df["change_24h"].idxmax(), "symbol"],
            "change":  float(df["change_24h"].max()),
        },
        "biggest_loser_24h": {
            "symbol":  df.loc[df["change_24h"].idxmin(), "symbol"],
            "change":  float(df["change_24h"].min()),
        },
        "coins_up_24h":    int((df["change_24h"] > 0).sum()),
        "coins_down_24h":  int((df["change_24h"] < 0).sum()),
    }


def categorize_by_price(df: pd.DataFrame) -> pd.Series:
    """Bucket coins by price tier — uses the groupby/value_counts pattern."""
    def tier(p):
        if p > 1000:  return "high (>$1000)"
        if p > 10:    return "mid ($10–$1000)"
        if p > 1:     return "low ($1–$10)"
        return "micro (<$1)"

    df["tier"] = df["current_price"].apply(tier)
    return df["tier"].value_counts()
