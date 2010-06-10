#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import swisseph
from datetime import *
import pytz
from pytz import timezone
from skt_names import *

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
#daycol = {0:'red',1:'blue',2:'blue',3:'blue',4:'blue',5:'blue',6:'red'}
daycol = {0:'blue',1:'blue',2:'blue',3:'blue',4:'blue',5:'blue',6:'blue'}

month = {1:'JANUARY', 2:'FEBRUARY', 3:'MARCH', 4:'APRIL', 5:'MAY', 6:'JUNE', 7:'JULY', 8:'AUGUST', 9:'SEPTEMBER', 10:'OCTOBER', 11: 'NOVEMBER', 12:'DECEMBER'}

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
      #double change
      tithi_2=(tithi%30)+1
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
      if tithi_end_str_2 == '\\textsf{अहोरात्रम्}':
        #needs correction, owing to the fact that we compute longitude every 24h, rather than at next sunrise
        #the second tithi cannot be 'all day'! It's ending will reflect in tomorrow's calendar
        tithi_str_2 = ''
        tithi_end_str_2 = ''
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
      nakshatram_str_2 = nakshatra_names[n_id%27+1]
      nakshatram_remaining_2 = (360.0/27)+(360.0/27) - ((longitude_moon%360) % (360.0/27))
      nakshatram_end_2 = nakshatram_remaining_2/daily_motion_moon*24
      nakshatram_end_str_2 = print_end_time(nakshatram_end_2,jd_rise_tmrw-jd_rise,t_rise)
      if nakshatram_end_str_2 == '\\textsf{अहोरात्रम्}':
        #needs correction, owing to the fact that we compute longitude every 24h, rather than at next sunrise
        #the second nakshatram cannot be 'all day'! It's ending will reflect in tomorrow's calendar
        nakshatram_str_2 = ''
        nakshatram_end_str_2 = ''
    else:
      nakshatram_str_2 = ''
      nakshatram_end_str_2 = ''
    
    nakshatram_str = nakshatra_names[n_id]
    nakshatram_remaining = (360.0/27) - ((longitude_moon%360) % (360.0/27))
    nakshatram_end = nakshatram_remaining/daily_motion_moon*24
    nakshatram_end_str = print_end_time(nakshatram_end,jd_rise_tmrw-jd_rise,t_rise)
   
    #Compute karanam details
    karanam = int(1+math.floor((longitude_moon-longitude_sun)%360 / 6.0))
    karanam_tmrw = int(1+math.floor((longitude_moon_tmrw-longitude_sun_tmrw)%360 / 6.0))

    if (karanam_tmrw-karanam)%60 > 3:
      #quadruple change
      karanam_4=((karanam+2)%60)+1
      karanam_str_4 = karanam_names[karanam_4]
      
      karanam_remaining_4 = 6*3+6-(((longitude_moon-longitude_sun)%360)%6)
      karanam_end_4 = karanam_remaining_4/(daily_motion_moon-daily_motion_sun)*24.0
      karanam_end_str_4 = print_end_time(karanam_end_4,jd_rise_tmrw-jd_rise,t_rise)
      if karanam_end_str_4 == '\\textsf{अहोरात्रम्}':
        #needs correction, owing to the fact that we compute longitude every 24h, rather than at next sunrise
        #the second karanam cannot be 'all day'! It's ending will reflect in tomorrow's calendar
        karanam_str_4 = ''
        karanam_end_str_4 = ''
    else:
     karanam_str_4 = ''
     karanam_end_str_4 = ''

    if (karanam_tmrw-karanam)%60 > 2:
      #triple change
      karanam_3=((karanam+1)%60)+1
      karanam_str_3 = karanam_names[karanam_3]
      
      karanam_remaining_3 = 6*2+6-(((longitude_moon-longitude_sun)%360)%6)
      karanam_end_3 = karanam_remaining_3/(daily_motion_moon-daily_motion_sun)*24.0
      karanam_end_str_3 = print_end_time(karanam_end_3,jd_rise_tmrw-jd_rise,t_rise)
      if karanam_end_str_3 == '\\textsf{अहोरात्रम्}':
        #needs correction, owing to the fact that we compute longitude every 24h, rather than at next sunrise
        #the second karanam cannot be 'all day'! It's ending will reflect in tomorrow's calendar
        karanam_str_3 = ''
        karanam_end_str_3 = ''
    else:
     karanam_str_3 = ''
     karanam_end_str_3 = ''

    if (karanam_tmrw-karanam)%60 > 1:
      #double change
      karanam_2=(karanam%60)+1
      karanam_str_2 = karanam_names[karanam_2]
      
      karanam_remaining_2 = 6+6-(((longitude_moon-longitude_sun)%360)%6)
      karanam_end_2 = karanam_remaining_2/(daily_motion_moon-daily_motion_sun)*24.0
      karanam_end_str_2 = print_end_time(karanam_end_2,jd_rise_tmrw-jd_rise,t_rise)
      if karanam_end_str_2 == '\\textsf{अहोरात्रम्}':
        #needs correction, owing to the fact that we compute longitude every 24h, rather than at next sunrise
        #the second karanam cannot be 'all day'! It's ending will reflect in tomorrow's calendar
        karanam_str_2 = ''
        karanam_end_str_2 = ''
    else:
     karanam_str_2 = ''
     karanam_end_str_2 = ''
    
    karanam_str = karanam_names[karanam]
    
    karanam_remaining = 6-(((longitude_moon-longitude_sun)%6)%6)
    karanam_end = karanam_remaining/(daily_motion_moon-daily_motion_sun)*24.0
    karanam_end_str = print_end_time(karanam_end,jd_rise_tmrw-jd_rise,t_rise)
    print '%%Karanam 1: %s; end: %s;'  % (karanam_str,karanam_end_str)
    print  ' Karanam 2: %s; end: %s;'  % (karanam_str_2,karanam_end_str_2)
    print  ' Karanam 3: %s; end: %s;'  % (karanam_str_3,karanam_end_str_3)
    print  ' Karanam 4: %s; end: %s\n' % (karanam_str_4,karanam_end_str_4)

    #Compute yogam details
    yogam = int(1+math.floor((longitude_moon+longitude_sun)%360 / (360.0/27.0)))
    yogam_tmrw = int(1+math.floor((longitude_moon_tmrw-longitude_sun_tmrw)%360 / (360.0/27.0)))

    if (yogam_tmrw-yogam)%27 > 2:
      #triple change
      yogam_3=((yogam+1)%27)+1
      yogam_str_3 = yogam_names[yogam_3]
      
      yogam_remaining_3 = (360.0/27.0)+(360.0/27.0)-(((longitude_moon+longitude_sun)%360)%(360.0/27.0))
      yogam_end_3 = yogam_remaining_3/(daily_motion_moon+daily_motion_sun)*24.0
      yogam_end_str_3 = print_end_time(yogam_end_3,jd_rise_tmrw-jd_rise,t_rise)
      if yogam_end_str_3 == '\\textsf{अहोरात्रम्}':
        #needs correction, owing to the fact that we compute longitude every 24h, rather than at next sunrise
        #the second yogam cannot be 'all day'! It's ending will reflect in tomorrow's calendar
        yogam_str_3 = ''
        yogam_end_str_3 = ''
    else:
     yogam_str_3 = ''
     yogam_end_str_3 = ''

    if (yogam_tmrw-yogam)%27 > 1:
      #double change
      yogam_2=(yogam%27)+1
      yogam_str_2 = yogam_names[yogam_2]
      
      yogam_remaining_2 = (360.0/27.0)+(360.0/27.0)-(((longitude_moon+longitude_sun)%360)%(360.0/27.0))
      yogam_end_2 = yogam_remaining_2/(daily_motion_moon+daily_motion_sun)*24.0
      yogam_end_str_2 = print_end_time(yogam_end_2,jd_rise_tmrw-jd_rise,t_rise)
      if yogam_end_str_2 == '\\textsf{अहोरात्रम्}':
        #needs correction, owing to the fact that we compute longitude every 24h, rather than at next sunrise
        #the second yogam cannot be 'all day'! It's ending will reflect in tomorrow's calendar
        yogam_str_2 = ''
        yogam_end_str_2 = ''
    else:
     yogam_str_2 = ''
     yogam_end_str_2 = ''
    
    yogam_str = yogam_names[yogam]
    
    yogam_remaining = (360.0/27.0)-(((longitude_moon+longitude_sun)%360)%(360.0/27.0))
    yogam_end = yogam_remaining/(daily_motion_moon+daily_motion_sun)*24.0
    yogam_end_str = print_end_time(yogam_end,jd_rise_tmrw-jd_rise,t_rise)

    print '%%Yogam 1: %s; end: %s;' % (yogam_str,yogam_end_str)
    print ' Yogam 2: %s; end: %s;' % (yogam_str_2,yogam_end_str_2)
    print ' Yogam 3: %s; end: %s\n' % (yogam_str_3,yogam_end_str_3)

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
    
    if nakshatram_end_str_2!='' and tithi_end_str_2!='':
      print '\caldata{\\textcolor{%s}{%s}}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (daycol[weekday],d,month_data,rise,set,madhya,tithi_str,tithi_end_str,tithi_str_2,tithi_end_str_2,nakshatram_str,nakshatram_end_str,nakshatram_str_2,nakshatram_end_str_2,rahu,yama)
    elif nakshatram_end_str_2!='' and tithi_end_str_2=='':
      print '\caldata{\\textcolor{%s}{%s}}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (daycol[weekday],d,month_data,rise,set,madhya,tithi_str,tithi_end_str,nakshatram_str,nakshatram_end_str,nakshatram_str_2,nakshatram_end_str_2,rahu,yama)
    elif nakshatram_end_str_2=='' and tithi_end_str_2!='':
      print '\caldata{\\textcolor{%s}{%s}}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (daycol[weekday],d,month_data,rise,set,madhya,tithi_str,tithi_end_str,tithi_str_2,tithi_end_str_2,nakshatram_str,nakshatram_end_str,rahu,yama)
    elif nakshatram_end_str_2=='' and tithi_end_str_2=='':
      print '\caldata{\\textcolor{%s}{%s}}{%s}{\\sundata{%s}{%s}{%s}}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{%s} {\\tiny \\RIGHTarrow} %s}{}{}{\\textsf{राहु}~%s~~\\textsf{यम}~%s} ' % (daycol[weekday],d,month_data,rise,set,madhya,tithi_str,tithi_end_str,nakshatram_str,nakshatram_end_str,rahu,yama)
  
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
