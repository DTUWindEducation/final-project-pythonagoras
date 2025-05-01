import sys
sys.path.append("src")

from wind_power_forecast.compute_error import compute_errors

# Test values for comparison
y_real = [0.2, 0.3, 0.25, 0.4]
y_pred = [0.25, 0.28, 0.22, 0.35]

# Call the function
errors = compute_errors(y_real, y_pred)

# Show the results
print(errors)
