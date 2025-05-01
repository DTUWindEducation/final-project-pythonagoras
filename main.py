import sys
sys.path.append("src")

from wind_power_forecast.loader import load_site_data
from wind_power_forecast.model_linear import linear_forecast
from wind_power_forecast.compute_error import compute_errors

# 1. Load the data
site = 1
df = load_site_data(site)

# 2. Linear regression model
y_test, y_pred = linear_forecast(df)

# 3. Calculate errors
errors = compute_errors(y_test, y_pred)

# 4. Show results
print(f"Results for site {site}")
for k, v in errors.items():
    print(f"{k}: {v:.4f}")
