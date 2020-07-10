from enum import Enum


## Types of browser in which tests can be perform.
class BrowserType(Enum):
    def __str__(self):
        return str(self.name).title()

    CHROME = 1
