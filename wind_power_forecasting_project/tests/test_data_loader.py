from src.wind_forecasting.data_loader import load_and_plot_data
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_load_and_plot_variable():
    df = load_and_plot_data("inputs/Location1.csv", "Power", 0, 100)
    assert not df.empty
    assert "Power" in df.columns
