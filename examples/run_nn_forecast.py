import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np # For numerical operations
from src.datahandler import DataHandler # Custom module for data handling
from src.model_nn import train_and_predict_nn # Custom module for training and predicting with neural networks
from sklearn.metrics import mean_squared_error, mean_absolute_error # For error metrics
import matplotlib.pyplot as plt # For plotting

def main():
    # Load data
    data_handler = DataHandler() # Create an instance of DataHandler
    data = data_handler.load_csv("Location1") # Load the CSV file "Location1.csv" from the 'inputs' directory

    # Train and predict
    predictions, actuals = train_and_predict_nn(data, variable="Power") # Call the function to train the model and get predictions

    # Compute error metrics
    mse = mean_squared_error(actuals, predictions) # Mean Squared Error
    mae = mean_absolute_error(actuals, predictions) # Mean Absolute Error
    rmse = np.sqrt(mse) # Root Mean Squared Error

    print(f"MSE: {mse}, MAE: {mae}, RMSE: {rmse}") # Print the error metrics

    # Plot predictions vs actuals
    plt.figure(figsize=(10, 6))
    plt.plot(actuals, label="Actual")
    plt.plot(predictions, label="Predicted")
    plt.legend()
    plt.title("Predicted vs Actual Power Output")
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.show()

if __name__ == "__main__": # Check if the script is being run directly
    main() # Call the main function to execute the script