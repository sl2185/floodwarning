from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2B test"""

    output = []

    stations = build_station_list()

    update_water_levels(stations)
    
    results = stations_level_over_threshold(stations, 0.8)

    for station in results:
        output.append((station[0].name, station[1]))
    
    print("main output", output)
    print(len(output))
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()