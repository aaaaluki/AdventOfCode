#!/bin/bash

WORK_DIR=$(dirname $0)

function copy_if_not_exists() {
    src=$1
    dst=$2

    if [ ! -f $dst ]; then
        echo "file does not exist"
        cp $src $dst
    fi
}

set -e
[ $# -ge 3 ] && echo -e "$0 <day> <year>" && exit 1

# Set day
if [[ $1 != "" ]]; then
    day=$1
else
    day=$(date +%d)
fi
day_padded=$(printf "%02d" "${day}")

# Set year
if [[ $2 != "" ]]; then
    year=$2
else
    year=$(date +%Y)
fi

folder="${WORK_DIR}/${year}/${day_padded}"

mkdir -p $folder
echo "Created ${folder}"

copy_if_not_exists "${WORK_DIR}/day.py" "${folder}/day${day_padded}.py"
copy_if_not_exists "${WORK_DIR}/day.go" "${folder}/day${day_padded}.go"
touch "${folder}/test"
# curl --cookie "${WORK_DIR}/cookies.txt" "https://adventofcode.com/${year}/day/${day}/input" > "${folder}/input"
