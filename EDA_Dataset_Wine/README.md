## Wine Dataset — Exploratory Data Analysis (EDA)
## Overview

This project explores the Wine Reviews Dataset (1,103 records, 11 features) to understand how geography, grape variety, winery characteristics, 
expert ratings, and price relate to each other.
The analysis focuses on data cleaning, missing data handling, statistical profiling, and visual insights into wine pricing and quality.

## Dataset

Source: UCI Machine Learning Repository

Rows: 1,103

Columns: 11

Key features:

country, province, region_1, region_2 – geography

variety, winery, designation, description – wine details

points – expert rating

price – bottle price (target for many insights)

## Methods & Workflow
### 1. Data Cleaning

- Removed index column

- Handled missing values:

  - region_2 dropped (55% missing)

  - price imputed using median

  - designation and region_1 filled with "Unknown"

### 2. Exploratory Analysis

- Summary statistics for points and price

- Distribution analysis using histograms

- Outlier detection with boxplots

- Missing data visualised with missingno

- Correlation analysis for numeric features

### 3. Visual Insights

- Heatmaps for correlation

- Scatterplots for price vs. points

- Country-level comparisons (avg price & rating)

- Grape variety quality distribution (Top 10 varieties)

## Key Findings

- Price and rating show a moderate positive correlation (0.43).

- Most wines cluster around 90 points and $20–50.

- Price outliers include premium wines priced up to $500.

- Italy, US, Spain, France, Portugal have the highest review volumes.

- Italian wines tend to be highest priced and highly rated on average.

- Pinot Noir, Chardonnay, and Cabernet Sauvignon show strong, consistent quality.

## Tech Stack

Python

Pandas, NumPy

Matplotlib, Seaborn

Missingno

Jupyter Notebook
