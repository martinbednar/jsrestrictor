from datetime import datetime

import setting


def test_hours(driver):
	hours = driver.execute_script("let d = new Date(); return d.getHours()")
	assert hours == datetime.now().hour


def test_minutes(driver):
	minutes = driver.execute_script("let d = new Date(); return d.getMinutes()")
	assert minutes == datetime.now().minute


def test_seconds(driver):
	seconds = driver.execute_script("let d = new Date(); return d.getSeconds()")
	assert seconds == datetime.now().second


def test_milliseconds(driver):
	milliseconds = driver.execute_script("let d = new Date(); return d.getMilliseconds()")
	assert milliseconds == 0
