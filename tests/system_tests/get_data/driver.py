from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def create_driver(with_jsr):
    d = DesiredCapabilities.CHROME
    d['browserName'] = 'chrome'
    d['javascriptEnabled'] = True
    d['loggingPreferences'] = {'browser': 'ALL'}

    o = Options()
    if with_jsr:
        o.add_extension('../../common_files/JSR/chrome_JSR.crx')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=d,
        options=o)
    return driver
