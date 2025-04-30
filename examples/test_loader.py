import sys
sys.path.append("src")  # Añadir esta línea

from wind_power_forecast.loader import load_site_data

df = load_site_data(1)
print(df.head())
