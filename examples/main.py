# flake8: noqa
import sys
import os # Provides access to Python runtime environment, including the module search path (sys.path)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sklearn.metrics import mean_squared_error, mean_absolute_error
from src.task3 import simulate_forecast
from src.task3 import evaluate_forecast
from src.datahandler import DataHandler
from src.split_data import split_data
from src.predict_persistence import predict_persistence
from src.model_linear import linear_forecast
from src.compute_errors import compute_errors
from src.datahandler import DataHandler
from src.model_nn import train_and_predict_nn
sys.path.append(os.path.join(os.path.dirname(__file__), 'examples'))
from persistence_forecast import get_persistence_forecast_data


# Ensure the 'outputs' folder exists
os.makedirs("outputs", exist_ok=True)

# Task 7 - Function to Plot Predicted vs Actual Power Output
def plot_predicted_vs_actual(y_true, y_pred, title="Predicted vs Actual Power Output"):
    """
    Plots the predicted vs real power values and saves the plot to the outputs folder.

    Parameters:
        y_true (array-like): Real power values
        y_pred (array-like): Predicted power values
        title (str): Title of the plot
    """
      # Flatten y_true and y_pred if they are 2D arrays
    if len(y_true.shape) > 1:
        y_true = y_true.ravel()
    if len(y_pred.shape) > 1:
        y_pred = y_pred.ravel()
     # Convert to pandas.Series if necessary
    y_true = pd.Series(y_true)
    y_pred = pd.Series(y_pred)

    plt.figure(figsize=(10, 5))
    plt.plot(y_true.reset_index(drop=True), label="Actual Power", linewidth=2, color="blue")
    plt.plot(y_pred.reset_index(drop=True), label="Predicted Power", linestyle="--", color="orange")
    plt.xlabel("Time Step")
    plt.ylabel("Power (normalized)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Ensure the 'outputs' folder exists
    os.makedirs("outputs", exist_ok=True)

    # Save the plot to the outputs folder
    output_filename = f"outputs/{title.replace(' ', '_').lower()}.png"
    plt.savefig(output_filename)
    print(f"Plot saved to {output_filename}")

    # Show the plot
    plt.show()



#Task 2 - Plot Power for Location 1
"""
The `sys` module provides access to variables and functions that interact with the Python runtime environment.
It allows manipulation of the Python interpreter's behavior, such as modifying the module search path (`sys.path`),
retrieving command-line arguments, and handling standard input/output streams.
"""
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
#__file__:contains the path to the current file (run_4_5.py)
#os.path.dirname(__file__):gets the directory that the current file is in (examples/)
#os.path.join(..., '..'):means "go one folder up": examples/ -> final-project-pythonagoras/
#sys.path.append(...):adds that parent folder to Python’s module search path
# Appends the 'inputs' directory to the system path so Python can find and import modules from it.

# Task 2 - Plot Power for Location 1
if __name__ == "__main__":
    # Load the data
    file_path = "inputs/Location1.csv"
    data = pd.read_csv(file_path, parse_dates=["Time"])

    # Plot the "Power" variable
    plt.figure(figsize=(10, 6))
    plt.plot(data["Time"][:200], data["Power"][:200], label="Power", color="blue")
    plt.title("Power from Location1.csv")
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.legend()
    plt.grid(True)

    # Ensure the 'outputs' folder exists
    os.makedirs("outputs", exist_ok=True)

    # Save the plot to the outputs folder
    plt.savefig("outputs/task2_plot_power_location1.png")
    print("Plot for Task 2 saved to outputs/task2_plot_power_location1.png")

    # Show the plot
    plt.show()


# Task 2 - Plot Wind Speed and Power Over Time
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
plt.savefig("outputs/task2_wind_speed_power.png")  # Save the plot
plt.show()

#Task 3 Compute mse, maem rmse
if __name__ == "__main__":
    # 1. Load real data from Location1.csv
    df = pd.read_csv("inputs/Location1.csv")

    # 2. Select the variable you want (e.g., 'Power' or 'wind_speed_100m')
    variable_name = "Power"  # Change this to "wind_speed_100m" if you want
    real_series = df[variable_name].dropna()  # Drop NaNs if any

    # 3. Simulate a forecast
    predicted_series = simulate_forecast(real_series)

    # 4. Evaluate the forecast
    mse, mae, rmse = evaluate_forecast(real_series, predicted_series)

    # 5. Print the results
    print(f"Results for {variable_name}:")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

#Task 5 - Predict-Persistence ML
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():

    input_folder = "inputs"
    site = "Power"  # Prediction of one hour ahead power output

    handler = DataHandler(input_folder)
    print("Loaded files:", handler.data.keys())  # ✅ Checkpoint 2

    df = handler.data["Location1.csv"]
    print("DataFrame shape:", df.shape)
    print("Columns:", df.columns.tolist())  # ✅ Checkpoint 3

    train, test = split_data(df)
    y_true = test[site]
    y_pred = predict_persistence(test, site)

    y_true = y_true.iloc[1:]
    y_pred = y_pred.iloc[1:]

    from sklearn.metrics import mean_squared_error
    mse = mean_squared_error(y_true, y_pred)
    print(f" Persistence model MSE on {site}: {mse:.4f}")

    #Plot predictions vs actuals

    plt.figure(figsize=(10, 6))
    plt.plot(y_true.index, y_true.values, label="Actual")
    plt.plot(y_pred.index, y_pred.values, label="Predicted", linestyle="--")
    plt.legend()
    plt.title("Predicted vs Actual Power Output(Predict-Persistence)")
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.show()

if __name__ == "__main__":
    main()
#Task 6
sys.path.append("src")
# 1. Load the data
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
# 2. Linear regression model
y_test, y_pred = linear_forecast(df)
# 3. Calculate errors
errors = compute_errors(y_test, y_pred)
# 4. Show results
print(f"Results for site 1")
for k, v in errors.items():
    print(f"{k}: {v:.4f}")

# Task 6 - Neural Network Forecast

if __name__ == "__main__":
    print("\n--- Task 6: Neural Network Forecast ---")
    data_handler = DataHandler("inputs")  # Create an instance of DataHandler
    data = data_handler.load_csv("Location1.csv")  # Load the CSV file "Location1.csv" from the 'inputs' directory

    # Train and predict
    predictions, actuals = train_and_predict_nn(data, variable="Power")  # Call the function to train the model and get predictions

    # Compute error metrics
    mse = mean_squared_error(actuals, predictions)  # Mean Squared Error
    mae = mean_absolute_error(actuals, predictions)  # Mean Absolute Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error

    print(f"MSE: {mse}, MAE: {mae}, RMSE: {rmse}")  # Print the error metrics

    # Plot predictions vs actuals
    plt.figure(figsize=(10, 6))
    plt.plot(actuals, label="Actual")
    plt.plot(predictions, label="Predicted")
    plt.legend()
    plt.title("Predicted vs Actual Power Output (Neural Network)")
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.savefig("outputs/task6_nn_forecast.png")  # Save the plot
    plt.show()

    # Task 7
    print("\n--- Task 7: Plot Predicted vs Actual Power Output ---")
    plot_predicted_vs_actual(actuals, predictions, title="Task7 Predicted vs Actual Power Output")
    plt.show()





