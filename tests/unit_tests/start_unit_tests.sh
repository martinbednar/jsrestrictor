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
	# Get current script.
	script=$(jq -r ".scripts[$k]" ./config/global.json);
	
	# Get script name.
	name=$(jq -r '.name' <<< "$script");
	test_script_name="${name}_tests.js"
	source_script_name="${name}.js"
	# Add current script name to list of all testing scripts that will be run.
	if [ $k -eq 0 ]
	then
		script_names+="\"${test_script_name}\""
	else
		script_names+=", \"${test_script_name}\""
	fi
	
	cp ./tests/$test_script_name ./tmp/$test_script_name
	
	all_test_script_requirements=""
	
	# Iterate over test script requirements.
	for l in $(jq '.test_script_requirements | keys | .[]' <<< "$script"); do
		# Get current script.
		requirements_type=$(jq -r ".test_script_requirements[$l]" <<< "$script");
		
		# Get requirement type.
		type=$(jq -r '.type' <<< "$requirements_type");
		
		for m in $(jq '.requirements | keys | .[]' <<< "$requirements_type"); do
			# Get current requirements.
			requirements=$(jq -r ".requirements[$m]" <<< "$requirements_type");
			
			# Get requirement from.
			from=$(jq -r '.from' <<< "$requirements");
			
			all_test_script_requirements+="${type} { "
			
			for n in $(jq '.names | keys | .[]' <<< "$requirements"); do
				# Get current requirement name.
				requirement_name=$(jq -r ".names[$n]" <<< "$requirements");
				
				# Add current requirement name.
				if [ $n -eq 0 ]
				then
					all_test_script_requirements+="${requirement_name}"
				else
					all_test_script_requirements+=", ${requirement_name}"
				fi
				
			done
			
			all_test_script_requirements+=" } = require('${from}');"
		done
	done
	
	sed -i "1s~^~$all_test_script_requirements~" ./tmp/$test_script_name
	
	
	cp ../../common/$source_script_name ./tmp/$source_script_name
	
	remove_custom_namespace=$(jq -r '.remove_custom_namespace' <<< "$script")
	if [ $remove_custom_namespace == "true" ]
	then
		sed -i -e "s/(function() {//" -e "s/})();//" -e "s/successCallback/return/" ./tmp/$source_script_name
	fi
	
	
	# Get code for injecting.
	inject_code=$(jq -r '.inject_code_to_src' <<< "$script");
	
	sed -i "1s~^~$inject_code~" ./tmp/$source_script_name
	
	
	all_src_script_requirements=""
	
	# Iterate over source script requirements.
	for l in $(jq '.src_script_requirements | keys | .[]' <<< "$script"); do
		# Get current script.
		requirements_type=$(jq -r ".src_script_requirements[$l]" <<< "$script");
		
		# Get requirement type.
		type=$(jq -r '.type' <<< "$requirements_type");
		
		for m in $(jq '.requirements | keys | .[]' <<< "$requirements_type"); do
			# Get current requirements.
			requirements=$(jq -r ".requirements[$m]" <<< "$requirements_type");
			
			# Get requirement from.
			from=$(jq -r '.from' <<< "$requirements");
			
			# Get requirement name.
			requirement_name=$(jq -r '.name' <<< "$requirements");
			
			all_src_script_requirements+="${type} ${requirement_name} = require('${from}');"
		done
	done
	
	sed -i "1s~^~$all_src_script_requirements~" ./tmp/$source_script_name
	
	exports=""
	
	while IFS= read -r line; do
		if [[ $remove_custom_namespace == "false" ]] ;
		then
			if [[ $line == function* ]] ;
			then
				IFS=' (' read -ra line_divided <<< "$line"
				function_name="${line_divided[1]}"
				exports+="exports.${function_name} = ${function_name}; "
			elif [[ $line == var* ]] ;
			then
				IFS=' =' read -ra line_divided <<< "$line"
				var_name="${line_divided[1]}"
				exports+="exports.${var_name} = ${var_name}; "
			fi
		else
			line=$(sed 's/^.//' <<< $line)
			if [[ $line == function* ]] ;
			then
				IFS=' (' read -ra line_divided <<< "$line"
				function_name="${line_divided[1]}"
				exports+="exports.${function_name} = ${function_name}; "
			elif [[ $line == var* ]] ;
			then
				IFS=' =' read -ra line_divided <<< "$line"
				var_name="${line_divided[1]}"
				exports+="exports.${var_name} = ${var_name}; "
			fi
		fi
	done < ./tmp/$source_script_name
	
	if [[ $(jq '.extra_exports' <<< "$script") != "null" ]] ;
	then
		for l in $(jq '.extra_exports | keys | .[]' <<< "$script"); do
			# Get current export.
			export=$(jq -r ".extra_exports[$l]" <<< "$script");
			exports+="exports.${export} = ${export}; "
		done
	fi
	
	echo $exports >> ./tmp/$source_script_name
done

cp ./config/jasmine.json ./tmp/jasmine.json

sed -i "s/<<SPEC_FILES>>/$script_names/" ./tmp/jasmine.json

# Run unit tests in framework Jasmine for NodeJS.
jasmine --config=./tmp/jasmine.json

# Remove ./tmp directory after tests finished.
rm -rf ./tmp
