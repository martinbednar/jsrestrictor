def test_device_memory(driver, expected):
	device_memory = driver.execute_script("return window.navigator.deviceMemory")
	assert device_memory == expected.device.deviceMemory


def test_hardware_concurrency(driver, expected):
	hardware_concurrency = driver.execute_script("return window.navigator.hardwareConcurrency")
	assert hardware_concurrency == expected.device.hardwareConcurrency
