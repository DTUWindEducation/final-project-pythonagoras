# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pandas as pd
import numpy as np
from model_linear import linear_forecast

def test_linear_forecast():
    """
    Test the linear_forecast function.
    """
    # Create a mock DataFrame
    data = {
        "Power": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        "windspeed_100m": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "winddirection_100m": [180, 190, 200, 210, 220, 230, 240, 250, 260, 270],
        "temperature_2m": [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    }
    df = pd.DataFrame(data)

    # Call the function
    y_test, y_pred = linear_forecast(df)

    # Assertions
    assert len(y_test) == len(y_pred), "y_test and y_pred should have the same length."
    assert not y_pred.isnull().any(), "y_pred should not contain null values."
    assert isinstance(y_test, pd.Series), "y_test should be a pandas Series."
    assert isinstance(y_pred, pd.Series), "y_pred should be a pandas Series."

    # Check that the predictions are numeric
    assert np.issubdtype(y_pred.dtype, np.number), "y_pred should contain numeric values."