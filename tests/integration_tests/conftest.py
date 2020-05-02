import pytest
import importlib
import browser
import expected_values


@pytest.fixture(scope="session", autouse=True)
def driver():
    importlib.reload(browser)
    return browser.driver


@pytest.fixture(scope="session", autouse=True)
def expected():
    if browser.jsr_level == 0:
        return expected_values.level0
    elif browser.jsr_level == 1:
        return expected_values.level1
    elif browser.jsr_level == 2:
        return expected_values.level1
    elif browser.jsr_level == 3:
        return expected_values.level1
