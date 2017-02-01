"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation
import floodsystem.stationdata as stationdata

# Build station list
stationdata.stations = build_station_list();


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

def test_relative_water_level():
    # Update water levels
    stationdata.update_water_levels(stations);

    # Test that the water levels are eiher float or None
    for station in stations:
        if station.relative_water_level() != None:
            assert type(station.relative_water_level()) == float;
        else:
            assert station.relative_water_level() == None;