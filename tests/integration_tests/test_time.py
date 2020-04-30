from datetime import datetime

import expected_values


def test_hours(driver):
	hours = driver.execute_script("let d = new Date(); return d.getHours()")
	assert hours == datetime.now().hour


def test_minutes(driver):
	minutes = driver.execute_script("let d = new Date(); return d.getMinutes()")
	assert minutes == datetime.now().minute


def test_seconds(driver):
	js_seconds = driver.execute_script("let d = new Date(); return d.getSeconds()")
	p_seconds = datetime.now().second
	assert (js_seconds >= (p_seconds-1)) and (js_seconds <= (p_seconds+1))


def test_milliseconds(driver):
	milliseconds = driver.execute_script("let d = new Date(); return d.getMilliseconds()")
	assert milliseconds == 0
