#!/bin/bash
if [[ $# -lt 4 ]]
then
  echo "Usage: $0 <city name> <lat> <lon> <tz name> [year] [script]"
  exit 1
fi
if [[ $# -eq 6 ]]
then
  script=$6
  y=$5
elif [[ $# -eq 5 ]]
then
  y=$5
  script="deva"
elif [[ $# -gt 6 ]]
then
  echo "Usage: $0 <city name> <lat> <lon> <tz name> [year] [script]"
  exit 1
else
  y=`date +%Y`
  script="deva"
fi

city_name=$1
lat=$2
lon=$3
tz=$4

for x in *_names.txt
do 
  if [[ init_names.py -ot $x ]]
  then
    echo "Regenerating init_names.py since it is older than $x"
    ./gen_init_names_py.sh
  fi
done

echo -ne "Computing $y panchangam for $city_name ($lat,$lon) - $tz in $script script... "
./write_panchangam_tex.py $city_name $lat $lon $tz $y $script > cal-$y-$city_name-$script.tex
mv cal_log* debug_logs/
echo "done. "

echo -ne "Generating PDF (log --> /tmp/cal-$y-$city_name.texlog)... "
xelatex cal-$y-$city_name-$script.tex > /tmp/cal-$y-$city_name-$script.texlog
rm cal-$y-$city_name-$script.log
echo done

mkdir -p data
mv cal-$y-$city_name-$script.* data/

mkdir -p pdf
mv data/cal-$y-$city_name-$script.pdf pdf/
