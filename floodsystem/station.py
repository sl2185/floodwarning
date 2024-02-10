# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


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
       
        if self.typical_range is None:
            #no data in typical range
            return None

        low,high = self.typical_range
        
        if low is None or high is None or high < low:
            #data is inconsistent
            return None

        #returns the ration
        return (self.latest_level) / typical_range

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
        if station.typical_range_consistent():
            # Calculate the relative water level for the current station
            relative_level = station.relative_water_level()
            
            # Check if the relative water level is not None and above the specified tolerance
            if relative_level is not None and relative_level > tol:
                # If both conditions are met, add the station and its relative level to the valid_stations list
                valid_stations.append((station, relative_level))
                
    # Sort the valid stations based on their relative water levels in descending order
    valid_stations_sorted = sorted(valid_stations, key=lambda x: x[1], reverse=True)

    # Return the sorted list of valid stations
    return valid_stations_sorted