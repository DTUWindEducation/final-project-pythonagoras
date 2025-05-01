import numpy as np
import pandas as pd
from src.preprocessing import generate_lagged_features,normalize_features # Custom module for generating lagged features
from src.preprocessing import normalize_features # Custom module for normalizing features
from sklearn.preprocessing import MinMaxScaler # For scaling features
from tensorflow.keras.models import Sequential # For building the neural network model
from tensorflow.keras.layers import LSTM, Dense # For LSTM and Dense layers
from typing import Tuple # For type hinting

def split_train_test(X: np.ndarray, y: np.ndarray, test_ratio: float = 0.2) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Splits the dataset into training and testing sets in chronological order.

    Args:
        X (np.ndarray): Feature matrix.
        y (np.ndarray): Target vector.
        test_ratio (float): Proportion of data to use for testing (default is 0.2).

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: X_train, X_test, y_train, y_test.
    """
    split_index = int(len(X) * (1 - test_ratio)) # Calculate the split index
    X_train, X_test = X[:split_index], X[split_index:] # Split the features into training and testing sets
    y_train, y_test = y[:split_index], y[split_index:] # Split the target into training and testing sets
    return X_train, X_test, y_train, y_test # Return the training and testing sets

def train_and_predict_nn(data: pd.DataFrame, variable: str, forecast_horizon: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Trains an LSTM neural network to predict 1-hour ahead wind power.

    Args:
        data (pd.DataFrame): Input DataFrame containing time series data.
        variable (str): Target variable for prediction (e.g., "Power").
        forecast_horizon (int): Number of steps ahead to forecast (default is 1).

    Returns:
        Tuple[np.ndarray, np.ndarray]: Predicted values and actual target values.
    """
    # Generate lagged features
    lag_steps = 12  # Example: Use past 12 time steps as input
    X, y = generate_lagged_features(data, variable, lag_steps, forecast_horizon)

    # Normalize features
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    # Build LSTM model
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)), # LSTM layer
        Dense(1) # Output layer
    ])
    model.compile(optimizer='adam', loss='mse')

    # Train the model
    model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=0)

    # Make predictions
    predictions = model.predict(X_test)

    # Align y_test with predictions
    y_test = y_test[:len(predictions)]

    return predictions, y_test