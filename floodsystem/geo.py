# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from .utils import sorted_by_key  # noqa
import haversine #calculating distance from two points

def stations_by_distance(stations, p):
    '''Task 1A returns a sorted list of (station, distance) tuples with distance from p'''
    
    stations_distance_p = []

    for station in stations:

        #uses haversine fuction from python
        distance_p = haversine.haversine(station.coord, p)

        #tuple with station and its distance from p
        statDisTup = (station, distance_p)

        #adds this station onto the preexisting tuple
        stations_distance_p.append(statDisTup)

    #sorting the stations
    sorted_stations_distance_p = sorted_by_key(stations_distance_p, 1)

    return (sorted_stations_distance_p)

def stations_within_radius(stations, centre, r):
    '''returns a list of all stations within radius r of a geographic coordinate x'''

    stations_in_radius = []

    #sorts stations by their distance from the centre
    sorted_stations_distance_p = stations_by_distance(stations, centre)

    #if the distance from the centre is less than radius, it is added to the tuple
    for station in sorted_stations_distance_p:
        if station[1] < r:
            stations_in_radius.append(station[0])
        else:
            break
    return stations_in_radius

    
def rivers_with_station(stations):
    '''
    Returns a list of rivers with a monitoring stations

    Args:
        stations(list): A list of MonitoringStations objects

    Returns:
        unique_rivers: a list of rivers with no duplicates
    '''

    unique_rivers = [] #creates a blank list to store river values

    for station in stations:
         if station.river not in unique_rivers:
            unique_rivers.append(station.river)
    
    return unique_rivers

def stations_by_river(stations):
    '''Maps river names to a list of stations on that river
    
    Args:
        stations(list): A list of MonitoringStations objects
    
     Returns:
        station_river_dict(dict): A dictionary that maps river names (key) to a list of station objects '''
    
    station_river_dict = {} #create an empty dictionary

    
    for station in stations.sort():
        if station.river not in station_river_dict: 
            station_river_dict[station.river] = [] #create an empty list if the river is not already inside the dictionary keys
        station_river_dict[station.river].append(station) #adds the station to the river's list of stations
    
    return station_river_dict[station.river] 
    