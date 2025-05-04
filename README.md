[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zjSXGKeR)
# Our Great Package

Team: Pythonagoras

## Overview

This package predicts one-hour-ahead wind turbine power production using a combination of simple and machine learning models. It is designed to handle time series data from wind farms in Location1 and provides both a persistence model and a linear regression model, along with standard error evaluation and timeseries plotting.

The project was developed during the Scientific Programming in Wind Energy course at DTU, and fulfills the functional requirements outlined in the final assignment.

## Quick-start guide

1. Clone this repository
2. Install required packages:
pip install pandas numpy scikit-learn matplotlib
3. Run the main script:
PYTHONPATH=src python3 main.py
4. You can test individual components:
python3 examples/test_loader.py python3 examples/test_errors.py
5. All plots or saved models go in the `outputs/` directory.



## Architecture

""" wind_power_forecasting/ ├── inputs/ # Contains all the input CSV or ERA5 data files ├── outputs/ # Stores output plots and result files ├── setup.py # Setup instructions for installing the package ├── README.md # Project overview and documentation ├── main.py # Main executable script that calls and runs functions │ ├── src/ # Source code directory │ ├── init.py # Initializes the package and imports core functions │ ├── loader.py # Loads and prepares input data │ ├── plot.py # Functions for plotting timeseries and wind roses │ ├── compute_error.py # Calculates error metrics for model evaluation """

## Peer review

Reviewed by group members. Code and logic were discussed collaboratively during development.

