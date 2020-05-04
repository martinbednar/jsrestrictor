from values_tested import TestedValues
from web_browser_type import BrowserType

level0 = TestedValues(
    user_agent={BrowserType.FIREFOX: 'REAL VALUE',
                BrowserType.CHROME: 'REAL VALUE'},
    app_version='REAL VALUE',
    platform='REAL VALUE',
    vendor={BrowserType.FIREFOX: 'REAL VALUE',
            BrowserType.CHROME: 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    do_not_track='REAL VALUE',
    cookie_enabled='REAL VALUE',
    oscpu='REAL VALUE',
    accuracy={'value': 'REAL VALUE',
              'accuracy': 'EXACTLY'},
    altitude={'value': 'REAL VALUE',
              'accuracy': 'EXACTLY'},
    altitude_accurac={'value': 'REAL VALUE',
                      'accuracy': 'EXACTLY'},
    heading={'value': 'REAL VALUE',
             'accuracy': 'EXACTLY'},
    latitude={'value': 'REAL VALUE',
              'accuracy': 'EXACTLY'},
    longitude={'value': 'REAL VALUE',
               'accuracy': 'EXACTLY'},
    speed={'value': 'REAL VALUE',
           'accuracy': 'EXACTLY'},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 'EXACTLY'},
    device_memory='REAL VALUE',
    hardware_concurrency='REAL VALUE',
    referrer='REAL VALUE',
    accuracy_of_date='REAL VALUE',
    accuracy_performance='REAL VALUE',
    protect_canvas=False
)

level1 = TestedValues(
    user_agent={BrowserType.FIREFOX: 'REAL VALUE',
                BrowserType.CHROME: 'REAL VALUE'},
    app_version='REAL VALUE',
    platform='REAL VALUE',
    vendor={BrowserType.FIREFOX: 'REAL VALUE',
            BrowserType.CHROME: 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    do_not_track="1",
    cookie_enabled=True,
    oscpu='REAL VALUE',
    accuracy={'value': 'REAL VALUE',
              'accuracy': 1230},
    altitude={'value': 'REAL VALUE',
              'accuracy': 1230},
    altitude_accurac={'value': 'REAL VALUE',
                      'accuracy': 1230},
    heading={'value': 'REAL VALUE',
             'accuracy': 1230},
    latitude={'value': 'REAL VALUE',
              'accuracy': 12.34000},
    longitude={'value': 'REAL VALUE',
               'accuracy': 12.34000},
    speed={'value': 'REAL VALUE',
           'accuracy': 1230},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 1.230},
    device_memory=4,
    hardware_concurrency=2,
    referrer='REAL VALUE',
    accuracy_of_date=1.230,
    accuracy_performance=1230,
    protect_canvas="off"
)

level2 = TestedValues(
    user_agent={BrowserType.FIREFOX: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
                BrowserType.CHROME: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/74.0.3729 Safari/537.36"},
    app_version="5.0 (Windows)",
    platform="Win32",
    vendor={BrowserType.FIREFOX: "",
            BrowserType.CHROME: "Google Inc."},
    language='REAL VALUE',
    languages='REAL VALUE',
    do_not_track="1",
    cookie_enabled=True,
    oscpu=None,
    accuracy={'value': 'REAL VALUE',
              'accuracy': 1200},
    altitude={'value': 'REAL VALUE',
              'accuracy': 1200},
    altitude_accurac={'value': 'REAL VALUE',
                      'accuracy': 1200},
    heading={'value': 'REAL VALUE',
             'accuracy': 1200},
    latitude={'value': 'REAL VALUE',
              'accuracy': 12.30000},
    longitude={'value': 'REAL VALUE',
               'accuracy': 12.30000},
    speed={'value': 'REAL VALUE',
           'accuracy': 1200},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 1.200},
    device_memory=4,
    hardware_concurrency=2,
    referrer="",
    accuracy_of_date=1.200,
    accuracy_performance=1200,
    protect_canvas="on"
)

level3 = TestedValues(
    user_agent={
        BrowserType.FIREFOX: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/74.0.3729 Safari/537.36",
        BrowserType.CHROME: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/74.0.3729 Safari/537.36"},
    app_version="5.0 (Windows)",
    platform="Win32",
    vendor={BrowserType.FIREFOX: "Google Inc.",
            BrowserType.CHROME: "Google Inc."},
    language="en-US",
    languages=["en-US", "en"],
    do_not_track="1",
    cookie_enabled=True,
    oscpu=None,
    accuracy={'value': '0',
              'accuracy': 'EXACTLY'},
    altitude={'value': '0',
              'accuracy': 'EXACTLY'},
    altitude_accurac={'value': '0',
                      'accuracy': 'EXACTLY'},
    heading={'value': 'REAL VALUE',
             'accuracy': 1200},
    latitude={'value': 'REAL VALUE',
              'accuracy': 12.30000},
    longitude={'value': 'REAL VALUE',
               'accuracy': 12.30000},
    speed={'value': 'REAL VALUE',
           'accuracy': 1200},
    timestamp={'value': '0',
               'accuracy': 'EXACTLY'},
    device_memory=4,
    hardware_concurrency=2,
    referrer="",
    accuracy_of_date=1.000,
    accuracy_performance=1000,
    protect_canvas="on"
)
