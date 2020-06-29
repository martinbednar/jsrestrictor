import sys
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from testing_logs import get_page_logs


def create_driver():
    d = DesiredCapabilities.CHROME
    d['browserName'] = 'chrome'
    d['javascriptEnabled'] = True
    d['loggingPreferences'] = {'browser': 'ALL'}
    #d['loggingPrefs'] = {'browser': 'ALL'}

    o = Options()
    #o.add_extension('D:\\Development\\jsrestrictor\\tests\\common_files\\JSR\\chrome_JSR.crx')
    #options.add_argument("user-data-dir=C:\\Users\\Martin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=d,
        options=o)
    return driver



def start_test(top_sites):
    driver = create_driver()

    for top_site in top_sites:
        logs = get_page_logs(driver, top_site)

        f = open('../data/logs/logs_without_jsr.json', 'a', newline='')
        f.write(logs.to_json() + ',')
        f.close()

    driver.close()
