import pytest

import browser
from browser_type import BrowserType


myChrome = browser.Browser(BrowserType.FIREFOX)
myChrome.jsr_level = 3
pytest.main()
myChrome.quit()