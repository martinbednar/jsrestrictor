import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import expected_values
from driver import driver


@pytest.fixture(scope='module', autouse=True)
def position():
	show_gps_button = driver.find_element_by_xpath("//button[text()='Show GPS data']")
	show_gps_button.click()
	WebDriverWait(driver, 10).until(
		ec.presence_of_element_located((By.ID, 'mapnavi'))
	)
	location = driver.find_element_by_id('placeToWriteGPSDetails').text
	location = location.replace(" ", "").split()
	my_dict = {}
	for property in location:
		property = property.split(':')
		my_dict[property[0].lower()] = property[1]
	yield my_dict


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
