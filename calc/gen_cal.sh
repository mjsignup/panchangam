#!/bin/bash
if [[ $# -ne 4 ]]
then
  echo "Usage: $0 <city name> <lat> <lon> <tz name>"
  exit 1
fi

city_name=$1
lat=$2
lon=$3
tz=$4

y=2010

echo -ne "Computing panchangam for $city_name ($lat,$lon) - $tz... "

./write_panchangam_tex.py $city_name $lat $lon $tz > cal-$y-$city_name.tex

echo -ne "done. "

echo -ne "Generating PDF... (log --> /tmp/cal-$y-$city_name.texlog)"

xelatex cal-$y-$city_name.tex > /tmp/cal-$y-$city_name.texlog

echo done

mkdir -p data

mv cal-* data/

mkdir -p pdf

mv data/*.pdf pdf/

