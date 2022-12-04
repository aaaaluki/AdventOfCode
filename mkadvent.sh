#!/bin/bash

set -e
[ $# -ne 0 ] && echo -e "$ $0" && exit 1

day=$(date +%d)
year=$(date +%Y)
folder="${year}/${day}"

mkdir -p $folder
echo "Created ${folder}"

cp day.py "${folder}/day${day}.py"
cp day.go "${folder}/day${day}.go"
touch "${folder}/test"
curl --cookie cookies.txt "https://adventofcode.com/2022/day/${day#0}/input" > "${folder}/input"
