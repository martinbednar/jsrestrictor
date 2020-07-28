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
	Write-Host "An error noticed during setup the test environment. Integration testing can not be started. Look at the README file and follow instructions to run the setup again."
}
else {
	Write-Host "No error noticed during setup the test environment. Integration testing is starting..."
	cd .\get_data
	python .\start.py
	cd ..\analyze_data
	python .\start_screenshots_analysis.py
	python .\start_logs_analysis.py
	cd ..\
}
