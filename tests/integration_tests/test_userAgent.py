from browser import driver
import expected_values


def test_user_agent():
	user_agent = driver.execute_script("return window.navigator.userAgent")
	assert user_agent == expected_values.level1.navigator.userAgent


def test_app_version():
	app_version = driver.execute_script("return window.navigator.appVersion")
	assert app_version == expected_values.level1.navigator.appVersion


def test_platform():
	platform = driver.execute_script("return window.navigator.platform")
	assert platform == expected_values.level1.navigator.platform


def test_vendor():
	vendor = driver.execute_script("return window.navigator.vendor")
	assert vendor == expected_values.level1.navigator.vendor


def test_language():
	language = driver.execute_script("return window.navigator.language")
	assert language == expected_values.level1.navigator.language


def test_languages():
	languages = driver.execute_script("return window.navigator.languages")
	assert languages == expected_values.level1.navigator.languages


def test_cookie_enabled():
	cookie_enabled = driver.execute_script("return window.navigator.cookieEnabled")
	assert cookie_enabled == expected_values.level1.navigator.cookieEnabled


def test_do_not_track():
	do_not_track = driver.execute_script("return window.navigator.doNotTrack")
	assert do_not_track == expected_values.level1.navigator.doNotTrack
