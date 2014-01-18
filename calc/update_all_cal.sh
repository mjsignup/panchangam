#!/bin/bash
chmod +x write_panchangam_*.py *.sh

./gen_cal.sh Chennai 13:05:24 80:16:12 'Asia/Calcutta' 2014 deva #Place Lat Lon TZ
./gen_ics.sh Chennai 13:05:24 80:16:12 'Asia/Calcutta' 2014 deva
./gen_ics.sh Chennai 13:05:24 80:16:12 'Asia/Calcutta' 2014 iast
./gen_cal.sh Zurich  47:22:48  8:32:24 'Europe/Zurich' 2014
./gen_ics.sh Zurich  47:22:48  8:32:24 'Europe/Zurich' 2014 iast
./gen_cal.sh London  51:30:00  0:07:00 'Europe/London' 2014
./gen_ics.sh London  51:30:00  0:07:00 'Europe/London' 2014 iast
#./gen_cal.sh Mumbai  18:57:36 72:49:12 'Asia/Calcutta' 2014
cp ics/*2014*.ics pdf/*-2014* ~/Dropbox/panchangam/
