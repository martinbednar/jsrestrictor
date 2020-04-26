import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import expected_values


def test_a2(driver):
	js_url = driver.execute_script("return window.navigator.appVersion")
	assert js_url == expected_values.expected_values.navigator.appVersion
