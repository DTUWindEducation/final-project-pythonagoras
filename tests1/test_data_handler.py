import sys
import os
import pandas as pd
import pytest
from src.datahandler import DataHandler
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



@pytest.fixture
def mock_input_folder(tmp_path):
    """
    Creates a temporary folder with mock CSV files for testing.
    """
    # Create mock data
    data1 = {
        "Time": ["2025-01-01 00:00", "2025-01-01 01:00", "2025-01-01 02:00"],
        "Power": [0.1, 0.2, 0.3],
        "Temperature": [15, 16, 17],
    }
    data2 = {
        "Time": ["2025-01-02 00:00", "2025-01-02 01:00", "2025-01-02 02:00"],
        "Power": [0.4, 0.5, 0.6],
        "Temperature": [18, 19, 20],
    }

    # Save mock data to temporary CSV files
    file1 = tmp_path / "mock_data1.csv"
    file2 = tmp_path / "mock_data2.csv"
    pd.DataFrame(data1).to_csv(file1, index=False)
    pd.DataFrame(data2).to_csv(file2, index=False)
    return tmp_path


def test_load_all_csv_files(mock_input_folder):
    """
    Test the _load_all_csv_files method.
    """
    handler = DataHandler(input_folder=mock_input_folder)
    assert len(handler.data) == 2, "Should load 2 CSV files"
    assert "mock_data1.csv" in handler.data, "mock_data1.csv should be loaded"
    assert "mock_data2.csv" in handler.data, "mock_data2.csv should be loaded"


def test_load_csv(mock_input_folder):
    """
    Test the load_csv method.
    """
    handler = DataHandler(input_folder=mock_input_folder)
    data = handler.load_csv("mock_data1.csv")
    assert isinstance(data, pd.DataFrame), "The returned object should be a pandas DataFrame"
    assert "Power" in data.columns, "The DataFrame should contain the 'Power' column"


def test_load_csv_file_not_found(mock_input_folder):
    """
    Test the load_csv method with a non-existent file.
    """
    handler = DataHandler(input_folder=mock_input_folder)
    with pytest.raises(ValueError, match="File non_existent.csv not found in"):
        handler.load_csv("non_existent.csv")


def test_plot_variable(mock_input_folder):
    """
    Test the plot_variable method.
    """
    handler = DataHandler(input_folder=mock_input_folder)
    # Ensure no exceptions are raised during plotting
    handler.plot_variable("mock_data1.csv", "Power", start_idx=0, end_idx=2)


def test_plot_variable_missing_column(mock_input_folder):
    """
    Test the plot_variable method with a missing column.
    """
    handler = DataHandler(input_folder=mock_input_folder)
    with pytest.raises(ValueError, match="Column 'NonExistentColumn' not found in mock_data1.csv"):
        handler.plot_variable("mock_data1.csv", "NonExistentColumn")