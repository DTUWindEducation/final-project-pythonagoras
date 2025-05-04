from sklearn.metrics import mean_squared_error
from src.datahandler import DataHandler
from src.split_data import split_data
from src.predict_persistence import predict_persistence


def predict_persistence_model(input_folder: str, site: str):
    """
    Runs the Predict-Persistence model for one-hour-ahead power output.

    Args:
        input_folder (str): Path to the folder containing input CSV files.
        site (str): Column name for the target variable (e.g., "Power").

    Returns:
        tuple: (y_true, y_pred, mse)
    """
    handler = DataHandler(input_folder)
    print("Loaded files:", handler.data.keys())

    df = handler.data["Location1.csv"]
    print("DataFrame shape:", df.shape)
    print("Columns:", df.columns.tolist())

    train, test = split_data(df)
    y_true = test[site]
    y_pred = predict_persistence(test, site)

    # Align the actual and predicted values
    y_true = y_true.iloc[1:]
    y_pred = y_pred.iloc[1:]

    # Compute the Mean Squared Error
    mse = mean_squared_error(y_true, y_pred)
    print(f"Persistence model MSE on {site}: {mse:.4f}")

    return y_true, y_pred, mse
