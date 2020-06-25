from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})
driver.get("https://github.com")
print('>>>>> GETTING PAGE FINISHED')
print(driver.title)
print('>>>>> GETTING PAGE TITLE FINISHED')