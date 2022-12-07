#!/bin/bash

WORK_DIR=$(dirname $0)

set -e
[ $# -ne 0 ] && echo -e "$ $0" && exit 1

day=$(date +%d)
year=$(date +%Y)
folder="${WORK_DIR}/${year}/${day}"

mkdir -p $folder
echo "Created ${folder}"

cp "${WORK_DIR}/day.py" "${folder}/day${day}.py"
cp "${WORK_DIR}/day.go" "${folder}/day${day}.go"
touch "${folder}/test"
curl --cookie "${WORK_DIR}/cookies.txt" "https://adventofcode.com/2022/day/${day#0}/input" > "${folder}/input"
