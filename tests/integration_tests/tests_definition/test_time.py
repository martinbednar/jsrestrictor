from datetime import datetime
import time
import random

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
	is_millisecond_rounded = True
	for _ in range(3):
		time.sleep(random.randint(1, 3))
		time_in_milliseconds = browser.driver.execute_script("let d = new Date(); return d.getTime()")
		if expected.time['accuracy'] == 'EXACTLY':
			if int(time_in_milliseconds/10)*10 != time_in_milliseconds:
				is_millisecond_rounded = False
		else:
			assert is_in_accuracy(time_in_milliseconds, int(expected.time['accuracy']*1000))

	if expected.time['accuracy'] == 'EXACTLY':
		assert not is_millisecond_rounded
