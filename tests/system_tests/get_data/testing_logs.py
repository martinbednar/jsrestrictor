import time
import json


class Site_logs:
    site = ''
    logs = []

    def __init__(self, site, logs):
        self.site = site
        self.logs = logs

    def to_json(self):
        return '{"site": "' + self.site + '", "logs": ' + json.dumps(self.logs) + '}'


def get_page_logs(driver, top_site):
    try:
        print("Getting page started.")
        driver.get('http://www.' + top_site)
        print("Getting page finished.")
        time.sleep(5)
    except e:
        print("An exception occurred while loading page: " + top_site)
        print(e)
        logs = Site_logs(top_site, 'ERROR_WHILE_LOADING_PAGE')
    else:
        print("Getting logs started.")
        logs = Site_logs(top_site, driver.get_log('browser'))
        print("Getting logs finished.")
    return logs
