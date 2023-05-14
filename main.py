print('Hello World!')

import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
M = 5.972e24  # Mass of the Earth (kg)
R = 6371000  # Radius of the Earth (m)
coefficient = 2.2 #sample drag coefficient of satellite
cross_area = 10 #sample surface cross sectional area of satellite (m^2)








def calculate_satellite_parameters():
    # User input
    height = float(input("Enter the height of the satellite (in meters): "))
    mass = float(input("Enter the mass of the satellite (in kg): "))
    drag_coefficient = float(input("Enter the drag coefficient of the satellite (default: 2.2): ") or coefficient)
    cross_sectional_area = float(input("Enter the cross-sectional area of the satellite (default: 10): ") or cross_area)

    #Calculations
    # Calculate gravitational force 
    gravitational_force = (G * M * mass) / (R + height)**2
    # Calculate satellite speed
    satellite_speed = math.sqrt(gravitational_force / mass)
    # Calculate satellite period
    satellite_period = 2 * math.pi * math.sqrt((R + height)**3 / (G * M))
    # Calculate atmospheric density (assuming simple linear model)
    atmospheric_density = 1.225 * math.exp(-height / 8200)
    # Calculate drag force
    drag_force = 0.5 * drag_coefficient * cross_sectional_area * atmospheric_density * satellite_speed**2
    # Calculate acceleration due to atmospheric drag
    acceleration_drag = drag_force / mass
    # Calculate change in altitude (assuming no other forces)
    change_in_altitude = -satellite_speed * math.sin(math.pi/2) - (acceleration_drag / (2 * math.pi / satellite_period)) * math.cos(math.pi/2)

    # Print the results
    print("Gravitational Force: {:.2f} N".format(gravitational_force))
    print("Satellite Speed: {:.2f} m/s".format(satellite_speed))
    print("Satellite Period: {:.2f} seconds".format(satellite_period))
    print("Atmospheric Density: {:.2f} kg/m^3".format(atmospheric_density))
    print("(" + str(atmospheric_density) + ")")
    print("Drag Force: {:.2f} N".format(drag_force))
    print("(" + str(drag_force) + ")")
    print("Acceleration due to Atmospheric Drag: {:.2f} m/s^2".format(acceleration_drag))
    print("(" + str(acceleration_drag) + ")")
    print("Change in Altitude: {:.2f} meters".format(change_in_altitude))
    
    return (gravitational_force, satellite_speed, satellite_period, drag_force, acceleration_drag, change_in_altitude)



# Calculate satellite parameters
parameters = calculate_satellite_parameters()
