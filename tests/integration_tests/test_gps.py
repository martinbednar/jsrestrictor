import time
import pytest

import setting


@pytest.fixture(scope='module',autouse=True)
def position(driver):
	show_gps_button = driver.find_element_by_xpath("//button[text()='Show GPS data']")
	show_gps_button.click()
	time.sleep(5)
	location = driver.find_element_by_xpath("//div[@id='placeToWriteGPSDetails']").text
	location = location.replace(" ", "").split()
	myDict = {}
	for property in location:
		property = property.split(':')
		myDict[property[0].lower()] = property[1]
	return myDict


def test_accuracy(position):
	assert position['accuracy'] == '0'


def test_altitude(position):
	assert position['altitude'] == '0'


def test_altitudeaccurac(position):
	assert position['altitudeaccurac'] == '0'


def test_heading(position):
	assert position['heading'] == '0'


def test_latitude(position):
	assert position['latitude'] == '0'


def test_longitude(position):
	assert position['longitude'] == '0'


def test_speed(position):
	assert position['speed'] == '0'


def test_timestamp(position):
	assert position['timestamp'] == '0'
