from web_browser_type import BrowserType
from test_type import TestType


class MetaConfig(type):
    @property
    def sites_to_test_csv_path(self):
        return self._sites_to_test_csv_path
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
    def is_grid_server_on_this_device(self):
        return self._is_grid_server_on_this_device
    @property
    def grid_server_ip_address(self):
        return self._grid_server_ip_address
    @property
    def number_of_grid_nodes_on_this_device(self):
        return self._number_of_grid_nodes_on_this_device
    @property
    def number_of_concurent_sites_testing(self):
        return self._number_of_concurent_sites_testing
    @property
    def get_page_logs_timeout(self):
        return self._get_page_logs_timeout
    @property
    def wait_between_checks_if_logs_loaded(self):
        return self._wait_between_checks_if_logs_loaded
    @property
    def selenium_server_jar_path(self):
        return self._selenium_server_jar_path
    @property
    def chrome_driver_path(self):
        return self._chrome_driver_path


class Config(metaclass=MetaConfig):
    _sites_to_test_csv_path = './tranco/top_sites.csv'
    _tested_browsers = [BrowserType.CHROME]
    _jsr_level = 2
    _perform_tests = [TestType.LOGS, TestType.SCREENSHOTS]

    _number_of_sites_for_testing = 6
    _is_grid_server_on_this_device = True
    _grid_server_ip_address = 'localhost'
    _number_of_grid_nodes_on_this_device = 1
    #max is number_of_grid_nodes * 5
    _number_of_concurent_sites_testing = 1
    # in seconds
    _get_page_logs_timeout = 180
    #in seconds
    _wait_between_checks_if_logs_loaded = 9

    _selenium_server_jar_path = './selenium/selenium-server-standalone-3.141.59.jar'
    _chrome_driver_path = '../../common_files/webbrowser_drivers/chromedriver.exe'
