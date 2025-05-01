import numpy as np
import pickle

def add_wind_direction_features(df, column_name):
    """
    Adds sine and cosine columns for a given wind direction in degrees
    
    Parameters:
        df (DataFrame): table containing the wind direction column
        column_name (str): name of the column with wind direction in degrees

    Returns:
        DataFrame with two new columns: *_sin and *_cos
    """
    radians = np.deg2rad(df[column_name])
    df[column_name + "_sin"] = np.sin(radians)
    df[column_name + "_cos"] = np.cos(radians)
    return df


def save_model(model, filename):
    """
    Saves a trained model to a file using pickle
    """
    with open(filename, 'wb') as f:
        pickle.dump(model, f)


def load_model(filename):
    """
    Loads a previously saved model using pickle
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)
