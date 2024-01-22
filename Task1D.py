from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D test"""

    #Build a list of stations
    stations = build_station_list()

    #Build a list of rivers with at least one station
    riverlist = rivers_with_station(stations)
    riverlist.sort()

    number_of_rivers = len(riverlist)
    

    #Build a dictionary of stations on individual rivers
    stations_per_river = stations_by_river(stations)
    
    #List of rivers we want the stations for
    wanted_rivers = ['River Aire', 'River Cam', 'River Thames']

    print(f"{number_of_rivers} stations. First 10 - {riverlist[:9]}" )
    
    for river in wanted_rivers:
        stations_on_wanted_river = stations_per_river[river]
        station_names = []
        for station in stations_on_wanted_river:
            station_names.append(station.name)
        station_names.sort()
    
        print (f"{river} has the following stations: {station_names}")



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
