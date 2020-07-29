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

# Go to root directory of JSR project.
cd ..\..\..\

# Clean previous build.
.\MakeForWin.ps1 clean

# Build.
.\MakeForWin.ps1

# Create directory for JSR package if does not exists. Like "touch" on Linux.
New-Item -ItemType Directory -Path ".\tests\common_files\JSR" -Force

# Create xpi package of JSR for Mozilla Firefox from zip archive created by make.
Copy-Item ".\firefox_JSR.zip" -Destination ".\tests\common_files\JSR\firefox_JSR.xpi" -Force

$JSRPath = Get-Location

# Get path to chrome.exe.
$Chrome = "C:\Program Files (x86)\Google\Chrome\Application"
if (-Not (Test-Path $Chrome\chrome.exe -PathType Leaf)) {
	Write-Host
	$Chrome = Read-Host -Prompt 'Enter path into directory, where is chrome.exe stored'
	if (-Not (Test-Path $Chrome\chrome.exe -PathType Leaf)) {
		Write-Error -Message "Entered path ${Chrome} is not valid path into directory."
	}
}
cd $Chrome

# Create crx package of JSR for Google Chrome from source files.
#  | Out-Null force PowerShell to wait when packaging by Chorme is completed.
.\chrome.exe --pack-extension=$JSRPath\chrome_JSR | Out-Null
cd $JSRPath

# Remove unnecessary file created during crx package creating.
Remove-Item ".\chrome_JSR.pem" -Recurse -Force

# Move crx package of JSR to right location (same as xpi package of JSR).
Move-Item ".\chrome_JSR.crx" -Destination .\tests\common_files\JSR\chrome_JSR.crx -Force

# Go back to common scripts directory.
cd .\tests\common_files\scripts
