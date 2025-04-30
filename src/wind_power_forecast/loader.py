# src/wind_power_forecast/loader.py

import pandas as pd

def load_site_data(site_index):
    """
    Carga el dataset CSV correspondiente a un sitio específico.
    
    Parámetros:
        site_index (int): Número del site (1, 2, 3 or 4).
        
    Retorna:
        pandas.DataFrame: DataFrame con los datos cargados y ordenados por fecha.
    """
    # Construir el path al archivo
    path = f"inputs/Location{site_index}.csv"
    
    # Cargar el CSV
    df = pd.read_csv(path, parse_dates=["Time"])
    
    # Ordenar por tiempo
    df = df.sort_values("Time")
    
    return df
