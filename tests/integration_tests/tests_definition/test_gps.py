import pytest
from time import time

from values_getters import get_position
from math_operations import is_in_accuracy


@pytest.fixture(scope='module', autouse=True)
def position(browser):
    return get_position(browser.driver)


def test_accuracy(browser, position, expected):
    if expected.geolocation.accuracy['value'] == 'REAL VALUE':
        if expected.geolocation.accuracy['accuracy'] == 'EXACTLY':
            assert (abs(int(position['accuracy']) - int(browser.real.geolocation.accuracy)) < 20) and (
                    position['accuracy'] != '0')
        else:
            assert is_in_accuracy(position['accuracy'], expected.geolocation.accuracy['accuracy'])
    else:
        assert position['accuracy'] == expected.geolocation.accuracy['value']


def test_altitude(browser, position, expected):
    if expected.geolocation.altitude['value'] == 'REAL VALUE':
        if expected.geolocation.altitude['accuracy'] == 'EXACTLY':
            assert position['altitude'] == browser.real.geolocation.altitude
        else:
            assert is_in_accuracy(position['altitude'], expected.geolocation.altitude['accuracy'])
    else:
        assert position['altitude'] == expected.geolocation.altitude['value']


def test_altitudeaccurac(browser, position, expected):
    if expected.geolocation.altitudeAccurac['value'] == 'REAL VALUE':
        if expected.geolocation.altitudeAccurac['accuracy'] == 'EXACTLY':
            assert position['altitudeaccurac'] == browser.real.geolocation.altitudeAccurac
        else:
            assert is_in_accuracy(position['altitudeaccurac'],
                                  expected.geolocation.altitudeAccurac['accuracy'])
    else:
        assert position['altitudeaccurac'] == expected.geolocation.altitudeAccurac['value']


def test_heading(browser, position, expected):
    if expected.geolocation.heading['value'] == 'REAL VALUE':
        if expected.geolocation.heading['accuracy'] == 'EXACTLY':
            assert position['heading'] == browser.real.geolocation.heading
        else:
            assert is_in_accuracy(position['heading'], expected.geolocation.heading['accuracy'])
    else:
        assert position['heading'] == expected.geolocation.heading['value']


def test_latitude(browser, position, expected):
    if expected.geolocation.latitude['value'] == 'REAL VALUE':
        if expected.geolocation.latitude['accuracy'] == 'EXACTLY':
            assert round(float(position['latitude']), 1) == round(float(browser.real.geolocation.latitude), 1)
        else:
            assert is_in_accuracy(round(float(position['latitude']), 3) * 1000,
                                  expected.geolocation.latitude['accuracy'] * 1000)
    else:
        assert position['latitude'] == expected.geolocation.latitude['value']


def test_longitude(browser, position, expected):
    if expected.geolocation.longitude['value'] == 'REAL VALUE':
        if expected.geolocation.longitude['accuracy'] == 'EXACTLY':
            assert round(float(position['longitude']), 1) == round(float(browser.real.geolocation.longitude), 1)
        else:
            assert is_in_accuracy(round(float(position['longitude']), 3) * 1000,
                                  expected.geolocation.longitude['accuracy'] * 1000)
    else:
        assert position['longitude'] == expected.geolocation.longitude['value']


def test_speed(browser, position, expected):
    if expected.geolocation.speed['value'] == 'REAL VALUE':
        if expected.geolocation.speed['accuracy'] == 'EXACTLY':
            assert position['speed'] == browser.real.geolocation.speed
        else:
            assert is_in_accuracy(position['speed'], expected.geolocation.speed['accuracy'])
    else:
        assert position['speed'] == expected.geolocation.speed['value']


def test_timestamp(position, expected):
    if expected.geolocation.timestamp['value'] == 'REAL VALUE':
        if expected.geolocation.timestamp['accuracy'] == 'EXACTLY':
            assert abs(time() - int(position['timestamp'])/1000) < 1
        else:
            assert is_in_accuracy(position['timestamp'], expected.geolocation.timestamp['accuracy'])
    else:
        assert position['timestamp'] == expected.geolocation.timestamp['value']
