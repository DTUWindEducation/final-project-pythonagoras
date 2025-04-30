import os                      # Imports the os module for interacting with the operating system
import pandas as pd            # Imports pandas with the alias 'pd' for data handling and analysis.
import matplotlib.pyplot as plt # Imports the matplotlib module for plotting, aliased as 'plt'.


class DataHandler:
    """Handles loading and basic operations on input CSV files."""

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Loads a CSV file into a DataFrame.

        Args:
            filename (str): Name of the CSV file (without the path).

        Returns:
            pd.DataFrame: Loaded data.
        """
           # Check if the filename already contains a path
        if not filename.startswith("inputs/"): # If the filename does not start with 'inputs/', prepend it.
            filepath = f"inputs/{filename}.csv" # Constructs the full path to the CSV file.
        else:
            filepath = filename # If it already contains a path, use it as is.
        try: # Attempt to read the CSV file into a DataFrame.
            data = pd.read_csv(filepath) # Reads the CSV file into a pandas DataFrame.
            return data # Returns the loaded DataFrame.
        except FileNotFoundError: # If the file is not found, handle the exception.
            raise ValueError(f"File {filename} not found in inputs directory.") # Raises a ValueError with a message indicating the file was not found.

    def plot_variable(self, filename: str, variable: str, start_idx: int = 0, end_idx: int = None):
        """
        Plots a specific variable from a CSV file.

        Args:
            filename (str): Name of the CSV file (without the path).
            variable (str): Column name of the variable to plot.
            start_idx (int): Starting index for slicing the data.
            end_idx (int): Ending index for slicing the data.
        """
        data = self.load_csv(filename) # Loads the CSV file into a DataFrame using the load_csv method.
        if variable not in data.columns: # Checks if the specified variable exists in the DataFrame.
            raise ValueError(f"Column '{variable}' not found in {filename}.csv") # Raises a ValueError if the variable is not found.

        # Plot the variable
        plt.figure(figsize=(10, 6))
        plt.plot(data[variable].iloc[start_idx:end_idx], label=variable)
        plt.title(f"{variable} from {filename}.csv")
        plt.xlabel("Index")
        plt.ylabel(variable)
        plt.legend()
        plt.show()


