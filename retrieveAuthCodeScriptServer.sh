#!/bin/bash

python -m http.server 5000 2>&1 > /dev/null &

wd=$1
echo $wd
user=$2
echo $user
passwd=$3
#echo $passwd

python -u getCallbackUrlServer.py $wd $user $passwd > $wd/log/auth_code.log

echo "Cleaning up background processes"

PIDs=`pgrep -l python|awk '{print $1}'`
echo $PIDs

for pid in $PIDs
do
        if [[ "" != "$pid" ]]; then
                echo "Killing python http server process id $pid"
                kill -9 "$pid"
        fi
done
exit 0
