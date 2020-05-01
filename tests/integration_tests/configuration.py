from browser_type import BrowserType


class Config:
    def __init__(self):
        self.browsers = [BrowserType.FIREFOX, BrowserType.CHROME]
        self.jsr_levels = [3]


config = Config()