# Create directory ./tmp if not exists.
New-Item -ItemType Directory -Force -Path .\tmp | Out-Null

# Preprocessing JSR source code before unit tests running. Save preprocessed to the new ./tmp directory.
$src_scripts = @(
	'helpers',
    'browser',
	'url',
	'levels',
	'code_builders',
	'wrapping',
	'background',
	'wrappingS-GEO'
)

$tests_to_run = ""

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
		elseif (($script_name -eq "wrappingS-GEO") -AND ($word -match '(?m)\r?\n\tfunction$')) {
			$exports += $words[$i+1].Split('(')[0]
		}
		# Is the current word the keyword 'var'? If yes, save variable name (next word).
		if ($word -match '(?m)\r?\nvar$') {
			$exports += $words[$i+1].Split('=')[0]
		}
		elseif (($script_name -eq "wrappingS-GEO") -AND ($word -match '(?m)\r?\n\tvar$')) {
			$exports += $words[$i+1].Split('=')[0]
		}
		
		
		if ($script_name -eq "browser") {
			if ($word -match 'browser') {
				$exports += 'browser';
			}
		}
		
		$i++
	}
	
	if ($script_name -eq $src_scripts[0]) {
		$tests_to_run = '"' + $script_name + '_tests.js"'
	}
	else {
		$tests_to_run += ', "' + $script_name + '_tests.js"'
	}
	
	$script_imports = ""
	
	if ($script_name -eq "levels") {
		$script_imports = "const { extractSubDomains } = require('../tmp/url.js');`n`n"
	}
	
	if ($script_name -eq "code_builders") {
		$script_imports = "const { build_wrapping_code } = require('../tmp/wrapping.js');`n`n"
	}
	
	if ($script_name -eq "background") {
		$script_imports = "const { getCurrentLevelJSON } = require('../tmp/levels.js');`n`n"
	}
	
	if ($script_name -eq "wrappingS-GEO") {
		$script_imports = "const { add_wrappers } = require('../tmp/wrapping.js');`n`n"
		$script_imports += '
	function gen_random32() {
		return 0.2 * 4294967295;
	}'
	}
	
	$script_exports = ""
	foreach ($to_export in $exports) {
		$script_exports += "exports." + $to_export + " = " + $to_export + "`n"
	}
	
	$updated_script = "const chrome = require('sinon-chrome');`n`n" +
						 "const navigator = require('navigator');`n`n" +
						 "const window = require('window');`n`n" +
						 $script_imports +
						 (Get-Content .\mock_objects\browser.js -Raw) +
						"`n" +
						$script +
						"`n" +
						$script_exports
	
	Set-Content -Path ".\tmp\$script_name.js" -Value $updated_script
}

(Get-Content .\tmp\wrappingS-GEO.js).
	replace('(function() {', '').
	replace('})();', '').
	replace('successCallback', 'return') | Set-Content .\tmp\wrappingS-GEO.js

#Automatically set test for running in Jasmine config.
$jasmine_config = Get-Content .\config\jasmine.json -Raw
$jasmine_config.Replace("SPEC_FILES", $tests_to_run) | Set-Content .\config\jasmine.json

# Run unit tests in framework Jasmine for NodeJS.
jasmine --config=./config/jasmine.json

# Remove ./tmp directory after tests finished.
#Remove-Item -Recurse -Force .\tmp | Out-Null
Set-Content -Path .\config\jasmine.json -Value $jasmine_config
