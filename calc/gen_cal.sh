#!/bin/bash
if [[ $# -lt 4 ]]
then
  echo "Usage: $0 <city name> <lat> <lon> <tz name> [year]"
  exit 1
fi
if [[ $# -eq 5 ]]
then
	y=$5
elif [[ $# -gt 5 ]]
then
  echo "Usage: $0 <city name> <lat> <lon> <tz name> [year]"
  exit 1
else
	y=2010
fi

city_name=$1
lat=$2
lon=$3
tz=$4

echo -ne "Computing $y panchangam for $city_name ($lat,$lon) - $tz... "
./write_panchangam_tex.py $city_name $lat $lon $tz $y > cal-$y-$city_name.tex
echo "done. "

echo -ne "Generating PDF... (log --> /tmp/cal-$y-$city_name.texlog)"
xelatex cal-$y-$city_name.tex > /tmp/cal-$y-$city_name.texlog
echo done

mkdir -p data
mv cal-* data/

mkdir -p pdf
mv data/*.pdf pdf/

