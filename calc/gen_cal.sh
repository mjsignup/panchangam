#!/bin/bash
if [[ $# -ne 5 ]]
then
  echo "Usage: $0 <city name> <lat> <lon> <tz offset> <dst - 0/1>"
  exit 1
fi

city_name=$1
lat=$2
lon=$3
tz=$4
dst=$5

y=2010

./write_panchangam_tex.py $city_name $lat $lon $tz $dst > $y-$city_name.tex

cat cal_template.tex | sed "s/FILENAME/$y-$city_name.tex/;s/YEAR/$y/;s/CITY/$city_name/" > cal-$y-$city_name.tex

xelatex cal-$y-$city_name.tex > cal-$y-$city_name.texlog

mkdir -p data

mv $y-* cal-* data/

mkdir -p pdf

mv data/*.pdf pdf/

