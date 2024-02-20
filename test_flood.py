from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    # Mock stations with different typical ranges and latest levels
    stations = build_station_list()
    update_water_levels(stations)

    tol = 0.8
    
    result = stations_level_over_threshold(stations, tol)

    for station in result:
        # latest level of each station is greater than the threshold
        assert station[1] > tol

    # check each station's latest level is greater >= to the next station's level
    assert all(result[i][1] >= result[i+1][1] for i in range(len(result)-1))


def test_stations_highest_rel_level():
    stations = build_station_list()

    update_water_levels(stations)

    N = 10

    # N stations with the highest relative water levels
    result = stations_highest_rel_level(stations, N)

    #check results is a list
    assert isinstance(result,list)

    # check result length = N
    assert len(result) == N

    # each station in the result has a >= relative water level compared to the next station
    assert all(result[i].relative_water_level() >= result[i+1].relative_water_level() for i in range(len(result)-1))
    
    # each element in  result is in  MonitoringStation class
    assert all(isinstance(result[i], MonitoringStation) for i in range(len(result)))