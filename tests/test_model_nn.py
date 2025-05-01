import pytest
import pandas as pd
from src.model_nn import train_and_predict_nn

def test_train_and_predict_nn():
    # Load a small sample of data
    data = pd.read_csv("inputs/Location1.csv").head(100)

    # Call the function
    predictions, actuals = train_and_predict_nn(data, variable="Power")

    # Assert shapes match
    assert predictions.shape == actuals.shape, "Prediction and actual shapes do not match."

    # Assert no exceptions occurred
    assert predictions is not None and actuals is not None