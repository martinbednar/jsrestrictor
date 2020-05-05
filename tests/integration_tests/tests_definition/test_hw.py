import pytest

from values_getters import get_device


@pytest.fixture(scope='module', autouse=True)
def device(browser):
	return get_device(browser.driver)


def test_device_memory(browser, device, expected):
	if expected.device.deviceMemory == 'REAL VALUE':
		assert device['deviceMemory'] == browser.real.device.deviceMemory
	else:
		assert device['deviceMemory'] == expected.device.deviceMemory


def test_hardware_concurrency(browser, device, expected):
	if expected.device.hardwareConcurrency == 'REAL VALUE':
		assert device['hardwareConcurrency'] == browser.real.device.hardwareConcurrency
	else:
		assert device['hardwareConcurrency'] == expected.device.hardwareConcurrency
