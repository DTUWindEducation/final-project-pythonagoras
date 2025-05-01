import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("inputs/Location1.csv", parse_dates=["Time"])
df = df.sort_values("Time")

# Make persistence prediction: shift Power column forward by 1 row (1 hour)
df["Predicted_Power"] = df["Power"].shift(1)

# Drop the first row (since it has no prediction)
df = df.dropna(subset=["Predicted_Power"])

# Actual and predicted values
y_true = df["Power"]
y_pred = df["Predicted_Power"]

# Calculate error metrics
mse = mean_squared_error(y_true, y_pred)
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mse)

print("📈 Persistence Model Results:")
print(f"MAE  = {mae:.4f}")
print(f"MSE  = {mse:.4f}")
print(f"RMSE = {rmse:.4f}")

# Plot a slice of real vs predicted values
plt.figure(figsize=(12, 5))
plt.plot(df["Time"][:200], y_true[:200], label="Actual Power", color="green")
plt.plot(df["Time"][:200], y_pred[:200], label="Predicted (Persistence)", color="orange")
plt.title("Actual vs Persistence Forecast (First 200 hours)")
plt.xlabel("Time")
plt.ylabel("Power")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
