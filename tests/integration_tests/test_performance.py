import time
import random

from browser import driver
import expected_values


def test_performance():
	time.sleep(random.randint(1, 3))
	performance1 = str(driver.execute_script("return window.performance.now()"))
	time.sleep(random.randint(1, 3))
	performance2 = str(driver.execute_script("return window.performance.now()"))
	time.sleep(random.randint(1, 3))
	performance3 = str(driver.execute_script("return window.performance.now()"))
	assert performance1[-1] == '0'
	if len(performance1) > 1: assert performance1[-2] == '0'
	if len(performance1) > 2: assert performance1[-3] == '0'
	assert performance2[-1] == '0'
	if len(performance2) > 1: assert performance2[-2] == '0'
	if len(performance2) > 2: assert performance2[-3] == '0'
	assert performance3[-1] == '0'
	if len(performance3) > 1: assert performance3[-2] == '0'
	if len(performance3) > 2: assert performance3[-3] == '0'
