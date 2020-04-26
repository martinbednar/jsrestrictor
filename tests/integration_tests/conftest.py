import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def set_jsr_to_level(driver, level):
	driver.get('chrome-extension://ammoloihpcbognfddfjcljgembpibcmb/options.html')
	driver.find_element_by_id('level-' + str(level)).click()
	driver.get('https://polcak.github.io/jsrestrictor/')

@pytest.fixture(scope="session",autouse=True)
def driver(request):
	executable_path = "G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\Selenium\\SeleniumWebDriverJava\\WebDrivers\\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = executable_path
	
	options = Options()
	options.add_extension('G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\JSRescrictor\\jsrestrictor_0_2_1_0.crx')
	options.add_argument("user-data-dir=C:\\Users\\Martin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
	
	driver = webdriver.Chrome(executable_path=executable_path, options=options)
	set_jsr_to_level(driver, level=3)
	yield driver
	driver.quit()
