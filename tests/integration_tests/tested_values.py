class Navigator:
    def __init__(self,
                 user_agent,
                 app_version,
                 platform,
                 vendor,
                 language,
                 languages,
                 do_not_track,
                 cookie_enabled,
                 oscpu):
        self.userAgent = user_agent
        self.appVersion = app_version
        self.platform = platform
        self.vendor = vendor
        self.language = language
        self.languages = languages
        self.doNotTrack = do_not_track
        self.cookieEnabled = cookie_enabled
        self.oscpu = oscpu


class Geolocation:
    def __init__(self,
                 accuracy,
                 altitude,
                 altitude_accurac,
                 heading,
                 latitude,
                 longitude,
                 speed,
                 timestamp):
        self.accuracy = accuracy
        self.altitude = altitude
        self.altitudeAccurac = altitude_accurac
        self.heading = heading
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.timestamp = timestamp


class Device:
    def __init__(self,
                 device_memory,
                 hardware_concurrency):
        self.deviceMemory = device_memory
        self.hardwareConcurrency = hardware_concurrency


class TestedValues:
    def __init__(self,
                 user_agent,
                 app_version,
                 platform,
                 vendor,
                 language,
                 languages,
                 do_not_track,
                 cookie_enabled,
                 oscpu,

                 accuracy,
                 altitude,
                 altitude_accurac,
                 heading,
                 latitude,
                 longitude,
                 speed,
                 timestamp,

                 device_memory,
                 hardware_concurrency,

                 referrer,
                 accuracy_of_date,
                 accuracy_performance,
                 protect_canvas
                 ):
        self.navigator = Navigator(
            user_agent,
            app_version,
            platform,
            vendor,
            language,
            languages,
            do_not_track,
            cookie_enabled,
            oscpu
        )
        self.geolocation = Geolocation(
            accuracy,
            altitude,
            altitude_accurac,
            heading,
            latitude,
            longitude,
            speed,
            timestamp
        )
        self.device = Device(
            device_memory,
            hardware_concurrency
        )
        self.referrer = referrer
        self.accuracyOfDate = accuracy_of_date
        self.accuracyPerformance = accuracy_performance
        self.protectCanvas = protect_canvas
