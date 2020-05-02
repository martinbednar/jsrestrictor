from datetime import datetime
import pytest
import importlib

import browser
import expected_values


@pytest.fixture(scope='module', autouse=True)
def reload_modules():
	importlib.reload(browser)


def test_hours():
	hours = browser.driver.execute_script("let d = new Date(); return d.getHours()")
	assert hours == datetime.now().hour


def test_minutes():
	minutes = browser.driver.execute_script("let d = new Date(); return d.getMinutes()")
	assert minutes == datetime.now().minute


def test_seconds():
	js_seconds = browser.driver.execute_script("let d = new Date(); return d.getSeconds()")
	p_seconds = datetime.now().second
	assert (js_seconds >= (p_seconds-1)) and (js_seconds <= (p_seconds+1))


def test_milliseconds():
	milliseconds = browser.driver.execute_script("let d = new Date(); return d.getMilliseconds()")
	assert milliseconds == 0
