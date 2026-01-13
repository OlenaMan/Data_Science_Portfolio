## US Crime Patterns

## PCA and Unsupervised Machine Learning Analysis

### Project Overview

This project demonstrates an end-to-end **unsupervised machine learning workflow** with a focus on **Principal Component Analysis (PCA)** and **clustering techniques**. The notebook explores how dimensionality reduction can be used to better understand high-dimensional data and improve clustering performance and interpretability.

The analysis follows a structured, data-science-oriented pipeline: data exploration, preprocessing, feature scaling, correlation analysis, PCA, and clustering.

---

### Objectives
- Explore and understand the structure of a multivariate dataset
- Prepare data correctly for unsupervised learning
- Reduce dimensionality using PCA while retaining explanatory power
- Identify meaningful clusters using multiple clustering algorithms
- Analyse and interpret clusters in the reduced feature space

---

### Workflow Summary

#### 1. Load the Dataset
- Import the dataset into a pandas DataFrame
- Inspect structure, data types, and basic statistics

#### 2. Exploratory Data Analysis (EDA)
- Review distributions and summary statistics
- Identify potential scaling and correlation issues
- Check for data quality considerations

#### 3. Feature Scaling
- Standardise features to ensure equal contribution
- Prepare data for PCA and distance-based clustering algorithms

#### 4. Correlation Analysis
- Examine correlations between features
- Motivate the need for dimensionality reduction

#### 5. Principal Component Analysis (PCA)
- Apply PCA to the scaled dataset
- Analyse explained variance ratios
- Reduce dimensionality while preserving most of the information

#### 6. Selecting the Number of Principal Components
- Use explained variance plots (e.g. cumulative variance)
- Balance dimensionality reduction with information retention

#### 7. Clustering
- Apply **K-Means clustering**
- Apply **Hierarchical clustering**
- Compare clustering behaviour in PCA-reduced space

#### 8. Cluster Analysis
- Interpret clusters using PCA components
- Compare cluster structure across algorithms
- Draw insights from cluster composition

---

## Key Techniques Used
- Principal Component Analysis (PCA)
- Standardisation / scaling
- K-Means clustering
- Hierarchical clustering
- Exploratory data analysis
- Correlation analysis

---

## Tools and Libraries
- Python
- pandas
- numpy
- scikit-learn
- matplotlib / seaborn

---

