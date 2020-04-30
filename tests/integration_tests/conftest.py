import pytest

from Browser_type import BrowserType
from Browser import Browser


@pytest.fixture(scope="session", autouse=True)
def driver():
    browser = Browser(type=BrowserType.FIREFOX)
    browser.jsr_level = 3
    yield browser.driver
    browser.driver.quit()
