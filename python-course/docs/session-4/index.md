---
hide:
  - toc
---

# Visualisation

This session shifts focus from preparing and calculating data to **communicating** it. Building on the business dataset skills developed in Session 3, this session works with a synthetic company-year panel dataset and uses it to introduce Matplotlib, the foundational Python charting library that underpins much of the wider data visualisation ecosystem.

The session is organised into six sequential parts:

- **Introducing the Synthetic Business Dataset** — inspecting the shape, columns, and company-year structure of the dataset before any charts are built.
- **Why Visualisation Matters** — understanding when and why a chart communicates a pattern more effectively than a table, and how to choose the right chart type for the question being asked.
- **Core Chart Types in Matplotlib** — building bar charts, scatter plots, and histograms, the everyday building blocks of business visualisation.
- **Trends Over Time** — visualising company-level and average trends using line charts, and calculating growth rates to distinguish real movement from noise.
- **Breakdowns, Grouping and Business Comparisons** — combining pandas grouping with visualisation to compare sectors, regions, company sizes, and other categories.
- **Exploring Relationships and Distributions** — using scatter plots and correlation matrices to investigate relationships between variables before any formal modelling begins.

A spreadsheet or DataFrame may contain everything needed for an analysis, but it's often genuinely difficult to spot a pattern from raw rows and columns alone. A chart lets an analyst *see* structure directly: whether sales are rising, whether values are unusually dispersed, whether one sector dominates the sample, or whether two variables move together. In business specifically, visualisation is also a communication tool, managers, clients, and stakeholders often need to grasp a result in seconds, and a single well-chosen chart can convey what would otherwise take several paragraphs to explain.

That said, a poorly designed chart can just as easily mislead, exaggerate a difference, or hide an outlier. The purpose of this session isn't just to introduce Matplotlib's individual functions, it's to build the habit of starting every chart with a clear question (are we showing a trend, a comparison, a distribution, or a relationship?), and letting that question determine the chart type, rather than picking a chart because it happens to look visually interesting.

By the end of the session, moving from a raw business dataset to a clear, correctly chosen, well-labelled chart, and reading that chart critically rather than at face value, should feel like a natural, repeatable process.

Here is a brief list of key commands frequently used throughout this session.

| Motivation | Section |
| --- | --- |
| Confirms the shape, column names, and structure of a dataset using **`data.shape`**, **`data.columns`**, and **`data["company"].value_counts()`** before any chart is built, so later charts are correctly interpreted rather than misread. | Introducing the Synthetic Business Dataset |
| Creates the canvas and controls its proportions using **`plt.figure(figsize=(...))`**, the standard first step before drawing any chart. | Core Chart Types in Matplotlib |
| Draws the three everyday chart families: **`.plot(kind="bar")`** for comparing categories, **`plt.scatter()`** for relationships between two numeric variables, and **`plt.hist()`** for the distribution of a single variable. | Core Chart Types in Matplotlib |
| Reshapes long, one-row-per-observation data into a wide, one-column-per-category table using **`.pivot_table()`**, making it straightforward to plot several companies' or sectors' trends on a single chart. | Trends Over Time |
| Converts raw levels into growth rates using **`.pct_change()`**, applied within **`.groupby("company")`** so each company's growth is calculated relative only to its own prior year. | Trends Over Time |
| Summarises data across one or more categories in a single, readable call using **`.groupby([...]).agg(...)`**, before visualising the result, the core tool behind every sector, region, or size-group comparison in this session. | Breakdowns, Grouping and Business Comparisons |
| Splits a numeric variable into evenly-sized groups using **`pd.qcut()`**, for example dividing companies into "Small," "Medium," and "Large" by employee count, ready for grouped comparison. | Breakdowns, Grouping and Business Comparisons |
| Summarises the strength and direction of every pairwise relationship in a dataset at once using **`.corr()`**, then visualises the result as a heatmap with **`plt.imshow()`**, a fast way to spot relationships worth investigating further before formal modelling. | Exploring Relationships and Distributions |
