## Wind Power Forecasting
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

-1st Option:
2. Install the needed Python packages

```bash
pip install pandas numpy scikit-learn matplotlib  tensorflow.keras pickle 
```

3. Run the project:
   1st Option: Open Visio Studio and then the folder that you have already clone. Go to folder "examples" and then RUN the main.py script
   After every plot that gets generated, PRESS the X button to the plot window to keep running the code

-2nd Option: Open Anaconda -> run: conda create -n tfenv python 3.9
  -> pip install tensorflow
  -> pip install pandas
  -> pip install matplotlib
  -> pip install scikit-learn
  -> run python examples/main.py
--------------------------------------------------------------------------------------------------------------------------------
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
├── htmlcov #optional file

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
├── tests/ # Unit tests for modules
│ ├── test_compute_errors.py
│ ├── test_data_handler.py
│ ├──test_data_loader.py
│ ├── test_features.py
│ ├── test_model_linear.py
│ ├── test_model_nn.py
│ ├── test_predict_persistence.py
│ ├── test_preprocessing.py
│ ├── test_split_data.py
│ └── test_task3.py
│ └── test_task5.py
│ └── test_task6.py
│
├── README.md # Project documentation
├── pytest.ini # pytest configuration

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
    │ │  compute MAE,MSE,RMSE  │  (predict_persistence.py) │ │
    │ │    (task3.py)          └──────────────┬────────────┘ │
    │ │                        │              │              │
    │ │                        │      SVM, NN Models         │
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
Everything was reviewed by all group members. Code and logic were discussed collaboratively during development.
We checked:

- That functions had clear names and comments
- That the plots were working
- The code runs at a proper time in less than 10 min
  
After that, we cleaned the main code and pushed the final version to GitHub.

## Final Test Run

Expected output:

```
 1) 1st plot: Power for Location 1 for the first 200 rows
 2) Results for site Location1.csv applying normal (Gaussian) distribution
 3) Persistence model MSE on Power and plot of Persistence Model vs Real Data
 4) Plots of Neural Netwoek vs Real Data and Support Vector Machine vs Real Data
```




