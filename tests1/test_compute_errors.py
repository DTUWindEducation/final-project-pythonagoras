import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import sys
print("\n".join(sys.path))

from src.compute_errors import compute_errors
import numpy as np
import pytest

def test_compute_errors():
    # Mock data
    y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_pred = np.array([1.1, 1.9, 3.2, 3.8, 5.1])

    # Expected values
    expected_mae = np.mean(np.abs(y_true - y_pred))
    expected_mse = np.mean((y_true - y_pred) ** 2)
    expected_rmse = np.sqrt(expected_mse)

    # Call the function
    errors = compute_errors(y_true, y_pred)

    # Assertions
    assert errors["MAE"] == expected_mae, f"Expected MAE: {expected_mae}, Got: {errors['MAE']}"
    assert errors["MSE"] == expected_mse, f"Expected MSE: {expected_mse}, Got: {errors['MSE']}"
    assert errors["RMSE"] == expected_rmse, f"Expected RMSE: {expected_rmse}, Got: {errors['RMSE']}"