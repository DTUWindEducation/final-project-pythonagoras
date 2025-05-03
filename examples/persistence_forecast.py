import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error


def get_persistence_forecast_data(file_path):
    """
    Prepares data for persistence forecasting.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        tuple: A tuple containing (time, y_true, y_pred, metrics_dict).
    """
    # Load the data
    df = pd.read_csv(file_path, parse_dates=["Time"])
    df = df.sort_values("Time")
    # Make persistence prediction: shift Power column forward by 1 row (1 hour)
    df["Predicted_Power"] = df["Power"].shift(1)

    # Drop the first row (since it has no prediction)
    df = df.dropna(subset=["Predicted_Power"])

    # Actual and predicted values
    y_true = df["Power"]
    y_pred = df["Predicted_Power"]

    # Calculate error metrics
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    metrics = {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse
    }

    return df["Time"], y_true, y_pred, metrics