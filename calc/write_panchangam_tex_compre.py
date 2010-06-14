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
  [h,m,s]=deci2sexa(d)
  return '%02d:%02d' % (h,m)

def get_last_dhanur_transit (jd_start,latitude,longitude):
  swisseph.set_sid_mode(swisseph.SIDM_LAHIRI) #Force Lahiri Ayanamsha
  for d in range(-25,0):
    jd = jd_start + d
    [y,m,d,t] = swisseph.revjul(jd)
  
    jd_sunrise=swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=longitude,
      lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
    jd_sunrise_tmrw=swisseph.rise_trans(jd_start=jd+1,body=swisseph.SUN,
      lon=longitude,lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
    jd_sunset =swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=longitude,
      lat=latitude,rsmi=swisseph.CALC_SET|swisseph.BIT_DISC_CENTER)[1][0]
  
    longitude_sun=swisseph.calc_ut(jd_sunrise,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_sunrise)
    longitude_sun_set=swisseph.calc_ut(jd_sunset,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_sunset)
    sun_month_rise = masa_names[int(1+math.floor(((longitude_sun)%360)/30.0))]
    sun_month = masa_names[int(1+math.floor(((longitude_sun_set)%360)/30.0))]
    longitude_sun_tmrw=swisseph.calc_ut(jd_sunrise+1,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_sunrise+1)
    sun_month_tmrw = masa_names[int(1+math.floor(((longitude_sun_tmrw)%360)/30.0))]

    if sun_month_rise!=sun_month_tmrw:
      if sun_month!=sun_month_tmrw:
        return jd+1
      else:
        return jd
  
def print_end_time (end_time, day_night_length, sunrise_time):
  if end_time/24.0>day_night_length:
    end_time_str = ahoratram
  else:
    te=deci2sexa(sunrise_time+end_time)
    if te[0]>=24:
      suff = '(+1)'
      te[0] = te[0]-24
    else:
      suff = '\\hspace{2ex}'
    end_time_str = '%02d:%02d%s' % (te[0],te[1],suff)
  return end_time_str

def get_ekadashi_name(paksha,month):
  if paksha=='shukla':
    if month==int(month):
      return '%s~%s' % (shukla_ekadashi_names[month],ekadashi)
    else:
      return '%s~%s' % (shukla_ekadashi_names[13],ekadashi)
  elif paksha=='krishna':
    if month==int(month):
      return '%s~%s' % (krishna_ekadashi_names[month],ekadashi)
    else:
      return '%s~%s' % (krishna_ekadashi_names[13],ekadashi)

def get_chandra_masa(month,chandra_masa_names):
  if month==int(month):
    return chandra_masa_names[month]
  else:
    return '%s~(%s)' % (chandra_masa_names[int(month)+1],adhika) 

def get_angam_data_string(angam_names, arc_len, jd_sunrise, jd_sunrise_tmrw, 
  t_sunrise, longitude_moon, longitude_sun, longitude_moon_tmrw, 
  longitude_sun_tmrw, w):

  daily_motion_moon = (longitude_moon_tmrw-longitude_moon)%360
  daily_motion_sun = (longitude_sun_tmrw-longitude_sun)%360

  num_angas = int(360.0/arc_len)
  angam = [0]*3
  angam_str = ['']*3
  angam_end_str = ['']*3
  angam_end = [0]*3
  angam_remaining = [0]*3

  #Compute karanam details
  angam[0] = int(1+math.floor((longitude_moon*w[0]+longitude_sun*w[1])%360 / arc_len))
  angam_tmrw = int(1+math.floor((longitude_moon_tmrw*w[0]+longitude_sun_tmrw*w[1])%360 / arc_len))

  # There cannot be more than 3 angams (max=3 for karanams) in a day, 
  # because of total arc ~ 12 deg and arclen per angam
  for i in range(0,3):
    if ((angam_tmrw-angam[0])%num_angas > i) or (i==0): #i=0 must be considered, because the angam may not change till the next sunrise
      #multiple change
      angam[i]=((angam[0]+(i-1))%num_angas)+1
      angam_str[i] = angam_names[angam[i]]
      angam_remaining[i] = arc_len*(i+1)-(((longitude_moon*w[0]+
        longitude_sun*w[1])%360)%arc_len)
      angam_end[i] = angam_remaining[i]/(daily_motion_moon*w[0]+
        daily_motion_sun*w[1])*24.0
      angam_end_str[i] = print_end_time(angam_end[i],jd_sunrise_tmrw-jd_sunrise,t_sunrise)
    else:
      angam_str[i] = ''
      angam_end_str[i] = ''
      
    if (angam_end_str[i] == ahoratram and i!=0):
      #needs correction, owing to the fact that we compute longitude every 24h,
      #rather than at next sunrise the second/third angam cannot be 'all day'!
      #It's ending will reflect in tomorrow's calendar
      angam_str[i] = ''
      angam_end_str[i] = ''


  angam_data_string=''
  for i in range(0,3):
    if angam_str[i] != '': 
      if i==2:
        angam_data_string = angam_data_string+'\\\\'
      if (angam_end_str[i] == ahoratram):
        angam_data_string = '%s\\mbox{%s {\\tiny \\RIGHTarrow} %s}'           % (angam_data_string,angam_str[i],angam_end_str[i])
      else:
        angam_data_string = '%s\\mbox{%s {\\tiny \\RIGHTarrow} \\textsf{%s}}' % (angam_data_string,angam_str[i],angam_end_str[i])
    
  return [angam[0],angam_data_string]

#USEFUL 'constants'
yamagandam_octets  = [5,4,3,2,1,7,6]
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
  
  swisseph.set_sid_mode(swisseph.SIDM_LAHIRI) #Force Lahiri Ayanamsha
  
  sun_month_day = jd-get_last_dhanur_transit(jd,latitude,longitude)
  
  month_start_after_set = 0
  
  template_file=open('cal_template_compre.tex')
  template_lines=template_file.readlines()
  for i in range(0,len(template_lines)-3):
    print template_lines[i][:-1]
  
  samvatsara_id = (year - 1568)%60 + 1; #distance from prabhava
  samvatsara_names = '%s–%s' % (year_names[samvatsara_id], 
    year_names[(samvatsara_id%60)+1])
  
  print '\\mbox{}'
  print '{\\font\\x="Warnock Pro" at 60 pt\\x %d\\\\[0.3cm]}' % year
  print '\\mbox{\\font\\x="Sanskrit 2003:script=deva" at 48 pt\\x %s}\\\\[0.5cm]' % samvatsara_names
  print '{\\font\\x="Warnock Pro" at 48 pt\\x \\uppercase{%s}\\\\[0.3cm]}' % city_name
  print '\hrule'


  #INITIALISE VARIABLES
  jd_sunrise=[None]*368
  jd_sunset=[None]*368
  jd_moonrise=[None]*368
  longitude_moon=[None]*368
  longitude_sun=[None]*368
  longitude_sun_set=[None]*368
  sun_month_id=[None]*368
  sun_month=[None]*368
  sun_month_rise=[None]*368
  moon_month=[None]*368
  month_data=[None]*368
  tithi_data_string=[None]*368
  tithi_sunrise=[None]*368
  nakshatram_data_string=[None]*368
  nakshatram_sunrise=[None]*368
  karanam_data_string=[None]*368
  karanam_sunrise=[None]*368
  yogam_data_string=[None]*368
  yogam_sunrise=[None]*368
  weekday=[None]*368
  sunrise=[None]*368
  sunset=[None]*368
  madhya=[None]*368
  rahu=[None]*368
  yama=[None]*368
  festivals=['']*368
  
  weekday_start=swisseph.day_of_week(jd)+1
  #swisseph has Mon = 0, non-intuitively!
  
  for d in range(0,367):
    jd = jd_start-1+d
    [y,m,dt,t] = swisseph.revjul(jd)
    weekday = (weekday_start -1 + d)%7 
  
    local_time = pytz.timezone(tz).localize(datetime(y, m, dt, 6, 0, 0))
    #checking @ 6am local - can we do any better?
    tz_off=datetime.utcoffset(local_time).seconds/3600.0 
    #compute offset from UTC

    jd_sunrise[d+1]=swisseph.rise_trans(jd_start=jd+1,body=swisseph.SUN,
      lon=longitude,lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
    jd_sunset[d+1]=swisseph.rise_trans(jd_start=jd+1,body=swisseph.SUN,
      lon=longitude,lat=latitude,rsmi=swisseph.CALC_SET|swisseph.BIT_DISC_CENTER)[1][0]
    jd_moonrise[d+1]=swisseph.rise_trans(jd_start=jd+1,body=swisseph.MOON,
      lon=longitude,lat=latitude,rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
  
    longitude_sun[d+1]=swisseph.calc_ut(jd_sunrise[d+1],swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_sunrise[d+1])
    longitude_moon[d+1]=swisseph.calc_ut(jd_sunrise[d+1],swisseph.MOON)[0]-swisseph.get_ayanamsa(jd_sunrise[d+1])
    longitude_sun_set[d+1]=swisseph.calc_ut(jd_sunset[d+1],swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_sunset[d+1])
    
    sun_month_id[d+1] = int(1+math.floor(((longitude_sun_set[d+1])%360)/30.0))
    sun_month[d+1] = masa_names[int(1+math.floor(((longitude_sun_set[d+1])%360)/30.0))]

    sun_month_rise[d+1] = masa_names[int(1+math.floor(((longitude_sun[d+1])%360)/30.0))]

    if(d==0):
      continue

    t_sunrise=(jd_sunrise[d]-jd)*24.0+tz_off;
    t_sunset=(jd_sunset[d]-jd)*24.0+tz_off;

  
    #Solar month calculations
    if month_start_after_set==1:
      sun_month_day = 0
      month_start_after_set = 0
  
    if sun_month[d]!=sun_month[d+1]:
      sun_month_day = sun_month_day + 1

      if sun_month[d]!=sun_month_rise[d+1]:
        month_start_after_set=1
        [_m,sun_month_end_time] = get_angam_data_string(masa_names, 30, jd_sunrise[d],
          jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], longitude_moon[d+1],
          longitude_sun[d+1], [0,1])
 
    elif sun_month_rise[d]!=sun_month[d]:
      #mAsa pirappu!
      #sun moves into next rAsi before sunset -- check rules!
      sun_month_day = 1

      [_m,sun_month_end_time] = get_angam_data_string(masa_names, 30, jd_sunrise[d],
      jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], longitude_moon[d+1],
      longitude_sun[d+1], [0,1])
    
    else:
      sun_month_day = sun_month_day + 1
      sun_month_end_time = ''
    
    month_data[d] = '\\sunmonth{%s}{%d}{%s}' % (sun_month[d],sun_month_day,sun_month_end_time)
  
    #Sunrise/sunset and related stuff (like rahu, yama)
    [rhs, rms, rss] = deci2sexa(t_sunrise)  #rise hour sun, rise minute sun, rise sec sun
    [shs, sms, sss] = deci2sexa(t_sunset)   
  
    length_of_day = t_sunset-t_sunrise
    yamagandam_start = t_sunrise + (1/8.0)*(yamagandam_octets[weekday]-1)*length_of_day
    yamagandam_end = yamagandam_start + (1/8.0)*length_of_day
    rahukalam_start = t_sunrise + (1/8.0)*(rahukalam_octets[weekday]-1)*length_of_day
    rahukalam_end = rahukalam_start + (1/8.0)*length_of_day
    madhyahnikam_start = t_sunrise + (1/5.0)*length_of_day
  
    sunrise[d]  = '%02d:%02d' % (rhs,rms)
    sunset[d]   = '%02d:%02d' % (shs,sms)
    madhya[d] = print_time(madhyahnikam_start)
    rahu[d] = '%s--%s' % (print_time(rahukalam_start), print_time(rahukalam_end))
    yama[d] = '%s--%s' % (print_time(yamagandam_start),print_time(yamagandam_end))
    
    [tithi_sunrise[d],tithi_data_string[d]]=get_angam_data_string(tithi_names, 12, jd_sunrise[d],
      jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], longitude_moon[d+1],
      longitude_sun[d+1], [1,-1])
    [nakshatram_sunrise [d], nakshatram_data_string[d]]=get_angam_data_string(nakshatra_names, (360.0/27.0),
      jd_sunrise[d], jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], 
      longitude_moon[d+1], longitude_sun[d+1], [1,0])
    [karanam_sunrise[d],karanam_data_string[d]]=get_angam_data_string(karanam_names, 6, jd_sunrise[d],
      jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], longitude_moon[d+1],
      longitude_sun[d+1], [1,-1])
    [yogam_sunrise[d],yogam_data_string[d]]=get_angam_data_string(yogam_names, (360.0/27.0), jd_sunrise[d],
      jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], longitude_moon[d+1],
      longitude_sun[d+1], [1,1])

  last_month_change = 1
  last_moon_month = None
  for d in range(1,367):
    #Assign moon_month for each day
    if(tithi_sunrise[d]==1):
      for i in range(last_month_change,d):
        print '%%Setting moon_month to sun_month_id, for i=%d:%d to %d' %(last_month_change,d-1,sun_month_id[d])
        if (sun_month_id[d]==last_moon_month):
          moon_month[i] = sun_month_id[d]%12 + 0.5
        else:
          moon_month[i] = sun_month_id[d]
      last_month_change = d 
      last_moon_month = sun_month_id[d]

  for i in range(last_month_change,367):
    moon_month[i]=sun_month_id[last_month_change-1]+1
    
  for d in range(1,367):
    jd = jd_start-1+d
    [y,m,dt,t] = swisseph.revjul(jd)
    print '%%#%02d-%02d-%4d: %3d:%s (sunrise tithi=%d) {%s}' % (dt,m,y,d,moon_month[d],tithi_sunrise[d],tithi_data_string[d])

  for d in range(1,367):
    jd = jd_start-1+d
    [y,m,dt,t] = swisseph.revjul(jd)
    weekday = (weekday_start -1 + d)%7 

    #Festival details
    if tithi_sunrise[d]==11 or tithi_sunrise[d]==12: #One of two consecutive tithis must appear @ sunrise!
      #check for shukla ekadashi
      if (tithi_sunrise[d]==11 and tithi_sunrise[d+1]==11) or (tithi_sunrise[d]==10 and tithi_sunrise[d+1]==12):
        festivals[d+1]=get_ekadashi_name(paksha='shukla',month=moon_month[d])
      elif (tithi_sunrise[d]==11 and tithi_sunrise[d+1]!=11): 
        festivals[d]=get_ekadashi_name(paksha='shukla',month=moon_month[d])

    if tithi_sunrise[d]==26 or tithi_sunrise[d]==27:
      #check for krishna ekadashi
      if (tithi_sunrise[d]==26 and tithi_sunrise[d+1]==27) or (tithi_sunrise[d]==26 and tithi_sunrise[d+1]==27):
        festivals[d+1]=get_ekadashi_name(paksha='krishna',month=moon_month[d])
      elif (tithi_sunrise[d]==26 and tithi_sunrise[d+1]!=26): 
        festivals[d]=get_ekadashi_name(paksha='krishna',month=moon_month[d])

 

    #Layout calendar in LATeX format
    if dt==1:
      if m>1:
        if weekday!=0: #Space till Sunday
          for i in range(weekday,6):
            print "{}  &"
          print "\\\\ \hline"
        print '\end{tabular}'
        print '\n\n'
  
      #Begin tabular
      print '\\begin{tabular}{|c|c|c|c|c|c|c|}'
      print '\multicolumn{7}{c}{\Large \\bfseries \sffamily %s %s}\\\\[3mm]' % (month[m],y)
      print '\hline'
      print '\\textbf{\\textsf{SUN}} & \\textbf{\\textsf{MON}} & \\textbf{\\textsf{TUE}} & \\textbf{\\textsf{WED}} & \\textbf{\\textsf{THU}} & \\textbf{\\textsf{FRI}} & \\textbf{\\textsf{SAT}} \\\\ \hline'
      #print '\\textbf{भानु} & \\textbf{इन्दु} & \\textbf{भौम} & \\textbf{बुध} & \\textbf{गुरु} & \\textbf{भृगु} & \\textbf{स्थिर} \\\\ \hline'
  
      #Blanks for previous weekdays
      for i in range(0,weekday):
        print "{}  &"

    print '\caldata{\\textcolor{%s}{%s}}{%s{%s}}{\\sundata{%s}{%s}{%s}}{\\tnyk{%s}{%s}{%s}{%s}}{\\rahuyama{%s}{%s}}{%s} ' % (daycol[weekday],
      dt,month_data[d],get_chandra_masa(moon_month[d],chandra_masa_names),sunrise[d],sunset[d],madhya[d],tithi_data_string[d],nakshatram_data_string[d],
      yogam_data_string[d],karanam_data_string[d],rahu[d],yama[d],festivals[d])
  
    if weekday==6:
      print "\\\\ \hline"
    else:
      print "&"
  
    if m==12 and dt==31:
      break
  
    # For debugging specific dates
    #if m==4 and dt==10:
    #  break
  
  for i in range(weekday+1,6):
    print "{}  &"
  if weekday!=6:
    print "\\\\ \hline"
  print '\end{tabular}'
  print '\n\n'
  
  print template_lines[-2][:-1]
  print template_lines[-1][:-1]

if __name__=='__main__':
  main()
else:
  '''Imported as a module'''
