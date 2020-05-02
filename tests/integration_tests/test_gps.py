import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope='module', autouse=True)
def position(driver):
	driver.find_element_by_xpath("//button[text()='Show GPS data']").click()
	WebDriverWait(driver, 10).until(
		ec.presence_of_element_located((By.ID, 'mapnavi'))
	)
	location = driver.find_element_by_id('placeToWriteGPSDetails').text
	location = location.replace(" ", "").split()
	my_dict = {}
	for property in location:
		property = property.split(':')
		my_dict[property[0].lower()] = property[1]
	return my_dict


def test_accuracy(position, expected):
	assert position['accuracy'] == expected.geolocation.accuracy


def test_altitude(position, expected):
	assert position['altitude'] == expected.geolocation.altitude


def test_altitudeaccurac(position, expected):
	assert position['altitudeaccurac'] == expected.geolocation.altitudeAccurac


def test_heading(position, expected):
	assert position['heading'] == expected.geolocation.heading


def test_latitude(position, expected):
	assert position['latitude'] == expected.geolocation.latitude


def test_longitude(position, expected):
	assert position['longitude'] == expected.geolocation.longitude


def test_speed(position, expected):
	assert position['speed'] == expected.geolocation.speed


def test_timestamp(position, expected):
	assert position['timestamp'] == expected.geolocation.timestamp
