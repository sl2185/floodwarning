from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E test"""
    stations = build_station_list()
    N = 10

    top_N_rivers_by_station = rivers_by_station_number(stations, N)

    print(top_N_rivers_by_station)
    
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    
    run()