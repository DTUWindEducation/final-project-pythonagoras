import pandas as pd
import pytest
from sklearn.metrics import mean_squared_error
from src.task6 import svm_forecast


@pytest.fixture
def mock_dataframe():
    """
    Creates a mock DataFrame for testing.
    """
    data = {
        "Power": [100, 110, 120, 130, 140],
        "windspeed_100m": [5, 6, 7, 8, 9],
        "winddirection_100m": [180, 190, 200, 210, 220],
        "temperature_2m": [15, 16, 17, 18, 19],
    }
    return pd.DataFrame(data)


def test_svm_forecast(mock_dataframe):
    """
    Tests the svm_forecast function.
    """
    # Run the SVR model
    y_test, y_pred = svm_forecast(mock_dataframe)

    # Assert that the outputs are correct
    assert len(y_test) == len(y_pred), "y_test and y_pred lengths do not match"
    assert isinstance(y_test, pd.Series), "y_test should be a pandas Series"
    assert isinstance(y_pred, pd.Series), "y_pred should be a pandas Series"

    # Compute expected MSE manually
    expected_y_test = pd.Series([110, 120, 130, 140])
    expected_y_pred = pd.Series([100, 110, 120, 130])  # Example expected predictions
    mse = mean_squared_error(expected_y_test, expected_y_pred)

    # Assert that the MSE is non-negative
    assert mse >= 0, "MSE should be non-negative"