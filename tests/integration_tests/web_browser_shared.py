from web_browser_type import BrowserType
from web_browser import Browser

_shared_browser = None


def set_shared_browser(browser):
    global _shared_browser
    _shared_browser = browser


def get_shared_browser():
    global _shared_browser
    return _shared_browser
