from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C test"""

    # Build list of stations
    stations = build_station_list()

    stations_wihtin_radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    output = []

    for station in stations_wihtin_radius_list:
        output.append(station.name)
    print(sorted(output))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
