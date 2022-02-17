#!/bin/bash

set -e
[ $# -lt 1 ] && echo -e "Usage:\n    $ $0 <day-number>" && exit 1

for day in $@
do
    mkdir $day
    cp day.py "$day/day$day.py"
    touch "$day/test"
    touch "$day/utils.py"
done
