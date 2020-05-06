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


## Test accuracy of gps.
def test_accuracy(browser, position, expected):
    if expected.geolocation.accuracy['value'] == 'REAL VALUE':
        if expected.geolocation.accuracy['accuracy'] == 'EXACTLY':
            # Values do not have to be strictly equal.
            # A deviation of less than 20 is tolerated but only when accuracy should not be exactly 0.
            assert (abs(int(position['accuracy']) - int(browser.real.geolocation.accuracy)) < 20) and (
                    position['accuracy'] != '0')
        else:
            assert is_in_accuracy(position['accuracy'], expected.geolocation.accuracy['accuracy'])
    else:
        assert position['accuracy'] == expected.geolocation.accuracy['value']


## Test altitude.
def test_altitude(browser, position, expected):
    if expected.geolocation.altitude['value'] == 'REAL VALUE':
        if expected.geolocation.altitude['accuracy'] == 'EXACTLY':
            assert position['altitude'] == browser.real.geolocation.altitude
        else:
            assert is_in_accuracy(position['altitude'], expected.geolocation.altitude['accuracy'])
    else:
        assert position['altitude'] == expected.geolocation.altitude['value']


## Test altitude accuracy.
def test_altitudeaccurac(browser, position, expected):
    if expected.geolocation.altitudeAccurac['value'] == 'REAL VALUE':
        if expected.geolocation.altitudeAccurac['accuracy'] == 'EXACTLY':
            assert position['altitudeaccurac'] == browser.real.geolocation.altitudeAccurac
        else:
            assert is_in_accuracy(position['altitudeaccurac'],
                                  expected.geolocation.altitudeAccurac['accuracy'])
    else:
        assert position['altitudeaccurac'] == expected.geolocation.altitudeAccurac['value']


## Test heading.
def test_heading(browser, position, expected):
    if expected.geolocation.heading['value'] == 'REAL VALUE':
        if expected.geolocation.heading['accuracy'] == 'EXACTLY':
            assert position['heading'] == browser.real.geolocation.heading
        else:
            assert is_in_accuracy(position['heading'], expected.geolocation.heading['accuracy'])
    else:
        assert position['heading'] == expected.geolocation.heading['value']


## Test latitude.
def test_latitude(browser, position, expected):
    if expected.geolocation.latitude['value'] == 'REAL VALUE':
        if expected.geolocation.latitude['accuracy'] == 'EXACTLY':
            # Values do not have to be strictly equal. Before comparsion, values are rounded to 1 decimal place.
            assert round(float(position['latitude']), 1) == round(float(browser.real.geolocation.latitude), 1)
        else:
            assert is_in_accuracy(round(float(position['latitude']), 3) * 1000,
                                  expected.geolocation.latitude['accuracy'] * 1000)
    else:
        assert position['latitude'] == expected.geolocation.latitude['value']


## Test longtitude.
def test_longitude(browser, position, expected):
    if expected.geolocation.longitude['value'] == 'REAL VALUE':
        if expected.geolocation.longitude['accuracy'] == 'EXACTLY':
            # Values do not have to be strictly equal. Before comparsion, values are rounded to 1 decimal place.
            assert round(float(position['longitude']), 1) == round(float(browser.real.geolocation.longitude), 1)
        else:
            assert is_in_accuracy(round(float(position['longitude']), 3) * 1000,
                                  expected.geolocation.longitude['accuracy'] * 1000)
    else:
        assert position['longitude'] == expected.geolocation.longitude['value']


## Test speed (velocity).
def test_speed(browser, position, expected):
    if expected.geolocation.speed['value'] == 'REAL VALUE':
        if expected.geolocation.speed['accuracy'] == 'EXACTLY':
            assert position['speed'] == browser.real.geolocation.speed
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
