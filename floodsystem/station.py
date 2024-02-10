# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

from floodsystem.utils import sorted_by_key

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    
    def typical_range_consistent(self):
        """checks the typical high/low range data for consistency"""

        if self.typical_range is None:
            #no data in typical range
            return False

        low,high = self.typical_range
        
        if low is None or high is None or high < low:
            #data is inconsistent
            return False
        
        #data is consisten
        return True

    def relative_water_level(self):
        """Returns the latest water level as a fraction of the typical range."""

        # Check if typical range consistency or latest level existence is violated
        if not self.typical_range_consistent() or self.latest_level is None:
            return None  # Return None if there's no data in the typical range or latest level is missing

        # Unpack the typical range into low and high values
        low, high = self.typical_range
    
        # Check if any of the values in the typical range are None or if the high value is less than the low value
        if low is None or high is None or high < low:
            return None  # Return None if data is inconsistent

        # Calculate the relative water level as the ratio of the latest level to the typical range
        return (self.latest_level - low) / (high - low)

def inconsistent_typical_range_stations(stations):
    """Returns a list of stations that have inconsistent data"""

    inconsistent_range_stations = []

    for station in stations:
        if  station.typical_range_consistent() == False:
            inconsistent_range_stations.append(station)

    return inconsistent_range_stations

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
        over_threshold = []
        for station, level in relative_levels:
            if level > tol:
                over_threshold.append((station, level))

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

    over_threshold = stations_level_over_threshold(stations,1)

    sorted_stations = sorted_by_key(over_threshold, 1, reverse=True)

    output=[]

    for station in sorted_stations:
        output.append(station[0])

    # Return the top N stations
    return output[:int(N)]