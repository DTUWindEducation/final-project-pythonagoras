import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from typing import Tuple

def generate_lagged_features(data: pd.DataFrame, variable: str, lag_steps: int, forecast_horizon: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates lagged features for a time-series dataset.

    Args:
        data (pd.DataFrame): Input DataFrame containing time-series data.
        variable (str): Target variable for which lagged features are generated.
        lag_steps (int): Number of lagged time steps to include as features.
        forecast_horizon (int): Number of steps ahead to forecast (default is 1).

    Returns:
        Tuple[np.ndarray, np.ndarray]: Feature matrix (X) and target vector (y).
    """
    lagged_data = data.copy()
    for i in range(1, lag_steps + 1):
        lagged_data[f'{variable}_lag_{i}'] = lagged_data[variable].shift(i)

    # Drop rows with NaN values caused by lagging
    lagged_data = lagged_data.dropna()

    # Define features (X) and target (y)
    X = lagged_data[[f'{variable}_lag_{i}' for i in range(1, lag_steps + 1)]].values
    y = lagged_data[variable].shift(-forecast_horizon).dropna().values

    # Align X and y
    X = X[:len(y)]

    return X, y

def normalize_features(X: np.ndarray) -> Tuple[np.ndarray, MinMaxScaler]:
    """
    Normalizes features using MinMaxScaler.

    Args:
        X (np.ndarray): Feature matrix to be normalized.

    Returns:
        Tuple[np.ndarray, MinMaxScaler]: Normalized feature matrix and the scaler object.
    """
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler