from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

def run():
    """Requirements for Task 2B test"""
    stations = build_station_list()

    update_water_levels(stations)
    
    result = stations_level_over_threshold(stations, 0.8)

    output = []

    for station in result:
        output.append(station[0].name, station[1])
    
    print(sorted(output))
  
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()