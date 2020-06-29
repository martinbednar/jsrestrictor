import sys
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from testing_logs import get_page_logs


def create_driver(with_jsr):
    d = DesiredCapabilities.CHROME
    d['browserName'] = 'chrome'
    d['javascriptEnabled'] = True
    d['loggingPreferences'] = {'browser': 'ALL'}
    #d['loggingPrefs'] = {'browser': 'ALL'}

    o = Options()
    if with_jsr:
        o.add_extension('../../common_files/JSR/chrome_JSR.crx')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=d,
        options=o)
    return driver



def start_test(top_sites):
    driver = create_driver(with_jsr=False)
    for top_site in top_sites:
        logs = get_page_logs(driver, top_site)
        f = open('../data/logs/logs_without_jsr.json', 'a', newline='')
        f.write(logs.to_json() + ',')
        f.close()
    driver.close()

    driver = create_driver(with_jsr=True)
    for top_site in top_sites:
        logs = get_page_logs(driver, top_site)
        f = open('../data/logs/logs_with_jsr.json', 'a', newline='')
        f.write(logs.to_json() + ',')
        f.close()
    driver.close()
