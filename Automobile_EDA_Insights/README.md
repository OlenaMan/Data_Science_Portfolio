## Project Overview

This project performs a comprehensive Exploratory Data Analysis (EDA) on the Automobile dataset to understand how different vehicle characteristics,
such as, engine size, horsepower, body style, and fuel type—relate to market price.

The analysis focuses on uncovering key patterns, identifying outliers, and exploring correlations that help explain pricing behavior across different categories of cars.

## Dataset Information

- **Source**: UCI Machine Learning Repository — Automobile Dataset

- **Rows**: 205

- **Features**: 26 (mixture of numeric and categorical variables)

- **Topics covered**: Pricing, performance metrics, vehicle design attributes

The dataset includes a variety of car specifications such as symboling, make, fuel type, aspiration, doors, body style, horsepower, engine size, peak RPM, and price
— making it highly suitable for multivariate exploratory analysis.

## EDA Workflow

The analysis includes the following key steps:

1. **Data Cleaning & Preparation**

- Handling missing values in numeric and categorical features

- Converting data types for consistency

- Normalising and rounding numerical fields

- Removing or flagging anomalies for further inspection

2. **Descriptive Statistics & Distributions**

- Summary statistics to understand central tendencies and variability

- Visual exploration of price, horsepower, and engine size

- Histograms and bar charts for categorical variables

3. **Correlation & Relationship Analysis**

- Heatmaps to identify strongest numeric correlations

- Scatter plots to visualise relationships between engine size, horsepower, and price

- Pairplots to examine how price varies across body styles

4. **Categorical Feature Exploration**

- Comparing price distributions across:

  - Fuel types

  - Aspiration types

  - Body styles

  - Door configurations

## Key Insights

- Engine size and horsepower are the strongest predictors of vehicle price, showing a clear and consistent positive correlation.

- Higher-performance vehicles form noticeable outlier clusters, especially in horsepower and price.

- Body style categories (sedan, hatchback, convertible, etc.) show distinct pricing patterns, with some segments consistently priced higher.

- Fuel type and aspiration also influence price, indicating manufacturer design decisions tied to performance and market positioning.

These findings highlight how vehicle engineering choices and design attributes drive pricing, offering valuable insights for early modelling decisions or business intelligence use cases.
