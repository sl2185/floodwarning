from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.dates as dts

def run():
    dts.set_epoch(datetime.datetime.now())
    #Build list of stations and find the 5 with the highest current relative water level
    stations = build_station_list()
    update_water_levels(stations)
    
    top5 = stations_highest_rel_level(stations,5)


    for station in top5:
        dates,levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2))
        if dates and levels:
            plot_water_level_with_fit(station,dates,levels,4)
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()