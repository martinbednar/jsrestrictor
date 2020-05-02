def test_device_memory(driver, expected):
	device_memory = driver.execute_script("return window.navigator.deviceMemory")
	if expected.device.deviceMemory == 'REAL VALUE':
		assert True
	else:
		assert device_memory == expected.device.deviceMemory


def test_hardware_concurrency(driver, expected):
	hardware_concurrency = driver.execute_script("return window.navigator.hardwareConcurrency")
	if expected.device.hardwareConcurrency == 'REAL VALUE':
		assert True
	else:
		assert hardware_concurrency == expected.device.hardwareConcurrency
