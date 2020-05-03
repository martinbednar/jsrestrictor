from datetime import datetime

from math_operations import is_in_accuracy


def test_hours(browser):
	js_hours = browser.driver.execute_script("let d = new Date(); return d.getHours()")
	p_hours = datetime.now().hour
	assert abs(js_hours - p_hours) < 2


def test_minutes(browser):
	js_minutes = browser.driver.execute_script("let d = new Date(); return d.getMinutes()")
	p_minutes = datetime.now().minute
	assert abs(js_minutes - p_minutes) < 2


def test_seconds(browser):
	js_seconds = browser.driver.execute_script("let d = new Date(); return d.getSeconds()")
	p_seconds = datetime.now().second
	assert abs(js_seconds - p_seconds) < 2


def test_milliseconds(browser, expected):
	time_in_milliseconds = browser.driver.execute_script("let d = new Date(); return d.getTime()")
	if expected.accuracyOfDate == 'REAL VALUE':
		assert True
	else:
		assert is_in_accuracy(time_in_milliseconds, int(expected.accuracyOfDate*1000))
