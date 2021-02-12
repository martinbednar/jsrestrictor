#!/bin/bash

# Create directory ./tmp if not exists.
mkdir -p ./tmp

# String of all scripts names. Will be filled during iterating over scripts in global configuration.
script_names=""

# Convert EOL from Windows to Unix in configuration files.
#dos2unix ./config/global.json
#dos2unix ./config/jasmine.json

# Iterate over all scripts in global configuration.
for k in $(jq '.scripts | keys | .[]' ./config/global.json); do
	script=$(jq -r ".scripts[$k]" ./config/global.json);
	
	name=$(jq -r '.name' <<< "$script");
	if [ $k -eq 0 ]
	then
		script_names+="\"${name}_tests.js\""
	else
		script_names+="\" ,${name}_tests.js\""
	fi
	
done

jasmine_config_backup=$(cat ./config/jasmine.json)

sed -i "s/SPEC_FILES/$script_names/" ./config/jasmine.json

# Preprocessing JSR source code before unit tests running. Save preprocessed to the new ./tmp directory.
#sed -e 's/function/export function/' ../../common/helpers.js > ./tmp/helpers.mjs

# Run unit tests in framework Jasmine for NodeJS.
jasmine --config=./config/jasmine.json

# Remove ./tmp directory after tests finished.
#rm -rf ./tmp
echo $jasmine_config_backup > ./config/jasmine.json
