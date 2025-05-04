"""
This module provides a function to load, parse, and plot a dataset from a CSV
file. It includes error handling for file loading and checks for the presence
of the specified variable in the dataset.
"""
import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt


def load_and_plot_data(file_path, variable_name, start_idx=0, end_idx=500):
    """
    Load, parse, and plot the dataset.

    Args:
        file_path (str): Path to the dataset file.
        variable_name (str): Name of the variable/column to plot.
        start_idx (int): Starting index for slicing the data.
        end_idx (int): Ending index for slicing the data.

    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame.
    """
    # Load the dataset
    try:  # Attempt to load the dataset.
          # This block will handle any errors during the loading process.
        data = pd.read_csv(  # Try to read the CSV file into a DataFrame
            file_path
        )
    except Exception as e:  # If an error occurs during loading,
        # catch the exception
        raise ValueError(
            f"Error loading file: {e}"
        ) from e  # Explicitly re-raise the exception

    if variable_name not in data.columns:  # Check if the specified variable exists
        # in the DataFrame
        raise ValueError(
            f"Column '{variable_name}' not found in dataset."
        )  # Raise a ValueError if the variable is not found

    # Display basic info
    print("Dataset Info:")  # Print a label for the dataset info
    # Print metadata about the DataFrame
    # (columns, non-null counts, types, etc.)
    print(data.info())
    print("\nFirst few rows:")  # Print a label for the head of the DataFrame
    print(data.head())  # Print the first few rows of the dataset

    # Plot the data
    plt.figure(figsize=(10, 6))  # Create a new figure with size 10x6 inches
    plt.plot(
        data[variable_name].iloc[start_idx:end_idx],
        label=variable_name
    )  # Plot the variable from start to end index
    plt.title(f"{variable_name} over Time")  # Set the title of the plot
    plt.xlabel("Index")  # Set the label for the x-axis
    # Set the label for the y-axis (same as the variable name)
    plt.ylabel(variable_name)
    plt.legend()  # Add a legend to the plot
    plt.grid(True)  # Add a grid to the plot
    plt.tight_layout()  # Automatically adjust subplot params to fit the figure
    plt.show()  # Display plot

    return data  # Return the loaded dataset as a pandas DataFrame.
