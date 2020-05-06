import pytest

from values_getters import get_canvas
from values_canvas import EMPTY_CANVAS_LENGTH


## Setup method - it is run before referrer test execution starts.
#
#  This setup method initialize variable referrer that contains current data about referrer and
#  this variable is provided to referrer test and value in referrer variable is compared with expected values.
@pytest.fixture(scope='module', autouse=True)
def canvas(browser):
    return get_canvas(browser.driver)


## Test referrer - where the page was navigated from.
def test_canvas(browser, canvas, expected):
    if expected.canvas == 'REAL VALUE':
        assert len(canvas) > EMPTY_CANVAS_LENGTH[browser.type]
    else:
        # expected.canvas[browser.type] contains empty canvas of given browser type
        assert canvas == expected.canvas[browser.type]
