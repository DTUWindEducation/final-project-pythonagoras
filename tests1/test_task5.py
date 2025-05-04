import os
import pandas as pd
import pytest
from sklearn.metrics import mean_squared_error
from src.task5 import predict_persistence_model
from src.datahandler import DataHandler
from src.split_data import split_data
from src.predict_persistence import predict_persistence


@pytest.fixture
def mock_data_folder(tmp_path):
    """
    Creates a temporary folder with mock CSV data for testing.
    """
    # Create a temporary folder
    folder = tmp_path / "data"
    folder.mkdir()

    # Create a mock CSV file
    data = {
        "Power": [100, 110, 120, 130, 140],
        "windspeed_100m": [5, 6, 7, 8, 9],
        "winddirection_100m": [180, 190, 200, 210, 220],
        "temperature_2m": [15, 16, 17, 18, 19],
    }
    df = pd.DataFrame(data)
    csv_path = folder / "Location1.csv"
    df.to_csv(csv_path, index=False)

    return folder


def test_predict_persistence_model(mock_data_folder):
    """
    Tests the predict_persistence_model function.
    """
    # Run the persistence model
    y_true, y_pred, mse = predict_persistence_model(
        input_folder=str(mock_data_folder), site="Power"
    )

    # Assert that the outputs are correct
    assert len(y_true) == len(y_pred), "y_true and y_pred lengths do not match"
    assert mse >= 0, "MSE should be non-negative"

    # Compute expected MSE manually
    expected_y_true = pd.Series([110, 120, 130, 140])
    expected_y_pred = pd.Series([100, 110, 120, 130])
    expected_mse = mean_squared_error(expected_y_true, expected_y_pred)

    assert pytest.approx(mse, rel=1e-3) == expected_mse, "MSE does not match expected value"