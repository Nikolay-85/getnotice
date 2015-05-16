#!/bin/bash
# Utility to send messages to our great messaging system

HOST="localhost"
PORT="8080"

while [[ $# > 1 ]]
do
key="$1"


case $key in
    -m|--message)
    MESSAGE="$2"
    shift
    ;;
    -l|--level)
    LEVEL="$2"
    shift
    ;;
    -h|--host)
    HOST="$2"
    shift
    ;;
    -p|--port)
    PORT="$2"
    shift
    ;;
    *)
        # unknown option
    ;;
esac
shift
done
echo sending "${MESSAGE}"

curl -X POST --data '{"text":"'"${MESSAGE}"'", "level": "'"${LEVEL}"'"}'  -H "Content-type: application/json;charset=UTF-8" http://${HOST}:${PORT}/messages/