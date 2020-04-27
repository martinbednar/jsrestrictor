import time

import setting


def test_accuracy(driver):
    driver.execute_script("function getLocation() {"
                          "if (navigator.geolocation) {"
                          "navigator.geolocation.getCurrentPosition(showPosition);"
                          "} else {"
                          "console.log('ERROR');"
                          "}"
                          "}"
                          "function showPosition(position) {"
                          "console.warn(position.coords.accuracy);"
                          "}"
                          "getLocation();")
    time.sleep(1)
    logs = driver.get_log('browser')
    print('logy:')
    print(logs);
    assert 1 == 1
