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
	y=`date +%Y`
fi

city_name=$1
lat=$2
lon=$3
tz=$4

echo -ne "Computing $y panchangam for $city_name ($lat,$lon) - $tz... "
./write_panchangam_tex_compre.py $city_name $lat $lon $tz $y > cal-$y-$city_name.tex
echo "done. "

echo -ne "Generating PDF (log --> /tmp/cal-$y-$city_name.texlog)... "
xelatex cal-$y-$city_name.tex > /tmp/cal-$y-$city_name.texlog
rm cal-$y-$city_name.log
echo done

mkdir -p data
mv cal-$y-$city_name.* data/

mkdir -p pdf
mv data/cal-$y-$city_name.pdf pdf/

