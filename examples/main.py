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
from src.task6 import svm_forecast
sys.path.append(os.path.join(os.path.dirname(__file__), 'examples'))
from persistence_forecast import get_persistence_forecast_data


# Ensure the 'outputs' folder exists
os.makedirs("outputs", exist_ok=True)


#Task 2 - Plot Power for Location 1
"""
The `sys` module provides access to variables and functions that interact with the Python runtime environment.
It allows manipulation of the Python interpreter's behavior, such as modifying the module search path (`sys.path`),
retrieving command-line arguments, and handling standard input/output streams.
"""

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


if __name__ == "__main__":
    # Task 5 - Predict-Persistence ML
    input_folder = "inputs"
    site = "Power"  # Prediction of one hour ahead power output

    # Call the Task 5 function
    y_true, y_pred, mse = predict_persistence_model(input_folder, site)  # Correct function call

    # Plot predictions vs actuals
    plt.figure(figsize=(10, 6))
    plt.plot(y_true.index, y_true.values, label="Actual")
    plt.plot(y_pred.index, y_pred.values, label="Predicted", linestyle="--")
    plt.legend()
    plt.title("Predicted vs Actual Power Output (Predict-Persistence)")
    plt.xlabel("Time")
    plt.ylabel("Power")

    # Ensure the 'outputs' folder exists
    os.makedirs("outputs", exist_ok=True)

    # Save the plot to the outputs folder
    plt.savefig("outputs/task5_predict_persistence_plot.png")
    print("Plot for Task 5 saved to outputs/task5_predict_persistence_plot.png")

    # Show the plot
    plt.show()

#Task 6 - SVM Forecast


if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv("inputs/Location1.csv")

    # Call the SVM forecast function
    y_test, y_pred = svm_forecast(df)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(y_test, label="Actual Power", color="blue", linewidth=2)
    plt.plot(y_pred, label="Predicted Power", color="orange", linestyle="--")
    plt.title("SVM Forecast: Actual vs Predicted Power")
    plt.xlabel("Time Step")
    plt.ylabel("Power")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the plot
    plt.savefig("outputs/task6_svm_forecast_plot.png")
    plt.show()

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






