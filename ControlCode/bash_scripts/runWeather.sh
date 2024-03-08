#!/bin/bash

# Get the directory where the script is located
script_dir=$(dirname "$(readlink -f "$0")")

# Change the current directory to the script's directory
cd "$script_dir"

cd "../"

# Execute the flask webserver
sudo ../../venv/bin/py -m operations.weather_main $@