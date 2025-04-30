import sys
sys.path.append("src")

from wind_power_forecast.loader import load_site_data
from wind_power_forecast.model_linear import linear_forecast
from wind_power_forecast.compute_error import compute_errors

# 1. Cargar los datos
site = 1
df = load_site_data(site)

# 2. Modelo de regresión lineal
y_test, y_pred = linear_forecast(df)

# 3. Calcular errores
errors = compute_errors(y_test, y_pred)

# 4. Mostrar resultados
print(f"Resultados para el sitio {site}")
for k, v in errors.items():
    print(f"{k}: {v:.4f}")
