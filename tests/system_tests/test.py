import sys
import csv
import time
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Log:
    web_page = ''
    level = ''
    message = ''
    source = ''
    timestamp = ''

    def __init__(self, w, l, m, s, t):
        self.web_page = w
        self.level = l
        self.message = m
        self.source = s
        self.timestamp = t

    def __eq__(self, other):
        if self.web_page == other.web_page \
                and self.level == other.level \
                and self.message == other.message \
                and self.source == other.source:
            return True
        else:
            return False

    def __str__(self):
        return """{ web_page: %s\n \
level: %s\n \
message: %s\n \
source: %s\n \
timestamp: %s }""" % (self.web_page, self.level, self.message, self.source, self.timestamp)

    def __iter__(self):
        return iter([self.web_page, self.level, self.message, self.source, self.timestamp])


def create_driver():
    d = DesiredCapabilities.CHROME
    d['browserName'] = 'chrome'
    d['javascriptEnabled'] = True
    d['loggingPreferences'] = {'browser': 'ALL'}
    #d['loggingPrefs'] = {'browser': 'ALL'}

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=d)
    return driver


def get_page_logs(driver, top_site):
    try:
        print("Getting page started.")
        driver.get('http://www.' + top_site)
        print("Getting page finished.")
        time.sleep(5)
    except:
        print("An exception occurred while loading page: " + top_site)
        logs = [Log(top_site, 'ERROR', 'ERROR_WHILE_LOADING_PAGE', '', '')]
    else:
        logs = []
        print("Getting logs started.")
        driver_logs = driver.get_log('browser')
        print(driver_logs)
        for log in driver_logs:
            logs.append(Log(top_site, log['level'], log['message'], log['source'], log['timestamp']))
            print("Log.")
        print("Getting logs finished.")
    return logs


def main():
    driver = create_driver()

    logs = []
    f = open('logs_without_jsr.csv', 'a', newline='')
    logs_writer = csv.writer(f)
    logs = get_page_logs(driver, sys.argv[1])
    logs_writer.writerows(logs)
    f.close()

    driver.close()


if __name__ == "__main__":
    main()
