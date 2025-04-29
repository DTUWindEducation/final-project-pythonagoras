from src.wind_forecasting.data_loader import load_and_plot_data # Import the load_and_plot_data function from the data_loader module
import sys # Import the sys module for system-specific parameters and functions
import os # Import the os module for operating system dependent functionality
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add the parent directory to the system path

def test_load_and_plot_variable():
    """Test the load_and_plot_data function."""
    df = load_and_plot_data("inputs/Location1.csv", "Power", 0, 100)  # Loads and plots the 'Power' column from the first 100 rows of Location1.csv
    assert not df.empty  # Asserts that the DataFrame is not empty (i.e., data was loaded successfully)
    assert "Power" in df.columns  # Asserts that the 'Power' column exists in the loaded DataFrame