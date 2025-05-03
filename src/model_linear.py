"""
This module provides a function to train a linear regression model for forecasting power output.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


def linear_forecast(df):
    """
    Trains a linear regression model to predict power output 1 hour ahead.

    Args:
        df (pd.DataFrame): Input DataFrame containing the features and target variable.

    Returns:
        Tuple[pd.Series, pd.Series]: Actual and predicted values for the test set.
    """
    # Create target column: power 1 hour ahead
    df = df.copy()
    df["Target"] = df["Power"].shift(-1)
    df.dropna(inplace=True)

    # Input variables
    x = df[["windspeed_100m", "winddirection_100m", "temperature_2m"]]
    y = df["Target"]

    # Split into training and test sets
    split = int(0.8 * len(df))
    x_train, x_test = x.iloc[:split], x.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # Train model
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    return y_test.reset_index(drop=True), pd.Series(y_pred)
