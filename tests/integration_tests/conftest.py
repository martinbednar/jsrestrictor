import pytest
from web_browser_shared import get_shared_browser
import values_expected


@pytest.fixture(scope="session", autouse=True)
def browser():
    return get_shared_browser()


@pytest.fixture(scope="session", autouse=True)
def expected():
    if get_shared_browser().jsr_level == 0:
        return values_expected.level0
    elif get_shared_browser().jsr_level == 1:
        return values_expected.level1
    elif get_shared_browser().jsr_level == 2:
        return values_expected.level2
    elif get_shared_browser().jsr_level == 3:
        return values_expected.level3
