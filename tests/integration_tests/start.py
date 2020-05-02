import pytest

from web_browser import Browser
from web_browser_type import BrowserType
from configuration import config


for browser_type in config.browsers:
    my_browser = Browser(browser_type)
    for jsr_level in config.jsr_levels:
        my_browser.jsr_level = jsr_level
        pytest.main(['test_gps.py'])
    my_browser.quit()
