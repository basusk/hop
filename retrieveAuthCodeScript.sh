#!/usr/bin/sh

python -m http.server 5000 2>&1 > /dev/null &

wd=$1
#echo $wd
user=$2
#echo $user
passwd=$3
#echo $passwd

python -u getCallbackUrl.py $wd $user $passwd > $wd/log/auth_code.log

#python -u getCallbackUrl.py > C:/Users/Saikat.Basu/Documents/temp/hoptest/emails/new_work_9jan2025/for-check-in/log/auth_code.log

#rm C:/Users/Saikat.Basu/Documents/temp/hoptest/emails/new_work_9jan2025/for-check-in/jsonOut/auth_code.json


PIDs=`ps -ef | grep python | awk '{print $2}'`
echo $PIDs

for pid in $PIDs
do
        if [[ "" != "$pid" ]]; then
                echo "Killing python http server process id $pid"
                kill -9 "$pid"
        fi
done
