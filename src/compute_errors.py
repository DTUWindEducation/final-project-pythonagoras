from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def compute_errors(y_true, y_pred):
    """
    Calculates MAE, MSE y RMSE with real and predicted values 

    Parameters:
        y_true (array-like): Real values
        y_pred (array-like): Predicted values

    Returns:
        dict: {'MAE': ..., 'MSE': ..., 'RMSE': ...}
    """
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse
    }
