from browser import Browser
from browser_type import BrowserType


def init():
    brows = Browser(BrowserType.CHROME)
    brows.jsr_level = 3
    global driver
    driver = brows.driver