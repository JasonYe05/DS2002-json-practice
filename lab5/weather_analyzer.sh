#!/bin/bash

curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

echo "First six receipt times:"
jq -r '.[].receiptTime' aviation.json | head -n 6

echo -n "Average Temperature: "
jq -r '.[].temp' aviation.json | awk '{ sum += $1; count++ } END { print sum/count }'

CLOUDS=$(jq -r '.[].clouds[].cover' aviation.json)

TOTAL_HOURS=$(echo "$CLOUDS" | wc -l)
CLOUDY_HOURS=$(echo "$CLOUDS" | grep -v "FEW" | wc -l)

if [ $CLOUDY_HOURS -gt $(($TOTAL_HOURS / 2)) ]; then
    echo "Mostly Cloudy: true"
else
    echo "Mostly Cloudy: false"
fi
