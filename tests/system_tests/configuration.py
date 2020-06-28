class MetaConfig(type):
    @property
    def number_of_sites_for_testing(self):
        return self._number_of_sites_for_testing
    @property
    def number_of_grid_nodes(self):
        return self._number_of_grid_nodes


class Config(metaclass=MetaConfig):
    _number_of_sites_for_testing = 5
    _number_of_grid_nodes = 2
