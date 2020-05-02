import pytest
import importlib

import browser
import expected_values


@pytest.fixture(scope='module', autouse=True)
def reload_modules():
	importlib.reload(browser)


def test_device_memory():
	device_memory = browser.driver.execute_script("return window.navigator.deviceMemory")
	assert device_memory == expected_values.level1.device.deviceMemory


def test_hardware_concurrency():
	hardware_concurrency = browser.driver.execute_script("return window.navigator.hardwareConcurrency")
	assert hardware_concurrency == expected_values.level1.device.hardwareConcurrency
