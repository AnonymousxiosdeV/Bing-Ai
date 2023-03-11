#!/bin/bash

# Replace 'script.py' with the name of your Python script
SCRIPT_PATH="/home/pi/Documents/script.py"
RC_LOCAL_PATH="/etc/rc.local"

# Function to check if script is already set to run at boot
check_script() {
    grep -q "python3 $SCRIPT_PATH" $RC_LOCAL_PATH
    return $?
}

# Function to enable automatic execution of script at boot
enable_script() {
    if ! check_script; then
        sudo sed -i -e '$i python3 '"$SCRIPT_PATH"' &\n' $RC_LOCAL_PATH
        echo "Script enabled"
    else
        echo "Script already enabled"
    fi
}

# Function to disable automatic execution of script at boot
disable_script() {
    if check_script; then
        sudo sed -i "\|python3 $SCRIPT_PATH|d" $RC_LOCAL_PATH
        echo "Script disabled"
    else
        echo "Script already disabled"
    fi
}

# Function to add logging and error handling to script execution command in /etc/rc.local file.
add_logging_and_error_handling() {
  if check_script; then 
      sudo sed -i "\|python3 $SCRIPT_PATH|c\python3 $SCRIPT_PATH > /var/log/my_script.log 2>&1" $RC_LOCAL_PATH 
      echo "Logging and error handling added."
  else 
      echo "Script not found in /etc/rc.local file. Please enable it first."
  fi 
}

# Check command line arguments and call appropriate function(s)
if [ "$1" == "enable" ]; then
    enable_script
elif [ "$1" == "disable" ]; then
    disable_script 
elif [ "$1" == "log" ]; then 
    add_logging_and_error_handling 
else 
   echo "Usage: $0 [enable|disable|log]"
fi