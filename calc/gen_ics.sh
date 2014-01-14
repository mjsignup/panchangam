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
  script="iast"
elif [[ $# -gt 6 ]]
then
  echo "Usage: $0 <city name> <lat> <lon> <tz name> [year] [script]"
  exit 1
else
  y=`date +%Y`
  script="iast"
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

echo -ne "Computing $y ICS calendar for panchangam for $city_name ($lat,$lon) - $tz in $script script... "
./write_panchangam_ics.py $city_name $lat $lon $tz $y $script
echo "done. "

mkdir -p ics
mv *.ics ics/ 
