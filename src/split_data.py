import pandas as pd
# flake8: noqa

#task 4
def split_data(df, train_fraction=0.68): #0.68 specifies the % of the data will be used for training
    """
    Split the dataset into train and test sets.

    Args:
        df (pd.DataFrame): Full dataset.
        train_fraction (float): Fraction of data to use for training.

    Returns:
        (pd.DataFrame, pd.DataFrame): (train_set, test_set)
    """
    n_train = int(len(df) * train_fraction) #defines how many rows will be used for training, 
    #converting the result to an integer
    train = df.iloc[:n_train] #Select the training set as the first portion of the data up to the split index
    test = df.iloc[n_train:] #Select the test set as the remaining portion of the data after the split index
    return train, test 
