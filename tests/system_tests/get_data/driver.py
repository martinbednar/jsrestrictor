from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


## Find URL of JSR option page after JSR was installed to browser.
def find_options_jsr_page_url(driver):
    sleep(1)
    # KNOWN ISSUE: Tab in browser is sometimes not switched by this command.
    # And it leads to error and stopping execution of script. It is driver's issue.
    # Workaround for this issue is wait a while before and after tabs switching.
    driver.switch_to.window(driver.window_handles[-1])
    sleep(1)
    driver.get('chrome://system/')
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'extensions-value-btn'))
    )
    driver.find_element_by_id('extensions-value-btn').click()
    for elem in driver.find_element_by_id('extensions-value').text.splitlines():
        if 'JavaScript Restrictor' in elem:
            return "chrome-extension://" + elem.split(':')[0][:-1] + "/options.html"


def set_jsr_level(driver, level):
    options_page = find_options_jsr_page_url(driver)
    driver.get(options_page)
    driver.find_element_by_id('level-' + str(level)).click()


def create_driver(with_jsr, jsr_level):
    d = DesiredCapabilities.CHROME
    d['browserName'] = 'chrome'
    d['javascriptEnabled'] = True
    d['loggingPreferences'] = {'browser': 'ALL'}

    o = Options()
    o.add_argument("--start-maximized")
    # Pass the argument 1 to allow and 2 to block
    o.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 2
    })
    if with_jsr:
        o.add_extension('../../common_files/JSR/chrome_JSR.crx')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=d,
        options=o)

    if with_jsr:
        set_jsr_level(driver, jsr_level)
    return driver
