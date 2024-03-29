import pytest
import floodsystem.flood as flood
import floodsystem.stationdata as stationdata
from floodsystem.station import MonitoringStation 

# Build station list
stations = stationdata.build_station_list();
# Update water levels
stationdata.update_water_levels(stations);


def test_stations_level_over_threshold():
	# Test that the function runs without error
	assert flood.stations_level_over_threshold(stations, .5);

	result = flood.stations_level_over_threshold(stations, .5);
	# Test that the function returns a list of tuples
	assert isinstance(result, list);
	for item in result:
		assert isinstance(item, tuple);


def test_stations_highest_rel_level():
	result = flood.stations_highest_rel_level(stations, 10);
	# Test that the function runs without error
	assert result;

	# Test that the function returns the required number of elements
	assert len(result) == 10;

	# Test that the functino returns a list of stations
	assert type(result) == list;
	for item in result:
		assert isinstance(item, MonitoringStation);