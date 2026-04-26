# HouseValue AI – 智能房屋估价系统

## Product Overview

HouseValue AI is a data-driven house price analysis and prediction tool. It helps home buyers, real estate agents, and investors understand what factors most influence house prices and get a fair market value estimate.

## Target Users

- Home buyers looking for price guidance
- Real estate agents needing quick valuation support
- Property investors making data-informed decisions

## Key Features

- Feature importance analysis – identifies which factors drive prices
- 8 business-friendly visualizations (correlation heatmap, price distribution, living area vs price, basement area vs price, overall quality vs price, data standardization effect, multi-feature matrix, year built vs price)
- Machine learning prediction using Random Forest model (validation MAE around $20,000)
- Kaggle submission file generation (submission.csv)

## Tech Stack

- Python 3.9
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn (RandomForestRegressor, preprocessing)

## Repository Structure

HouseValue-AI/
├── comprehensive-data-exploration-with-python.ipynb   # Full analysis and model
├── charts/                                             # 8 key output charts
│   ├── 1_correlation_heatmap.png
│   ├── 2_price_distribution.png
│   └── ...
├── submission.csv                                      # Predictions on test set
├── README.md                                           # This file
└── reflection_report.md                                # Assignment reflection

Main Insights from Data

· Overall Quality is the strongest driver of house price.
· Living Area (GrLivArea) – larger space leads to higher price.
· Year Built – newer homes (post-2000) command a premium.
· Garage Cars – 2-3 car garages are most valued.

How to Run Locally

1. Clone this repository.
2. Install dependencies:
   pip install pandas numpy matplotlib seaborn scikit-learn
3. Run the Jupyter notebook:
   Open comprehensive-data-exploration-with-python.ipynb and execute cells in order (or click Run All).

Video Demo

Click here to watch the product introduction video

Reflection Report

See reflection_report.md for the full assignment reflection

Author

Jingting Luo– ACC102 Individual Mini Assignment (Track 2)
Date: April 2026

Data Source

House Prices: Advanced Regression Techniques – Kaggle
