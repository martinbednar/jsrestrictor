import pytest

from browser import Browser
from browser_type import BrowserType
from configuration import config


for browser_type in config.browsers:
    my_browser = Browser(browser_type)
    for jsr_level in config.jsr_levels:
        my_browser.jsr_level = jsr_level
        pytest.main(['-x', 'test_gps.py', '-s'])
    my_browser.quit()
