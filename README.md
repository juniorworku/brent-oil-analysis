# Brent Oil Price Analysis and Prediction

This project focuses on the analysis and prediction of Brent oil prices using various advanced time series models and machine learning techniques. The analysis includes historical trends, regime changes, and future price predictions, with models like ARIMA, Markov-Switching ARIMA, and Long Short-Term Memory (LSTM) networks.

## Table of Contents

- [Introduction](#introduction)
- [Data Collection and Preprocessing](#data-collection-and-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Advanced Time Series Models](#advanced-time-series-models)
  - [Markov-Switching ARIMA Model](#markov-switching-arima-model)
- [Machine Learning Model](#machine-learning-model)
  - [LSTM Model](#lstm-model)
- [Factors Influencing Oil Prices](#factors-influencing-oil-prices)
  - [Economic Indicators](#economic-indicators)
  - [Technological Changes](#technological-changes)
  - [Political and Regulatory Factors](#political-and-regulatory-factors)
- [Adapting the Model to New Scenarios](#adapting-the-model-to-new-scenarios)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Authors](#authors)

## Introduction

Brent crude oil is a major benchmark for global oil prices, influenced by various economic, technological, and geopolitical factors. Accurate modeling and prediction of oil prices are crucial for stakeholders in energy markets. This project utilizes a combination of statistical and machine learning models to provide a detailed examination and predictive modeling of historical Brent oil prices.

## Data Collection and Preprocessing

**Dataset:**

- Historical Brent oil prices from 1987 to 2024.

**Preprocessing Steps:**

- Convert the date column to datetime format.
- Handle missing values and outliers.
- Normalize data for machine learning models.

## Exploratory Data Analysis (EDA)

**Historical Trends:**

- The time series plot reveals significant volatility and price changes over the years.
- Key spikes correspond to historical events such as the 2008 financial crisis and recent geopolitical tensions.

## Advanced Time Series Models

### Markov-Switching ARIMA Model

**Model Overview:**

- Captures regime changes in the time series data.
- Identifies different states (regimes) with distinct statistical properties.

**Results:**

- Detailed model output including parameters for different regimes.

**Visualization:**

- Plot showing regime probabilities over time.

## Machine Learning Model

### LSTM Model

**Model Overview:**

- Captures long-term dependencies in time series data.
- Utilizes past price movements to predict future prices.

**Results:**

- Model performance metrics and loss values.

**Visualization:**

- Plot showing actual prices vs. predicted prices for training and testing datasets.

## Factors Influencing Oil Prices

### Economic Indicators

- GDP, Inflation Rates, Unemployment Rates, Exchange Rates.

### Technological Changes

- Advancements in Extraction Technologies, Renewable Energy Developments, Efficiency Improvements.

### Political and Regulatory Factors

- Environmental Regulations, Trade Policies.

## Adapting the Model to New Scenarios

- Extend the analysis framework to other commodities or related markets.
- Integrate additional data sources like economic reports, technological advancements, and regulatory changes.
- Validate the model’s performance using cross-validation techniques.

## Conclusion and Recommendations

This analysis provides valuable insights into historical trends, regime changes, and future price predictions for Brent oil prices. The findings can inform risk management and decision-making strategies in the oil market.

**Recommendations:**

- Deploy the trained LSTM model for real-time forecasting.
- Continuously update and retrain the model with new data.
- Incorporate additional features such as economic indicators and geopolitical events.
- Explore other advanced models and techniques for improved forecasting.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/juniorworku/brent-oil-price-analysis.git
   cd brent-oil-price-analysis

   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

   ```

3. Run the analysis:

### Dependencies

-Python 3.x
-Pandas
-NumPy
-Scikit-learn
-Statsmodels
-TensorFlow
-Matplotlib

### Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### License

This project is licensed under the MIT License.

### Contact

For any questions or inquiries, please contact [juniorworku@gmail.com].
