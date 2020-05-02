from values_tested import TestedValues
from position import get_position


def init(driver):
    position = get_position(driver)
    global real
    real = TestedValues(
        user_agent=None,
        app_version=None,
        platform=None,
        vendor=None,
        language=None,
        languages=None,
        do_not_track=None,
        cookie_enabled=None,
        oscpu=None,
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
