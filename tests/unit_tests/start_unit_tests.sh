# Create directory ./tmp if not exists.
mkdir -p ./tmp

# Preprocessing JSR source code before unit tests running. Save preprocessed to the new ./tmp directory.
sed -e 's/function/export function/' ../../common/helpers.js > ./tmp/helpers.mjs

# Run unit tests in framework Jasmine for NodeJS.
jasmine --config=./config/jasmine.json

# Remove ./tmp directory after tests finished.
rm -rf ./tmp
