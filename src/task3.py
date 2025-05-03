"""
This module provides functions for simulating and evaluating forecasts for time series data.
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error


def simulate_forecast(actual_series, noise_std=0.2):
    """
    Simulates a forecast by adding Gaussian noise to the real series.

    Args:
        actual_series (pd.Series): The real time series data.
        noise_std (float): Standard deviation of the Gaussian noise.

    Returns:
        pd.Series: Simulated forecasted series.
    """
    # Generate random values from a normal (Gaussian) distribution
    noise = np.random.normal(0, noise_std, size=len(actual_series))  # 0=mean
    return actual_series + noise


def evaluate_forecast(actual_series, forecasted_series):
    """
    Evaluates the forecast using MSE, MAE, and RMSE.

    Args:
        actual_series (pd.Series): The real time series data.
        forecasted_series (pd.Series): The forecasted time series data.

    Returns:
        tuple: (MSE, MAE, RMSE)
    """
    mse = mean_squared_error(actual_series, forecasted_series)
    mae = mean_absolute_error(actual_series, forecasted_series)
    rmse = np.sqrt(mse)
    return mse, mae, rmse


if __name__ == "__main__":
    # 1. Load real data from Location1.csv
    df = pd.read_csv("inputs/Location1.csv")

    # 2. Select the variable you want (e.g., 'Power' or 'wind_speed_100m')
    VARIABLE_NAME = "Power"  # Change this to "wind_speed_100m" if you want
    actual_series = df[VARIABLE_NAME].dropna()  # Drop NaNs if any

    # 3. Simulate a forecast
    forecasted_series = simulate_forecast(actual_series)

    # 4. Evaluate the forecast
    mse, mae, rmse = evaluate_forecast(actual_series, forecasted_series)

    # 5. Print the results
    print(f"Results for {VARIABLE_NAME}:")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")