import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pandas as pd
from src.split_data import split_data

def test_split_data():
    """
    Test the split_data function with a valid DataFrame.
    """
    # Create a mock DataFrame
    data = {
        "Power": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        "Temperature": [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    }
    df = pd.DataFrame(data)

    # Call the function
    train_fraction = 0.7
    train, test = split_data(df, train_fraction=train_fraction)

    # Assertions
    n_train = int(len(df) * train_fraction)
    assert len(train) == n_train, f"Train set should have {n_train} rows."
    assert len(test) == len(df) - n_train, f"Test set should have {len(df) - n_train} rows."
    assert train.iloc[-1].equals(df.iloc[n_train - 1]), "Last row of train set should match the split index."
    assert test.iloc[0].equals(df.iloc[n_train]), "First row of test set should match the split index."

def test_split_data_empty_dataframe():
    """
    Test the split_data function with an empty DataFrame.
    """
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Call the function
    train, test = split_data(df, train_fraction=0.7)

    # Assertions
    assert train.empty, "Train set should be empty for an empty DataFrame."
    assert test.empty, "Test set should be empty for an empty DataFrame."

def test_split_data_invalid_fraction():
    """
    Test the split_data function with an invalid train_fraction.
    """
    # Create a mock DataFrame
    data = {
        "Power": [0.1, 0.2, 0.3, 0.4, 0.5],
        "Temperature": [15, 16, 17, 18, 19],
    }
    df = pd.DataFrame(data)

    # Call the function with invalid fractions
    with pytest.raises(ValueError, match="train_fraction must be between 0 and 1"):
        split_data(df, train_fraction=1.5)

    with pytest.raises(ValueError, match="train_fraction must be between 0 and 1"):
        split_data(df, train_fraction=-0.5)