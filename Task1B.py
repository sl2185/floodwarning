from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B test"""

    # Build list of stations
    stations = build_station_list()

    ten_closest = stations_by_distance(stations,(52.2053, 0.1218))[:10]
    ten_furthest = stations_by_distance(stations,(52.2053, 0.1218))[-10:]
    
    # Check for  number of stations in list
    print("Number of stations: {}".format(len(ten_closest)))
    print("Number of stations: {}".format(len(ten_furthest)))


    # Print 10 closest and furthest stations
    print('ten closest stations from cambridge city centre:', ten_closest)
    print('ten furthest stations from cambridge city centre:', ten_furthest)
    

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
