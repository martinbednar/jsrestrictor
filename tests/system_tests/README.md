System tests for web browser extension Javascript Restrictor (JSR) automatically checks how
JSR affets tested websites.

It is necessary to partially set up manually a test environment before the first test run!

# SET UP TEST ENVIRONMENT

## Install required programs and tools

These programs and tools are required to be installed:
* [Python 3.5+](https://www.python.org/downloads/)
* [Python package `numpy`](https://pypi.org/project/numpy/)
* [Python package `selenium`](https://pypi.org/project/selenium/)
* [Python package `python-Levenshtein`](https://pypi.org/project/python-Levenshtein/)
* [Python package `sklearn`](https://pypi.org/project/sklearn/)
* [Python package `nltk`](https://pypi.org/project/nltk/)
* [Google Chrome](https://www.google.com/chrome/) - Install really Google Chrome, Chromium is not supported.


Předtím nainstalovat Visual C++ build tools: https://stackoverflow.com/questions/44951456/pip-error-microsoft-visual-c-14-0-is-required


python -m nltk.downloader stopwords
top sites file and jar file (selenium server)


## Download web browser drivers

Download web browser drivers needed for controlling web browsers by tests. Download drivers for both web browsers - Google Chrome and Mozilla Firefox - and for both platform - Windows and Linux.

For Google Chrome download the ChromeDriver from [download page](https://chromedriver.chromium.org/downloads).
Select the version coresponding to the version of your Google Chrome web browser. If you download an incompatible version, you will see an error during starting tests.
Download the correct ChromeDriver to folder `../common_files/webbrowser_drivers` with name `chromedriver.exe` (for Windows) or `chromedriver` (for Linux).
