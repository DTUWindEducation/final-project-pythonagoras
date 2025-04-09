import pytest # Import the pytest module for testing
import sys # Import the pytest module for testing
import os # Import the os module for file path manipulations
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add the parent directory to the system path
from inputs.datahandler import DataHandler # Import the DataHandler class from the datahandler module

def test_data_handler_loads_data_correctly():
    """Test that the DataHandler loads data correctly."""

    # Create a DataHandler object using the inputs folder
    inputs_folder = os.path.join(os.path.dirname(__file__), '../inputs') #Builds the path to the 'inputs' folder relative to this file
    data_handler = DataHandler(inputs_folder)  # Creates a DataHandler instance and loads CSV files


    # Assert that data was loaded correctly
    assert "Location1" in data_handler.data, "Location1 not found in data dictionary" # Check if "Location1" data is loaded

    # Assert that a known column like "Power" exists
    assert "Power" in data_handler.data["Location1"].columns, "'Power' column not found in Location1 data"


def test_data_handler_plot_variable_runs_without_errors():
    """Test that plot_variable() runs without errors."""
    # Create a DataHandler object using the inputs folder
    inputs_folder = os.path.join(os.path.dirname(__file__), '../inputs') # Builds the path to the 'inputs' folder
    data_handler = DataHandler(inputs_folder) # Initializes a DataHandler instance for testing


    # Call the plot_variable() method with valid parameters
    try:
        data_handler.plot_variable(location="Location1", variable="Power") # Calls the plot_variable method to plot the "Power" variable from "Location1"
    except Exception as e:
        pytest.fail(f"plot_variable() raised an exception: {e}") # If an exception occurs, the test fails with the exception message