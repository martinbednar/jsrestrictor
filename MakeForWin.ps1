param (
	[Parameter(Position=0)]
	[String]
	$makeCmd
)


function Firefox {
	Remove-Item "firefox_JSR.zip" -Recurse -Force -ErrorAction Ignore
	Remove-Item "firefox_JSR" -Recurse -Force -ErrorAction Ignore
	Copy-Item ".\common" -Destination ".\firefox_JSR" -Recurse -Force
	Copy-Item ".\firefox\*" -Destination ".\firefox_JSR" -Recurse -Force
	Copy-Item ".\LICENSE" -Destination ".\firefox_JSR" -Force
	.\fix_manifest.ps1 .\firefox_JSR\manifest.json
	
	$compressParams = @{
		Path = ".\firefox_JSR\*"
		DestinationPath = ".\firefox_JSR.zip"
	}
	Compress-Archive @compressParams -Force
}


function Chrome {
	Remove-Item "chrome_JSR.zip" -Recurse -Force -ErrorAction Ignore
	Remove-Item "chrome_JSR" -Recurse -Force -ErrorAction Ignore
	Copy-Item ".\common" -Destination ".\chrome_JSR" -Recurse -Force
	Copy-Item ".\chrome\*" -Destination ".\chrome_JSR" -Recurse -Force
	Copy-Item ".\LICENSE" -Destination ".\chrome_JSR" -Force
	.\fix_manifest.ps1 .\chrome_JSR\manifest.json
	
	$compressParams = @{
		Path = ".\chrome_JSR\*"
		DestinationPath = ".\chrome_JSR.zip"
	}
	Compress-Archive @compressParams -Force
}


function Clean {
	Remove-Item "firefox_JSR.zip" -Recurse -Force -ErrorAction Ignore
	Remove-Item "firefox_JSR" -Recurse -Force -ErrorAction Ignore
	Remove-Item "chrome_JSR.zip" -Recurse -Force -ErrorAction Ignore
	Remove-Item "chrome_JSR" -Recurse -Force -ErrorAction Ignore
}


if ($makeCmd -eq "clean") {
	Clean
}
else {
	Firefox
	Chrome
}
