import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import setting


def test_device_memory(driver):
	device_memory = driver.execute_script("return window.navigator.deviceMemory")
	assert device_memory == setting.expected_values.device.deviceMemory


def test_hardware_concurrency(driver):
	hardware_concurrency = driver.execute_script("return window.navigator.hardwareConcurrency")
	assert hardware_concurrency == setting.expected_values.device.hardwareConcurrency
