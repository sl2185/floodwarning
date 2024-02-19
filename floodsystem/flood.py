from .utils import sorted_by_key
def stations_level_over_threshold(stations, tol):
    """
    Returns a list of tuples containing stations and their relative water levels 
    that are above a specified tolerance level.
    """
    valid_stations = []

    for station in stations:

        # Check if the typical range of the station is consistent
        if station.typical_range_consistent() and station.latest_level is not None:
            # Calculate the relative water level for the current station
            valid_stations.append(station)
            
    #list of tuples with station and water level
    relative_levels = [(station, station.relative_water_level()) for station in valid_stations]
        
    # Check if the relative water level is not None and above the specified tolerance
    over_threshold = [(station, level) for station, level in relative_levels if level > tol]

    # Sort the valid stations based on their relative water levels in descending order
    sorted_stations = sorted_by_key(over_threshold, 1, reverse = True)

    # Return the sorted list of valid stations
    return sorted_stations


def stations_highest_rel_level(stations, N):
    """
    Returns a list of the N stations at which the water level, 
    relative to the typical range, is highest. The list is sorted in 
    descending order by relative level.
    """
    # stations with levels over a threshold 1
    over_threshold = stations_level_over_threshold(stations,1)

    #sort stations on their level
    sorted_stations = sorted_by_key(over_threshold, 1, reverse=True)

    output=[]

    for station in sorted_stations:
        output.append(station[0])

    # Return the top N stations
    return output[:int(N)]