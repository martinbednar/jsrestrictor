from web_browser_type import BrowserType
from web_browser import Browser

shared_browser = None


def set_shared_browser(browser):
    global shared_browser
    shared_browser = browser


def get_shared_browser():
    global shared_browser
    return shared_browser
