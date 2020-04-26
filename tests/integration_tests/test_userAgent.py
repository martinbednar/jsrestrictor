import setting


def test_user_agent(driver):
	user_agent = driver.execute_script("return window.navigator.userAgent")
	assert user_agent == setting.expected_values.navigator.userAgent


def test_app_version(driver):
	app_version = driver.execute_script("return window.navigator.appVersion")
	assert app_version == setting.expected_values.navigator.appVersion


def test_platform(driver):
	platform = driver.execute_script("return window.navigator.platform")
	assert platform == setting.expected_values.navigator.platform


def test_vendor(driver):
	vendor = driver.execute_script("return window.navigator.vendor")
	assert vendor == setting.expected_values.navigator.vendor


def test_language(driver):
	language = driver.execute_script("return window.navigator.language")
	assert language == setting.expected_values.navigator.language


def test_languages(driver):
	languages = driver.execute_script("return window.navigator.languages")
	assert languages == setting.expected_values.navigator.languages


def test_cookie_enabled(driver):
	cookie_enabled = driver.execute_script("return window.navigator.cookieEnabled")
	assert cookie_enabled == setting.expected_values.navigator.cookieEnabled


def test_do_not_track(driver):
	do_not_track = driver.execute_script("return window.navigator.doNotTrack")
	assert do_not_track == setting.expected_values.navigator.doNotTrack
