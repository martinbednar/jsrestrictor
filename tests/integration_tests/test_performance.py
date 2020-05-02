import time
import random

from math_operations import is_in_accuracy


def test_performance(driver, expected):
	for _ in range(3):
		time.sleep(random.randint(1, 3))
		performance = str(driver.execute_script("return window.performance.now()"))
		assert is_in_accuracy(performance, expected.accuracyPerformance)
