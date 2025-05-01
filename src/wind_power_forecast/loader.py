import pandas as pd

def load_site_data(site_index):
    """
    Load the CSV dataset from a specific site
    
    Parameters:
        site_index (int): Site number (1, 2, 3 or 4).
        
    Returns:
        pandas.DataFrame: DataFrame with the loaded data, sorted by date
    """
    # Build the file path
    path = f"inputs/Location{site_index}.csv"
    
    # Load the CSV
    df = pd.read_csv(path, parse_dates=["Time"])
    
    # Sort by time
    df = df.sort_values("Time")
    
    return df
