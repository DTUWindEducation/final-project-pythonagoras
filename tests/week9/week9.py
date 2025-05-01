import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


class GeneralWindTurbine:
    def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name):
        self.rotor_diameter = rotor_diameter  # in meters
        self.hub_height = hub_height  # in meters
        self.rated_power = rated_power  # in kW
        self.v_in = v_in  # in m/s
        self.v_rated = v_rated  # in m/s
        self.v_out = v_out  # in m/s
        self.name = name  # turbine name

    'function get_power() that return power output P at wind speed v using following rules'
    def get_power1(self, v):
        if v < self.v_in or v > self.v_out:
               power_output1 = 0
        elif self.v_in <= v < self.v_rated:
              power_output1 = self.rated_power * (v / self.v_rated) ** 3
        else:
              power_output1 = self.rated_power
        return power_output1

class WindTurbine(GeneralWindTurbine):
     def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name, power_curve_data):
          GeneralWindTurbine.__init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name)
          self.power_curve_data = power_curve_data
    
     'Extract wind speeds and power values from the power curve data'
     def get_power(self, v):
       wind_speeds = self.power_curve_data[:, 0]
       power = self.power_curve_data[:, 1]

       #Interpolate the power value based on the given wind speed
       power_output = np.interp(v, wind_speeds, power)
       return power_output

     'plot wind speed vs power'
     def plot_power_curve(self):
        wind_speeds = self.power_curve_data[:, 0]
        power_values = self.power_curve_data[:, 1]
        plt.figure(figsize=(10, 6))
        plt.plot(wind_speeds, power_values, marker='o', linestyle='-', color='b')
        plt.title(f'Power Curve for {self.name}')
        plt.xlabel('Wind Speed (m/s)')
        plt.ylabel('Power (kW)')
        plt.grid(True)
        plt.show()

'method to read data from a file'
def read_power_curve_data(file_path):
  return np.genfromtxt(file_path, delimiter=',', skip_header=1)

'specify the path of the file'
file_path = 'C:/Users/Admin/Desktop/DTU/Python/final-project-pythonagoras/LEANWIND_Reference_8MW_164.csv'
power_curve_data = read_power_curve_data(file_path)

'initialize the class WindTurbine'
turbine = WindTurbine(164, 110, 8000, 4, 12.5, 25, 'Leanwind 8 MW RWT', power_curve_data)
turbine.plot_power_curve()
