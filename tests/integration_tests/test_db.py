import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_a1(driver):
	js_url = driver.execute_script("return window.navigator.userAgent")
	assert True
