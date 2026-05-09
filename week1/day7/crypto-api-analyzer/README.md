## Day 7 — Pandas, Matplotlib + Week 1 Capstone Project

> **Why this day is the bridge to AI engineering.** Until today, you've been learning Python *the language*. Today you learn Python *the data tool* — and that's the version every AI engineer actually uses. Every AI/ML workflow on the planet has the same shape: **get data → clean it → analyze it → visualize it → make a decision**. Training a model? You shape the training set with pandas. Evaluating a RAG pipeline? You score retrievals into a DataFrame. Debugging an agent? You log every tool call and `groupby` the failures. Fine-tuning Claude on your company's data? You prep that data with pandas first. There is no AI engineer who doesn't speak pandas — it's not optional. Today you also build your **Week 1 Capstone**: a real "fetch from API → analyze → visualize → save → push to GitHub" pipeline. That's a portfolio piece. That's something you show in interviews.

---

### 📋 Table of Contents

- [The Big Picture — Why Pandas and Matplotlib?](#the-big-picture--why-pandas-and-matplotlib)
- [Installation](#installation)
- [Part 1 — Pandas Foundations](#part-1--pandas-foundations)
  - [1.1 Series vs DataFrame — The Two Building Blocks](#11-series-vs-dataframe--the-two-building-blocks)
  - [1.2 Creating a DataFrame — Five Ways](#12-creating-a-dataframe--five-ways)
  - [1.3 Reading Data — `read_csv`, `read_json`, `read_excel`](#13-reading-data--read_csv-read_json-read_excel)
  - [1.4 Inspecting a DataFrame](#14-inspecting-a-dataframe)
  - [1.5 Selecting Columns and Rows](#15-selecting-columns-and-rows)
  - [1.6 Filtering — The "WHERE Clause" of Pandas](#16-filtering--the-where-clause-of-pandas)
  - [1.7 `describe()`, `value_counts()`, and Quick Stats](#17-describe-value_counts-and-quick-stats)
  - [1.8 `groupby()` — The Most Powerful Verb](#18-groupby--the-most-powerful-verb)
  - [1.9 Adding, Updating, Deleting Columns](#19-adding-updating-deleting-columns)
  - [1.10 Sorting and Renaming](#110-sorting-and-renaming)
  - [1.11 Saving Data — `to_csv`, `to_json`](#111-saving-data--to_csv-to_json)
  - [1.12 Common Pitfalls](#112-common-pitfalls)
- [Part 2 — Matplotlib Foundations](#part-2--matplotlib-foundations)
  - [2.1 The Mental Model — Figure vs Axes](#21-the-mental-model--figure-vs-axes)
  - [2.2 Line Plots](#22-line-plots)
  - [2.3 Bar Charts](#23-bar-charts)
  - [2.4 Labels, Titles, Legends, Grids](#24-labels-titles-legends-grids)
  - [2.5 Saving Charts — `plt.savefig()`](#25-saving-charts--pltsavefig)
  - [2.6 Common Pitfalls](#26-common-pitfalls)
- [Part 3 — Week 1 Mini Project: Crypto API Analyzer](#part-3--week-1-mini-project-crypto-api-analyzer)
  - [3.1 Why CoinGecko (and not OpenWeather)](#31-why-coingecko-and-not-openweather)
  - [3.2 The Project Architecture](#32-the-project-architecture)
  - [3.3 Step-by-Step Build](#33-step-by-step-build)
  - [3.4 The Full Code](#34-the-full-code)
  - [3.5 Stretch Goals](#35-stretch-goals)
  - [3.6 Push to GitHub](#36-push-to-github)
- [Week 1 Reflection — What You Just Built](#week-1-reflection--what-you-just-built)
- [Looking Ahead — Week 2 Preview](#looking-ahead--week-2-preview)
- [Cheat Sheets](#cheat-sheets)

---

## The Big Picture — Why Pandas and Matplotlib?

Every AI/ML workflow follows the same five-step shape. Today you learn the tools for steps 2–4:

```
   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌──────────┐
   │ 1.Fetch │───▶│ 2.Clean │───▶│3.Analyze│───▶│4.Visual │───▶│ 5.Decide │
   │  data   │    │ /shape  │    │ patterns│    │  -ize   │    │  /train  │
   └─────────┘    └─────────┘    └─────────┘    └─────────┘    └──────────┘
       │              │              │              │              │
   requests        pandas         pandas       matplotlib        you
   (Day 6)        (today)        (today)        (today)        (later)
```

This is the same shape for:
- **Training a model** → fetch training data, clean labels, analyze class balance, visualize distribution, train
- **Evaluating a RAG system** → fetch test queries, run retriever, analyze precision/recall, visualize per-query, decide what to fix
- **Auditing an AI agent** → fetch logs, clean malformed entries, group by tool name, visualize failure rates, fix the worst tool
- **Fine-tuning Claude** → fetch your company's docs, clean & deduplicate, analyze token counts, visualize length distribution, prep JSONL

You're not learning two libraries. You're learning the **universal data shape of AI engineering**.

### Connecting to Your Power Platform Background

| Power Platform | Pandas equivalent | Why pandas wins for AI |
|---|---|---|
| Dataverse table | `DataFrame` | Lives in memory, no licensing, infinitely faster |
| List rows action | `pd.read_csv()` / `pd.read_json()` | Reads millions of rows in seconds |
| Filter rows action | `df[df["price"] > 100]` | One line, instant, runs locally |
| Apply to each + Compose | `df.apply(func)` / `df["new"] = ...` | Vectorized — 100× faster than loops |
| Aggregate (sum, count, avg) | `df.groupby().agg()` | One line vs. dozens of actions |
| Excel export | `df.to_csv()` | One line, no premium connector |
| Power BI chart | `matplotlib` | Embedded in your code, no separate tool |

You already know **what** these things do. Today you learn the **code-first version** that runs anywhere, in any AI app, with no licensing.

---

## Installation

```bash
pip install pandas matplotlib
```

You may also want:
```bash
pip install pandas matplotlib requests python-dotenv   # everything Week 1 used
```

Verify both:
```python
import pandas as pd
import matplotlib.pyplot as plt
print(pd.__version__)    # e.g., 2.2.0
print(plt.matplotlib.__version__)  # e.g., 3.8.0
```

> **About the `as pd` and `as plt`:** These are **conventions** the entire Python data ecosystem agrees on. Every tutorial, every Stack Overflow answer, every AI engineer codebase uses `pd` for pandas and `plt` for matplotlib's pyplot. Don't fight it — embrace it. When you see `pd.` or `plt.` in any code, you immediately know which library is being called.

---

## Part 1 — Pandas Foundations

### 1.1 Series vs DataFrame — The Two Building Blocks

Pandas has exactly two core data structures. Understand these and 80% of pandas falls into place.

```
       SERIES                          DATAFRAME
   (one column)                    (a full table)

   ┌──────────┐                ┌────────┬───────┬──────┐
   │ Bitcoin  │                │  coin  │ price │ rank │
   ├──────────┤                ├────────┼───────┼──────┤
   │ Ethereum │                │ BTC    │ 65000 │  1   │
   ├──────────┤                │ ETH    │  3200 │  2   │
   │ Solana   │                │ SOL    │   140 │  5   │
   ├──────────┤                │ ADA    │  0.45 │ 10   │
   │ Cardano  │                └────────┴───────┴──────┘
   └──────────┘
```

A **Series** is a single column with an index. Think: one Python list with row labels.
A **DataFrame** is a 2D table — many Series glued side by side, sharing the same row index.

```python
import pandas as pd

# A Series
prices = pd.Series([65000, 3200, 140, 0.45], index=["BTC", "ETH", "SOL", "ADA"])
print(prices)
# BTC    65000.00
# ETH     3200.00
# SOL      140.00
# ADA        0.45

# A DataFrame
df = pd.DataFrame({
    "coin": ["BTC", "ETH", "SOL", "ADA"],
    "price": [65000, 3200, 140, 0.45],
    "rank": [1, 2, 5, 10]
})
print(df)
#   coin    price  rank
# 0  BTC  65000.00     1
# 1  ETH   3200.00     2
# 2  SOL    140.00     5
# 3  ADA      0.45    10
```

> **Mental model:** Every column you pull out of a DataFrame is a Series. `df["price"]` returns a Series. `df[["price", "rank"]]` returns a smaller DataFrame. That's the whole rule.

---

### 1.2 Creating a DataFrame — Five Ways

You'll see all five in the wild. Memorize at least #1 and #4.

```python
import pandas as pd

# 1. From a dict of lists (most common, easy to read)
df = pd.DataFrame({
    "coin":  ["BTC", "ETH", "SOL"],
    "price": [65000, 3200, 140]
})

# 2. From a list of dicts (this is what APIs return!)
api_data = [
    {"coin": "BTC", "price": 65000},
    {"coin": "ETH", "price": 3200},
    {"coin": "SOL", "price": 140},
]
df = pd.DataFrame(api_data)

# 3. From a list of lists + column names
rows = [["BTC", 65000], ["ETH", 3200], ["SOL", 140]]
df = pd.DataFrame(rows, columns=["coin", "price"])

# 4. From a CSV file (real-world #1 source)
df = pd.read_csv("crypto_prices.csv")

# 5. From a JSON file (real-world #2 source — every API)
df = pd.read_json("crypto_prices.json")
```

> **#2 is the AI engineer's favorite.** Every API returns a list of JSON objects. `pd.DataFrame(response.json())` is one of the most common lines you'll write.

---

### 1.3 Reading Data — `read_csv`, `read_json`, `read_excel`

Pandas can read **almost any tabular file format** with one function call:

```python
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")           # needs: pip install openpyxl
df = pd.read_parquet("data.parquet")      # huge AI/ML datasets
df = pd.read_html("https://...")          # scrapes tables from a webpage!
df = pd.read_sql("SELECT * FROM ...", conn)
```

`read_csv` is the workhorse. The most useful arguments:

```python
df = pd.read_csv(
    "data.csv",
    sep=",",              # delimiter (use ";" for European CSVs, "\t" for TSV)
    encoding="utf-8",     # always specify
    header=0,             # row to use as column names (0 = first row)
    index_col=None,       # which column to use as row index
    nrows=1000,           # only read first 1000 rows (great for huge files!)
    usecols=["a", "b"],   # only read these columns (saves memory)
    parse_dates=["timestamp"],  # auto-convert to datetime
    na_values=["N/A", "missing", "-"],  # treat these as missing values
)
```

> ⚠️ **Day 4 callback:** Remember the `csv` module version where you had to manually loop through rows and split commas? Pandas does all that for you in one line — *and* handles edge cases like quoted commas, missing values, and weird encodings. This is why pandas exists.

---

### 1.4 Inspecting a DataFrame

The first thing every AI engineer does after loading data — **look at it**. Don't print the whole thing (it might be a million rows). Use these:

```python
df.head()           # First 5 rows
df.head(20)         # First 20 rows
df.tail()           # Last 5 rows
df.sample(5)        # 5 random rows (great for spot-checks)

df.shape            # (rows, columns) — e.g., (1000, 8)
df.columns          # list of column names
df.dtypes           # data type of each column
df.info()           # everything: rows, columns, dtypes, missing values, memory

df.describe()       # quick stats (count, mean, std, min, 25%, 50%, 75%, max)
                    # — only for numeric columns

df.isnull().sum()   # count missing values per column (CRITICAL for AI data!)
```

| Method | Returns | When you use it |
|---|---|---|
| `head()` / `tail()` | First/last N rows | "What does this data look like?" |
| `shape` | (rows, cols) | "How big is this?" |
| `dtypes` | Type of each col | "Why is this column treated as a string?" |
| `info()` | Full summary | First thing after loading any new dataset |
| `describe()` | Statistical summary | "Are there outliers? What's the range?" |
| `isnull().sum()` | Missing per col | **Always run this before training a model** |

> **AI engineering reality:** 80% of "the model isn't working" turns out to be "the data has problems you didn't see." `df.info()` and `df.isnull().sum()` will save you hours, every week, for the rest of your career.

---

### 1.5 Selecting Columns and Rows

```python
# ── COLUMNS ──────────────────────────────────────
df["price"]                  # one column → returns a Series
df[["coin", "price"]]        # multiple columns → returns a DataFrame
df.price                     # also works (only if name has no spaces)

# ── ROWS by position (.iloc) ─────────────────────
df.iloc[0]                   # first row (as a Series)
df.iloc[0:5]                 # first 5 rows
df.iloc[-1]                  # last row
df.iloc[0, 1]                # first row, second column (single value)

# ── ROWS by label (.loc) ─────────────────────────
df.loc[0]                    # row with index label 0
df.loc[0, "price"]           # row 0, column "price"
df.loc[0:5, ["coin", "price"]]   # rows 0–5, two columns

# ── A CELL ────────────────────────────────────────
df.at[0, "price"]            # fastest single-value lookup
```

> **The `.loc` vs `.iloc` rule:**
> - `.iloc` = **i**nteger location → "give me row #3" (positional)
> - `.loc` = **l**abel → "give me the row labeled 'BTC'" (by index name)
>
> When the index is just default 0, 1, 2, 3..., they look identical. They diverge the moment you set a custom index. **Use `.iloc` 90% of the time as a beginner.**

---

### 1.6 Filtering — The "WHERE Clause" of Pandas

This is the operation you'll do most often in AI engineering — picking subsets of data.

```python
# Single condition
df[df["price"] > 1000]

# How does this work?
# Step 1: df["price"] > 1000  →  produces a Series of True/False (a "boolean mask")
# Step 2: df[ mask ]          →  keeps only rows where mask is True

mask = df["price"] > 1000
print(mask)
# 0     True
# 1     True
# 2    False
# 3    False
df[mask]   # keeps rows 0 and 1
```

```python
# Multiple conditions — & for AND, | for OR, ~ for NOT
# CRITICAL: each condition MUST be in parentheses!

df[(df["price"] > 1000) & (df["rank"] <= 5)]      # AND
df[(df["coin"] == "BTC") | (df["coin"] == "ETH")] # OR
df[~(df["price"] < 100)]                           # NOT (price NOT less than 100)

# String matching
df[df["coin"].str.contains("BTC")]
df[df["coin"].str.startswith("E")]

# Membership (like SQL "IN")
df[df["coin"].isin(["BTC", "ETH", "SOL"])]

# Missing values
df[df["price"].isnull()]      # rows where price is missing
df[df["price"].notnull()]     # rows where price is present

# Range — SQL "BETWEEN"
df[df["price"].between(100, 1000)]
```

> ⚠️ **The #1 beginner pandas error:** Forgetting parentheses around each condition.
> ```python
> df[df["price"] > 1000 & df["rank"] <= 5]      # ❌ CRASHES with weird error
> df[(df["price"] > 1000) & (df["rank"] <= 5)]  # ✅ correct
> ```
> Why? `&` has higher precedence than `>`, so Python evaluates `1000 & df["rank"]` first → nonsense. Always wrap each condition.

> **Power Platform parallel:** This is the **OData filter** in "List rows" — `price gt 1000 and rank le 5` — except instant, free, and runs anywhere.

---

### 1.7 `describe()`, `value_counts()`, and Quick Stats

```python
df.describe()
#               price       rank
# count       4.0000     4.0000
# mean    17085.1125     4.5000
# std     31893.2345     3.6968
# min         0.4500     1.0000
# 25%        80.1125     1.7500
# 50%      1670.0000     3.5000
# 75%     18675.0000     6.2500
# max     65000.0000    10.0000
```

`describe()` runs **count, mean, std, min, max, and quartiles** on every numeric column. This is your first sanity check on any dataset — does the range make sense? Are there outliers?

For non-numeric (string) columns:
```python
df["coin"].value_counts()
# BTC    1
# ETH    1
# SOL    1
# ADA    1

# Real example with duplicates:
df["category"].value_counts()
# DeFi      45
# Gaming    23
# L1        18
# NFT       14
```

`value_counts()` is the **#1 tool for understanding categorical columns**. "What models am I running?" "What error types am I seeing?" "What countries are my users from?" — all `value_counts()`.

Other quick aggregations:
```python
df["price"].sum()
df["price"].mean()
df["price"].median()
df["price"].max()
df["price"].min()
df["price"].std()
df["price"].nunique()    # number of UNIQUE values
df["price"].unique()     # array of unique values
```

---

### 1.8 `groupby()` — The Most Powerful Verb

If pandas had only one feature, this would be it. `groupby` answers "**average X per Y**" type questions.

```python
df = pd.DataFrame({
    "coin":     ["BTC", "ETH", "BTC", "ETH", "SOL", "SOL"],
    "exchange": ["Binance", "Binance", "Coinbase", "Coinbase", "Binance", "Coinbase"],
    "price":    [65000, 3200, 64900, 3210, 140, 138]
})

# Average price per coin (across all exchanges)
df.groupby("coin")["price"].mean()
# BTC    64950.0
# ETH     3205.0
# SOL      139.0

# Average price per exchange (across all coins)
df.groupby("exchange")["price"].mean()
# Binance     22780.0
# Coinbase    22749.3

# Group by TWO columns
df.groupby(["coin", "exchange"])["price"].mean()
# coin  exchange
# BTC   Binance     65000
#       Coinbase    64900
# ETH   Binance      3200
#       Coinbase     3210
# ...

# Multiple aggregations at once
df.groupby("coin")["price"].agg(["mean", "min", "max", "count"])
#           mean    min    max  count
# coin
# BTC    64950.0  64900  65000      2
# ETH     3205.0   3200   3210      2
# SOL      139.0    138    140      2
```

**The mental model:**
```
1. SPLIT by the group column
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │ BTC     │  │ ETH     │  │ SOL     │
   │ 65000   │  │ 3200    │  │ 140     │
   │ 64900   │  │ 3210    │  │ 138     │
   └─────────┘  └─────────┘  └─────────┘

2. APPLY the function (mean) to each group
       ↓             ↓             ↓
     64950         3205          139

3. COMBINE the results into one Series/DataFrame
   BTC    64950.0
   ETH     3205.0
   SOL      139.0
```

This is called the **Split-Apply-Combine** pattern. Once it clicks, you'll see it everywhere — SQL `GROUP BY`, Power Platform aggregation, Spark, Excel pivot tables. Same pattern, different syntax.

> **AI engineering use case:** "Average latency per model" → `df.groupby("model")["latency_ms"].mean()`. "Error rate per tool" → `df.groupby("tool")["error"].sum() / df.groupby("tool").size()`. "Token cost per user" → `df.groupby("user_id")["tokens"].sum()`. You will write this verb hundreds of times.

---

### 1.9 Adding, Updating, Deleting Columns

```python
# Add a new column (computed from existing)
df["price_inr"] = df["price"] * 83        # convert USD → INR
df["is_expensive"] = df["price"] > 1000   # boolean column

# Add using .apply (when the logic is complex)
def categorize(price):
    if price > 10000:
        return "high"
    elif price > 100:
        return "mid"
    else:
        return "low"

df["tier"] = df["price"].apply(categorize)

# Or with a lambda (one-liner)
df["tier"] = df["price"].apply(lambda p: "high" if p > 10000 else "low")

# Update an existing column
df["price"] = df["price"] * 1.1            # 10% increase across the board

# Delete a column
df = df.drop(columns=["is_expensive"])
del df["price_inr"]                        # also works
```

> **Vectorization beats loops.** `df["price"] * 83` operates on the entire column at once — internally pandas runs it in C, not Python. This is **100× faster** than:
> ```python
> for i in range(len(df)):              # ❌ slow
>     df.at[i, "price_inr"] = df.at[i, "price"] * 83
> ```
> Rule of thumb: if you're writing a `for` loop over rows, you're probably doing it wrong. Use vectorized operations or `.apply()`.

---

### 1.10 Sorting and Renaming

```python
# Sort by one column
df.sort_values("price")                            # ascending
df.sort_values("price", ascending=False)           # descending

# Sort by multiple columns
df.sort_values(["rank", "price"], ascending=[True, False])

# Rename columns
df = df.rename(columns={"price": "price_usd", "rank": "market_cap_rank"})

# Make all column names lowercase (clean-up after API responses)
df.columns = df.columns.str.lower()

# Reset the index after filtering/sorting (gets rid of gaps)
df = df.reset_index(drop=True)
```

> **The `inplace=` debate:** Many pandas methods accept `inplace=True` to modify the DataFrame directly instead of returning a new one. **Don't use it.** It's being deprecated, and the modern style is to reassign: `df = df.sort_values("price")`. Cleaner, safer, more predictable.

---

### 1.11 Saving Data — `to_csv`, `to_json`

```python
# Save to CSV
df.to_csv("output.csv", index=False, encoding="utf-8")
# index=False is CRUCIAL — without it, pandas writes the row numbers
# as a useless first column.

# Save to JSON
df.to_json("output.json", orient="records", indent=2)
# orient="records" → list of dicts (the format APIs expect)
# indent=2 → human-readable formatting

# Save to Excel
df.to_excel("output.xlsx", index=False, sheet_name="Crypto Prices")

# Save to JSONL (one JSON object per line — required for Claude fine-tuning, OpenAI, HuggingFace datasets)
df.to_json("dataset.jsonl", orient="records", lines=True)
```

> ⚠️ **`index=False` is a forever-rule.** Forgetting it adds a junk column to every CSV you save. Make it a muscle memory.

---

### 1.12 Common Pitfalls

| Pitfall | Symptom | Fix |
|---|---|---|
| Forgot parentheses around filter conditions | Cryptic `TypeError` about boolean operations | Wrap each: `(df["a"] > 1) & (df["b"] < 5)` |
| `SettingWithCopyWarning` | Yellow warning in terminal | Use `.loc` for assignments: `df.loc[mask, "col"] = value` |
| Forgot `index=False` in `to_csv` | CSV has a useless "Unnamed: 0" column | Always pass `index=False` |
| Used a Python loop over rows | Code is super slow on big data | Vectorize: `df["new"] = df["a"] * df["b"]` |
| Modified a column you also filtered on | Confused state | Reassign: `df = df[df["x"] > 0].copy()` |
| Mixed `.loc` and `.iloc` | `KeyError` or wrong row | `iloc` = position, `loc` = label. Pick one. |
| Forgot `encoding="utf-8"` | `UnicodeDecodeError` on Indian/Chinese names | Always pass `encoding="utf-8"` |
| Confused Series with DataFrame | `AttributeError` because some methods don't exist on Series | `df[["col"]]` returns DataFrame, `df["col"]` returns Series |

---

## Part 2 — Matplotlib Foundations

### 2.1 The Mental Model — Figure vs Axes

Matplotlib has confused beginners for 20 years because it has **two APIs** that look similar. Here's the truth:

```
   ┌─── Figure (the canvas / window) ──────────────┐
   │                                                │
   │   ┌─── Axes (one chart inside the figure) ───┐│
   │   │                                            ││
   │   │   - x-axis label                          ││
   │   │   - y-axis label                          ││
   │   │   - title                                 ││
   │   │   - the actual line/bars                  ││
   │   │                                            ││
   │   └────────────────────────────────────────────┘│
   │                                                  │
   └──────────────────────────────────────────────────┘
```

- **Figure** = the entire window (the canvas)
- **Axes** = one individual chart (you can have multiple Axes per Figure for sub-plots)

For Day 7, we use the simple **state-machine API**: `plt.something()` always operates on the "current" figure/axes. Easy to start, perfect for one chart at a time.

```python
import matplotlib.pyplot as plt
```

That `plt` shorthand is the convention. Use it.

---

### 2.2 Line Plots

The default chart for **anything that changes over time** — prices, latencies, training loss, daily users.

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
prices = [62000, 63500, 64200, 63800, 65000, 66100, 65500]

plt.plot(days, prices)
plt.show()
```

That's it. 3 lines for a chart. Now make it readable:

```python
plt.plot(days, prices, marker="o", linestyle="-", color="green", label="BTC")
plt.xlabel("Day")
plt.ylabel("Price (USD)")
plt.title("Bitcoin price — last 7 days")
plt.legend()
plt.grid(True)
plt.show()
```

**Two lines on one chart** — most common AI engineering chart (training loss vs. validation loss):

```python
days   = [1, 2, 3, 4, 5, 6, 7]
btc    = [62000, 63500, 64200, 63800, 65000, 66100, 65500]
eth    = [3100, 3150, 3200, 3180, 3220, 3300, 3250]

plt.plot(days, btc, marker="o", label="BTC")
plt.plot(days, eth, marker="s", label="ETH")
plt.xlabel("Day")
plt.ylabel("Price (USD)")
plt.title("BTC vs ETH — 7-day price")
plt.legend()
plt.grid(True)
plt.show()
```

> **AI engineering use case:** Plot training loss and validation loss over epochs. If they diverge, you're overfitting. This single chart has saved more ML projects than any other.

---

### 2.3 Bar Charts

Use bar charts to **compare categories** — not for time series.

```python
coins  = ["BTC", "ETH", "SOL", "ADA", "DOGE"]
prices = [65000, 3200, 140, 0.45, 0.12]

plt.bar(coins, prices, color=["orange", "blue", "purple", "navy", "gold"])
plt.xlabel("Coin")
plt.ylabel("Price (USD)")
plt.title("Top 5 cryptocurrencies — current price")
plt.yscale("log")    # log scale because BTC dwarfs DOGE — without this DOGE is invisible!
plt.grid(True, axis="y")
plt.show()
```

**Horizontal bars** — better when category names are long:
```python
plt.barh(coins, prices)
```

> **The log-scale trick:** When values span many orders of magnitude (BTC at $65,000 vs DOGE at $0.12), a normal scale makes small ones invisible. `plt.yscale("log")` rescues the chart. You'll use this for token counts, latency distributions, file sizes — anything with big spread.

---

### 2.4 Labels, Titles, Legends, Grids

A chart without labels is **useless** — six months from now you won't know what you plotted. **Always** add these:

```python
plt.plot(x, y, label="My data")

plt.xlabel("X-axis description")     # required
plt.ylabel("Y-axis description")     # required
plt.title("What this chart shows")   # required
plt.legend()                         # if you have a `label`
plt.grid(True)                       # makes values easier to read

plt.xticks(rotation=45)              # rotate x labels if they overlap
plt.tight_layout()                   # auto-adjust spacing (prevents cut-off labels)
```

The `figsize` argument sets dimensions in inches:
```python
plt.figure(figsize=(10, 5))   # wide chart — good for time series
plt.figure(figsize=(6, 6))    # square — good for bar charts
```

---

### 2.5 Saving Charts — `plt.savefig()`

```python
plt.plot(x, y)
plt.title("My chart")
plt.savefig("chart.png", dpi=150, bbox_inches="tight")
plt.close()    # frees memory — important if you save many charts in a loop
```

| Argument | What it does | Recommended |
|---|---|---|
| `dpi=150` | Image resolution | 100 for screen, 150 for reports, 300 for print |
| `bbox_inches="tight"` | Crops empty borders | Always use this |
| `transparent=True` | No white background | For dark-themed dashboards |
| Format | Detected from extension | `.png` for web, `.pdf` for print, `.svg` for scaling |

> ⚠️ **`savefig()` must come BEFORE `show()`.** `show()` clears the figure. Always: `savefig()` first, then `show()` (or `close()` if running in a script).

---

### 2.6 Common Pitfalls

| Pitfall | Symptom | Fix |
|---|---|---|
| `savefig()` after `show()` | Saved file is blank | Save first, then show |
| Forgot `plt.close()` in a loop | Memory blows up after 100 charts | `plt.close()` after each save |
| All bars the same color | Can't distinguish categories | Pass `color=["red", "blue", ...]` |
| Tiny invisible bars | Outlier dwarfs the rest | `plt.yscale("log")` |
| X-axis labels overlap | Unreadable chart | `plt.xticks(rotation=45)` + `plt.tight_layout()` |
| No legend appears | Forgot `label=` in `plot()` | `plt.plot(x, y, label="...")` then `plt.legend()` |

---

## Part 3 — Week 1 Mini Project: Crypto API Analyzer

This is your **Week 1 capstone**. It uses every skill from Days 1–7. It's portfolio-grade. Build it, push it, talk about it in interviews.

### 3.1 Why CoinGecko (and not OpenWeather)

Day 6 used OpenWeather (single city, single moment). For Day 7 we need a **dataset** — many rows so we can actually analyze and visualize.

**CoinGecko** is perfect because:
- ✅ **No API key required** for the public endpoints (one less setup hurdle)
- ✅ Returns **a list of objects** (top 50/100/250 coins) → instant DataFrame
- ✅ Real-world data with rich numeric fields (price, volume, market cap, % change)
- ✅ Used by every crypto/finance product in production
- ✅ Generous rate limits (10–50 calls/min on free tier)
- ✅ The data has natural categories to `groupby()` (price tiers, % change buckets)

> **AI engineering parallel:** This is the same shape as fetching evaluation results, RAG retrieval logs, or LLM benchmark data — you hit a real API, get back a list of records, and analyze them.

---

### 3.2 The Project Architecture

```
crypto-api-analyzer/
│
├── .env                    🔒  (empty for now — no API key needed for CoinGecko free)
├── .env.example            ✅  template
├── .gitignore              ✅  ignores .env, venv, __pycache__, data/
├── requirements.txt        ✅  pandas, matplotlib, requests, python-dotenv
├── README.md               ✅  project description (separate from your main README)
│
├── main.py                 🚀  entry point — orchestrates everything
│
├── fetcher.py              📡  talks to CoinGecko
├── analyzer.py             📊  pandas analysis
├── visualizer.py           📈  matplotlib charts
│
└── output/                 💾  generated files (gitignored)
    ├── crypto_data.csv
    ├── crypto_summary.json
    ├── price_chart.png
    └── volume_chart.png
```

> **Why split into modules?** Same reason a Power Automate solution has multiple flows: **one file, one job.** If CoinGecko's API changes tomorrow, you only edit `fetcher.py`. If you want a new chart type, you only edit `visualizer.py`. This is **separation of concerns** and it scales — exactly the structure you'll use in real AI engineering codebases.

---

### 3.3 Step-by-Step Build

**Step 1 — Create the project folder**

```powershell
cd "C:\Users\smadavaram\OneDrive - Deloitte (O365D)\Desktop\AI-Engineering-Journey"
mkdir crypto-api-analyzer
cd crypto-api-analyzer
code .
```

**Step 2 — Create a virtual environment (good habit per Day 6)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

You'll see `(venv)` appear at the start of your prompt.

**Step 3 — Install dependencies**

```powershell
pip install pandas matplotlib requests python-dotenv
pip freeze > requirements.txt
```

**Step 4 — Create `.gitignore`**

```
venv/
__pycache__/
*.pyc
.env
output/
.vscode/
```

**Step 5 — Build the four files (code below). Run with:**

```powershell
python main.py
```

**Step 6 — Verify outputs in `output/`** — CSV, JSON, two PNG charts.

---

### 3.4 The Full Code

#### `fetcher.py` — Talks to CoinGecko

```python
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
```

#### `analyzer.py` — Pandas Analysis

```python
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
```

#### `visualizer.py` — Matplotlib Charts

```python
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
```

#### `main.py` — Orchestrator

```python
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
```

#### Run it:

```powershell
python main.py
```

You should see ~50 rows printed, summary stats, tier counts, and four files in `output/`.

---

### 3.5 Stretch Goals

Once the basics work, push further. These are the "show this in interviews" upgrades:

1. **Add a CLI flag** — `python main.py --limit 100 --currency inr`. Use `argparse`.
2. **Schedule it** — run every hour with Windows Task Scheduler. Append each run to a master CSV. Now you have a **time series**.
3. **Plot the time series** — once you have a few hours of data, plot BTC price over time. This is exactly what every AI monitoring dashboard looks like.
4. **Send a Claude summary** (Day 6 callback!) — pass the stats dict to Claude and ask "summarize today's crypto market in 3 bullet points." Save the response. Now your project is **AI-powered**.
5. **Email yourself** when a coin moves >10% in 24h. (Connects to your Power Platform email skills, but in code.)
6. **Replace CoinGecko with the Anthropic usage API** — track your own Claude API token usage daily. Now it's directly career-relevant.

> **#4 is the move that turns this from "learning project" into "AI engineer portfolio piece."** It uses every skill from Week 1 + the AI part. Do it.

---

### 3.6 Push to GitHub

In your **main** AI-Engineering-Journey repo, add a `week1-project/` folder containing this entire mini-project. From your main repo root:

```powershell
# Make sure .env is gitignored (Day 6 rule!)
git status
# .env should NOT appear in the list. Only .env.example should.

git add .
git commit -m "Day 7: pandas, matplotlib + Week 1 capstone (Crypto API Analyzer)"
git push
```

Then go to your repo on GitHub and **add the chart PNGs to the README** so they show up on the project page. Recruiters look at your GitHub.

---

## Week 1 Reflection — What You Just Built

In 7 days you went from "Python is installed?" to a working data pipeline. Take a moment to look back at what's now in your toolbelt:

| Day | What you learned | What it unlocks |
|---|---|---|
| **1** | Variables, types, control flow, terminal, Git | The vocabulary of programming |
| **2** | Functions, modules, packages, imports | Writing reusable code |
| **3** | Lists, dicts, sets, comprehensions | Holding any data shape |
| **4** | Files, errors, JSON, CSV | Persisting state, surviving failures |
| **5** | Classes, inheritance, magic methods | Modeling real systems |
| **6** | `requests`, `dotenv`, HTTP, secrets | Talking to **any API on the internet** |
| **7** | Pandas, matplotlib, full pipeline | Analyzing and visualizing **any dataset** |

Look at the last three rows specifically. You can now: **call any API → store the data → analyze it → visualize it → save the result → version-control everything.** That is the **core skeleton** of every AI engineering project. Every. Single. One.

> **What separates you from someone who "watches AI tutorials":** you have a real GitHub repo, with real code, that talks to a real API, and produces real artifacts (CSVs, charts, JSON summaries). You can show this in an interview. You can extend it. That's a **moat**.

### The Power Platform → AI Engineer Bridge (Where You Stand)

```
Your starting point:                Your Week 1 endpoint:
─────────────────────               ────────────────────
Power Automate (drag flows)    →    Python scripts (write flows)
HTTP connector                  →    requests library
Connection references           →    .env + python-dotenv
Dataverse tables                →    pandas DataFrames
Power BI dashboards             →    matplotlib charts
Solution → ALM                  →    Git/GitHub
```

You're not abandoning your Power Platform skills — you're **upgrading** them to a code-first version that runs anywhere, scales to AI workloads, and gets you paid more.

---

## Looking Ahead — Week 2 Preview

**Week 2 is when the AI starts.** Everything you've built was the foundation. Here's what's coming:

| Day | Topic | What you'll do |
|---|---|---|
| 8 | LLM fundamentals | What is a token? What's a transformer (lightly)? Pricing, context windows, system prompts. |
| 9 | **First Claude API call** | Use Day 6's `requests` skills to actually talk to Claude. This is the moment. |
| 10 | The Anthropic SDK | Replace raw HTTP with `from anthropic import Anthropic`. See why SDKs exist. |
| 11 | Prompt engineering | System prompts, few-shot, XML tags, chain-of-thought. |
| 12 | Tool use | Let Claude call your Python functions. The skill that powers every agent. |
| 13 | Streaming responses | Real-time output. The thing every chat UI uses. |
| 14 | Mini project: AI-powered version of Day 7's analyzer |

> **Big picture:** Week 1 = Python + data + Git. Week 2 = LLMs. Week 3 = building real apps (FastAPI, Streamlit). Week 4 = production skills, RAG, agents, eval, deployment, **job prep**. You're 23% through and you've got the scaffolding. Now we add intelligence on top.

---

## Cheat Sheets

### Pandas — Quick Reference

```python
import pandas as pd

# CREATE
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})    # from dict
df = pd.DataFrame(list_of_dicts)                  # from API response
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")

# INSPECT
df.head()                # first 5 rows
df.shape                 # (rows, cols)
df.info()                # everything
df.describe()            # numeric stats
df.isnull().sum()        # missing per column
df["col"].value_counts() # category counts
df["col"].unique()       # unique values

# SELECT
df["col"]                # one column → Series
df[["a", "b"]]           # multiple → DataFrame
df.iloc[0]               # row by position
df.loc[0, "col"]         # row by label, specific column

# FILTER
df[df["price"] > 100]
df[(df["a"] > 1) & (df["b"] < 5)]    # always parenthesize!
df[df["coin"].isin(["BTC", "ETH"])]

# MUTATE
df["new"] = df["a"] * df["b"]
df["tier"] = df["price"].apply(lambda p: "high" if p > 100 else "low")
df = df.drop(columns=["junk"])
df = df.rename(columns={"old": "new"})

# AGGREGATE
df["price"].mean()
df.groupby("category")["price"].mean()
df.groupby("category")["price"].agg(["mean", "max", "count"])

# SAVE
df.to_csv("out.csv", index=False)
df.to_json("out.json", orient="records", indent=2)
```

### Matplotlib — Quick Reference

```python
import matplotlib.pyplot as plt

# LINE PLOT
plt.plot(x, y, marker="o", label="Series A")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Title")
plt.legend()
plt.grid(True)

# BAR CHART
plt.bar(categories, values, color="steelblue")
plt.barh(categories, values)               # horizontal
plt.yscale("log")                           # for big spread

# FIGURE SIZE
plt.figure(figsize=(10, 5))

# X-AXIS LABEL ROTATION
plt.xticks(rotation=45)
plt.tight_layout()

# SAVE — always before show()!
plt.savefig("chart.png", dpi=150, bbox_inches="tight")
plt.close()
```

### Project Pipeline — The 5-Step Pattern

```python
# 1. FETCH
raw = requests.get(URL).json()

# 2. SHAPE
df = pd.DataFrame(raw)

# 3. ANALYZE
stats = df.groupby("col")["val"].agg(["mean", "max"])

# 4. VISUALIZE
plt.bar(...); plt.savefig(...); plt.close()

# 5. SAVE
df.to_csv("out.csv", index=False)
```

This pattern is **every** AI engineering project's data layer. Memorize the shape.

---

> **Note to future me:** Day 7 is the day Python stopped being theoretical. You now have a real pipeline that fetches live data from the internet, shapes it, analyzes it, draws charts, and saves the output. **This is what AI engineering looks like 80% of the time** — the other 20% is calling LLMs (Week 2 onwards). The SDKs change. The models change. The 5-step pattern (fetch → shape → analyze → visualize → save) does not. When you forget how groupby works in 2 months, come back to §1.8. When matplotlib confuses you, re-read §2.1. The cheat sheets at the bottom are your daily driver.

> **Philosophy:** Recruiters don't read tutorials. They read your GitHub. After today, your GitHub has: a 30-day learning README, a working Crypto API Analyzer with real charts, and clean code split across modules. That puts you ahead of 90% of "I'm learning AI" candidates who only have notebook screenshots. Keep pushing. Week 2 is where it gets *interesting*.