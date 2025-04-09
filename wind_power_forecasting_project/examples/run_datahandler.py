import sys
"""
The `sys` module provides access to variables and functions that interact with the Python runtime environment.
It allows manipulation of the Python interpreter's behavior, such as modifying the module search path (`sys.path`),
retrieving command-line arguments, and handling standard input/output streams.
"""
# Provides access to Python runtime environment, including the module search path (sys.path)
import os
# Add the 'inputs' folder to Python's module search path
from inputs.datahandler import DataHandler
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'inputs'))

if __name__ == "__main__":
    handler = DataHandler()
    handler.plot_variable("Location1", "Power", 0, 200)