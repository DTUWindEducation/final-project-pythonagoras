import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "inputs/Location1.csv"  # Adjust if your path is different
df = pd.read_csv(file_path, parse_dates=["Time"])

# Make sure the time is sorted
df = df.sort_values("Time")

# Plot wind speed and power over time
plt.figure(figsize=(12, 5))

# Subplot 1: Wind speed at 100m
plt.subplot(1, 2, 1)
plt.plot(df["Time"], df["windspeed_100m"], color='blue')
plt.title("Wind Speed at 100m")
plt.xlabel("Time")
plt.ylabel("Wind Speed (m/s)")
plt.grid(True)

# Subplot 2: Normalized power
plt.subplot(1, 2, 2)
plt.plot(df["Time"], df["Power"], color='green')
plt.title("Normalized Power Output")
plt.xlabel("Time")
plt.ylabel("Power (0 to 1)")
plt.grid(True)

plt.tight_layout()
plt.show()

