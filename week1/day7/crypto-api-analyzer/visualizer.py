"""
visualizer.py — Generates and saves charts.
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def plot_top10_prices(df: pd.DataFrame, output_path: Path) -> None:
    """Bar chart of the top 10 coins by market cap."""
    top10 = df.head(10)

    plt.figure(figsize=(11, 6))
    plt.bar(top10["symbol"], top10["current_price"], color="steelblue")
    plt.yscale("log")    # BTC at $65k vs SHIB at $0.00002 — log scale or nothing!
    plt.xlabel("Coin")
    plt.ylabel("Price (USD, log scale)")
    plt.title("Top 10 cryptocurrencies — current price")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"📊 Saved: {output_path}")


def plot_24h_changes(df: pd.DataFrame, output_path: Path) -> None:
    """Bar chart of 24h price changes for the top 15 coins."""
    top15 = df.head(15).sort_values("change_24h")

    colors = ["red" if c < 0 else "green" for c in top15["change_24h"]]

    plt.figure(figsize=(11, 6))
    plt.barh(top15["symbol"], top15["change_24h"], color=colors)
    plt.axvline(x=0, color="black", linewidth=0.8)   # zero line
    plt.xlabel("24-hour price change (%)")
    plt.ylabel("Coin")
    plt.title("Top 15 coins — 24-hour price change")
    plt.grid(True, axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"📊 Saved: {output_path}")
    