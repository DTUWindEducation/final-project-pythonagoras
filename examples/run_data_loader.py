from src.data_loader import load_and_plot_data

# Define the file path and variable name
file_path = "src/Location1.csv"  # Update this path to the actual CSV file
variable_name = "Power"  # Replace with the column name you want to plot

# Call the function
data = load_and_plot_data(file_path, variable_name, start_idx=0, end_idx=500)