import matplotlib.pyplot as plt
from .analysis import polyfit
import numpy as np
import matplotlib.dates as dts
import datetime


def plot_water_levels(station, dates, levels):
   
    '''Plots and displays a plot of the water level data against time for a station, 
    includes typical low and high levels.
    Args:
        Station: MonitoringStation object
        Dates: List of dates and times for corresponding water level readings
        Levels: list of level readings for specified dates
    '''
    #Get low and high levels for the station
    low = station.typical_range[0]
    high = station.typical_range[1]

    plt.plot(dates,levels,label=f'{station.name} water levels against time.')
    plt.axhline(y=low, color='r', linestyle='-',label="Typical Low")
    plt.axhline(y=high, color='b', linestyle='-',label="Typical High")
    plt.legend()

    plt.xlabel("Date and Time")
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name) 

    # Display plot
    plt.tight_layout()  

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    '''
    Plots and displays a plot of the water level data against time (in days ago) for a station, 
    includes typical low and high levels and a polynomial fit for the data
    Args:
        Station: MonitoringStation object
        Dates: List of dates and times for corresponding water level readings
        Levels: list of level readings for specified dates
        p: Polynomial degree for fit'''
    #Find coefficients for the polynomial 
    poly, d0 = polyfit(dates,levels,p)

    date_float_list = dts.date2num(dates)

    #Get low and high levels for the station
    low = station.typical_range[0]
    high = station.typical_range[1]

    #Plot existing datapoints and low/high lines
    plt.plot(date_float_list,levels,label=f'{station.name} water levels against time.')
    plt.axhline(y=low, color='r', linestyle='-',label="Typical Low")
    plt.axhline(y=high, color='b', linestyle='-',label="Typical High")

    #Plots polynomial calculated
    fx = np.linspace(date_float_list[0],date_float_list[-1],30)
    plt.plot(fx,poly(fx-date_float_list[0]),label= f'Fitted Curve: {poly}')

    plt.legend()
    plt.xlabel("Days ago")
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name) 

   # Display plot
    plt.tight_layout()  
    plt.show()