class Navigator:
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729 Safari/537.36"
    appVersion = "5.0 (Windows)"
    platform = "Win32"
    vendor = "Google Inc."
    language = "en-US, en"
    languages = "en-US, en"
    doNotTrack = "yes"
    cookieEnabled = "yes"
    oscpu = "undefined"


class Geolocation:
    latitude = 0
    longitude = 0
    altitude = 0
    latitude = 0
    altitude = 0
    heading = 0
    velocity = 0


class Device:
    deviceMemory = 4
    hardwareConcurrency = 2


class ExpectedValues:
    navigator = Navigator()
    referrer = ""
    accuracyOfDate= 1.000
    accuracyPerformance = 1000
    protectCanvas = "on"
    geolocation = Geolocation()
    device = Device()


expected_values = ExpectedValues()
