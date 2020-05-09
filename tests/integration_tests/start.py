import pytest
import output

from web_browser import Browser
from web_browser_type import BrowserType
from web_browser_shared import set_shared_browser
from configuration import Config


## Main module - it starts and control testing.
#
#  To start testing call this module from PowerShell, CommandPrompt, Terminal or Bash: python start.py
#  For every browser and for every jsr_level defined in configuration.py set of all tests is run.
def main():
    #  For every browser from configuration.py run set of test.
    for browser_type in Config.tested_browsers:
        # create new browser of given type (Chrome, Firefox, etc.)
        my_browser = Browser(browser_type)
        # set current browser as shared browser for all testing levels (do not create new browser for every JSR_level)
        set_shared_browser(my_browser)
        # for every browser from configuration.py run set of test.
        for jsr_level in Config.tested_jsr_levels:
            output.print_testing_header(browser_type, jsr_level)
            # set jsr_level to given level
            my_browser.jsr_level = jsr_level
            # run set of tests
            pytest.main(['--ignore=./tests_definition/test_performance.py'])
            output.print_testing_footer(browser_type, jsr_level)
        # Close browser.
        my_browser.quit()


if __name__ == "__main__":
    main()
