class MetaConfig(type):
    @property
    def jsr_level(self):
        return self._jsr_level
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
    _jsr_level = 3
    _number_of_sites_for_testing = 10
    _number_of_grid_nodes = 1
    #max is number_of_grid_nodes * 5
    _number_of_browser_instances = 1
    # in seconds
    _get_page_logs_timeout = 180
    #in seconds
    _wait_between_checks_if_logs_loaded = 9
