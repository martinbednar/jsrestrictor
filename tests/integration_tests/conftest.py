import pytest
import importlib
import browser


@pytest.fixture(scope="session", autouse=True)
def driver():
    importlib.reload(browser)
    return browser.driver
