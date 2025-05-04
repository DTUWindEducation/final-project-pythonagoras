# import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pandas as pd
import numpy as np
from features import add_wind_direction_features, save_model, load_model

def test_add_wind_direction_features():
    """
    Test the add_wind_direction_features function.
    """
    # Create a mock DataFrame
    data = {
        "wind_direction": [0, 90, 180, 270, 360]
    }
    df = pd.DataFrame(data)

    # Call the function
    df = add_wind_direction_features(df, "wind_direction")

    # Assertions
    assert "wind_direction_sin" in df.columns, "The DataFrame should contain the 'wind_direction_sin' column."
    assert "wind_direction_cos" in df.columns, "The DataFrame should contain the 'wind_direction_cos' column."

    # Check sine and cosine values
    expected_sin = np.sin(np.deg2rad(data["wind_direction"]))
    expected_cos = np.cos(np.deg2rad(data["wind_direction"]))
    assert np.allclose(df["wind_direction_sin"], expected_sin), "Sine values are incorrect."
    assert np.allclose(df["wind_direction_cos"], expected_cos), "Cosine values are incorrect."

def test_save_and_load_model(tmp_path):
    """
    Test the save_model and load_model functions.
    """
    # Create a mock model (dictionary for simplicity)
    model = {"key": "value"}

    # Define file path
    file_path = tmp_path / "mock_model.pkl"

    # Save the model
    save_model(model, file_path)

    # Ensure the file exists
    assert os.path.exists(file_path), "The model file should exist after saving."

    # Load the model
    loaded_model = load_model(file_path)

    # Assertions
    assert loaded_model == model, "The loaded model should match the saved model."