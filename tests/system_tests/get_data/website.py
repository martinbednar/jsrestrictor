from json import dumps


class Logs:
    site = ''
    logs_without_jsr = []
    logs_with_jsr = []

    def __init__(self, site, logs_without_jsr, logs_with_jsr):
        self.site = site
        self.logs_without_jsr = logs_without_jsr
        self.logs_with_jsr = logs_with_jsr

    def to_json(self):
        return '{"site": "' + self.site + '", "logs_without_jsr": ' + dumps(self.logs_without_jsr) + ', "logs_with_jsr": ' + dumps(self.logs_with_jsr) + '}'
