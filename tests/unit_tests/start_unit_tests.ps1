# Create directory ./tmp if not exists.
New-Item -ItemType Directory -Force -Path .\tmp | Out-Null

# Preprocessing JSR source code before unit tests running. Save preprocessed to the new ./tmp directory.
(Get-Content ..\..\common\helpers.js).replace('function', 'export function') | Set-Content .\tmp\helpers.mjs | Out-Null

# Run unit tests in framework Jasmine for NodeJS.
jasmine --config=./config/jasmine.json

# Remove ./tmp directory after tests finished.

