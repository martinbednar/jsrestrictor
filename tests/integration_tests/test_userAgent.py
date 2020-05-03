from values_from_browser import get_navigator


def test_user_agent(browser, expected):
	if expected.navigator.userAgent == 'REAL VALUE':
		assert get_navigator(browser.driver)['userAgent'] == browser.real.navigator.userAgent
	else:
		assert get_navigator(browser.driver)['userAgent'] == expected.navigator.userAgent


def test_app_version(browser, expected):
	if expected.navigator.appVersion == 'REAL VALUE':
		assert get_navigator(browser.driver)['appVersion'] == browser.real.navigator.appVersion
	else:
		assert get_navigator(browser.driver)['appVersion'] == expected.navigator.appVersion


def test_platform(browser, expected):
	if expected.navigator.platform == 'REAL VALUE':
		assert get_navigator(browser.driver)['platform'] == browser.real.navigator.platform
	else:
		assert get_navigator(browser.driver)['platform'] == expected.navigator.platform


def test_vendor(browser, expected):
	if expected.navigator.vendor == 'REAL VALUE':
		assert get_navigator(browser.driver)['vendor'] == browser.real.navigator.vendor
	else:
		assert get_navigator(browser.driver)['vendor'] == expected.navigator.vendor


def test_language(browser, expected):
	if expected.navigator.language == 'REAL VALUE':
		assert get_navigator(browser.driver)['language'] == browser.real.navigator.language
	else:
		assert get_navigator(browser.driver)['language'] == expected.navigator.language


def test_languages(browser, expected):
	if expected.navigator.languages == 'REAL VALUE':
		assert get_navigator(browser.driver)['languages'] == browser.real.navigator.languages
	else:
		assert get_navigator(browser.driver)['languages'] == expected.navigator.languages


def test_cookie_enabled(browser, expected):
	if expected.navigator.cookieEnabled == 'REAL VALUE':
		assert get_navigator(browser.driver)['doNotTrack'] == browser.real.navigator.doNotTrack
	else:
		assert get_navigator(browser.driver)['cookieEnabled'] == expected.navigator.cookieEnabled


def test_do_not_track(browser, expected):
	if expected.navigator.doNotTrack == 'REAL VALUE':
		assert get_navigator(browser.driver)['cookieEnabled'] == browser.real.navigator.cookieEnabled
	else:
		assert get_navigator(browser.driver)['doNotTrack'] == expected.navigator.doNotTrack


def test_oscpu(browser, expected):
	if expected.navigator.doNotTrack == 'REAL VALUE':
		assert get_navigator(browser.driver)['oscpu'] == browser.real.navigator.oscpu
	else:
		assert get_navigator(browser.driver)['oscpu'] == expected.navigator.oscpu
