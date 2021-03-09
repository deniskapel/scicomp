#!/bin/bash
# Proper header for a Bash script.

# chmod +rx scriptname (gives everyone read/execute permission)
# to run it with ./scriptname

while [[ $name = "" ]]
do
  echo -n "What is your name? "
  read name
done

echo "Hello, $name"
exit 0
