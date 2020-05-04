import pytest

from web_browser import Browser
from web_browser_type import BrowserType
from web_browser_shared import set_shared_browser
from configuration import Config


for browser_type in Config.tested_browsers:
    my_browser = Browser(browser_type)
    set_shared_browser(my_browser)
    for jsr_level in Config.tested_jsr_levels:
        my_browser.jsr_level = jsr_level
        pytest.main(['test_hw.py', '-s'])
    my_browser.quit()
