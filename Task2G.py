from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import matplotlib.dates as dts
dts.set_epoch(datetime.datetime.now())

#Find all current water levels
station_raw_list = build_station_list()
update_water_levels (station_raw_list)

#Find those with a current water level over the typical range
over_threshold = stations_level_over_threshold(station_raw_list,2)
#Print the number of stations to the terminal
num_of_valid_stations = len(over_threshold)



#sort stations on their level
sorted_stations = sorted_by_key(over_threshold, 1, reverse=True)
output=[]

for station in sorted_stations:
    # Get the dates and levels of the station over the last 2 days
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
    
    # Check if dates and levels are not empty
    if dates and levels:
        # Fit a polynomial of order 4 for the water levels
        poly, d0 = polyfit(dates, levels, 4)
        poly_d = np.polyder(poly, m=1)
        
        current_date_num = dts.date2num(datetime.datetime.now())

        # Evaluate the derivative polynomial at the current date (Instantaneous rate of Change in water level)
        gradient_at_current_date = poly_d(current_date_num)
        
        if gradient_at_current_date > 0.6:
            risk = "Severe"
        elif gradient_at_current_date > 0.3:
            risk = 'High'
        elif gradient_at_current_date < 0:
            risk = "Low"
        else:
            risk = "Medium"
        output.append((station[0].name, risk))
    else:
        num_of_valid_stations -= 1

print("Number of stations with flood risk: " + str(num_of_valid_stations))
print(output)
