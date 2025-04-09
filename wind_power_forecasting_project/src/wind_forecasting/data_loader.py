import pandas as pd
import matplotlib.pyplot as plt


def load_and_plot_data(file_path, variable_name, start_idx=0, end_idx=500):
    """
    Load, parse, and plot the dataset.

    Args:
        file_path (str): Path to the dataset file.

    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame.
    """
    # Load the dataset
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")
    if variable_name not in data.columns:
        raise ValueError(f"Column '{variable_name}' not found in dataset.")


# Display basic info
    print("Dataset Info:")
    print(data.info())
    print("\nFirst few rows:")
    print(data.head())

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(data[variable_name].iloc[start_idx:end_idx], label=variable_name)
    plt.title(f"{variable_name} over Time")
    plt.xlabel("Index")
    plt.ylabel(variable_name)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return data
