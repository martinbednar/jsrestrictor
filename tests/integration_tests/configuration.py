from web_browser_type import BrowserType


class Config:
    tested_browsers = [BrowserType.CHROME, BrowserType.FIREFOX]
    tested_jsr_levels = [0, 1, 2, 3]
    firefox_driver = "D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\geckodriver.exe"
    firefox_profile = "C:\\Users\\Martin\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\voxsqf3a.default-esr"
    firefox_jsr_extension = "D:\\Development\\jsrestrictor\\tests\\common_files\\JSR\\firefox\\firefox_JSR_master.xpi"
    chrome_driver = "D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\chromedriver.exe"
    chrome_jsr_extension = "D:\\Development\\jsrestrictor\\tests\\common_files\\JSR\\chrome\\chrome_JSR_master.crx"
    testing_page = "https://polcak.github.io/jsrestrictor/test/test.html"
