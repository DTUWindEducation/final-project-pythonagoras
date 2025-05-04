"""
This module provides functions to train and predict using an LSTM neural network
for time series forecasting.
"""

import os
import sys
from typing import Tuple
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential  # pylint: disable=E0401
from tensorflow.keras.layers import LSTM, Dense  # pylint: disable=E0401
from preprocessing import generate_lagged_features
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def split_train_test(
    x: np.ndarray, y: np.ndarray, test_ratio: float = 0.2
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Splits the dataset into training and testing sets in chronological order.

    Args:
        x (np.ndarray): Feature matrix.
        y (np.ndarray): Target vector.
        test_ratio (float): Proportion of data to use for testing (default is 0.2).

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: x_train, x_test, y_train, y_test.
    """
    split_index = int(len(x) * (1 - test_ratio))
    x_train, x_test = x[:split_index], x[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]
    return x_train, x_test, y_train, y_test


def train_and_predict_nn(
    data: pd.DataFrame, variable: str, forecast_horizon: int = 1
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Trains an LSTM neural network to predict 1-hour ahead wind power
    using the provided time series data.

    Args:
        data (pd.DataFrame): Input DataFrame containing time series data.
        variable (str): Target variable for prediction ("Power").
        forecast_horizon (int): Number of steps ahead to forecast
            (default is 1).

    Returns:
        Tuple[np.ndarray, np.ndarray]: Predicted values and actual target
        values.
    """
    lag_steps = 12
    x, y = generate_lagged_features(
        data, variable, lag_steps, forecast_horizon
    )

    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = split_train_test(x, y)

    model = Sequential([
        LSTM(50, activation="relu", input_shape=(x_train.shape[1], 1)),
        Dense(1),
    ])
    model.compile(optimizer="adam", loss="mse")
    model.fit(x_train, y_train, epochs=20, batch_size=32, verbose=0)

    predictions = model.predict(x_test)
    y_test = y_test[: len(predictions)]

    return predictions, y_test
