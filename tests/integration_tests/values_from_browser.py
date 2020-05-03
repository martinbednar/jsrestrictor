from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def get_position(driver):
    driver.get('https://polcak.github.io/jsrestrictor/test/test.html')
    driver.find_element_by_xpath("//button[text()='Show GPS data']").click()
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'mapnavi'))
    )
    location = driver.find_element_by_id('placeToWriteGPSDetails').text
    location = location.replace(" ", "").split()
    position = {}
    for property in location:
        property = property.split(':')
        position[property[0].lower()] = property[1]
    return position


def get_navigator(driver):
    navigator = {'userAgent': driver.execute_script("return window.navigator.userAgent"),
                 'appVersion': driver.execute_script("return window.navigator.appVersion"),
                 'platform': driver.execute_script("return window.navigator.platform"),
                 'vendor': driver.execute_script("return window.navigator.vendor"),
                 'language': driver.execute_script("return window.navigator.language"),
                 'languages': driver.execute_script("return window.navigator.languages"),
                 'cookieEnabled': driver.execute_script("return window.navigator.cookieEnabled"),
                 'doNotTrack': driver.execute_script("return window.navigator.doNotTrack"),
                 'oscpu': driver.execute_script("return window.navigator.oscpu")}
    return navigator


def get_device(driver):
    device = {'deviceMemory': driver.execute_script("return window.navigator.deviceMemory"),
              'hardwareConcurrency': driver.execute_script("return window.navigator.hardwareConcurrency")}
    return device
