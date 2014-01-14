#!/usr/bin/python
import sys
from panchangam import *

def  main():
   [city_name,latitude,longitude,tz]=sys.argv[1:5]
   year = int(sys.argv[5])
   
   if len(sys.argv)==7:
     script = sys.argv[6]
   else:
     script = 'iast' #Default script is IAST for writing calendar

   City = city(city_name,latitude,longitude,tz)

   Panchangam = panchangam(city=City,year=year,script=script)  

   Panchangam.computeAngams()
   Panchangam.assignLunarMonths()
   Panchangam.computeFestivals()
   Panchangam.computeSolarEclipses()
   Panchangam.computeLunarEclipses()

   Panchangam.computeIcsCalendar()
   Panchangam.writeIcsCalendar('%s-%d-%s.ics' % (city_name,year,script))

if  __name__=='__main__':
   main()
else:
   '''Imported as a module'''
   
