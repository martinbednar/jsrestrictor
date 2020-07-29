#
#  JavaScript Restrictor is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
#  Copyright (C) 2020  Martin Bednar
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

$Error.clear()

# Go to common scripts directory.
cd ..\common_files\scripts

# Run script build_JSR_package.ps1
.\build_JSR_package.ps1

# Go back to system_tests directory.
cd ..\..\system_tests

# Start testing if everything ok.
Write-Host
# Handle errors.
if($Error.length -gt 0)
{
	Write-Host "An error noticed during setup the test environment. System tests can not be started. Look at the README file and follow instructions to run the setup again."
}
else {
	Write-Host "No error noticed during setup the test environment. System tests are starting..."
	cd .\get_data
	python .\start.py
	cd ..\analyze_data
	python .\start_screenshots_analysis.py
	python .\start_logs_analysis.py
	cd ..\
}
