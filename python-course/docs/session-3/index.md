---
hide:
  - toc
---

# Data Analysis

This session moves from the general-purpose Python, NumPy, and pandas foundations built in Session 2 toward a complete, realistic **business data workflow**. Rather than treating pandas as a collection of isolated commands, this session follows a single dataset through every stage an analyst genuinely encounters in practice: building a DataFrame, importing external data, cleaning and preparing it, deriving new variables, exploring it statistically, and finally merging it with a second dataset for comparison.

The session is organised into six sequential parts:

- **Creating DataFrames** — building a DataFrame from scratch, using a small dictionary-based example.
- **Importing Data** — bringing in real external data from FRED (macroeconomic indicators) and Yahoo Finance (stock prices).
- **Preparing Data** — cleaning, renaming, validating, and exporting a dataset so it's ready for analysis.
- **Data Analysis** — deriving new variables such as returns, indicators, lags, and rolling statistics.
- **Data Inspection** — using descriptive and grouped statistics to explore a dataset before drawing any conclusions.
- **Merging Datasets** — combining two related datasets on a shared key, with proper validation.

In business, economics, and finance, data rarely arrives ready to use. A real dataset has to be found, downloaded, cleaned, checked, and reshaped before it can answer any meaningful question, and every one of those steps is a place where a small oversight can quietly produce a misleading result. A date stored as text rather than a true date can silently break a trend calculation. A duplicated observation can distort an average. A careless merge can double-count rows without any obvious error message.

The purpose of this session isn't just to introduce pandas commands in isolation, it's to build the *habits* of a careful analyst: checking a dataset's shape and column names immediately after loading it, validating for missing or duplicated values before trusting a calculation, and confirming that a merge produced exactly the relationship you expected rather than assuming it did. These habits matter more, in practice, than memorising any individual method, since they're what catches the errors that would otherwise undermine an entire analysis.

By the end of the session, working with genuine business and financial data, pulling it from an external source, shaping it into something usable, deriving meaningful new variables, and combining it with other sources, should feel like a single, coherent process rather than a set of disconnected tricks.

Here is a brief list of key commands frequently used throughout this session.

| Motivation | Section |
| --- | --- |
| Turns raw Python data (like a dictionary) into a structured table of rows and columns using **`pd.DataFrame()`**, the starting point for almost everything else, since every other pandas tool is built to work with this structure. | Creating DataFrames |
| Real analysis begins with real data. **`pd.read_csv()`**, **`fred.get_series()`**, and **`yf.Ticker().history()`** are the everyday entry points for bringing external business, economic, and financial data into Python, rather than typing observations in by hand. | Importing Data |
| Converts text that merely *looks* like a date into a genuine datetime type using **`pd.to_datetime()`**. Skipping this quietly breaks sorting, rolling calculations, and merging later on, one of the most common early sources of hard-to-diagnose bugs. | Importing Data / Preparing Data |
| The two fastest checks for whether a dataset is actually trustworthy, **`.isna().sum()`** and **`.duplicated().sum()`**, reveal whether any values are missing and whether any observation has been accidentally counted twice. Running these before analysis catches problems while they're still cheap to fix. | Preparing Data |
| Converts raw levels (like prices) into percentage changes (like returns) using **`.pct_change()`**, the standard way analysts make very different variables genuinely comparable with one another. | Data Analysis |
| **`.groupby()`** paired with **`.agg()`** is the core tool for summarising and comparing groups, positive versus negative return days, sectors, categories, without writing manual loops. This is the "split-apply-combine" pattern that underlies most real-world data summaries. | Data Inspection |
| Combines two related datasets into one, using a shared key such as a date, via **`pd.merge()`**. Paired with `validate=`, it also confirms the merge behaved exactly as expected, rather than silently duplicating or dropping rows. | Merging Datasets |
