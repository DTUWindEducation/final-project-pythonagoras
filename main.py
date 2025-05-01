# flake8: noqa
import sys
import os # Provides access to Python runtime environment, including the module search path (sys.path)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from src.task3 import simulate_forecast
from src.task3 import evaluate_forecast
from src.datahandler import DataHandler
from src.split_data import split_data
from src.predict_persistence import predict_persistence
from src.model_linear import linear_forecast
from src.compute_errors import compute_errors



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


# Add the 'inputs' folder to Python's module search path
from src.datahandler import DataHandler

# Appends the 'inputs' directory to the system path so Python can find and import modules from it.

if __name__ == "__main__": # Checks if the script is being run directly (not imported
    handler = DataHandler("inputs") # Creates an instance of the DataHandler class, which loads CSV files from the 'inputs' folder.
    handler.plot_variable("Location1.csv", "Power", 0, 200) # Calls the plot_variable method to plot the "Power" variable from "Location1" CSV file, slicing the first 200 rows.

#Task 3 - Compute mse, mae, rmse

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
    plt.title("Predicted vs Actual Power Output")
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

