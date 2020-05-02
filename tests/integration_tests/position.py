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
    my_dict = {}
    for property in location:
        property = property.split(':')
        my_dict[property[0].lower()] = property[1]
    return my_dict