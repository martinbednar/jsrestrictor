import pytest

from web_browser import Browser
from web_browser_type import BrowserType
from configuration import Config


for browser_type in config.tested_browsers:
    my_browser = Browser(browser_type)
    for jsr_level in config.tested_jsr_levels:
        my_browser.jsr_level = jsr_level
        pytest.main()
    my_browser.quit()
