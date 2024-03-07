#!/bin/bash

# * CD to the script file location
# Get the directory where the script is located
script_dir=$(dirname "$(readlink -f "$0")")

# Change the current directory to the script's directory
cd "$script_dir"

# * Define variables that will be used
# Source directories
user_dir="../../install/services/user"
root_dir="../../install/services/root"

# Destination directories
user_destination_dir="$HOME/.config/systemd/user/"
root_destination_dir="/etc/systemd/system/"

# Arrays to store file names
user_services=()
user_services+=("$user_dir"/*) # add the names of all the files in $user_dir/ to the user_services array

root_services=()
root_services+=("$root_dir"/*) # add the names of all the files in $root_dir/ to the user_services array

# * Stop the services
# Stop the user services
echo -e "\nStopping User Services..."
for service_file in "${user_services[@]}"; do
    if ! systemctl --user stop "$(basename "$service_file" .service)"; then
        echo "Error: Stopping $(basename "$service_file" .service) service failed."
        exit 1
    fi
done
echo "done!"

# Stop the root services
echo -e "\nStopping Root Services..."
for service_file in "${root_services[@]}"; do
    if ! sudo systemctl stop "$(basename "$service_file" .service)"; then
        echo "Error: Stopping $(basename "$service_file" .service) service failed."
        exit 1
    fi
done
echo -e "done!\n"