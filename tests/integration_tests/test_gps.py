import pytest

from values_from_browser import get_position


@pytest.fixture(scope='module', autouse=True)
def position(browser):
	return get_position(browser.driver)


def test_accuracy(browser, position, expected):
	if expected.geolocation.accuracy == 'REAL VALUE':
		assert (abs(int(position['accuracy']) - int(browser.real.geolocation.accuracy)) < 20) and (position['accuracy'] != '0')
	else:
		assert position['accuracy'] == expected.geolocation.accuracy


def test_altitude(browser, position, expected):
	if expected.geolocation.altitude == 'REAL VALUE':
		assert position['altitude'] == browser.real.geolocation.altitude
	else:
		assert position['altitude'] == expected.geolocation.altitude


def test_altitudeaccurac(browser, position, expected):
	if expected.geolocation.altitudeAccurac == 'REAL VALUE':
		assert position['altitudeaccurac'] == browser.real.geolocation.altitudeAccurac
	else:
		assert position['altitudeaccurac'] == expected.geolocation.altitudeAccurac


def test_heading(browser, position, expected):
	if expected.geolocation.heading == 'REAL VALUE':
		assert position['heading'] == browser.real.geolocation.heading
	else:
		assert position['heading'] == expected.geolocation.heading


def test_latitude(browser, position, expected):
	if expected.geolocation.latitude == 'REAL VALUE':
		assert round(float(position['latitude']), 1) == round(float(browser.real.geolocation.latitude), 1)
	else:
		assert position['latitude'] == expected.geolocation.latitude


def test_longitude(browser, position, expected):
	if expected.geolocation.latitude == 'REAL VALUE':
		assert round(float(position['longitude']), 1) == round(float(browser.real.geolocation.longitude), 1)
	else:
		assert position['longitude'] == expected.geolocation.longitude


def test_speed(browser, position, expected):
	if expected.geolocation.speed == 'REAL VALUE':
		assert position['speed'] == browser.real.geolocation.speed
	else:
		assert position['speed'] == expected.geolocation.speed


def test_timestamp(browser, position, expected):
	if expected.geolocation.timestamp == 'REAL VALUE':
		assert True
	else:
		assert position['timestamp'] == expected.geolocation.timestamp
