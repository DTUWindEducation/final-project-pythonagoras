import pandas as pd
import numpy as np
from inputs.datahandler import DataHandler
from src.model_nn import train_and_predict_nn
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Load data
data_handler = DataHandler()
data = data_handler.load_csv("inputs/Location1.csv")

# Train and predict
predictions, actuals = train_and_predict_nn(data, variable="Power")

# Compute error metrics
mse = mean_squared_error(actuals, predictions)
mae = mean_absolute_error(actuals, predictions)
rmse = np.sqrt(mse)

print(f"MSE: {mse}, MAE: {mae}, RMSE: {rmse}")

# Plot predictions vs actuals
plt.figure(figsize=(10, 6))
plt.plot(actuals, label="Actual")
plt.plot(predictions, label="Predicted")
plt.legend()
plt.title("Predicted vs Actual Power Output")
plt.xlabel("Time")
plt.ylabel("Power")
plt.show()