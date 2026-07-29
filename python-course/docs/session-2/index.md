---
hide:
  - toc
---

# Session 2: Working with Python Data

## Overview

This session moves from writing individual lines of Python toward working with **data** in a structured, organised way. Building on the basic syntax introduced in Session 1, this session covers how Python stores, represents, and manipulates information, then extends these ideas into the numerical computing tools provided by NumPy and the tabular data tools provided by pandas.

The session is organised into a sequence of parts:

- **Variable Assignment** — revisiting variables and assignment statements, and covering Python's reserved keywords in detail.
- **Common Python Data Types** — numerical types, strings, lists, and dictionaries, and how to store, manipulate, and extract information from each.
- **NumPy Basics** — what NumPy is, why it matters for numerical computing, and how to create and inspect arrays.
- **Random Numbers** — generating random numbers from various distributions, and using a random seed for reproducibility.
- **Statistical Operations** — summarising numerical data using means, standard deviations, percentiles, and axis-based aggregation.
- **Matrix Manipulation and Data Preparation** — reshaping, stacking, and combining arrays ready for analysis.
- **Pandas** — creating and inspecting DataFrames, then loading and inspecting a real dataset.
- **Accessing, Modifying and Filtering Data** — indexing, dropping, replacing, and filtering rows and columns in a DataFrame.
- **DataFrame Processing** — merging datasets, grouped calculations, and applying custom transformations.
- **Essential Pandas Tools** — missing data, `.loc` vs `.iloc`, sorting, concatenation, text and date handling, duplicates, and exporting.
- **Comparing Variable Types Across Python, NumPy, and Pandas** — a reference table connecting every variable type introduced in the session.

Data rarely arrives in a form that's immediately useful. Before any meaningful analysis can happen, information first has to be stored in an appropriate variable, organised into the right data structure, and, for anything beyond a handful of values, handled through tools built specifically for speed and scale rather than one value at a time. This is exactly the progression this session follows: individual variables and data types first, then NumPy's fast, uniform arrays for numerical work, and finally pandas' labelled, tabular DataFrames for genuinely realistic, mixed-type datasets.

The purpose of this session isn't just to introduce a long list of new commands, it's to build an intuition for *which* data type or tool fits a given task, and to recognise how each layer builds directly on the one below it: a pandas DataFrame is a table of NumPy-like columns, and a NumPy array is a faster, stricter version of a Python list. Once that relationship feels natural, choosing the right tool becomes a matter of asking a simple question, rather than remembering an arbitrary rule.

By the end of the session, moving fluidly between single values, collections, numerical arrays, and full tabular datasets, and knowing which one a given task actually calls for, should feel like a natural and connected skill, rather than a set of separate topics.

Here is a brief list of key commands frequently used throughout this session.

| Motivation | Section |
| --- | --- |
| Stores and labels a value in memory using an **assignment statement** (`age = 25`), the starting point for every Python program, and a habit worth pairing with meaningful, descriptive variable names. | Variable Assignment |
| Checks what kind of data a value actually is using **`type()`**, one of the fastest ways to catch a bug before it causes bigger problems further down the code. | Common Python Data Types |
| Creates a fast, uniform grid of numbers using **`np.array()`**, the foundation of everything else NumPy offers, trading Python's flexible mixed types for considerably faster numerical computation. | NumPy Basics |
| Generates reproducible "random" values using **`np.random.seed()`** alongside **`np.random.rand()`**, **`np.random.randn()`**, and **`np.random.normal()`**, essential for simulation and for results that can be checked or repeated by someone else. | Random Numbers |
| Summarises an array's values using **`.mean()`**, **`.std()`**, and **`np.percentile()`**, with the `axis=` argument controlling whether the summary runs down columns, across rows, or over the whole array. | Statistical Operations |
| Reshapes and recombines arrays using **`.reshape()`**, **`np.vstack()`**, and **`np.hstack()`**, the everyday tools for preparing numerical data into whatever shape a later calculation or model expects. | Matrix Manipulation and Data Preparation |
| Builds a labelled, spreadsheet-like table using **`pd.DataFrame()`**, then inspects it immediately with **`.head()`**, **`.shape`**, and **`.describe()`**, the standard first steps after creating or loading any dataset. | Pandas |
| Selects, changes, or narrows down a dataset using **`.loc[]`**, **`.drop()`**, and Boolean filtering (`data[condition]`), the recipe behind almost every row- or column-level operation in pandas. | Accessing, Modifying and Filtering Data |
| Combines two related datasets using **`.merge()`**, and summarises data by category using **`.groupby()`**, the "split-apply-combine" pattern that underlies most real-world data summaries. | DataFrame Processing |
| Handles the everyday practicalities of real data, missing values with **`.isna()`** and **`.fillna()`**, precise positional access with **`.iloc`**, and saving results with **`.to_csv()`**, that come up in almost every genuine analysis. | Essential Pandas Tools |
