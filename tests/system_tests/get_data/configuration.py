﻿class MetaConfig(type):
    @property
    def number_of_sites_for_testing(self):
        return self._number_of_sites_for_testing
    @property
    def number_of_grid_nodes(self):
        return self._number_of_grid_nodes
    @property
    def number_of_browser_instances(self):
        return self._number_of_browser_instances


class Config(metaclass=MetaConfig):
    _number_of_sites_for_testing = 50
    _number_of_grid_nodes = 1
    #max is number_of_grid_nodes * 5
    _number_of_browser_instances = 1
