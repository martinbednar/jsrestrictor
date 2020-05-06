import time
import random

from math_operations import is_in_accuracy


def test_performance(browser, expected):
	is_performance_rounded = True
	for _ in range(3):
		time.sleep(random.randint(1, 3))
		performance = browser.driver.execute_script("return window.performance.now()")
		if expected.performance['accuracy'] == 'EXACTLY':
			if int(performance/10)*10 != performance:
				is_performance_rounded = False
		else:
			assert is_in_accuracy(performance, expected.performance['accuracy'])

	if expected.performance['accuracy'] == 'EXACTLY':
		assert not is_performance_rounded
