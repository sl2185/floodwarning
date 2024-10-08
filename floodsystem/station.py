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