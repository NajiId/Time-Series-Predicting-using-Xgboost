# Energy Usage Prediction

This project aims to predict energy usage using XGBoost regression on the PJME hourly dataset.

## Table of Contents

- [Overview](#overview)
- [Explore Data](#explore-data)
- [Feature Creation](#feature-creation)
- [Analysis](#analysis)
- [Modeling](#modeling)
- [Contributing](#contributing)

## Overview

In this project, we analyze the PJME hourly dataset to predict energy usage trends using XGBoost regression. We explore the dataset, create additional features, and perform analysis to understand patterns and relationships. Then, we build and evaluate an XGBoost regression model to predict future energy usage based on historical data.

## Explore Data

We load the PJME hourly dataset and examine its basic properties, such as shape, data types, and missing values. We visualize the energy usage over time to identify trends and patterns.

## Feature Creation

We create additional features from the datetime index, including hour, day of week, month, quarter, year, and day of year. These features provide additional information that may improve the predictive performance of our model.

## Analysis

We conduct exploratory data analysis (EDA) to understand the relationships between different features and energy usage. We use box plots to visualize energy usage by hour, month, and quarter, identifying any seasonal or hourly patterns.

## Modeling

We split the dataset into training and test sets and build an XGBoost regression model using the training data. We evaluate the model's performance on the test set using mean squared error (MSE) as the evaluation metric.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
