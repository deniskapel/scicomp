#!/bin/bash

PWD=`pwd`
PATTERN='/\.'

if [[ $PWD =~ $PATTERN ]]; then
    echo hidden
    exit 0
fi

exit 0
