from datetime import datetime

from math_operations import is_in_accuracy


def test_hours(driver):
	js_hours = driver.execute_script("let d = new Date(); return d.getHours()")
	p_hours = datetime.now().hour
	assert abs(js_hours - p_hours) < 2


def test_minutes(driver):
	js_minutes = driver.execute_script("let d = new Date(); return d.getMinutes()")
	p_minutes = datetime.now().minute
	assert abs(js_minutes - p_minutes) < 2


def test_seconds(driver):
	js_seconds = driver.execute_script("let d = new Date(); return d.getSeconds()")
	p_seconds = datetime.now().second
	assert abs(js_seconds - p_seconds) < 2


def test_milliseconds(driver, expected):
	time_in_milliseconds = driver.execute_script("let d = new Date(); return d.getTime()")
	if expected.accuracyOfDate == 'REAL VALUE':
		assert True
	else:
		assert is_in_accuracy(time_in_milliseconds, int(expected.accuracyOfDate*1000))
