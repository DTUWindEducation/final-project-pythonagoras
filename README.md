# Our Great Package

Team: Pythonagoras

## Overview

This package was made to forecast wind power production one hour ahead. It uses two models: one very simple (the persistence model), and one based on machine learning (linear regression). 
We use time series data that comes from ERA5 and contains wind data for four locations. We also include error calculations to see how good the predictions are. This project was made as part of the Scientific Programming in Wind Energy course at DTU.

## Quick-start guide

First, the installation instructions are as follows.

1. Clone the repository
 
```bash
git clone https://github.com/DTUWindEducation/final-project-pythonagoras.git
cd final-project-pythonagoras
```

2. Install the needed Python packages

```bash
pip install pandas numpy scikit-learn matplotlib
```

3. Run the project

```bash
PYTHONPATH=src python3 main.py
```

Now, a step-by-step of what we did

Step 1: Set up a GitHub repo

- Cloned the GitHub Classroom project
- Created new branches with our names

Step 2: Wrote the first scripts

- Made `plot_timeseries.py` to draw timeseries plots
- Created `persistence_forecast.py` to make a simple forecast model
- Plotted and printed data to check that everything worked

Step 3: Created the folder structure

We made the full structure with folders:

```
inputs/, outputs/, examples/, tests/, src/wind_power_forecast/
```

Step 4: Added files to `src/`

- `loader.py` to load CSV files for each location
- `compute_error.py` for MAE, MSE, RMSE
- `model_linear.py` to train and predict with regression
- Pushed all our codes to GitHub and made pull requests one by one

Step 5: Fixed input data

- The `inputs/` folder was missing because `.csv` files were not added to Git
- We added the files manually to test locally

Step 6: Wrote test files

- `test_loader.py` checked that files loaded correctly
- `test_errors.py` tested the error function with small fake data

Step 7: Made `main.py`

- This script brings together all tasks from 2 to 6 and unifies all the different codes
- It runs the forecast, evaluation, and plots everything in one place

Step 8: Final push

- Cleaned the repo
- Moved example files to the correct folders
- Ran final tests

## Architecture

```
wind_power_forecasting/
├── inputs/                 # Input CSV data files
├── outputs/                # Plots and outputs
├── examples/               # Example scripts
│   └── test_errors.py      # Test for compute_errors()
├── src/                    # Main code
│       ├── datahandler.py         # Class to load the CSVs
│       ├── compute_errors.py      # Calculates MSE, MAE, RMSE
│       ├── model_linear.py        # Linear regression model
│       ├── predict_persistence.py # Simple forecast
│       ├── plot_timeseries.py     # Makes timeseries plots
│       ├── split_data.py          # Splits into train/test
│       ├── task3.py               # simulate and evaluate forecast
├── main.py                # Main script
├── README.md              # Documentation
```

### Architecture Diagram

```text
+------------------+       +-----------------+
| inputs/*.csv     +<----->+ DataHandler     |
+--------+---------+       +--------+--------+
                                 |
                                 v
                        +--------+--------+
                        | split_data.py   |
                        +--------+--------+
                                 |
                  +--------------+--------------+
                  |                             |
          +-------v-------+             +-------v--------+
          | predict_      |             | model_linear   |
          | persistence.py|             |.py (regression)|
          +-------+-------+             +-------+--------+
                  |                             |
                  +--------------+--------------+
                                 v
                        +--------+--------+
                        | compute_errors  |
                        +-----------------+
```

##  Implemented Classes

- `DataHandler`

File: `src/datahandler.py`

This class loads all CSVs from the input folder and saves them.

How to use it:

```python
handler = DataHandler("inputs")
df = handler.data["Location1.csv"]
```

Method:

```python
handler.plot_variable("Location1", "Power", 0, 200)
```

Now it plots a variable from a location.


## Peer Review

The code was reviewed together with my group. We checked:

- That functions had clear names and comments
- That error metrics made sense
- That the plots were working
- That linear regression was trained properly

After that, we cleaned the main code and pushed the final version to GitHub.

## Final Test Run

To test all the steps:

```bash
PYTHONPATH=src python3 main.py
```

Expected output:

```
Persistence model MSE on Power: 0.0014
Results for site Location1.csv:
MAE: 0.1469
MSE: 0.0338
RMSE: 0.1840
```

Everything was reviewed by all group members. Code and logic were discussed collaboratively during development.

