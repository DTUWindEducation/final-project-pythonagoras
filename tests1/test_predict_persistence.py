import pandas as pd
import pytest
from src.predict_persistence import predict_persistence

def test_predict_persistence():
    """
    Test the predict_persistence function.
    """
    # Create a mock DataFrame
    data = {
        "Power": [0.1, 0.2, 0.3, 0.4, 0.5],
        "Temperature": [15, 16, 17, 18, 19],
    }
    df = pd.DataFrame(data)

    # Call the function
    predictions = predict_persistence(df, "Power")

    # Assertions
    assert isinstance(predictions, pd.Series), "The returned object should be a pandas Series."
    assert len(predictions) == len(df), "The length of predictions should match the input DataFrame."
    assert predictions.iloc[1] == df["Power"].iloc[0], "The second prediction should match the first value of the column."
    assert pd.isnull(predictions.iloc[0]), "The first prediction should be NaN due to the shift."

def test_predict_persistence_invalid_column():
    """
    Test the predict_persistence function with an invalid column name.
    """
    # Create a mock DataFrame
    data = {
        "Power": [0.1, 0.2, 0.3, 0.4, 0.5],
        "Temperature": [15, 16, 17, 18, 19],
    }
    df = pd.DataFrame(data)

    # Call the function with an invalid column
    with pytest.raises(KeyError, match="not in index"):
        predict_persistence(df, "NonExistentColumn")