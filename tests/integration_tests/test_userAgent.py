def test_user_agent(driver, expected):
	user_agent = driver.execute_script("return window.navigator.userAgent")
	if expected.navigator.userAgent == 'REAL VALUE':
		assert True
	else:
		assert user_agent == expected.navigator.userAgent


def test_app_version(driver, expected):
	app_version = driver.execute_script("return window.navigator.appVersion")
	if expected.navigator.appVersion == 'REAL VALUE':
		assert True
	else:
		assert app_version == expected.navigator.appVersion


def test_platform(driver, expected):
	platform = driver.execute_script("return window.navigator.platform")
	if expected.navigator.platform == 'REAL VALUE':
		assert True
	else:
		assert platform == expected.navigator.platform


def test_vendor(driver, expected):
	vendor = driver.execute_script("return window.navigator.vendor")
	if expected.navigator.vendor == 'REAL VALUE':
		assert True
	else:
		assert vendor == expected.navigator.vendor


def test_language(driver, expected):
	language = driver.execute_script("return window.navigator.language")
	if expected.navigator.language == 'REAL VALUE':
		assert True
	else:
		assert language == expected.navigator.language


def test_languages(driver, expected):
	languages = driver.execute_script("return window.navigator.languages")
	if expected.navigator.languages == 'REAL VALUE':
		assert True
	else:
		assert languages == expected.navigator.languages


def test_cookie_enabled(driver, expected):
	cookie_enabled = driver.execute_script("return window.navigator.cookieEnabled")
	if expected.navigator.cookieEnabled == 'REAL VALUE':
		assert True
	else:
		assert cookie_enabled == expected.navigator.cookieEnabled


def test_do_not_track(driver, expected):
	do_not_track = driver.execute_script("return window.navigator.doNotTrack")
	if expected.navigator.doNotTrack == 'REAL VALUE':
		assert True
	else:
		assert do_not_track == expected.navigator.doNotTrack
