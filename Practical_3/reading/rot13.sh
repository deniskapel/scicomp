#!/bin/bash

LETTERS=abcdefghijklmnopqrstuvwxyz

while [[ $msg = "" ]]
do
  echo -n "Enter a message to encode or decode? "
  read msg
done

ouput=""

for (( i=0; i<${#msg}; i++ )); do
    letter=${msg:$i:1}
    if [[ $LETTERS =~ $letter ]]; then
        shift=$(((12 + `expr index "$LETTERS" $letter`) % 26))
        output+=${letter/$letter/${LETTERS:$shift:1}}
    fi
done

echo $output
exit 0
