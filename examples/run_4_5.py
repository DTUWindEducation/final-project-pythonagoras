import sys
import os
# flake8: noqa

"""
The `sys` module provides access to variables and functions that interact with the Python runtime environment.
It allows manipulation of the Python interpreter's behavior, such as modifying the module search path (`sys.path`),
retrieving command-line arguments, and handling standard input/output streams.It is used to make sure Python can find
and import modules from your project's parent folder.
"""

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#__file__:contains the path to the current file (run_4_5.py)
#os.path.dirname(__file__):gets the directory that the current file is in (examples/)
#os.path.join(..., '..'):means "go one folder up": examples/ -> final-project-pythonagoras/
#sys.path.append(...):adds that parent folder to Python’s module search path


from src.datahandler import DataHandler
from src.split_data import split_data
from src.predict_persistence import predict_persistence
from sklearn.metrics import mean_squared_error


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

    mse = mean_squared_error(y_true, y_pred)
    print(f" Persistence model MSE on {site}: {mse:.4f}")

if __name__ == "__main__":
    main()
