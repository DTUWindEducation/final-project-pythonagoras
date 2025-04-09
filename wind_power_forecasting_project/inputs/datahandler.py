import os                      # Imports the os module for interacting with the operating system (e.g., file paths).
import pandas as pd            # Imports pandas with the alias 'pd' for data handling and analysis.
import matplotlib.pyplot as plt # Imports the matplotlib module for plotting, aliased as 'plt'.

class DataHandler:
    """_A class to handle loading and plotting data from CSV files."""
    def __init__(self, input_folder="inputs"):
        self.input_folder = input_folder # Sets the folder where CSV input files are located.
        self.data = {} # Initializes an empty dictionary to store data from the CSV files.
        self.load_csv_files() # Calls a method to load all CSV files from the input folder.

    def load_csv_files(self):
        """Loads all CSV files from the input folder into a dictionary."""
        for filename in os.listdir(self.input_folder):  # Iterates over each file in the input folder.
            if filename.endswith(".csv"):               # Processes only files with the `.csv` extension.
                file_path = os.path.join(self.input_folder, filename)  # Builds the full path to the file.
                df = pd.read_csv(file_path)             # Reads the CSV file into a pandas DataFrame.
                self.data[filename] = df                # Stores the DataFrame in the dictionary using filename as the key.

    def plot_variable(self, location, variable, start=None, end=None):
        """
        Plots a selected variable from a specific location CSV file.
        """
        file_name = f"{location}.csv"                    # Constructs the CSV filename based on the given location.
        if file_name not in self.data:                   # Checks if the file has been loaded.
            print(f"File '{file_name}' not loaded.")     # Informs the user if the file wasn't found in the data dictionary.
            return                                       # Exits the method early if the file is missing.

        df = self.data[file_name]                        # Retrieves the DataFrame for the specified file.
        if variable not in df.columns:                   # Checks if the variable (column) exists in the DataFrame.
            print(f"Column '{variable}' not found in {file_name}.")  # Warns if the column doesn't exist.
            return                                       # Exits the method early if the column is missing.

        sliced_data = df[variable][start:end] # Slices the DataFrame to get the specified variable.
        sliced_data.plot(title=f"{variable} in {location}") # Plots the sliced data with a title.
        plt.xlabel("Time index") # Sets the x-axis label to "Time index".
        plt.ylabel(variable) # Sets the y-axis label to the variable name.
        plt.grid(True) # Enables grid lines on the plot for better readability.
        plt.show() # Displays the plot.