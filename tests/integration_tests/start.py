import pytest

import browser
from browser_type import BrowserType


myChrome = browser.Browser(BrowserType.CHROME)
myChrome.jsr_level = 3
pytest.main()
myChrome.driver.quit()