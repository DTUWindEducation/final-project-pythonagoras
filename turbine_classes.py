import numpy as np
import matplotlib.pyplot as plt


class GeneralWindTurbine:
    """
    A class to represent a general wind turbine and calculate its power output based on wind speed.
    Attributes:
        rotor_diameter (float): The diameter of the rotor in meters.
        hub_height (float): The height of the hub above the ground in meters.
        rated_power (float): The rated power output of the turbine in watts.
        v_in (float): The cut-in wind speed (minimum wind speed for power generation) in m/s.
        v_rated (float): The rated wind speed (wind speed at which the turbine generates its rated power) in m/s.
        v_out (float): The cut-out wind speed (maximum wind speed for safe operation) in m/s.
        name (str, optional): The name or identifier of the wind turbine. Defaults to None.
    Methods:
        get_power(wind_speed):
            Calculates the power output of the turbine based on the given wind speed.
            Returns 0 if the wind speed is outside the operational range.
    """

    def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name=None):
        if not (v_in < v_rated < v_out):
            raise ValueError("v_in must be less than v_rated, and v_rated must be less than v_out.")

        self.rotor_diameter = rotor_diameter
        self.hub_height = hub_height
        self.rated_power = rated_power
        self.v_in = v_in
        self.v_rated = v_rated
        self.v_out = v_out
        self.name = name

    def get_power(self, wind_speed):
        """
        Calculate the power output of the turbine based on the given wind speed.
        Parameters:
            wind_speed (float): The speed of the wind in meters per second (m/s).
        Returns:
            float: The power output of the turbine in watts (W). Returns 0 if the wind speed
                   is outside the operational range (below `v_in` or above `v_out`).
                   If the wind speed is between `v_in` and `v_rated`, the power is calculated
                   proportionally to the cube of the wind speed. If the wind speed is between
                   `v_rated` and `v_out`, the power output is constant at `rated_power`.
        """

        if wind_speed < self.v_in or wind_speed > self.v_out:
            return 0
        elif self.v_in <= wind_speed < self.v_rated:
            return self.rated_power * (wind_speed / self.v_rated) ** 3
        elif self.v_rated <= wind_speed <= self.v_out:
            return self.rated_power


class WindTurbine(GeneralWindTurbine):
    """
    A class representing a wind turbine, inheriting from GeneralWindTurbine.
    This class extends the functionality of the GeneralWindTurbine class by
    allowing the use of a power curve to determine the power output based on
    wind speed.
    Attributes:
        power_curve_data (numpy.ndarray or None): A 2D array where the first column
            contains wind speeds and the second column contains corresponding power
            outputs. If None, the power output is determined using the parent class's
            method.
    Methods:
        get_power(wind_speed):
            Calculates the power output of the wind turbine for a given wind speed.
            If a power curve is provided, it interpolates the power output using the
            curve. Otherwise, it falls back to the parent class's method.
    """

    def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name=None, power_curve_data=None):
        super().__init__(rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name)
        self.power_curve_data = power_curve_data

    def get_power(self, wind_speed):
        if self.power_curve_data is not None:
            wind_speeds = self.power_curve_data[:, 0]
            powers = self.power_curve_data[:, 1]
            return float(np.interp(wind_speed, wind_speeds, powers))
        else:
            return super().get_power(wind_speed)


# Load power curve data
data = np.loadtxt("/Users/apostolossalepis/Desktop/python/46120-PIWE/week09_classes_inheritance_and_OOP/LEANWIND_Reference_8MW_164.csv", delimiter=",", skiprows=1)
wind_speeds_data = data[:, 0]
powers_data = data[:, 1]

# Create a GeneralWindTurbine object
turbine_general = GeneralWindTurbine(
    rotor_diameter=164,
    hub_height=110,
    rated_power=8000,
    v_in=4,
    v_rated=12.5,
    v_out=25,
    name="LEANWIND_8MW"
)

# Create a WindTurbine object with interpolation-based power curve
turbine_interp = WindTurbine(
    rotor_diameter=164,
    hub_height=110,
    rated_power=8000,
    v_in=4,
    v_rated=12.5,
    v_out=25,
    name="LEANWIND_8MW_Interp",
    power_curve_data=data
)

# Generate a wind speed range for plotting
wind_range = np.linspace(0, 26, 200)

# Get power outputs
general_powers = [turbine_general.get_power(v) for v in wind_range]
interp_powers = [turbine_interp.get_power(v) for v in wind_range]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(wind_range, general_powers, label="GeneralWindTurbine (analytical)", linestyle="--")
plt.plot(wind_range, interp_powers, label="WindTurbine (interpolated)", linestyle="-")
plt.scatter(wind_speeds_data, powers_data, color='red', s=10, label="Original data points")

plt.xlabel("Wind Speed [m/s]")
plt.ylabel("Power Output [kW]")
plt.title("Power Curve Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
