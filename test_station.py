# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    
    # Test Case 1: Consistent range
    station1 = MonitoringStation(1, 1, 'Station1', (0, 0), (10, 20), 'River1', 'Town1')
    assert station1.typical_range_consistent() is True

    # Test Case 2: Inconsistent range (high < low)
    station2 = MonitoringStation(2, 1, 'Station2', (0, 0), (30, 20), 'River2', 'Town2')
    assert station2.typical_range_consistent() is False

    # Test Case 3: Inconsistent range (low is None)
    station3 = MonitoringStation(3, 1, 'Station3', (0, 0), (None, 20), 'River3', 'Town3')
    assert station3.typical_range_consistent() is False

    # Test Case 4: Inconsistent range (high is None)
    station4 = MonitoringStation(4, 1, 'Station4', (0, 0), (10, None), 'River4', 'Town4')
    assert station4.typical_range_consistent() is False

    # Test Case 5: Inconsistent range (typical_range is None)
    station5 = MonitoringStation(5, 1, 'Station5', (0, 0), None, 'River5', 'Town5')
    assert station5.typical_range_consistent() is False