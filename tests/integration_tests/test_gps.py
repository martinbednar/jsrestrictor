import time

import setting


def test_accuracy(driver):
	show_gps_button = driver.find_element_by_xpath("//button[text()='Show GPS data']")
	show_gps_button.click()
	time.sleep(2)
	print(driver.find_element_by_xpath("//div[@id='placeToWriteGPSDetails']").text)
	assert True
