# Create directory ./tmp if not exists.
New-Item -ItemType Directory -Force -Path .\tmp | Out-Null

# Preprocessing JSR source code before unit tests running. Save preprocessed to the new ./tmp directory.
$src_scripts = @(
	'helpers',
    'background'
)

foreach ( $script_name in $src_scripts ) {
	$script = Get-Content ..\..\common\$script_name.js -Raw
	$words = $script.Split(" ")
	$i = 0
	$exports = @()
	foreach ($word in $words) {
		# Is the current word the keyword 'function'? If yes, save function name (next word) without argument list.
		if ($word -match '(?m)\r?\nfunction$') {
			$exports += $words[$i+1].Split('(')[0]
		}
		# Is the current word the keyword 'var'? If yes, save variable name (next word).
		if ($word -match '(?m)\r?\nvar$') {
			$exports += $words[$i+1].Split('=')[0]
		}
		$i++
	}
	
	$script_exports = ""
	foreach ($to_export in $exports) {
		$script_exports += "exports." + $to_export + " = " + $to_export + "`n"
	}
	
	$updated_script = "const chrome = require('sinon-chrome');`n`n" +
						(Get-Content .\mock_objects\browser.js -Raw) +
						"`n" +
						$script +
						"`n" +
						$script_exports
	
	Set-Content -Path ".\tmp\$script_name.js" -Value $updated_script
}

# Run unit tests in framework Jasmine for NodeJS.
jasmine --config=./config/jasmine.json

# Remove ./tmp directory after tests finished.
#Remove-Item -Recurse -Force .\tmp | Out-Null
