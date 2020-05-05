from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from web_browser_type import BrowserType
import values_real
from configuration import Config


class Browser:
    def find_options_jsr_page_url(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        if self.type == BrowserType.FIREFOX:
            self.driver.get('about:memory')
            self.driver.find_element_by_id('measureButton').click()
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.ID, 'end0'))
            )
            for elem in self.driver.find_elements_by_css_selector(
                    'div#mainDiv div.outputContainer div.sections div.section:first-child > pre.entries > span.kids > '
                    'span.mrName'):
                if 'id=jsr@javascriptrestrictor' in elem.text:
                    self._jsr_options_page = elem.text.split(',')[2].split('=')[1][:-1] + "options.html"
        if self.type == BrowserType.CHROME:
            self.driver.get('chrome://system/')
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.ID, 'extensions-value-btn'))
            )
            self.driver.find_element_by_id('extensions-value-btn').click()
            for elem in self.driver.find_element_by_id('extensions-value').text.splitlines():
                if 'JavaScript Restrictor' in elem:
                    self._jsr_options_page = "chrome-extension://" + elem.split(':')[0][:-1] + "/options.html"

    def __init__(self, type):
        self.type = type
        self.__jsr_level = 2
        self._jsr_options_page = ""
        if type == BrowserType.FIREFOX:
            self.driver = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(Config.firefox_profile),
                                            executable_path=Config.firefox_driver)
            self.real = values_real.init(self.driver)
            self.driver.install_addon(Config.firefox_jsr_extension, temporary=True)
            self.find_options_jsr_page_url()
        elif type == BrowserType.CHROME:
            driver_tmp = webdriver.Chrome(executable_path=Config.chrome_driver)
            self.real = values_real.init(driver_tmp)
            driver_tmp.quit()
            options = Options()
            options.add_extension(Config.chrome_jsr_extension)
            self.driver = webdriver.Chrome(executable_path=Config.chrome_driver, options=options)
            self.find_options_jsr_page_url()

    @property
    def jsr_level(self):
        return self.__jsr_level

    @jsr_level.setter
    def jsr_level(self, level):
        if self.type == BrowserType.CHROME:
            self.driver.get(self._jsr_options_page)
        elif self.type == BrowserType.FIREFOX:
            self.driver.get(self._jsr_options_page)
        self.driver.find_element_by_id('level-' + str(level)).click()
        self.__jsr_level = level
        self.driver.get(Config.testing_page)

    def quit(self):
        self.driver.quit()
        del self