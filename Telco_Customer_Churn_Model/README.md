## Telco Customer Churn Analysis & Prediction
### Overview

This project demonstrates an end-to-end machine learning workflow to analyze and predict customer churn using a telecommunications dataset. 
It focuses on data preprocessing, exploratory analysis, model building, and evaluation, with an emphasis on interpretability and practical business relevance.

The notebook applies both linear and tree-based classification models to understand churn drivers and assess predictive performance.

### Business Context

Customer churn is a major risk factor in subscription-based industries such as telecommunications. Accurately identifying customers at risk of leaving enables targeted retention strategies,
improved customer experience, and reduced revenue loss.

This project explores how customer demographics, service usage, and contract characteristics influence churn and evaluates how effectively different machine learning models capture these patterns.

### What I Did

- Loaded and inspected the Telco Customer Churn dataset

- Cleaned and preprocessed data, including encoding categorical variables

- Conducted exploratory data analysis to examine churn patterns

- Prepared features and target variable for machine learning

- Built and evaluated a Logistic Regression model

- Built and evaluated a Random Forest classifier

- Compared model performance using classification metrics

- Assessed results to balance predictive power and interpretability

### Key Skills Demonstrated

- Data cleaning and preprocessing

- Exploratory data analysis (EDA)

- Binary classification

- Logistic Regression

- Random Forest modeling

- Model evaluation (accuracy, precision, recall, confusion matrix)

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)

### Dataset

- Based on the Telco Customer Churn dataset, a real-world classification dataset for churn analysis.

- Target variable: Churn

- Feature types: demographic, service usage, and contract attributes

- Task type: binary classification

- Categorical variables were encoded to enable machine learning models.

### Models Used

#### Logistic Regression

- Baseline, interpretable classification model

- Useful for understanding linear relationships with churn

#### Random Forest Classifier

- Non-linear, ensemble-based model

- Captures feature interactions and complex patterns

### Results (High Level)

- Both models successfully identify patterns associated with customer churn

- Logistic Regression provides clearer interpretability of feature influence

- Random Forest improves predictive performance by capturing non-linear relationships

- Results highlight trade-offs between explainability and model complexity

- (Exact metrics, confusion matrices, and evaluation outputs are available in the notebook.)
