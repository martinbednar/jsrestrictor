import pytest
from time import time

from values_getters import get_position
from math_operations import is_in_accuracy

## Setup method - it is run before gps tests execution starts.
#
#  This setup method initialize variable position that contains current data about position and
#  this variable is provided to gps tests and values in position variable are compared with expected values.
@pytest.fixture(scope='module', autouse=True)
def position(browser):
    return get_position(browser.driver)


## Test accuracy of the latitude and longitude properties in meters.
def test_accuracy(browser, position, expected):
    if expected.geolocation.accuracy['value'] == 'REAL VALUE':
        if expected.geolocation.accuracy['accuracy'] == 'EXACTLY':
            # Values do not have to be strictly equal.
            # A deviation of less than 50 meters is tolerated but only when accuracy should not be exactly 0.
            assert (abs(int(position['accuracy']) - int(browser.real.geolocation.accuracy)) < 50) and (
                    position['accuracy'] != '0')
        else:
            assert is_in_accuracy(position['accuracy'], expected.geolocation.accuracy['accuracy'])
    else:
        assert position['accuracy'] == expected.geolocation.accuracy['value']


## Test position's altitude in meters, relative to sea level.
def test_altitude(browser, position, expected):
    if expected.geolocation.altitude['value'] == 'REAL VALUE':
        if expected.geolocation.altitude['accuracy'] == 'EXACTLY':
            if position['altitude'] == "null":
                assert position['altitude'] == browser.real.geolocation.altitude
            else:
                assert abs(position['altitude'] - browser.real.geolocation.altitude) < 10
        else:
            assert is_in_accuracy(position['altitude'], expected.geolocation.altitude['accuracy'])
    else:
        assert position['altitude'] == expected.geolocation.altitude['value']


## Test accuracy of the altitude property in meters.
def test_altitudeaccurac(browser, position, expected):
    if expected.geolocation.altitudeAccurac['value'] == 'REAL VALUE':
        if expected.geolocation.altitudeAccurac['accuracy'] == 'EXACTLY':
            if position['altitude'] == "null":
                assert position['altitudeaccurac'] == browser.real.geolocation.altitudeAccurac
            else:
                assert abs(position['altitudeaccurac'] - browser.real.geolocation.altitudeAccurac) < 10
        else:
            assert is_in_accuracy(position['altitudeaccurac'],
                                  expected.geolocation.altitudeAccurac['accuracy'])
    else:
        assert position['altitudeaccurac'] == expected.geolocation.altitudeAccurac['value']


## Test heading.
#
# Heading is the direction in which the device is traveling. This value, specified in degrees,
# indicates how far off from heading true north the device is. 0 degrees represents true north,
# and the direction is determined clockwise (east is 90 degrees and west is 270 degrees).
# If speed is 0, heading is NaN. If the device is unable to provide heading information, this value is null
def test_heading(browser, position, expected):
    if expected.geolocation.heading['value'] == 'REAL VALUE':
        if expected.geolocation.heading['accuracy'] == 'EXACTLY':
            if position['heading'] == "null":
                assert position['heading'] == browser.real.geolocation.heading
            else:
                assert abs(position['heading'] - browser.real.geolocation.heading) < 30
        else:
            assert is_in_accuracy(position['heading'], expected.geolocation.heading['accuracy'])
    else:
        assert position['heading'] == expected.geolocation.heading['value']


## Test position's latitude in decimal degrees.
def test_latitude(browser, position, expected):
    if expected.geolocation.latitude['value'] == 'REAL VALUE':
        if expected.geolocation.latitude['accuracy'] == 'EXACTLY':
            # Values do not have to be strictly equal.
            assert abs(int(float(position['latitude'])) - int(float(browser.real.geolocation.latitude))) < 1
        else:
            assert is_in_accuracy(round(float(position['latitude']), 3) * 1000,
                                  expected.geolocation.latitude['accuracy'] * 1000)
    else:
        assert position['latitude'] == expected.geolocation.latitude['value']


## Test position's longitude in decimal degrees.
def test_longitude(browser, position, expected):
    if expected.geolocation.longitude['value'] == 'REAL VALUE':
        if expected.geolocation.longitude['accuracy'] == 'EXACTLY':
            # Values do not have to be strictly equal. Before comparsion, values are rounded to 1 decimal place.
            assert abs(int(float(position['longitude'])) - int(float(browser.real.geolocation.longitude))) < 1
        else:
            assert is_in_accuracy(round(float(position['longitude']), 3) * 1000,
                                  expected.geolocation.longitude['accuracy'] * 1000)
    else:
        assert position['longitude'] == expected.geolocation.longitude['value']


## Test speed (velocity) of the device in meters per second. This value can be null.
def test_speed(browser, position, expected):
    if expected.geolocation.speed['value'] == 'REAL VALUE':
        if expected.geolocation.speed['accuracy'] == 'EXACTLY':
            if position['speed'] == "null":
                assert position['speed'] == browser.real.geolocation.speed
            else:
                assert abs(position['speed'] - browser.real.geolocation.speed) < 5
        else:
            assert is_in_accuracy(position['speed'], expected.geolocation.speed['accuracy'])
    else:
        assert position['speed'] == expected.geolocation.speed['value']


## Test timestamp.
def test_timestamp(position, expected):
    if expected.geolocation.timestamp['value'] == 'REAL VALUE':
        if expected.geolocation.timestamp['accuracy'] == 'EXACTLY':
            # Values do not have to be strictly equal because executing command takes some time.
            # A deviation of less than 1 (in seconds) is tolerated.
            assert abs(time() - int(position['timestamp'])/1000) < 1
        else:
            assert is_in_accuracy(position['timestamp'], expected.geolocation.timestamp['accuracy'])
    else:
        assert position['timestamp'] == expected.geolocation.timestamp['value']
