from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
import haversine #calculating distance from two points

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
