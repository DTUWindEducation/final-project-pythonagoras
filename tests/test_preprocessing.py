# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
import pandas as pd
import numpy as np
from preprocessing import generate_lagged_features, normalize_features


@pytest.fixture
def mock_dataframe():
    """
    Creates a mock DataFrame for testing.
    """
    data = {
        "Power": [100, 110, 120, 130, 140, 150, 160],
        "windspeed_100m": [5, 6, 7, 8, 9, 10, 11],
        "temperature_2m": [15, 16, 17, 18, 19, 20, 21],
    }
    return pd.DataFrame(data)


def test_generate_lagged_features(mock_dataframe):
    """
    Tests the generate_lagged_features function.
    """
    x, y = generate_lagged_features(mock_dataframe, variable="Power", lag_steps=2, forecast_horizon=1)

    # Assertions
    assert x.shape[1] == 2, "The number of lagged features should match the lag_steps."
    assert len(x) == len(y), "The length of x and y should be the same."
    assert isinstance(x, np.ndarray), "x should be a numpy array."
    assert isinstance(y, np.ndarray), "y should be a numpy array."


def test_generate_lagged_features_invalid_column(mock_dataframe):
    """
    Tests the generate_lagged_features function with an invalid column.
    """
    with pytest.raises(KeyError, match=".*NonExistentColumn.*"):
        generate_lagged_features(mock_dataframe, variable="NonExistentColumn", lag_steps=2)


def test_normalize_features():
    """
    Tests the normalize_features function.
    """
    x = np.array([[1, 2], [3, 4], [5, 6]])
    x_scaled, scaler = normalize_features(x)

    # Assertions
    assert x_scaled.min() == 0, "The minimum value of the scaled features should be 0."
    assert x_scaled.max() == 1, "The maximum value of the scaled features should be 1."
    assert isinstance(x_scaled, np.ndarray), "x_scaled should be a numpy array."
    # assert isinstance(scaler, MinMaxScaler), "scaler should be an instance of MinMaxScaler."