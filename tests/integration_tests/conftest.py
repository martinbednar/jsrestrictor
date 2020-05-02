import pytest
import importlib
import web_browser
import values_expected


@pytest.fixture(scope="session", autouse=True)
def browser():
    importlib.reload(web_browser)
    return web_browser.browser


@pytest.fixture(scope="session", autouse=True)
def expected():
    if web_browser.jsr_level == 0:
        return values_expected.level0
    elif web_browser.jsr_level == 1:
        return values_expected.level3
    elif web_browser.jsr_level == 2:
        return values_expected.level3
    elif web_browser.jsr_level == 3:
        return values_expected.level3
