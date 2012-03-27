#!/usr/bin/python
# -*- coding: utf-8 -*-
from skt_names import *
#from roman_names import *

#type of month | month number | type of angam (tithi|nakshatram) | angam number | min_t cut off for considering prev day (without sunrise_angam) as festival date
purvaviddha_rules={akshaya_tritiya:['moon_month',2,'tithi',3,0],
chitra_purnima:['sun_month',1,'tithi',15,0],
durgashtami:['moon_month',7,'tithi',8,0],
mahanavami:['moon_month',7,'tithi',9,0],
vijayadashami:['moon_month',7,'tithi',10,0],
dipavali:['moon_month',7,'tithi',29,0],
shankara_jayanti:['moon_month',2,'tithi',5,0],
yajur_upakarma:['moon_month',5,'tithi',15,0],
rg_upakarma:['moon_month',5,'nakshatram',22,0],
sama_upakarma:['sun_month',5,'nakshatram',13,0],
rishi_panchami:['moon_month',6,'tithi',5,0],
ananta_chaturdashi:['moon_month',6,'tithi',14,0],
mahalaya_paksham:['moon_month',6,'tithi',16,0],
hanumat_jayanti:['sun_month',9,'tithi',30,0],
ardra_darshanam:['sun_month',9,'nakshatram',6,0],
ratha_saptami:['sun_month',10,'tithi',7,0],
goda_jayanti:['sun_month',4,'nakshatram',11,0],
adi_krittika:['sun_month',4,'nakshatram',3,0],
phalguni_uttaram:['sun_month',12,'nakshatram',12,4],
mahalaya_amavasya:['moon_month',6,'tithi',30,0],
uma_maheshvara_vratam:['moon_month',6,'tithi',15,0]}
