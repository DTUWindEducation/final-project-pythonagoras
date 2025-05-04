# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pandas as pd
import numpy as np
import pytest
from task3 import simulate_forecast, evaluate_forecast


@pytest.fixture
def mock_series():
    """
    Creates a mock time series for testing.
    """
    return pd.Series([100, 110, 120, 130, 140])


def test_simulate_forecast(mock_series):
    """
    Tests the simulate_forecast function.
    """
    forecasted_series = simulate_forecast(mock_series, noise_std=0.2)
    assert len(forecasted_series) == len(mock_series), \
        (
            "Forecasted series length does not match the original series"
        )
    assert not forecasted_series.equals(mock_series), "Forecasted series should not be identical to the original series"


def test_evaluate_forecast(mock_series):
    """
    Tests the evaluate_forecast function.
    """
    # Simulate a forecast
    forecasted_series = simulate_forecast(mock_series, noise_std=0.2)

    # Evaluate the forecast
    mse, mae, rmse = evaluate_forecast(mock_series, forecasted_series)

    # Assert that the metrics are non-negative
    assert mse >= 0, "MSE should be non-negative"
    assert mae >= 0, "MAE should be non-negative"
    assert rmse >= 0, "RMSE should be non-negative"