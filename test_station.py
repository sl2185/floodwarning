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


def test_relative_water_level(self):
    # Test Case 1: Latest level and typical range available and consistent
    station1 = MonitoringStation(1, 1, 'Station1', (0, 0), (0, 10), 'River1', 'Town1')
    station1.latest_level = 5
    assert station1.relative_water_level() == 0.5

    # Test Case 2: Latest level is None
    station2 = MonitoringStation(2, 2, 'Station2', (0, 0), (0, 10), 'River2', 'Town2')
    assert station2.relative_water_level() is None

    # Test Case 3: Typical range is inconsistent (high < low)
    station3 = MonitoringStation(3, 3, 'Station3', (0, 0), (10, 0), 'River3', 'Town3')
    station3.latest_level = 5
    assert station3.relative_water_level() is None

    # Test Case 4: Typical range is inconsistent (high - low == 0)
    station4 = MonitoringStation(4, 4, 'Station4', (0, 0), (5, 5), 'River4', 'Town4')
    station4.latest_level = 5
    assert station4.relative_water_level() is None

    # Test Case 5: Latest level and typical range available, but latest level is higher than high
    station5 = MonitoringStation(5, 5, 'Station5', (0, 0), (0, 10), 'River5', 'Town5')
    station5.latest_level = 15
    assert station5.relative_water_level() is None