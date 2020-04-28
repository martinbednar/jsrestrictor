import pytest
import os
from enum import Enum

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BrowserType(Enum):
	FIREFOX = 1
	CHROME = 2
	EDGE = 3


@pytest.fixture(scope="session",autouse=True)
def driver():
	browser = Browser(type=BrowserType.FIREFOX)
	browser.jsr_level = 3;
	yield browser.driver
	browser.driver.quit()

class Browser:
	def __init__(self, type):
		self._type = type
		self.__jsr_level = 2
		if type == BrowserType.FIREFOX:
			executable_path = "D:\\Development\\jsrestrictor\\tests\\necessary_support_files\\webbrowser_drivers\\geckodriver.exe"
			os.environ["webdriver.firefox.driver"] = executable_path

			profile = webdriver.FirefoxProfile('C:\\Users\\Martin\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\bcm9f5hz.default')

			self.driver = webdriver.Firefox(profile, executable_path=executable_path)
			self.driver.install_addon('D:\\Development\\jsrestrictor\\tests\\necessary_support_files\\JSR\\firefox\\firefox_JSR_master.xpi', temporary=True)


		elif type == BrowserType.CHROME:
			executable_path = "G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\Selenium\\SeleniumWebDriverJava\\WebDrivers\\chromedriver.exe"
			os.environ["webdriver.chrome.driver"] = executable_path

			options = Options()
			options.add_extension('G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\JSRescrictor\\jsrestrictor_0_2_1_0.crx')
			options.add_argument("user-data-dir=C:\\Users\\Martin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

			self.driver = webdriver.Chrome(executable_path=executable_path, options=options)

	@property
	def jsr_level(self):
		return self.__jsr_level

	@jsr_level.setter
	def jsr_level(self, level):
		self.driver.switch_to.window(self.driver.window_handles[0])

		if self._type == BrowserType.CHROME:
			self.driver.get('chrome-extension://ammoloihpcbognfddfjcljgembpibcmb/options.html')
		elif self._type == BrowserType.FIREFOX:
			self.driver.get('moz-extension://96dbea1a-e86a-475b-a161-2e4537875519/options.html')

		self.driver.find_element_by_id('level-' + str(level)).click()
		self.driver.get('https://polcak.github.io/jsrestrictor/test/test.html')
		self.__jsr_level = level
