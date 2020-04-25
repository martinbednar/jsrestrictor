#import os

#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#def setup_module(module):
#    print "in setup_module"
#    executable_path = "G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\Selenium\\SeleniumWebDriverJava\\WebDrivers\\chromedriver.exe"
#    os.environ["webdriver.chrome.driver"] = executable_path
#
#    # enable browser logging
#    d = DesiredCapabilities.CHROME
#    d['loggingPreferences'] = {'browser': 'ALL'}
#
#    options = Options()
#    options.add_extension('G:\\My Drive\\FIT\\4_semestr_MIS\\DIP\\JSRescrictor\\jsrestrictor_0_2_1_0.crx')
#    options.add_argument("user-data-dir=C:\\Users\\Martin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
#
#    module.driver = webdriver.Chrome(executable_path=executable_path, options=options, desired_capabilities=d)


#def teardown_module(module):
#    module.driver.quit()


#class TestClass:
#    def test_answer(self):
#        js_url = module.driver.execute_script("return window.navigator.userAgent")
#        assert js_url == js_url


# content of a/test_db.py
def test_a1(db):
    assert 0, db  # to show value
