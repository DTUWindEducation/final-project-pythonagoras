import sys
sys.path.append("src") 

from wind_power_forecast.loader import load_site_data

df = load_site_data(1)
print(df.head())
