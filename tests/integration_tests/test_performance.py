import time
import random

from math_operations import is_in_accuracy


def test_performance(browser, expected):
	for _ in range(3):
		time.sleep(random.randint(1, 3))
		performance = str(browser.driver.execute_script("return window.performance.now()"))
		if expected.accuracyPerformance == 'REAL VALUE':
			assert True
		else:
			assert is_in_accuracy(performance, expected.accuracyPerformance)
