import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def linear_forecast(df):
    """
    Entrena modelo de regresión lineal para predecir la potencia una hora adelante.
    Devuelve y_test, y_pred
    """
    # Crear columna objetivo: potencia 1 hora adelante
    df = df.copy()
    df["Target"] = df["Power"].shift(-1)
    df.dropna(inplace=True)

    # Input variables
    X = df[["windspeed_100m", "winddirection_100m", "temperature_2m"]]
    y = df["Target"]

    # Separar datos en entrenamiento y prueba
    split = int(0.8 * len(df))
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # Modelo
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return y_test.reset_index(drop=True), pd.Series(y_pred)
