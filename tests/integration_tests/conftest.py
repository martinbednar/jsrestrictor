import pytest

from browser_type import BrowserType
from browser import Browser


@pytest.fixture(scope="session", autouse=True)
def driver():
    browser = Browser(type=BrowserType.CHROME)
    browser.jsr_level = 3
    yield browser.driver
    browser.driver.quit()
