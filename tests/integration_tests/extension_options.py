import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


executable_path = "G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\Selenium\\SeleniumWebDriverJava\\WebDrivers\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path

options = Options()
options.add_extension('G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\JSRescrictor\\jsrestrictor_0_2_1_0.crx')
options.add_argument("user-data-dir=C:\\Users\\Martin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

driver = webdriver.Chrome(executable_path=executable_path, options=options)

driver.get('chrome-extension://ammoloihpcbognfddfjcljgembpibcmb/options.html')
level_3 = driver.find_element_by_id('level-3')
time.sleep(2)
level_3.click();
time.sleep(2)
driver.get('https://www.seznam.cz/')
time.sleep(2)


driver.quit()