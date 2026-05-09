"""
main.py — The entry point. Runs the full pipeline:
fetch → analyze → visualize → save.
"""

import json
from pathlib import Path
from datetime import datetime

from fetcher import fetch_top_coins
from analyzer import build_dataframe, compute_stats, categorize_by_price
from visualizer import plot_top10_prices, plot_24h_changes


OUTPUT_DIR = Path("output")


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 1. FETCH
    raw = fetch_top_coins(limit=50)

    # 2. SHAPE (pandas DataFrame)
    df = build_dataframe(raw)
    print(f"\n📋 DataFrame shape: {df.shape}")
    print(df.head(10).to_string(index=False))

    # 3. ANALYZE
    stats = compute_stats(df)
    tiers = categorize_by_price(df)

    print("\n📈 Summary statistics:")
    print(json.dumps(stats, indent=2))

    print("\n💰 Coins by price tier:")
    print(tiers.to_string())

    # 4. VISUALIZE
    plot_top10_prices(df, OUTPUT_DIR / "top10_prices.png")
    plot_24h_changes(df, OUTPUT_DIR / "changes_24h.png")

    # 5. SAVE — CSV (raw data) and JSON (summary)
    df.to_csv(OUTPUT_DIR / "crypto_data.csv", index=False)
    print(f"💾 Saved: {OUTPUT_DIR / 'crypto_data.csv'}")

    summary = {
        "fetched_at": datetime.now().isoformat(),
        "stats":      stats,
        "tiers":      tiers.to_dict(),
    }
    with open(OUTPUT_DIR / "crypto_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"💾 Saved: {OUTPUT_DIR / 'crypto_summary.json'}")

    print("\n✅ Pipeline complete.")


if __name__ == "__main__":
    main()