"""
This module implements a persistence model to predict one-hour-ahead power output.
"""

import pandas as pd


def predict_persistence(df: pd.DataFrame, site_column: str) -> pd.Series:
    """
    Predict one-hour-ahead power output using the persistence model.

    Arguments:
        df (pd.DataFrame): Dataset.
        site_column (str): Name of the column for the selected site.

    Returns:
        pd.Series: Predicted power output.
    """
    return df[site_column].shift(1)  # shifts the column by one timestep
