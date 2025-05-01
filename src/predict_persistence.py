import pandas as pd
# flake8: noqa


#task 5
def predict_persistence(df, site_column):
    """
    Predict one-hour-ahead power output using the persistence model.

    Arguments:
        df (pd.DataFrame): Dataset.
        site_column (str): Name of the column for the selected site.

    Returns:
        pd.Series: Predicted power output.
    """
    return df[site_column].shift(1) #shifts the column by one timestep


