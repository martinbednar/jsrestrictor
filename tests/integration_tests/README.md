Integration tests for web browser extension Javascript Restrictor automatically verify that
requied JavaScript API are wrapped and conversely that non wrapped JavaScript API provide real values.

Integration tests run directly in selected browsers with installed JSR extension.

It is necessary to manually setup testing environment before first tests running!



# SETUP TEST ENVIRONMENT


## Install required program and tools

These programs and tools are required to be installed:
* [Python 3.5+](https://www.python.org/downloads/)
* [Python package "pytest"](https://pypi.org/project/pytest/)
* [Python package "selenium"](https://pypi.org/project/selenium/)
* [Google Chrome](https://www.google.com/chrome/)
* [Mozilla Firefox ESR](https://www.mozilla.org/en-US/firefox/all/#product-desktop-esr) - Be careful, ESR (or Developer or Nightly edition) is required. But the ESR edition is preferred.

No other versions of Google Chrome and especially Mozilla Firefox have to be installed.
Web browser driver automatically select installed version of web browser so it is better to have installed only one correct version of each web browser.
Web browsers may not have installed Javascript restrictor extension. Python script will install it itself before running tests.


## Setup web browsers

Open Mozilla Firefox ESR and change preference xpinstall.signatures.required to false in the Firefox Configuration Editor (about:config page).
You can follow [official Mozilla support](https://support.mozilla.org/en-US/kb/add-on-signing-in-firefox#w_what-are-my-options-if-i-want-to-use-an-unsigned-add-on-advanced-users).

Open testing page [https://polcak.github.io/jsrestrictor/test/test.html](https://polcak.github.io/jsrestrictor/test/test.html) and click on button "Show GPS data".
Firefox will ask you if you want to enable page to access location. Check option "Remember this decision" and then click "Allow".

Google Chrome is already prepared in default state for testing web browser extensions, the Chorme settings do not need to be changed.


## Update tests configuration

Open file "configuration.py" from folder "integration_tests" for editing and update paths to needed files and folders. Always insert full paths.

### on Windows OS

All single '\' in path have to be replaced with '\\'.

* firefox_driver = path to gecko driver. Gecko driver is included in folder "common_files" or it is able to download it.
* firefox_profile = path to folder of firefox profile of Mozilla Firefox ESR with enabled access to location. It is typically located in C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\<profilename>.default-esr
* firefox_jsr_extension = path to xpi package of JSR (package importable to Firefox). Xpi packages is included in folder "common_files" or it is able to create it from JSR source files.
* chrome_driver = path to chrome driver. Chrome driver is included in folder "common_files" or it is able to download it.
* chrome_jsr_extension = path to xcr package of JSR (package importable to Chrome). Xcr packages is included in folder "common_files" or it is able to create it from JSR source files.

### on Linux OS



# RUN TESTS

### on Windows OS

Open PowerShell in folder "integration_tests" and run command:
	python start.py

When script execution starts for the first time, OS Windows will ask you to allow Firewall Exception for this script (for Python). Click "Allow".

### on Linux OS


If something unexpected happened during Python script execution, try to check configuration file and start testing again.