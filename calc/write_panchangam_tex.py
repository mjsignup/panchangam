#!/usr/bin/python
import sys
import math
import swisseph
from datetime import *

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
tithi_names={
1:'spra',
2:'sdvi',
3:'stri',
4:'scha',
5:'spanc',
6:'ssha',
7:'ssap',
8:'sasht',
9:'snav',
10:'sdas',
11:'seka',
12:'sdva',
13:'stra',
14:'schaturdashi',
15:'purnima',
16:'kpra',
17:'kdvi',
18:'ktri',
19:'kcha',
20:'kpanc',
21:'ksha',
22:'ksap',
23:'kasht',
24:'knav',
25:'kdas',
26:'keka',
27:'kdva',
28:'ktra',
29:'kchaturdashi',
30:'ama'
}

nakshatra_names={1:'ashwini',
2:'apabharani',
3:'krittika',
4:'rohini',
5:'mrigashirsha',
6:'ardra',
7:'punarvasu',
8:'pushya',
9:'ashresha',
10:'magha',
11:'purvaphalguni',
12:'uttaraphalguni',
13:'hasta',
14:'chitra',
15:'svati',
16:'vishakha',
17:'anuradha',
18:'jyeshtha',
19:'mula',
20:'purvashadha',
21:'uttarashadha',
22:'shravana',
23:'shravishtha',
24:'shatabhishak',
25:'proshthapada',
26:'uttaraproshthapada',
27:'revati'}


#MAIN CODE

#place = {'name':'Chennai','latitude':sexa2deci(13,4),'longitude':sexa2deci(80,17)}
place = {'name':sys.argv[1], 'latitude':sexastr2deci(sys.argv[2]), 'longitude':sexastr2deci(sys.argv[3]), 'tz':float(sys.argv[4]), 'dst':float(sys.argv[5])}

start_year = 2010
year = 2010
jd=swisseph.julday(year,1,1,0)
jd_start=jd
start_date = datetime(year=year,month=1,day=1,hour=0,minute=0,second=0)

day_of_year=0
tz_off = place['tz'] # Need to consider daylight saving etc too
dst_bit = place['dst']

swisseph.set_sid_mode(swisseph.SIDM_LAHIRI) #Force Lahiri Ayanamsha

while 1:
  if year>start_year:
    break

  day_of_year = day_of_year + 1  


  [y,m,d,t] = swisseph.revjul(jd)
  weekday = (swisseph.day_of_week(jd) + 1)%7 #swisseph has Mon = 0, non-intuitively!


  #ADJUST FOR EUROPEAN DST, others will be more complex!

  if dst_bit!=0:
    if m==3 and d>24 and weekday==0:
      tz_off=tz_off+1

    if m==10 and d>24 and weekday==0:
      tz_off=tz_off-1

  jd_rise=swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=place['longitude'],lat=place['latitude'],rsmi=swisseph.CALC_RISE|swisseph.BIT_DISC_CENTER)[1][0]
  jd_set =swisseph.rise_trans(jd_start=jd,body=swisseph.SUN,lon=place['longitude'],lat=place['latitude'],rsmi=swisseph.CALC_SET|swisseph.BIT_DISC_CENTER)[1][0]

  [_y,_m,_d, t_rise]=swisseph.revjul(jd_rise+tz_off/24.0)
  [_y,_m,_d, t_set]=swisseph.revjul(jd_set+tz_off/24.0)

  lmoon=swisseph.calc_ut(jd_rise,swisseph.MOON)[0]-swisseph.get_ayanamsa(jd_rise)
  lmoon_tmrw=swisseph.calc_ut(jd_rise+1,swisseph.MOON)[0]-swisseph.get_ayanamsa(jd_rise+1)

  lsun=swisseph.calc_ut(jd_rise,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_rise)
  lsun_tmrw=swisseph.calc_ut(jd_rise+1,swisseph.SUN)[0]-swisseph.get_ayanamsa(jd_rise+1)

  dmc = lmoon_tmrw-lmoon
  dmr = lsun_tmrw-lsun


  tithi = tithi_names[int(1+math.floor((lmoon-lsun)%360 / 12.0))]
  tithi_remaining = 12-(((lmoon-lsun)%360)%12)
  t_end = tithi_remaining/(dmc-dmr)*24.0
  te=deci2sexa(t_rise+t_end)
  if te[0]>=24:
    suff = '(+1)'
    te[0] = te[0]-24
  else:
    suff = '\\hspace{2ex}'

  tithi_end = '%02d:%02d%s' % (te[0],te[1],suff)

  nakshatram = nakshatra_names[int(1+math.floor((lmoon%360) /(360.0/27)))]
  nakshatram_remaining = (360.0/27) - ((lmoon%360) % (360.0/27))
  n_end = nakshatram_remaining/dmc*24
  ne=deci2sexa(t_rise+n_end)
  if ne[0]>=24:
    ne[0] = ne[0]-24
    suff = '(+1)'
  else:
    suff='\\hspace{2ex}'

  nakshatram_end = '%02d:%02d%s' % (ne[0],ne[1],suff)

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
    print '\multicolumn{7}{c}{\Large \\bfseries %s %s}\\\\' % (month[m],y)
    print '\hline'
    print '\\textbf{SUN} & \\textbf{MON} & \\textbf{TUE} & \\textbf{WED} & \\textbf{THU} & \\textbf{FRI} & \\textbf{SAT} \\\\ \hline'

    #Blanks for previous weekdays
    for i in range(0,weekday):
      print "{}  &"
  
  print '\caldata{%s}{%s}{%s}{%s}{%s}{%s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s}{\\textsf{\\%s} {\\tiny \\RIGHTarrow} %s} ' % (d,rise,madhya,rahu,yama,set,tithi,tithi_end,nakshatram,nakshatram_end)

  if weekday==6:
    print "\\\\ \hline"
  else:
    print "&"

  jd = jd + 1
  year = swisseph.revjul(jd)[0]

print "\\\\ \hline"
print '\end{tabular}'
print '\n\n%\clearpage'
