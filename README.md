[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zjSXGKeR)

# Our Great Package

Team: Pythonagoras

## Overview

This Python package was developed to support short-term wind power forecasting, specifically targeting 1-hour-ahead predictions using a combination of machine learning (ML) techniques. It leverages a real-world dataset based on ERA5 reanalysis data, which includes meteorological observations (such as wind speed, direction, and temperature) and normalized wind power production data for four different locations.

The package implements and compares three forecasting approaches:

 1) Persistence Model: A simple baseline that assumes future values equal current ones.

 2) Support Vector Machine (SVM): A supervised ML method used for non-linear regression.

 3) Neural Network (NN): A data-driven model that captures complex relationships in time series.

The library includes modules for data loading, preprocessing (e.g., lag feature generation and normalization), training, and evaluation. Forecast performance is evaluated using error metrics such as MAE, MSE, and RMSE.

This package was created as part of the course "Scientific Programming for Wind Energy" at the Technical University of Denmark (DTU) and follows good practices in modular Python development and testing.

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

3. Run the project: Open Visio Studio and then the folder that you have already clone. Go to file exercises and then RUN the main.py script

--------------------------------------------------------------------------------------------------------------------------------

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
final-project-pythonagoras/
wind_power_forecasting/
├── inputs/ # Contains input CSV files (e.g., Location1.csv)
│ ├── Location1.csv
│ ├── Location2.csv
│ ├── Location3.csv
│ ├── Location4.csv
│ └── readme.txt
│
├── outputs/ # Stores generated plots and output data
│ └── *.png
│
├── examples/ # Demo scripts and helper tools
│ ├── main.py
│ ├── plot_timeseries.py
│ ├── persistence_forecast.py # Example for persistence forecasting
│ ├── run_4_5.py
│ ├── run_data_loader.py
│ ├── run_datahandler.py
│ └── run_nn_forecast.py
│
├── src/ # Core source code
│ ├── init.py
│ ├── compute_errors.py # Error metric calculations (MAE, MSE, RMSE)
│ ├── data_loader.py # Standalone function to load and plot data
│ ├── datahandler.py # Class to manage multiple CSVs
│ ├── features.py # Feature engineering tools
│ ├── model_linear.py # Linear regression forecasting model
│ ├── model_nn.py # Neural network model definition
│ ├── predict_persistence.py # One-step-ahead prediction baseline
│ ├── preprocessing.py # Lag generation and normalization
│ ├── split_data.py # Train/test data splitter
│ ├── task3.py # Simulated forecasts and evaluation
│ ├── task5.py # Predict-persistence implementation
│ └── task6.py # SVM-based power forecasting
│
├── tests1/ # Unit tests for modules
│ ├── test_compute_errors.py
│ ├── test_data_loader.py
│ ├── test_features.py
│ ├── test_model_linear.py
│ ├── test_model_nn.py
│ ├── test_predict_persistence.py
│ ├── test_preprocessing.py
│ ├── test_split_data.py
│ └── test_task5.py
│
├── README.md # Project documentation
├── pytest.ini # pytest configuration
└── .coverage # Test coverage tracking
```

### Architecture Diagram

```text
                      ┌────────────────────────┐
                      │     CSV Input Files    │
                      │   (inputs/*.csv)       │
                      └──────────┬─────────────┘
                                 │
                  ┌──────────────▼─────────────┐
                  │    DataHandler Class       │
                  │ (src/datahandler.py)       │
                  └──────────────┬─────────────┘
                                 │
           ┌────────────────────▼────────────────────┐
           │    Preprocessing Functions              │
           │ (src/preprocessing.py, src/features.py) │
           └────────────────────┬────────────────────┘
                                │
    ┌───────────────────────────▼────────────────────────────┐
    │              Forecasting Models (Task 3, 5, 6)         │
    │ ┌────────────────────────┬───────────────────────────┐ │
    │ │  simulate_forecast     │  predict_persistence      │ │
    │ │  (task3.py)            │  (predict_persistence.py) │ │
    │ │                        └──────────────┬────────────┘ │
    │ │  linear_regression     │              │              │
    │ │  (model_linear.py)     │      SVM, NN Models         │
    │ │                        │ (task6.py, model_nn.py)     │
    │ └────────────┬───────────┴────────────────────────────┘
                   │
       ┌───────────▼────────────┐
       │   compute_errors.py    │ ← Evaluate MAE, MSE, RMSE
       └───────────┬────────────┘
                   │
       ┌───────────▼────────────┐
       │   Visual Output        │ ← Plots (matplotlib)
       │   (outputs/*.png)      │
       └────────────────────────┘

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

It plots a variable from a location.


## Peer Review

The code was reviewed together by all groupmembers. The method that we followed was to divide the tasks to the three of us and discussed it in person for better communication.
We checked:

- That functions had clear names and comments
- That the plots were working
- The code runs at a proper time in less than 10 min
- 

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


