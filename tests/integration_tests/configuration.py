from web_browser_type import BrowserType


class Config:
    def __init__(self):
        self.browsers = [BrowserType.CHROME, BrowserType.FIREFOX]
        self.jsr_levels = [0, 1, 2, 3]


config = Config()
