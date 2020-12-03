### Build JSR from scratch

#### GNU/Linux and Apple Mac OS:

1. Go to the project repository: [https://github.com/polcak/jsrestrictor](https://github.com/polcak/jsrestrictor).
1. Download the desired branch, e.g. as zip archive.
1. Unpack the zip archive.
1. Run `make`.
	* You will need common software, such as `zip`, `wget`, `bash`, `awk`, `sed`.
1. Import the extension to the browser.
	* Firefox: [https://extensionworkshop.com/documentation/develop/temporary-installation-in-firefox/](https://extensionworkshop.com/documentation/develop/temporary-installation-in-firefox/)
		* Use the file `firefox_JSR.zip` created by `make`.
	* Chromium-based browsers:
		1. Open `chrome://extensions`.
		1. Enable developper mode.
		1. Click `Load unpacked`.
		1. Import the `chrome_JSR/` directory created by `make`.

#### Windows:
1. Install Windows Subsystem for Linux (WSL): [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
1. Go to the project repository: [https://github.com/polcak/jsrestrictor](https://github.com/polcak/jsrestrictor).
1. Download the desired branch, e.g. as zip archive.
1. Unpack the zip archive.
1. Change EOL from "CR LF" to "CR" for the file `fix_manifest.sh` (you can use the application Notepad++ on Windows or the tool `dos2unix` in WSL).
1. Open the JSR project folder in WSL, run `make`.
	* Before it, install missing tools in WSL, especially `zip`.
1. On Windows, import the extension to the browser according to the instructions for Linux (above).
