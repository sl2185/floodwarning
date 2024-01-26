from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_river
import haversine #calculating distance from two points
import floodsystem.station
def test_stations_by_distance():
    # Build list of stations
    test_stations = build_station_list()

    test_ten_closest = stations_by_distance(test_stations,(52.2053, 0.1218))[:10]
    
    assert len(test_ten_closest) == 10


def test_stations_within_radius():

    # Build list of stations
    test_stations = build_station_list()

    # Test the function with a known center and radius
    centre = (52.2053, 0.1218)
    radius = 10
    result = stations_within_radius(test_stations, centre, radius)

    # Check if all stations in the result are within the specified radius
    for station in result:
        distance = haversine.haversine(station.coord, centre)
        assert distance < radius, f"Station {station.name} is outside the specified radius."

class StationsByRiverTestError(Exception):
    pass

#test for stations_by_river function 
def test_stations_by_river():
    try:
        # Build list of monitoringstation objects that have a specified river attribute
        
        test_station1 = floodsystem.station.MonitoringStation(label = Station1, river = River1)
        test_station2 = floodsystem.station.MonitoringStation(label = Station2, river = River1)
        test_station3 = floodsystem.station.MonitoringStation(label = Station3, river = River1)
        test_station4 = floodsystem.station.MonitoringStation(label = Station4, river = River2)
        test_station5 = floodsystem.station.MonitoringStation(label = Station5, river = River2)
        test_station6 = floodsystem.station.MonitoringStation(label = Station6, river = River3)

        test_station_list = [ test_station1, test_station2, test_station3, test_station4, test_station5, test_station6]

        result = stations_by_river(test_station_list)
    
        if "Station1" and "Station2" and "Station3 " not in result[River1]:
            raise StationsByRiverTestError("Test failed for stations_by_river")
        
        elif "Station4" and "Station5" not in result[River2]:
            raise StationsByRiverTestError("Test failed for stations_by_river")
        
        elif "Station6" not in result[River3]:
            raise StationsByRiverTestError("Test failed for stations_by_river")
    except:
        print("An unexpected error occurred")
    


