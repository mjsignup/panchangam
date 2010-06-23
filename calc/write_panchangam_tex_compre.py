#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import swisseph
from datetime import *
import pytz
from pytz import timezone
from skt_names import *
from festival_rules import *

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
    sun_month_rise = int(1+math.floor(((longitude_sun)%360)/30.0))
    sun_month = int(1+math.floor(((longitude_sun_set)%360)/30.0))
    longitude_sun_tmrw=swisseph.calc_ut(jd_sunrise+1,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_sunrise+1)
    sun_month_tmrw = int(1+math.floor(((longitude_sun_tmrw)%360)/30.0))

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

def get_tithi(jd):
  ldiff=(swisseph.calc_ut(jd,swisseph.MOON)[0]-swisseph.calc_ut(jd,swisseph.SUN)[0])%360
  return int(1+math.floor(ldiff / 12.0))

def get_nakshatram(jd):
  lmoon=(swisseph.calc_ut(jd,swisseph.MOON)[0]-swisseph.get_ayanamsa(jd))%360
  return int(1+math.floor(lmoon / (360.0/27.0)))

def get_chandra_masa(month,chandra_masa_names):
  if month==int(month):
    return chandra_masa_names[month]
  else:
    return '%s~(%s)' % (chandra_masa_names[int(month)+1],adhika) 

def get_festival_day_purvaviddha(festival_angam,angam_sunrise,d,jd_sunrise,jd_sunrise_tmrw,get_angam_func,min_t):
  t_cutoff=(jd_sunrise_tmrw-jd_sunrise)*min_t/60.0 #at least 4 nazhis
  
  if angam_sunrise[d]==(festival_angam-1) or angam_sunrise[d]==festival_angam:
    if angam_sunrise[d]==festival_angam or (angam_sunrise[d]==(festival_angam-1) and angam_sunrise[d+1]==(festival_angam+1)):
      if angam_sunrise[d-1]!=festival_angam:#otherwise yesterday would have already been assigned
        #Return d-1 if angam changes within say 2hrs, else d
        if get_angam_func(jd_sunrise+t_cutoff)!=angam_sunrise[d]:
          return d-1
        else:
          return d
    elif angam_sunrise[d+1]==festival_angam:
      #Return d if angam changes within say 2hrs, else d-1
      if get_angam_func(jd_sunrise_tmrw+t_cutoff)!=angam_sunrise[d+1]:
        return d
      else:
        return d+1
  return None

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
MON = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11: 'November', 12:'December'}
WDAY = {0:'Sun',1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat'}

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
  new_yr=mesha_sankranti+'~('+year_names[(samvatsara_id%60)+1]+'-'+samvatsara+')'
  
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
  festival_day_list={}
  festivals=['']*368
  
  weekday_start=swisseph.day_of_week(jd)+1
  #swisseph has Mon = 0, non-intuitively!
  
  for d in range(-1,367):
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
    sun_month[d+1] = int(1+math.floor(((longitude_sun_set[d+1])%360)/30.0))

    sun_month_rise[d+1] = int(1+math.floor(((longitude_sun[d+1])%360)/30.0))

    if(d<=0):
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
    
    month_data[d] = '\\sunmonth{%s}{%d}{%s}' % (masa_names[sun_month[d]],sun_month_day,sun_month_end_time)

    #KARADAYAN NOMBU -- easy to check here
    if sun_month_end_time !='': #month ends today
      if (sun_month[d]==12 and sun_month_day==1) or (sun_month[d]==11 and sun_month_day!=1):
        festival_day_list[karadayan_nombu] = [d]
  
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
    [nakshatram_sunrise[d], nakshatram_data_string[d]]=get_angam_data_string(nakshatra_names, (360.0/27.0),
      jd_sunrise[d], jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], 
      longitude_moon[d+1], longitude_sun[d+1], [1,0])
    [karanam_sunrise[d],karanam_data_string[d]]=get_angam_data_string(karanam_names, 6, jd_sunrise[d],
      jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], longitude_moon[d+1],
      longitude_sun[d+1], [1,-1])
    [yogam_sunrise[d],yogam_data_string[d]]=get_angam_data_string(yogam_names, (360.0/27.0), jd_sunrise[d],
      jd_sunrise[d+1], t_sunrise, longitude_moon[d], longitude_sun[d], longitude_moon[d+1],
      longitude_sun[d+1], [1,1])

  #ASSIGN MOON MONTHS
  last_month_change = 1
  last_moon_month = None
  for d in range(1,367):
    #Assign moon_month for each day
    if(tithi_sunrise[d]==1):
      for i in range(last_month_change,d):
        #print '%%#Setting moon_month to sun_month_id, for i=%d:%d to %d' %(last_month_change,d-1,sun_month_id[d])
        if (sun_month_id[d]==last_moon_month):
          moon_month[i] = sun_month_id[d]%12 + 0.5
        else:
          moon_month[i] = sun_month_id[d]
      last_month_change = d 
      last_moon_month = sun_month_id[d]
    elif(tithi_sunrise[d]==2 and tithi_sunrise[d-1]==30):
      #prathama tithi was never seen @ sunrise
      for i in range(last_month_change,d):
        #print '%%@Setting moon_month to sun_month_id, for i=%d:%d to %d (last month = %d)' %(last_month_change,d-1,sun_month_id[d],last_moon_month)
        if (sun_month_id[d-1]==last_moon_month):
          moon_month[i] = sun_month_id[d-1]%12 + 0.5
        else:
          moon_month[i] = sun_month_id[d-1]
      last_month_change = d 
      last_moon_month = sun_month_id[d-1]

  for i in range(last_month_change,367):
    moon_month[i]=sun_month_id[last_month_change-1]+1
    
  #for d in range(1,367):
    #jd = jd_start-1+d
    #[y,m,dt,t] = swisseph.revjul(jd)
    #print '%%#%02d-%02d-%4d: %3d:%s (sunrise tithi=%d) {%s}' % (dt,m,y,d,moon_month[d],tithi_sunrise[d],tithi_data_string[d])


  #PRINT CALENDAR

  for d in range(1,367):
    jd = jd_start-1+d
    [y,m,dt,t] = swisseph.revjul(jd)
    weekday = (weekday_start -1 + d)%7 

    ##################
    #Festival details#
    ##################

    ###--- MONTHLY VRATAMS ---###

    #EKADASHI Vratam
    if tithi_sunrise[d]==11 or tithi_sunrise[d]==12: #One of two consecutive tithis must appear @ sunrise!
      #check for shukla ekadashi
      if (tithi_sunrise[d]==11 and tithi_sunrise[d+1]==11): 
        festivals[d+1]=sarva+'~'+get_ekadashi_name(paksha='shukla',month=moon_month[d])#moon_month[d] or [d+1]?
        if moon_month[d+1]==4:
          festivals[d+1]+='\\\\'+chaturmasya_start
        if moon_month[d+1]==8:
          festivals[d+1]+='\\\\'+chaturmasya_end
      elif (tithi_sunrise[d]==11 and tithi_sunrise[d+1]!=11): 
        #Check dashami end time to decide for whether this is sarva/smartha
        tithi_arunodayam = get_tithi(jd_sunrise[d]-(1/15.0)*(jd_sunrise[d]-jd_sunrise[d-1])) #Two muhurtams is 1/15 of day-length
        if tithi_arunodayam==10:
          festivals[d]=smartha+'~'+get_ekadashi_name(paksha='shukla',month=moon_month[d])
          festivals[d+1]=vaishnava+'~'+get_ekadashi_name(paksha='shukla',month=moon_month[d])
          if moon_month[d]==4:
            festivals[d]+='\\\\'+chaturmasya_start
          if moon_month[d]==8:
            festivals[d]+='\\\\'+chaturmasya_end
        else:
          festivals[d]=sarva+'~'+get_ekadashi_name(paksha='shukla',month=moon_month[d])
          if moon_month[d]==4:
            festivals[d]+='\\\\'+chaturmasya_start
          if moon_month[d]==8:
            festivals[d]+='\\\\'+chaturmasya_end
      elif (tithi_sunrise[d-1]!=11 and tithi_sunrise[d]==12):
        festivals[d]=sarva+'~'+get_ekadashi_name(paksha='shukla',month=moon_month[d])
        if moon_month[d]==4:
          festivals[d]+='\\\\'+chaturmasya_start
        if moon_month[d]==8:
          festivals[d]+='\\\\'+chaturmasya_end

 
    if tithi_sunrise[d]==26 or tithi_sunrise[d]==27: #One of two consecutive tithis must appear @ sunrise!
      #check for krishna ekadashi
      if (tithi_sunrise[d]==26 and tithi_sunrise[d+1]==26): 
        festivals[d+1]=sarva+'~'+get_ekadashi_name(paksha='krishna',month=moon_month[d])#moon_month[d] or [d+1]?
      elif (tithi_sunrise[d]==26 and tithi_sunrise[d+1]!=26): 
        #Check dashami end time to decide for whether this is sarva/smartha
        tithi_arunodayam = get_tithi(jd_sunrise[d]-(1/15.0)*(jd_sunrise[d]-jd_sunrise[d-1])) #Two muhurtams is 1/15 of day-length
        if tithi_arunodayam==25:
          festivals[d]=smartha+'~'+get_ekadashi_name(paksha='krishna',month=moon_month[d])
          festivals[d+1]=vaishnava+'~'+get_ekadashi_name(paksha='krishna',month=moon_month[d])
        else:
          festivals[d]=sarva+'~'+get_ekadashi_name(paksha='krishna',month=moon_month[d])
      elif (tithi_sunrise[d-1]!=26 and tithi_sunrise[d]==27):
        festivals[d]=sarva+'~'+get_ekadashi_name(paksha='krishna',month=moon_month[d])

    #PRADOSHA Vratam
    if tithi_sunrise[d]==12 or tithi_sunrise[d]==13:
      ldiff_set=(swisseph.calc_ut(jd_sunset[d],swisseph.MOON)[0]-swisseph.calc_ut(jd_sunset[d],swisseph.SUN)[0])%360
      ldiff_set_tmrw=(swisseph.calc_ut(jd_sunset[d+1],swisseph.MOON)[0]-swisseph.calc_ut(jd_sunset[d+1],swisseph.SUN)[0])%360
      tithi_sunset = int(1+math.floor(ldiff_set/12.0))
      tithi_sunset_tmrw = int(1+math.floor(ldiff_set_tmrw/12.0))
      if tithi_sunset<=13 and tithi_sunset_tmrw!=13:
        festivals[d]=pradosham
      elif tithi_sunset_tmrw==13:
        festivals[d+1]=pradosham

    if tithi_sunrise[d]==27 or tithi_sunrise[d]==28:
      ldiff_set=(swisseph.calc_ut(jd_sunset[d],swisseph.MOON)[0]-swisseph.calc_ut(jd_sunset[d],swisseph.SUN)[0])%360
      ldiff_set_tmrw=(swisseph.calc_ut(jd_sunset[d+1],swisseph.MOON)[0]-swisseph.calc_ut(jd_sunset[d+1],swisseph.SUN)[0])%360
      tithi_sunset = int(1+math.floor(ldiff_set/12.0))
      tithi_sunset_tmrw = int(1+math.floor(ldiff_set_tmrw/12.0))
      if tithi_sunset<=28 and tithi_sunset_tmrw!=28:
        festivals[d]=pradosham
      elif tithi_sunset_tmrw==28:
        festivals[d+1]=pradosham

    #SANKATAHARA chaturthi
    if tithi_sunrise[d]==18 or tithi_sunrise[d]==19:
      ldiff_moonrise_yest=(swisseph.calc_ut(jd_moonrise[d-1],swisseph.MOON)[0]-swisseph.calc_ut(jd_moonrise[d-1],swisseph.SUN)[0])%360
      ldiff_moonrise=(swisseph.calc_ut(jd_moonrise[d],swisseph.MOON)[0]-swisseph.calc_ut(jd_moonrise[d],swisseph.SUN)[0])%360
      ldiff_moonrise_tmrw=(swisseph.calc_ut(jd_moonrise[d+1],swisseph.MOON)[0]-swisseph.calc_ut(jd_moonrise[d+1],swisseph.SUN)[0])%360
      tithi_moonrise_yest = int(1+math.floor(ldiff_moonrise_yest/12.0))
      tithi_moonrise = int(1+math.floor(ldiff_moonrise/12.0))
      tithi_moonrise_tmrw = int(1+math.floor(ldiff_moonrise_tmrw/12.0))

      if tithi_moonrise==19:
        if tithi_moonrise_yest!=19:#otherwise yesterday would have already been assigned
          festivals[d]=chaturthi 
          if moon_month[d]==5:#shravana krishna chaturthi
            festivals[d]=maha+festivals[d]
      elif tithi_moonrise_tmrw==19:
          festivals[d+1]=chaturthi 
          if moon_month[d]==5: #moon_month[d] and[d+1] are same, so checking [d] is enough
            festivals[d+1]=maha+festivals[d+1]

    #SHASHTHI Vratam
    if tithi_sunrise[d]==5 or tithi_sunrise[d]==6:
      if tithi_sunrise[d]==6 or (tithi_sunrise[d]==5 and tithi_sunrise[d+1]==7):
        if tithi_sunrise[d-1]!=6:#otherwise yesterday would have already been assigned
          festivals[d]=shashthi 
          if moon_month[d]==8:#kArtika krishna shashthi
            festivals[d]=skanda+festivals[d]
      elif tithi_sunrise[d+1]==6:
          festivals[d+1]=shashthi 
          if moon_month[d]==8: #moon_month[d] and[d+1] are same, so checking [d] is enough
            festivals[d+1]=skanda+festivals[d+1]


    ###--- OTHER (MAJOR) FESTIVALS ---###

    for x in iter(purvaviddha_rules.keys()):
      rule=purvaviddha_rules[x]
      if rule[0]=='moon_month':
        if moon_month[d]==rule[1]:
          if rule[2]=='tithi':
            fday = get_festival_day_purvaviddha(rule[3],tithi_sunrise,d,jd_sunrise[d],jd_sunrise[d+1],get_tithi,rule[4])
          elif rule[2]=='nakshatram':
            fday = get_festival_day_purvaviddha(rule[3],nakshatram_sunrise,d,jd_sunrise[d],jd_sunrise[d+1],get_nakshatram,rule[4])
          if fday is not None:
            if festival_day_list.has_key(x):
              if festival_day_list[x][0]!=fday:
                #Second occurrence of a festival within a Gregorian calendar year
                festival_day_list[x]=[festival_day_list[x][0],fday]
            else:
              festival_day_list[x]=[fday]
      elif rule[0]=='sun_month':
        if sun_month[d]==rule[1]:
          if rule[2]=='tithi':
            fday = get_festival_day_purvaviddha(rule[3],tithi_sunrise,d,jd_sunrise[d],jd_sunrise[d+1],get_tithi,rule[4])
          elif rule[2]=='nakshatram':
            fday = get_festival_day_purvaviddha(rule[3],nakshatram_sunrise,d,jd_sunrise[d],jd_sunrise[d+1],get_nakshatram,rule[4])
          if fday is not None:
            if festival_day_list.has_key(x):
              if festival_day_list[x][0]!=fday:
                #Second occurrence of a festival within a Gregorian calendar year
                festival_day_list[x]=[festival_day_list[x][0],fday]
            else:
              festival_day_list[x]=[fday]
      else:
        print 'Error; unknown string in rule: %s' % (rule[0])    
        return

    #NAVARATRI START
    if moon_month[d]==7 and moon_month[d-1]==6:
      festival_day_list[navaratri_start]=[d]

    #PONGAL/AYANAM
    if sun_month[d]==10 and sun_month[d-1]==9:
      festival_day_list[uttarayanam]=[d]

    if sun_month[d]==4 and sun_month[d-1]==3:
      festival_day_list[dakshinayanam]=[d]

    if sun_month[d]==1 and sun_month[d-1]==12:
      festival_day_list[new_yr]=[d]

    if moon_month[d]==1 and moon_month[d-1]!=1:
      festival_day_list[yugadi]=[d]

    #SHRIRAMANAVAMI
    if moon_month[d]==1:
      if tithi_sunrise[d]==8 or tithi_sunrise[d]==9:
        t_11 = get_tithi(jd_sunrise[d]+(jd_sunset[d]-jd_sunrise[d])*(2.0/5.0))#madhyahna1 start
        t_12 = get_tithi(jd_sunrise[d]+(jd_sunset[d]-jd_sunrise[d])*(3.0/5.0))#madhyahna1 end 
        t_21 = get_tithi(jd_sunrise[d+1]+(jd_sunset[d+1]-jd_sunrise[d+1])*(2.0/5.0))#madhyahna2 start
        t_22 = get_tithi(jd_sunrise[d+1]+(jd_sunset[d+1]-jd_sunrise[d+1])*(3.0/5.0))#madhyahna2 end
        if t_11==9 or t_12==9:
          if t_21==9 or t_22==9:
            festival_day_list[ramanavami]=[d+1]
          else:
            festival_day_list[ramanavami]=[d]

 
    #JANMASHTAMI
    if moon_month[d]==5:
      if tithi_sunrise[d]==22 or tithi_sunrise[d]==23:
        t_11 = get_tithi(jd_sunset[d]+(jd_sunrise[d+1]-jd_sunset[d])*(7.0/15.0))#nishita1 start
        t_12 = get_tithi(jd_sunset[d]+(jd_sunrise[d+1]-jd_sunset[d])*(8.0/15.0))#nishita1 end
        #t_11 = get_tithi(jd_sunset[d]+(jd_sunrise[d+1]-jd_sunset[d])*(2.0/5.0))#madhyaratri1 start
        #t_12 = get_tithi(jd_sunset[d]+(jd_sunrise[d+1]-jd_sunset[d])*(3.0/5.0))#madhyaratri1 end
        t_21 = get_tithi(jd_sunset[d+1]+(jd_sunrise[d+2]-jd_sunset[d+1])*(7.0/15.0))#nishita2 start
        t_22 = get_tithi(jd_sunset[d+1]+(jd_sunrise[d+2]-jd_sunset[d+1])*(8.0/15.0))#nishita2 end
        #t_21 = get_tithi(jd_sunset[d+1]+(jd_sunrise[d+2]-jd_sunset[d+1])*(2.0/5.0))#madhyaratri2 start
        #t_22 = get_tithi(jd_sunset[d+1]+(jd_sunrise[d+2]-jd_sunset[d+1])*(3.0/5.0))#madhyaratri2 end
        if t_11==23 or t_12==23:
          if t_21==23 or t_22==23:
            festival_day_list[janmashtami]=[d+1]
          else:
            festival_day_list[janmashtami]=[d]

    #SHIVARATRI
    if moon_month[d]==11:
      if tithi_sunrise[d]==28 or tithi_sunrise[d]==29:
        t_11 = get_tithi(jd_sunset[d]+(jd_sunrise[d+1]-jd_sunset[d])*(7.0/15.0))#nishita1 start
        t_12 = get_tithi(jd_sunset[d]+(jd_sunrise[d+1]-jd_sunset[d])*(8.0/15.0))#nishita1 end
        t_21 = get_tithi(jd_sunset[d+1]+(jd_sunrise[d+2]-jd_sunset[d+1])*(7.0/15.0))#nishita2 start
        t_22 = get_tithi(jd_sunset[d+1]+(jd_sunrise[d+2]-jd_sunset[d+1])*(8.0/15.0))#nishita2 end
        if t_11==29 or t_12==29:
          if t_21==29 or t_22==29:
            festival_day_list[shivaratri]=[d+1]
          else:
            festival_day_list[shivaratri]=[d]

    #VINAYAKA CHATURTHI
    if moon_month[d]==6:
      if tithi_sunrise[d]==3 or tithi_sunrise[d]==4:
        t_11 = get_tithi(jd_sunrise[d]+(jd_sunset[d]-jd_sunrise[d])*(2.0/5.0))#madhyahna1 start
        t_12 = get_tithi(jd_sunrise[d]+(jd_sunset[d]-jd_sunrise[d])*(3.0/5.0))#madhyahna1 end 
        t_21 = get_tithi(jd_sunrise[d+1]+(jd_sunset[d+1]-jd_sunrise[d+1])*(2.0/5.0))#madhyahna2 start
        t_22 = get_tithi(jd_sunrise[d+1]+(jd_sunset[d+1]-jd_sunrise[d+1])*(3.0/5.0))#madhyahna2 end
        if t_11==4 or t_12==4:
          if t_21==4 or t_22==4:
            festival_day_list[vchaturthi]=[d+1]
          else:
            festival_day_list[vchaturthi]=[d]

  #Add saved festivals
  festival_day_list[gayatri_japam]=[festival_day_list[yajur_upakarma][0]+1]
  festival_day_list[varalakshmi_vratam]=[festival_day_list[yajur_upakarma][0]-((weekday_start-1+festival_day_list[yajur_upakarma][0]-5)%7)]
  #KARADAYAN_NOMBU
  for x in iter(festival_day_list.keys()):
    for j in range(0,len(festival_day_list[x])):
      if festivals[festival_day_list[x][j]]!='':
        festivals[festival_day_list[x][j]]+='\\\\';
      festivals[festival_day_list[x][j]]+=x;

  ######----- FESTIVAL ADDITIONS COMPLETE -----#####

  ###--- PRINT LIST OF FESTIVALS (Page 2) ---###
  print '\\newpage'
  print '\\centerline {\\LARGE \\textsf{\\textbf{List of Festivals}}}\\mbox{}\\\\[2cm]'
  print '\\begin{center}'
  print '\\begin{minipage}[t]{0.3\\linewidth}'
  print '\\begin{center}'
  print '\\begin{tabular}{>{\\sffamily}r>{\\sffamily}r>{\\sffamily}cp{6cm}}'

  mlast=1
  for d in range(1,367):
    jd = jd_start-1+d
    [y,m,dt,t] = swisseph.revjul(jd)
    weekday = (weekday_start -1 + d)%7 
   
    if festivals[d]!='':
      if m!=mlast:
        mlast=m
        #print '\\hline\\\\'
        print '\\\\'
        if m==5 or m==9:
          print '\\end{tabular}'
          print '\\end{center}'
          print '\\end{minipage}\hspace{1cm}%'
          print '\\begin{minipage}[t]{0.3\\linewidth}'
          print '\\begin{center}'
          print '\\begin{tabular}{>{\\sffamily}r>{\\sffamily}l>{\\sffamily}cp{6cm}}'
          
      print '%s & %s & %s & {\\raggedright %s} \\\\' % (MON[m],dt,WDAY[weekday],festivals[d])

    if m==12 and dt==31:
      break

  print '\\end{tabular}'
  print '\\end{center}'
  print '\\end{minipage}'
  print '\\end{center}'
  print '\\clearpage'


  #Layout calendar in LATeX format
  #We use a separate loop here, because of festivals like varalakshmi
  #vratam, for which we backtrack to the previous friday from yajur
  #upakarma and change the list of festivals!

  for d in range(1,367):
    jd = jd_start-1+d
    [y,m,dt,t] = swisseph.revjul(jd)
    weekday = (weekday_start -1 + d)%7 

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
