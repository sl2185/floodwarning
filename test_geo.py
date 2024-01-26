from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
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

    # Build list of monitoringstation objects that have a specified river attribute
    test_station1 = floodsystem.station.MonitoringStation(label = 'Station1', river = 'River1',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station2 = floodsystem.station.MonitoringStation(label = 'Station2', river = 'River1',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station3 = floodsystem.station.MonitoringStation(label = 'Station3', river = 'River1',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station4 = floodsystem.station.MonitoringStation(label = 'Station4', river = 'River2',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station5 = floodsystem.station.MonitoringStation(label = 'Station5', river = 'River2',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station6 = floodsystem.station.MonitoringStation(label = 'Station6', river = 'River3',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")

    test_station_list = [ test_station1, test_station2, test_station3, test_station4, test_station5, test_station6]
    # Sort known stations by river
    result = stations_by_river(test_station_list)

    # Test that the result dictionary contains the required key value pairs of river and station lists
    for station in result['River1']:
        assert station.name in ['Station1', 'Station2', 'Station3']
    for station in result['River2']:
        assert station.name in ['Station4', 'Station5']
    for station in result['River3']:
        assert station.name in ['Station6']
 
def test_rivers_by_station_number():

    # Build list of monitoringstation objects that have a specified river attribute
    test_station1 = floodsystem.station.MonitoringStation(label = 'Station1', river = 'River1',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station2 = floodsystem.station.MonitoringStation(label = 'Station2', river = 'River2',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station3 = floodsystem.station.MonitoringStation(label = 'Station3', river = 'River2',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station4 = floodsystem.station.MonitoringStation(label = 'Station4', river = 'River1',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station5 = floodsystem.station.MonitoringStation(label = 'Station5', river = 'River3',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station6 = floodsystem.station.MonitoringStation(label = 'Station6', river = 'River3',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station7 = floodsystem.station.MonitoringStation(label = 'Station7', river = 'River3',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station8 = floodsystem.station.MonitoringStation(label = 'Station8', river = 'River3',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    test_station9 = floodsystem.station.MonitoringStation(label = 'Station9', river = 'River4',station_id="test",measure_id="test",coord= (0,0),typical_range=(0,0),town = "test")
    
    test_station_list = [test_station1,test_station2,test_station3,test_station4,test_station5,test_station6,test_station7,test_station8,test_station9]

    #Test if function will include all the rivers
    assert len(rivers_by_station_number(test_station_list,4)) == 4

    #Test if function is ordering the rivers correctly 
    for i in range(len(rivers_by_station_number(test_station_list,4)) - 1):
        assert rivers_by_station_number(test_station_list,4)[i][1] >= rivers_by_station_number(test_station_list,4)[i + 1][1]
    
    #Test the case where the Nth river has the same number of stations as another river
    assert len(rivers_by_station_number(test_station_list,2)) ==3
    
    #Test if function will return a blank list when N =0
    assert len(rivers_by_station_number(test_station_list,0)) == 0
