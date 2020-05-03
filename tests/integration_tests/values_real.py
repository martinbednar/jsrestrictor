from values_tested import TestedValues
import values_from_browser


def init(driver):
    position = values_from_browser.get_position(driver)
    navigator = values_from_browser.get_navigator(driver)
    global real
    real = TestedValues(
        user_agent=navigator['userAgent'],
        app_version=navigator['appVersion'],
        platform=navigator['platform'],
        vendor=navigator['vendor'],
        language=navigator['language'],
        languages=navigator['languages'],
        cookie_enabled=navigator['cookieEnabled'],
        do_not_track=navigator['doNotTrack'],
        oscpu=navigator['oscpu'],
        accuracy=position['accuracy'],
        altitude=position['altitude'],
        altitude_accurac=position['altitudeaccurac'],
        heading=position['heading'],
        latitude=position['latitude'],
        longitude=position['longitude'],
        speed=position['speed'],
        timestamp=None,
        device_memory=None,
        hardware_concurrency=None,
        referrer=None,
        accuracy_of_date=None,
        accuracy_performance=None,
        protect_canvas=None
    )
    return real
