import pytest
import importlib
from web_browser_shared import shared_browser
import values_expected


@pytest.fixture(scope="session", autouse=True)
def browser():
    #importlib.reload(web_browser_shared)
    return shared_browser


@pytest.fixture(scope="session", autouse=True)
def expected():
    #importlib.reload(web_browser_shared)
    print(shared_browser)
    if shared_browser.jsr_level == 0:
        return values_expected.level0
    elif shared_browser.jsr_level == 1:
        return values_expected.level1
    elif shared_browser.jsr_level == 2:
        return values_expected.level2
    elif shared_browser.jsr_level == 3:
        return values_expected.level3
