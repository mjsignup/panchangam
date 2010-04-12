#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import swisseph
from datetime import *
import pytz
from pytz import timezone

# FUNCTION DEFINITIONS

def sexa2deci(hour,minute=0.0,second=0.0):
  return hour*1.0+minute/60.0+second/3600.0

def sexastr2deci(str):
  if (str[0]=='-'):
    sgn = -1.0
    hms = str[1:].split(':')
  else:
    sgn = 1.0
    hms = str.split(':')
 
  decival = 0
  for i in range(0,len(hms)):
    decival = decival + float(hms[i])/(60.0**i)

  return decival*sgn

def deci2sexa(d):
  hour = math.floor(d)
  d = d-hour
  minute = math.floor(d*60.0)
  d = d-minute
  second = round(d*60)
  return [hour,minute,second]

def print_time (d):
  t=d.timetuple()
  return '%02d:%02d' % (t[3],t[4])

#USEFUL 'constants'
yamakandam_octets  = [5,4,3,2,1,7,6]
rahukalam_octets = [8,2,7,5,6,4,3]
#wday = {'Mon':1, 'Tue':2,'Wed':3, 'Thu':4, 'Fri':5, 'Sat':6, 'Sun':0}

month = {1:'JANUARY', 2:'FEBRUARY', 3:'MARCH', 4:'APRIL', 5:'MAY', 6:'JUNE', 7:'JULY', 8:'AUGUST', 9:'SEPTEMBER', 10:'OCTOBER', 11: 'NOVEMBER', 12:'DECEMBER'}

nakshatra_names={1:'अश्विनी',
2:'अपभरणी',
3:'कृत्तिका',
4:'रोहिणी',
5:'मृगशीर्ष',
6:'आर्द्रा',
7:'पुनर्वसू',
8:'पुष्य',
9:'आश्रेषा',
10:'मघा',
11:'पूर्वफल्गुनी',
12:'उत्तरफल्गुनी',
13:'हस्त',
14:'चित्रा',
15:'स्वाति',
16:'विशाखा',
17:'अनूराधा',
18:'ज्येष्ठा',
19:'मूला',
20:'पूर्वाषाढा',
21:'उत्तराषाढा',
22:'श्रवण',
23:'श्रविष्ठा',
24:'शतभिषक्',
25:'प्रोष्ठपदा',
26:'उत्तरप्रोष्ठपदा',
27:'रेवती'}

masa_names={1:'मेष',
2:'वृषभ',
3:'मिथुन',
4:'कर्कटक',
5:'सिंह',
6:'कन्या',
7:'तुला',
8:'वृश्चिक',
9:'धनुः',
10:'मकर',
11:'कुम्भ',
12:'मीन'
}

tithi_names={1:'shukla~प्रथमा',
2:'shukla~द्वितीया',
3:'shukla~तृतीया',
4:'shukla~चतुर्थी',
5:'shukla~पञ्चमी',
6:'shukla~षष्ठी',
7:'shukla~सप्तमी',
8:'shukla~अष्टमी',
9:'shukla~नवमी',
10:'shukla~दशमी',
11:'shukla~एकादशी',
12:'shukla~द्वादशी',
13:'shukla~त्रयोदशी',
14:'shukla~चतुर्दशी',
15:'fullmoon~पूर्णिमा',
16:'krishna~प्रथमा',
17:'krishna~द्वितीया',
18:'krishna~तृतीया',
19:'krishna~चतुर्थी',
20:'krishna~पञ्चमी',
21:'krishna~षष्ठी',
22:'krishna~सप्तमी',
23:'krishna~अष्टमी',
24:'krishna~नवमी',
25:'krishna~दशमी',
26:'krishna~एकादशी',
27:'krishna~द्वादशी',
28:'krishna~त्रयोदशी',
29:'krishna~चतुर्दशी',
30:'newmoon~अमावस्या'}

#MAIN CODE

city_name = sys.argv[1]
latitude = sexastr2deci(sys.argv[2])
longitude = sexastr2deci(sys.argv[3])
tz = sys.argv[4]

start_year = 2010
year = 2010
jd=swisseph.julday(year,1,1,0)
jd_start=jd
start_date = datetime(year=year,month=1,day=1,hour=0,minute=0,second=0)

day_of_year=0

swisseph.set_sid_mode(swisseph.SIDM_LAHIRI) #Force Lahiri Ayanamsha

sun_month_day = 16 #this has to be done in a generic fashion, by scanning for the transit into dhanur of the last year!

month_start_after_set = 0

template_file=open('cal_template.tex')
template_lines=template_file.readlines()
for i in range(0,len(template_lines)-3):
  print template_lines[i][:-1]


print '\\mbox{}'
print '{\\font\\x="Warnock Pro" at 60 pt\\x %d\\\\[0.5cm]}' % year
print '\\mbox{}'
print '{\\font\\x="Warnock Pro" at 48 pt\\x \\uppercase{%s}\\\\[0.3cm]}' % city_name
print '\hrule'

while 1:
  if year>start_year:
    break

  day_of_year = day_of_year + 1  


  [y,m,d,t] = swisseph.revjul(jd)
  weekday = (swisseph.day_of_week(jd) + 1)%7 #swisseph has Mon = 0, non-intuitively!

  local_time = pytz.timezone(tz).localize(datetime(y,m, d, 6, 0, 0)) #checking @ 6am local - can we do any better?
  tz_off=datetime.utcoffset(local_time).seconds/3600.0 #compute offset from UTC

  jd_rise=swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=longitude,lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
  jd_rise_tmrw=swisseph.rise_trans(jd_start=jd+1,body=swisseph.SUN,lon=longitude,lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
  jd_set =swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=longitude,lat=latitude,rsmi=swisseph.CALC_SET|swisseph.BIT_DISC_CENTER)[1][0]

  [_y,_m,_d, t_rise]=swisseph.revjul(jd_rise+tz_off/24.0)
  [_y,_m,_d, t_set]=swisseph.revjul(jd_set+tz_off/24.0)

  longitude_moon=swisseph.calc_ut(jd_rise,swisseph.MOON)[0]-swisseph.get_ayanamsa(jd_rise)
  longitude_moon_tmrw=swisseph.calc_ut(jd_rise+1,swisseph.MOON)[0]-swisseph.get_ayanamsa(jd_rise+1)

  longitude_sun=swisseph.calc_ut(jd_rise,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_rise)
  longitude_sun_set=swisseph.calc_ut(jd_set,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_set)
  sun_month_rise = masa_names[int(1+math.floor(((longitude_sun)%360)/30.0))];
  sun_month = masa_names[int(1+math.floor(((longitude_sun_set)%360)/30.0))];
  longitude_sun_tmrw=swisseph.calc_ut(jd_rise+1,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_rise+1)
  sun_month_tmrw = masa_names[int(1+math.floor(((longitude_sun_tmrw)%360)/30.0))];

  daily_motion_moon = (longitude_moon_tmrw-longitude_moon)%360
  daily_motion_sun = (longitude_sun_tmrw-longitude_sun)%360

  if month_start_after_set==1:
    sun_month_day = 0
    month_start_after_set = 0

  if sun_month_rise!=sun_month_tmrw:
    if sun_month!=sun_month_tmrw:
      month_start_after_set=1
      sun_month_day = sun_month_day + 1
    #mAsa pirappu!
    #sun_month = sun_month_tmrw #sun moves into next rAsi before sunset -- check rules!
    else:
      sun_month_day = 1
    month_remaining = 30-(longitude_sun%30.0);
    month_end = month_remaining/daily_motion_sun*24.0
    me = deci2sexa(t_rise+month_end);
    if me[0]>=24:
      suff='(+1)'
      me[0] = me[0] - 24
    else:
      suff='\\hspace{2ex}'
    sun_month_end_time = '{\\textsf{%s} {\\tiny \\RIGHTarrow} %02d:%02d%s}' % (last_sun_month,me[0],me[1],suff)
  else:
    sun_month_day = sun_month_day + 1
    sun_month_end_time = ''
  
  month_data = '\\sunmonth{%s}{%d}{%s}' % (sun_month,sun_month_day,sun_month_end_time)

  tithi = tithi_names[int(1+math.floor((longitude_moon-longitude_sun)%360 / 12.0))]
  tithi_remaining = 12-(((longitude_moon-longitude_sun)%360)%12)
  tithi_end = tithi_remaining/(daily_motion_moon-daily_motion_sun)*24.0

  if tithi_end/24.0+jd_rise>jd_rise_tmrw:
    tithi_end_str = '\\textsf{अहोरात्रम्}'
  else:
    te=deci2sexa(t_rise+tithi_end)
    if te[0]>=24:
      suff = '(+1)'
      te[0] = te[0]-24
    else:
      suff = '\\hspace{2ex}'
  
    tithi_end_str = '%02d:%02d%s' % (te[0],te[1],suff)


  nakshatram = nakshatra_names[int(1+math.floor((longitude_moon%360) /(360.0/27)))]
  nakshatram_remaining = (360.0/27) - ((longitude_moon%360) % (360.0/27))
  nakshatram_end = nakshatram_remaining/daily_motion_moon*24

  if nakshatram_end/24.0+jd_rise>jd_rise_tmrw:
    nakshatram_end_str = '\\textsf{अहोरात्रम्}'
  else:
    ne=deci2sexa(t_rise+nakshatram_end)
    if ne[0]>=24:
      ne[0] = ne[0]-24
      suff = '(+1)'
    else:
      suff='\\hspace{2ex}'
  
    nakshatram_end_str = '%02d:%02d%s' % (ne[0],ne[1],suff)

  [rh, rm, rs] = deci2sexa(t_rise) #rise_t hour, rise minute
  [sh, sm, ss] = deci2sexa(t_set) #set_t hour, set minute

  present_day = start_date + timedelta(days=day_of_year)
  rise_t = present_day + timedelta(hours=rh,minutes=rm)
  set_t = present_day + timedelta(hours=sh,minutes=sm)

  length_of_day = set_t-rise_t
  yamakandam_start = rise_t + timedelta(seconds=(1/8.0)*(yamakandam_octets[weekday]-1)*length_of_day.seconds)
  yamakandam_end = yamakandam_start + timedelta(seconds=(1/8.0)*length_of_day.seconds)
  rahukalam_start = rise_t + timedelta(seconds=(1/8.0)*(rahukalam_octets[weekday]-1)*length_of_day.seconds)
  rahukalam_end = rahukalam_start + timedelta(seconds=(1/8.0)*length_of_day.seconds)
  madhyahnikam_start = rise_t + timedelta(seconds=(1/5.0)*length_of_day.seconds)

  rise = '%02d:%02d' % (rh,rm)
  set = '%02d:%02d' % (sh,sm)
  madhya = print_time(madhyahnikam_start)
  rahu = '%s-%s' % (print_time(rahukalam_start), print_time(rahukalam_end))
  yama = '%s-%s' % (print_time(yamakandam_start),print_time(yamakandam_end))
  
  if d==1:
    if m>1:
      if weekday!=0: #Space till Sunday
        for i in range(weekday,6):
          print "{}  &"
        print "\\\\ \hline"
      print '\end{tabular}'
      print '\n\n%\clearpage'

    #Begin tabular
    print '\\begin{tabular}{|c|c|c|c|c|c|c|}'
    print '\multicolumn{7}{c}{\Large \\bfseries %s %s}\\\\[3mm]' % (month[m],y)
    print '\hline'
    print '\\textbf{SUN} & \\textbf{MON} & \\textbf{TUE} & \\textbf{WED} & \\textbf{THU} & \\textbf{FRI} & \\textbf{SAT} \\\\ \hline'
    #print '\\textbf{भानु} & \\textbf{इन्दु} & \\textbf{भौम} & \\textbf{बुध} & \\textbf{गुरु} & \\textbf{भृगु} & \\textbf{स्थिर} \\\\ \hline'

    #Blanks for previous weekdays
    for i in range(0,weekday):
      print "{}  &"
  
  print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{%s}{%s} ' % (d,month_data,rise,set,madhya,tithi,tithi_end_str,nakshatram,nakshatram_end_str,rahu,yama)

  if weekday==6:
    print "\\\\ \hline"
  else:
    print "&"

  jd = jd + 1
  year = swisseph.revjul(jd)[0]

  last_sun_month = sun_month

  # For debugging specific dates
  #if m==4 and d==10:
  #  break

print "\\\\ \hline"
print '\end{tabular}'
print '\n\n%\clearpage'

#print '\\input{%d-%s.tex}' % (year,city_name)
print template_lines[-2][:-1]
print template_lines[-1][:-1]
