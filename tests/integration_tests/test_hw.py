from browser import driver
import expected_values


def test_device_memory():
	device_memory = driver.execute_script("return window.navigator.deviceMemory")
	assert device_memory == expected_values.level1.device.deviceMemory


def test_hardware_concurrency():
	hardware_concurrency = driver.execute_script("return window.navigator.hardwareConcurrency")
	assert hardware_concurrency == expected_values.level1.device.hardwareConcurrency
