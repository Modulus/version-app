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
    echo "Checking without headers\n"
    output= curl "$1"
    
    echo "==========================\n"
    echo "CHecking with version: v1"
    output= curl -H "version: v1" "$1"

    echo "==========================\n"
    echo "CHecking with version: v1"
    output= curl -H "version: v2" "$1"

    echo "==========================\n"
    echo "CHecking with version: v3"
    output= curl -H "version: v3" "$1"
    echo "$output\n"
    echo "############################\n"



    sleep 2
done
