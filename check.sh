#!/bin/bash
if [ -z  "$1" ]
then
    echo "You have to enter the ip address to check, with port"
    echo "Usage example: check http://192.168.99.109:32087"
    echo "\n"
else
    echo "Listening on ip: $1\n"
fi

while true
do  
    output= curl "$1"
    echo "$output"
    sleep 1
done
