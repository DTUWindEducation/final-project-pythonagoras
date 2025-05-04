# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pandas as pd
import pytest
from data_loader import load_and_plot_data

@pytest.fixture
def mock_csv_file(tmp_path):
    """
    Creates a temporary mock CSV file for testing.
    """
    data = {
        "Time": ["2025-01-01 00:00", "2025-01-01 01:00", "2025-01-01 02:00"],
        "Power": [0.1, 0.2, 0.3],
        "Temperature": [15, 16, 17],
    }
    df = pd.DataFrame(data)
    file_path = tmp_path / "mock_data.csv"
    df.to_csv(file_path, index=False)
    return file_path

def test_load_and_plot_data(mock_csv_file):
    """
    Test the load_and_plot_data function.
    """
    # Call the function
    data = load_and_plot_data(mock_csv_file, variable_name="Power", start_idx=0, end_idx=2)

    # Assertions
    assert isinstance(data, pd.DataFrame), "The returned object should be a pandas DataFrame."
    assert "Power" in data.columns, "The DataFrame should contain the 'Power' column."
    assert len(data) == 3, "The DataFrame should have 3 rows."

def test_load_and_plot_data_missing_column(mock_csv_file):
    """
    Test the load_and_plot_data function with a missing column.
    """
    with pytest.raises(ValueError, match="Column 'NonExistentColumn' not found in dataset."):
        load_and_plot_data(mock_csv_file, variable_name="NonExistentColumn")

def test_load_and_plot_data_invalid_file():
    """
    Test the load_and_plot_data function with an invalid file path.
    """
    with pytest.raises(ValueError, match="Error loading file:"):
        load_and_plot_data("non_existent_file.csv", variable_name="Power")