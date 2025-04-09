import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inputs.datahandler import DataHandler

def test_data_handler_loads_data_correctly():
    """Test that the DataHandler loads data correctly."""

    # Create a DataHandler object using the inputs folder
    inputs_folder = os.path.join(os.path.dirname(__file__), '../inputs')
    data_handler = DataHandler(inputs_folder)

    # Assert that data was loaded correctly
    assert "Location1" in data_handler.data, "Location1 not found in data dictionary"

    # Assert that a known column like "Power" exists
    assert "Power" in data_handler.data["Location1"].columns, "'Power' column not found in Location1 data"


def test_data_handler_plot_variable_runs_without_errors():
    """Test that plot_variable() runs without errors."""
    # Create a DataHandler object using the inputs folder
    inputs_folder = os.path.join(os.path.dirname(__file__), '../inputs')
    data_handler = DataHandler(inputs_folder)

    # Call the plot_variable() method with valid parameters
    try:
        data_handler.plot_variable(location="Location1", variable="Power")
    except Exception as e:
        pytest.fail(f"plot_variable() raised an exception: {e}")