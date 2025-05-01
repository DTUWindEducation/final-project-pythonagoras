import os
import pandas as pd
import matplotlib.pyplot as plt


class DataHandler:
    """Handles loading and basic operations on input CSV files."""

    def __init__(self, input_folder: str):
        """
        Initializes the DataHandler with the input folder path and loads all CSV files.

        Args:
            input_folder (str): Path to the folder containing input CSV files.
        """
        self.input_folder = input_folder
        self.data = self._load_all_csv_files()

    def _load_all_csv_files(self) -> dict:
        """
        Loads all CSV files in the input folder into a dictionary.

        Returns:
            dict: A dictionary where keys are filenames and values are DataFrames.
        """
        data = {}
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".csv"):
                filepath = os.path.join(self.input_folder, filename)
                try:
                    data[filename] = pd.read_csv(filepath)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
        return data

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Loads a specific CSV file into a DataFrame.

        Args:
            filename (str): Name of the CSV file (without the path).

        Returns:
            pd.DataFrame: Loaded data.
        """
        filepath = os.path.join(self.input_folder, filename)
        try:
            data = pd.read_csv(filepath)
            return data
        except FileNotFoundError:
            raise ValueError(f"File {filename} not found in {self.input_folder} directory.")

    def plot_variable(self, filename: str, variable: str, start_idx: int = 0, end_idx: int = None):
        """
        Plots a specific variable from a CSV file.

        Args:
            filename (str): Name of the CSV file (without the path).
            variable (str): Column name of the variable to plot.
            start_idx (int): Starting index for slicing the data.
            end_idx (int): Ending index for slicing the data.
        """
        data = self.load_csv(filename)
        if variable not in data.columns:
            raise ValueError(f"Column '{variable}' not found in {filename}")

        # Plot the variable
        plt.figure(figsize=(10, 6))
        plt.plot(data[variable].iloc[start_idx:end_idx], label=variable)
        plt.title(f"{variable} from {filename}")
        plt.xlabel("Index")
        plt.ylabel(variable)
        plt.legend()
        plt.show()