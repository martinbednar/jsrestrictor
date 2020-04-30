import pytest

from browser_type import BrowserType
from browser import Browser


def pytest_addoption(parser):
    parser.addoption("--jsr_level", action="store", default="2")


@pytest.fixture(scope="session", autouse=True)
def jsr_level(pytestconfig):
    return pytestconfig.getoption("jsr_level")


@pytest.fixture(scope="session", autouse=True)
def driver(jsr_level):
    print(jsr_level)
    browser = Browser(type=BrowserType.CHROME)
    browser.jsr_level = 3
    yield browser.driver
    browser.driver.quit()
