import pytest

from browser import Browser
from browser_type import BrowserType
from configuration import config
import expected_values

for browser_type in config.browsers:
    my_browser = Browser(browser_type)
    for jsr_level in config.jsr_levels:
        my_browser.jsr_level = jsr_level
        pytest.main()
    my_browser.quit()
