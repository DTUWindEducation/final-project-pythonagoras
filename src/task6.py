"""
This module implements a Support Vector Regression (SVR) model to predict
one-hour-ahead power output
based on wind speed, wind direction, and temperature features.
"""

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import pandas as pd


def svm_forecast(df):
    """
    Trains a Support Vector Regression (SVR) model to predict one-hour-ahead power
    output.

    Parameters:
        df (DataFrame): Dataset with features and 'Power' column.

    Returns:
        y_test (Series), y_pred (Series)
    """
    df = df.copy()
    df["Target"] = df["Power"].shift(-1)
    df.dropna(inplace=True)

    # Input variables
    x = df[["windspeed_100m", "winddirection_100m", "temperature_2m"]]
    y = df["Target"]

    # Split into train and test
    split = int(0.8 * len(df))
    x_train, x_test = x.iloc[:split], x.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # Normalize features
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    # Train SVR model
    model = SVR(kernel="rbf", C=10, epsilon=0.01)
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)

    return y_test.reset_index(drop=True), pd.Series(y_pred)
