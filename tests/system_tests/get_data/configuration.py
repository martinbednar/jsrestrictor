from web_browser_type import BrowserType
from test_type import TestType


class MetaConfig(type):
    @property
    def sites_to_test_csv_path(self):
        return self._sites_to_test_csv_path
    @property
    def number_of_sites_for_testing(self):
        return self._number_of_sites_for_testing
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
    def grid_server_ip_address(self):
        return self._grid_server_ip_address
    @property
    def number_of_grid_nodes_on_this_device(self):
        return self._number_of_grid_nodes_on_this_device
    @property
    def number_of_concurent_sites_testing(self):
        return self._number_of_concurent_sites_testing
    @property
    def get_page_data_timeout(self):
        return self._get_page_data_timeout
    @property
    def wait_between_checks_if_page_data_loaded(self):
        return self._wait_between_checks_if_page_data_loaded
    @property
    def selenium_server_jar_path(self):
        return self._selenium_server_jar_path
    @property
    def chrome_driver_path(self):
        return self._chrome_driver_path
    @property
    def jsr_extension_for_chrome_path(self):
        return self._jsr_extension_for_chrome_path


class Config(metaclass=MetaConfig):
    _sites_to_test_csv_path = './top_sites/tranco.csv'
    _number_of_sites_for_testing = 6
    _tested_browsers = [BrowserType.CHROME]
    _jsr_level = 2
    _perform_tests = [TestType.LOGS, TestType.SCREENSHOTS]

    _grid_server_ip_address = 'localhost'
    _number_of_grid_nodes_on_this_device = 1
    #max is number_of_grid_nodes * 5
    _number_of_concurent_sites_testing = 1

    # in seconds
    _get_page_data_timeout = 180
    #in seconds
    _wait_between_checks_if_page_data_loaded = 9

    _selenium_server_jar_path = './selenium/selenium-server-standalone-3.141.59.jar'
    _chrome_driver_path = '../../common_files/webbrowser_drivers/chromedriver.exe'
    _jsr_extension_for_chrome_path = '../../common_files/JSR/chrome_JSR.crx'
