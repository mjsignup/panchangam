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

def get_last_dhanur_transit (jd_start,latitude,longitude):
  swisseph.set_sid_mode(swisseph.SIDM_LAHIRI) #Force Lahiri Ayanamsha
  for d in range(-25,0):
    jd = jd_start + d
    [y,m,d,t] = swisseph.revjul(jd)
  
    jd_rise=swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=longitude,lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
    jd_rise_tmrw=swisseph.rise_trans(jd_start=jd+1,body=swisseph.SUN,lon=longitude,lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
    jd_set =swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=longitude,lat=latitude,rsmi=swisseph.CALC_SET|swisseph.BIT_DISC_CENTER)[1][0]
  
    longitude_sun=swisseph.calc_ut(jd_rise,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_rise)
    longitude_sun_set=swisseph.calc_ut(jd_set,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_set)
    sun_month_rise = masa_names[int(1+math.floor(((longitude_sun)%360)/30.0))]
    sun_month = masa_names[int(1+math.floor(((longitude_sun_set)%360)/30.0))]
    longitude_sun_tmrw=swisseph.calc_ut(jd_rise+1,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_rise+1)
    sun_month_tmrw = masa_names[int(1+math.floor(((longitude_sun_tmrw)%360)/30.0))]

    #print '%f:%d-%d-%d: rise=%s, set=%s, tmrw=%s' %(jd,y,m,d,sun_month_rise,sun_month,sun_month_tmrw)

    if sun_month_rise!=sun_month_tmrw:
      if sun_month!=sun_month_tmrw:
        return jd+1
      else:
        return jd
  
def print_end_time (end_time, day_night_length, rise_time):
  if end_time/24.0>day_night_length:
    end_time_str = '\\textsf{अहोरात्रम्}'
  else:
    te=deci2sexa(rise_time+end_time)
    if te[0]>=24:
      suff = '(+1)'
      te[0] = te[0]-24
    else:
      suff = '\\hspace{2ex}'
    end_time_str = '%02d:%02d%s' % (te[0],te[1],suff)
  return end_time_str

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
25:'पूर्वप्रोष्ठपदा',
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
12:'मीन'}

tithi_names={1:'~प्रथमा',
2:'~द्वितीया',
3:'~तृतीया',
4:'~चतुर्थी',
5:'~पञ्चमी',
6:'~षष्ठी',
7:'~सप्तमी',
8:'~अष्टमी',
9:'~नवमी',
10:'~दशमी',
11:'~एकादशी',
12:'~द्वादशी',
13:'~त्रयोदशी',
14:'~चतुर्दशी',
15:'~पूर्णिमा',
30:'~अमावस्या'}

year_names={1:'प्रभव',
2:'विभव',
3:'शुक्ल',
4:'प्रमोद',
5:'प्रजापति',
6:'आङ्गिरस',
7:'श्रीमुख',
8:'भाव',
9:'युव',
10:'धात्री',
11:'ईश्वर',
12:'बहुधान्य',
13:'प्रमाधि',
14:'विक्रम',
15:'वृष',
16:'चित्रभानु',
17:'स्वभानु',
18:'तारण',
19:'पार्थिव',
20:'व्यय',
21:'सर्वजित्',
22:'सर्वधारी',
23:'विरोधी',
24:'विकृति',
25:'खर',
26:'नन्दन',
27:'विजय',
28:'जय',
29:'मन्मथ',
30:'दुर्मुखी',
31:'हेविलम्बी',
32:'विलम्बी',
33:'विकारी',
34:'शार्वरी',
35:'प्लव',
36:'शुभकृत्',
37:'शोभकृत्',
38:'क्रोधी',
39:'विश्वावसु',
40:'पराभव',
41:'प्लवङ्ग',
42:'कीलक',
43:'सौम्य',
44:'साधारण',
45:'विरोधिकृति',
46:'परिधावी',
47:'प्रमादीच',
48:'आनन्द',
49:'राक्षस',
50:'नल',
51:'पिङ्गल',
52:'कलायुक्ति',
53:'सिद्धार्थी',
54:'रौद्र',
55:'दुर्मति',
56:'दुन्दुभि',
57:'रुधिरोद्गारी',
58:'रक्ताक्षी',
59:'क्रोधन',
60:'अक्षय'}

#MAIN CODE
def main():
  city_name = sys.argv[1]
  latitude = sexastr2deci(sys.argv[2])
  longitude = sexastr2deci(sys.argv[3])
  tz = sys.argv[4]
  
  start_year = int(sys.argv[5])
  year = start_year
  jd=swisseph.julday(year,1,1,0)
  jd_start=jd
  start_date = datetime(year=year,month=1,day=1,hour=0,minute=0,second=0)
  
  day_of_year=0
  
  swisseph.set_sid_mode(swisseph.SIDM_LAHIRI) #Force Lahiri Ayanamsha
  
  sun_month_day = jd-get_last_dhanur_transit(jd,latitude,longitude)
  #this has to be done in a generic fashion, by scanning for the transit into dhanur of the last year!
  
  month_start_after_set = 0
  
  template_file=open('cal_template.tex')
  template_lines=template_file.readlines()
  for i in range(0,len(template_lines)-3):
    print template_lines[i][:-1]
  
  samvatsara_id = (year - 1568)%60 + 1; #distance from prabhava
  samvatsara_names = '%s–%s' % (year_names[samvatsara_id], year_names[(samvatsara_id%60)+1])
  
  print '\\mbox{}'
  print '{\\font\\x="Warnock Pro" at 60 pt\\x %d\\\\[0.3cm]}' % year
  print '\\mbox{\\font\\x="Sanskrit 2003:script=deva" at 48 pt\\x %s}\\\\[0.5cm]' % samvatsara_names
  print '{\\font\\x="Warnock Pro" at 48 pt\\x \\uppercase{%s}\\\\[0.3cm]}' % city_name
  print '\hrule'
  
  while year<=start_year:

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
    sun_month_rise = masa_names[int(1+math.floor(((longitude_sun)%360)/30.0))]
    sun_month = masa_names[int(1+math.floor(((longitude_sun_set)%360)/30.0))]
    longitude_sun_tmrw=swisseph.calc_ut(jd_rise+1,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_rise+1)
    sun_month_tmrw = masa_names[int(1+math.floor(((longitude_sun_tmrw)%360)/30.0))]
  
    daily_motion_moon = (longitude_moon_tmrw-longitude_moon)%360
    daily_motion_sun = (longitude_sun_tmrw-longitude_sun)%360
  
    #Solar month calculations
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
      month_remaining = 30-(longitude_sun%30.0)
      month_end = month_remaining/daily_motion_sun*24.0
      me = deci2sexa(t_rise+month_end)
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
    #print '%%@%f:%d-%d-%d: rise=%s, set=%s, tmrw=%s' %(jd,y,m,d,sun_month_rise,sun_month,sun_month_tmrw)
  
    #Compute tithi details
    tithi = int(1+math.floor((longitude_moon-longitude_sun)%360 / 12.0))
    tithi_tmrw = int(1+math.floor((longitude_moon_tmrw-longitude_sun_tmrw)%360 / 12.0))

    if (tithi_tmrw-tithi)%30 > 1:
      tithi_2=tithi+1
      #double change
      if tithi_2%15 != 0:
        paksha = ('shukla' if tithi_2<15 else 'krishna')
      else:
        if tithi_2 == 15:
          paksha = 'fullmoon'
        elif tithi_2 == 30:
          paksha = 'newmoon'
    
      if tithi_2%15 == 0:
        tithi_str_2 = paksha + tithi_names[tithi_2]
      else:
        tithi_str_2 = paksha + tithi_names[tithi_2%15]
      
      tithi_remaining_2 = 12+12-(((longitude_moon-longitude_sun)%360)%12)
      tithi_end_2 = tithi_remaining_2/(daily_motion_moon-daily_motion_sun)*24.0
      tithi_end_str_2 = print_end_time(tithi_end_2,jd_rise_tmrw-jd_rise,t_rise)
    else:
     tithi_str_2 = ''
     tithi_end_str_2 = ''
    
    if tithi%15 != 0:
      paksha = ('shukla' if tithi<15 else 'krishna')
    else:
      if tithi == 15:
        paksha = 'fullmoon'
      elif tithi == 30:
        paksha = 'newmoon'
  
    if tithi%15 == 0:
      tithi_str = paksha + tithi_names[tithi]
    else:
      tithi_str = paksha + tithi_names[tithi%15]
    
    tithi_remaining = 12-(((longitude_moon-longitude_sun)%360)%12)
    tithi_end = tithi_remaining/(daily_motion_moon-daily_motion_sun)*24.0
    tithi_end_str = print_end_time(tithi_end,jd_rise_tmrw-jd_rise,t_rise)
  
    #Compute nakshatram details
    n_id = int(1+math.floor((longitude_moon%360) /(360.0/27)))
    n_id_tmrw = int(1+math.floor((longitude_moon_tmrw%360) /(360.0/27)))
    if (n_id_tmrw-n_id)%27 > 1:
      #there is a double change
      nakshatram_str_2 = nakshatra_names[n_id+1]
      nakshatram_remaining_2 = (360.0/27)+(360.0/27) - ((longitude_moon%360) % (360.0/27))
      nakshatram_end_2 = nakshatram_remaining_2/daily_motion_moon*24
      nakshatram_end_str_2 = print_end_time(nakshatram_end_2,jd_rise_tmrw-jd_rise,t_rise)
    else:
      nakshatram_str_2 = ''
      nakshatram_end_str_2 = ''
    
    nakshatram_str = nakshatra_names[n_id]
    nakshatram_remaining = (360.0/27) - ((longitude_moon%360) % (360.0/27))
    nakshatram_end = nakshatram_remaining/daily_motion_moon*24
    nakshatram_end_str = print_end_time(nakshatram_end,jd_rise_tmrw-jd_rise,t_rise)
   
    #Sunrise/sunset and related stuff (like rahu, yama)
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
    rahu = '%s--%s' % (print_time(rahukalam_start), print_time(rahukalam_end))
    yama = '%s--%s' % (print_time(yamakandam_start),print_time(yamakandam_end))
    
    #Layout calendar in LATeX format
    if d==1:
      if m>1:
        if weekday!=0: #Space till Sunday
          for i in range(weekday,6):
            print "{}  &"
          print "\\\\ \hline"
        print '\end{tabular}'
        print '\n\n'
  
      #Begin tabular
      print '\\begin{tabular}{|c|c|c|c|c|c|c|}'
      print '\multicolumn{7}{c}{\Large \\bfseries %s %s}\\\\[3mm]' % (month[m],y)
      print '\hline'
      print '\\textbf{SUN} & \\textbf{MON} & \\textbf{TUE} & \\textbf{WED} & \\textbf{THU} & \\textbf{FRI} & \\textbf{SAT} \\\\ \hline'
      #print '\\textbf{भानु} & \\textbf{इन्दु} & \\textbf{भौम} & \\textbf{बुध} & \\textbf{गुरु} & \\textbf{भृगु} & \\textbf{स्थिर} \\\\ \hline'
  
      #Blanks for previous weekdays
      for i in range(0,weekday):
        print "{}  &"
    
#    if nakshatram_end_str_2!='' and tithi_end_str_2!='':
#      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,tithi_str_2,tithi_end_str_2,nakshatram_str,nakshatram_end_str,nakshatram_str_2,nakshatram_end_str_2,rahu,yama)
#    elif nakshatram_end_str_2!='' and tithi_end_str_2=='':
#      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,nakshatram_str,nakshatram_end_str,nakshatram_str_2,nakshatram_end_str_2,rahu,yama)
#    elif nakshatram_end_str_2=='' and tithi_end_str_2!='':
#      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,tithi_str_2,tithi_end_str_2,nakshatram_str,nakshatram_end_str,rahu,yama)
#    elif nakshatram_end_str_2=='' and tithi_end_str_2=='':
#      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{}{}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,nakshatram_str,nakshatram_end_str,rahu,yama)
    if nakshatram_end_str_2!='' and tithi_end_str_2!='':
      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,tithi_str_2,tithi_end_str_2,nakshatram_str,nakshatram_end_str,nakshatram_str_2,nakshatram_end_str_2,rahu,yama)
    elif nakshatram_end_str_2!='' and tithi_end_str_2=='':
      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,nakshatram_str,nakshatram_end_str,nakshatram_str_2,nakshatram_end_str_2,rahu,yama)
    elif nakshatram_end_str_2=='' and tithi_end_str_2!='':
      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,tithi_str_2,tithi_end_str_2,nakshatram_str,nakshatram_end_str,rahu,yama)
    elif nakshatram_end_str_2=='' and tithi_end_str_2=='':
      print '\caldata{%s}{%s}{\\sundata{%s}{%s}{%s}}{}{}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (d,month_data,rise,set,madhya,tithi_str,tithi_end_str,nakshatram_str,nakshatram_end_str,rahu,yama)

  
    if weekday==6:
      print "\\\\ \hline"
    else:
      print "&"
  
    jd = jd + 1

    last_sun_month = sun_month

    if m==12 and d==31:
      year = year + 1
  
    # For debugging specific dates
    #if m==4 and d==10:
    #  break
  
  for i in range(weekday+1,6):
    print "{}  &"
  if weekday!=6:
    print "\\\\ \hline"
  print '\end{tabular}'
  print '\n\n'
  
  #print '\\input{%d-%s.tex}' % (year,city_name)
  print template_lines[-2][:-1]
  print template_lines[-1][:-1]

if __name__=='__main__':
  main()
else:
  '''Imported as a module'''
