import pytest
import os
import time
from enum import Enum

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BrowserType(Enum):
	FIREFOX = 1
	CHROME = 2


@pytest.fixture(scope="session", autouse=True)
def driver():
	browser = Browser(type=BrowserType.FIREFOX)
	browser.jsr_level = 3
	yield browser.driver
	browser.driver.quit()


class Browser:
	def find_options_jsr_page_url(self):
		if self._type == BrowserType.FIREFOX:
			self.driver.get('about:memory')
			self.driver.find_element_by_id('measureButton').click()
			time.sleep(1)
			url = ""
			for elem in self.driver.find_elements_by_css_selector('div#mainDiv div.outputContainer div.sections div.section:first-child > pre.entries > span.kids > span.mrName'):
				if 'id=jsr@javascriptrestrictor' in elem.text:
					self._jsr_options_page = elem.text.split(',')[2].split('=')[1][:-1] + "options.html"

	def __init__(self, type):
		self._type = type
		self.__jsr_level = 2
		if type == BrowserType.FIREFOX:
			executable_path = "D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\geckodriver.exe"
			os.environ["webdriver.firefox.driver"] = executable_path

			profile = webdriver.FirefoxProfile('C:\\Users\\Martin\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\voxsqf3a.default-esr')

			self.driver = webdriver.Firefox(profile, executable_path=executable_path)
			self.driver.install_addon('D:\\Development\\jsrestrictor\\tests\\common_files\\JSR\\firefox\\firefox_JSR_rewrite.xpi', temporary=True)
			self.find_options_jsr_page_url()
		elif type == BrowserType.CHROME:
			executable_path = "D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\chromedriver.exe"
			os.environ["webdriver.chrome.driver"] = executable_path

			options = Options()
			options.add_extension('D:\\Development\\jsrestrictor\\tests\\common_files\\JSR\\chrome\\chrome_JSR_master.crx')
			options.add_argument("user-data-dir=C:\\Users\\Martin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

			self.driver = webdriver.Chrome(executable_path=executable_path, options=options)

	@property
	def jsr_level(self):
		return self.__jsr_level

	@jsr_level.setter
	def jsr_level(self, level):
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)

		if self._type == BrowserType.CHROME:
			self.driver.get('chrome-extension://ammoloihpcbognfddfjcljgembpibcmb/options.html')
		elif self._type == BrowserType.FIREFOX:
			self.driver.get(self._jsr_options_page)
		time.sleep(2)
		self.driver.find_element_by_id('level-' + str(level)).click()
		self.driver.get('https://polcak.github.io/jsrestrictor/test/test.html')
		self.__jsr_level = level
