from web_browser_type import BrowserType
from test_type import TestType


class MetaConfig(type):
    @property
    def tested_browsers(self):
        return self._tested_browsers
    @property
    def jsr_level(self):
        return self._jsr_level
    @property
    def perform_tests(self):
        return self._perform_tests
    @property
    def number_of_sites_for_testing(self):
        return self._number_of_sites_for_testing
    @property
    def number_of_grid_nodes(self):
        return self._number_of_grid_nodes
    @property
    def number_of_browser_instances(self):
        return self._number_of_browser_instances
    @property
    def get_page_logs_timeout(self):
        return self._get_page_logs_timeout
    @property
    def wait_between_checks_if_logs_loaded(self):
        return self._wait_between_checks_if_logs_loaded


class Config(metaclass=MetaConfig):
    _tested_browsers = [BrowserType.CHROME]
    _jsr_level = 3
    _perform_tests = [TestType.LOGS, TestType.SCREENSHOTS]
    _number_of_sites_for_testing = 10
    _number_of_grid_nodes = 1
    #max is number_of_grid_nodes * 5
    _number_of_browser_instances = 1
    # in seconds
    _get_page_logs_timeout = 180
    #in seconds
    _wait_between_checks_if_logs_loaded = 9
