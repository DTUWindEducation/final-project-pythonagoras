import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import numpy as np
import pandas as pd
import pytest
from src.preprocessing import generate_lagged_features, normalize_features

def test_generate_lagged_features():
    """
    Test the generate_lagged_features function.
    """
    # Create a mock DataFrame
    data = {
        "Power": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    }
    df = pd.DataFrame(data)

    # Call the function
    lag_steps = 3
    forecast_horizon = 1
    X, y = generate_lagged_features(df, variable="Power", lag_steps=lag_steps, forecast_horizon=forecast_horizon)

    # Assertions
    assert X.shape[1] == lag_steps, f"X should have {lag_steps} columns for lagged features."
    assert len(X) == len(y), "X and y should have the same number of rows."
    assert np.allclose(y, df["Power"].iloc[lag_steps + forecast_horizon - 1:].values), "y values are incorrect."

def test_generate_lagged_features_invalid_column():
    """
    Test the generate_lagged_features function with an invalid column.
    """
    # Create a mock DataFrame
    data = {
        "Temperature": [15, 16, 17, 18, 19]
    }
    df = pd.DataFrame(data)

    # Call the function with an invalid column
    with pytest.raises(KeyError, match="not found in axis"):
        generate_lagged_features(df, variable="Power", lag_steps=3, forecast_horizon=1)

def test_normalize_features():
    """
    Test the normalize_features function.
    """
    # Create a mock feature matrix
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Call the function
    X_scaled, scaler = normalize_features(X)

    # Assertions
    assert X_scaled.shape == X.shape, "The shape of X_scaled should match the input X."
    assert np.allclose(X_scaled.min(axis=0), 0), "The minimum value of each feature in X_scaled should be 0."
    assert np.allclose(X_scaled.max(axis=0), 1), "The maximum value of each feature in X_scaled should be 1."
    assert isinstance(scaler, type(MinMaxScaler())), "The scaler should be an instance of MinMaxScaler."