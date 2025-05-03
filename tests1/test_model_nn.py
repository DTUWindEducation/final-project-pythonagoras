import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import numpy as np
import pandas as pd
import pytest
from src.model_nn import split_train_test, train_and_predict_nn

@pytest.fixture
def mock_data():
    """
    Creates a mock DataFrame for testing.
    """
    data = {
        "Power": np.random.rand(100),  # Random power values
        "windspeed_100m": np.random.rand(100),
        "winddirection_100m": np.random.rand(100),
        "temperature_2m": np.random.rand(100),
    }
    return pd.DataFrame(data)

def test_split_train_test():
    """
    Test the split_train_test function.
    """
    # Mock data
    X = np.random.rand(100, 10)  # 100 samples, 10 features
    y = np.random.rand(100)

    # Call the function
    X_train, X_test, y_train, y_test = split_train_test(X, y, test_ratio=0.2)

    # Assertions
    assert len(X_train) == 80, "80% of the data should be in the training set."
    assert len(X_test) == 20, "20% of the data should be in the testing set."
    assert len(y_train) == 80, "80% of the target should be in the training set."
    assert len(y_test) == 20, "20% of the target should be in the testing set."


def test_train_and_predict_nn(mock_data):
    """
    Test the train_and_predict_nn function.
    """
    # Call the function
    predictions, y_test = train_and_predict_nn(mock_data, variable="Power", forecast_horizon=1)

    # Assertions
    assert len(predictions) == len(y_test), "Predictions and y_test should have the same length."
    assert isinstance(predictions, np.ndarray), "Predictions should be a numpy array."
    assert isinstance(y_test, np.ndarray), "y_test should be a numpy array."
    assert predictions.ndim == 2, "Predictions should be a 2D array (batch size, 1)."
    assert y_test.ndim == 1, "y_test should be a 1D array."


def test_train_and_predict_nn_invalid_column(mock_data):
    """
    Test the train_and_predict_nn function with an invalid column.
    """
    with pytest.raises(KeyError, match="not found in axis"):
        train_and_predict_nn(mock_data, variable="NonExistentColumn", forecast_horizon=1)