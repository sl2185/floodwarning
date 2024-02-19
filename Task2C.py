from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2C"""

    stations = build_station_list()
    update_water_levels(stations)

    stations_over_threshold = stations_highest_rel_level(stations,10)
    
    for station in stations_over_threshold:
        print(station.name, station.relative_water_level(), "\n")

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()