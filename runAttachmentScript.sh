#!/usr/bin/sh

wd=$1
echo $wd

python -u storeDownloadedAttacments.py $wd > $wd/log/file_details.log
rm "$wd"/jsonOut/*.json
