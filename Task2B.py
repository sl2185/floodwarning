from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations, stations_level_over_threshold, relative_water_level
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 2B test"""
    stations = build_station_list()

    # Print the name of each station and its relative level
    for station_name, relative_level in stations_level_over_threshold(stations, 0.8):
        print(f"{station_name} {relative_level}")
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    
    run()