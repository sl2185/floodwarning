from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F test"""
    output = []

    # Build list of stations
    stations = build_station_list()

    for station in inconsistent_typical_range_stations(stations):
        output.append(station.name)
    
    print(sorted(output))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()