import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
# flake8: noqa

"""
    Simulates a forecast by adding Gaussian noise to the real series.
    """
def simulate_forecast(real_series, noise_std=0.2):  #noise_stg=standard_diviation=0.2
    #give random values from a normal (Gaussian) distribution
    noise = np.random.normal(0, noise_std, size=len(real_series)) #0=mean
    return real_series + noise

"""
    Computes MSE, MAE, and RMSE between real and forecasted series.
    """
def evaluate_forecast(real_series, predicted_series):
    mse = mean_squared_error(real_series, predicted_series)
    mae = mean_absolute_error(real_series, predicted_series)
    rmse = np.sqrt(mse)
    return mse, mae, rmse

if __name__ == "__main__":
    # 1. Load real data from Location1.csv
    df = pd.read_csv("inputs/Location1.csv")

    # 2. Select the variable you want (e.g., 'Power' or 'wind_speed_100m')
    variable_name = "Power"  # Change this to "wind_speed_100m" if you want
    real_series = df[variable_name].dropna()  # Drop NaNs if any

    # 3. Simulate a forecast
    predicted_series = simulate_forecast(real_series)

    # 4. Evaluate the forecast
    mse, mae, rmse = evaluate_forecast(real_series, predicted_series)

    # 5. Print the results
    print(f"Results for {variable_name}:")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")