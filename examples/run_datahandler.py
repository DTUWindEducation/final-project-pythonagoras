import sys
"""
The `sys` module provides access to variables and functions that interact with the Python runtime environment.
It allows manipulation of the Python interpreter's behavior, such as modifying the module search path (`sys.path`),
retrieving command-line arguments, and handling standard input/output streams.
"""
# Provides access to Python runtime environment, including the module search path (sys.path)
import os
# Add the 'inputs' folder to Python's module search path
from inputs.datahandler import DataHandler # Imports the DataHandler class from the datahandler.py file inside the inputs folder.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'inputs'))
# Appends the 'inputs' directory to the system path so Python can find and import modules from it.

if __name__ == "__main__": # Checks if the script is being run directly (not imported
    handler = DataHandler() # Creates an instance of the DataHandler class, which loads CSV files from the 'inputs' folder.
    handler.plot_variable("Location1", "Power", 0, 200) # Calls the plot_variable method to plot the "Power" variable from "Location1" CSV file, slicing the first 200 rows.
