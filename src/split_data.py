"""
This module provides a function to split a dataset into training and testing sets.
"""

import pandas as pd


def split_data(
    df: pd.DataFrame, train_fraction: float = 0.68
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split the dataset into train and test sets.

    Args:
        df (pd.DataFrame): Full dataset.
        train_fraction (float): Fraction of data to use for training.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: (train_set, test_set)
    """
    n_train = int(len(df) * train_fraction)  # Calculate the number of rows for training
    train = df.iloc[:n_train]  # Select the training set
    test = df.iloc[n_train:]  # Select the test set
    return train, test
