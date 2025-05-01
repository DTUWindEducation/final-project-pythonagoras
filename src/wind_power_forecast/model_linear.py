import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def linear_forecast(df):
    """
    Trains a linear regression model to predict power output 1 hour ahead
    
    Returns:
        y_test, y_pred
    """
    # Create target column: power 1 hour ahead
    df = df.copy()
    df["Target"] = df["Power"].shift(-1)
    df.dropna(inplace=True)

    # Input variables
    X = df[["windspeed_100m", "winddirection_100m", "temperature_2m"]]
    y = df["Target"]

    # Split into training and test sets
    split = int(0.8 * len(df))
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return y_test.reset_index(drop=True), pd.Series(y_pred)

