import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    '''Plots and displays a plot of the water level data against time for a station, 
    includes typical low and high levels.
    Args:
        Station: MonitoringStation obkect
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
    plt.xticks(rotation=45);
    plt.title(station.name) 

    # Display plot
    plt.tight_layout()  

    plt.show()