import sys
from panchangam import *
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

def  main():
   city_name = sys.argv[1]
   latitude = sexastr2deci(sys.argv[2])
   longitude = sexastr2deci(sys.argv[3])
   tz = sys.argv[4]
   year = int(sys.argv[5])
   
   if len(sys.argv)==7:
     script = sys.argv[6]
   else:
     script = 'deva' #Default script is devanagari

   City = city(city_name,latitude,longitude,tz)

   Panchangam = panchangam(city=City,year=year)  

   Panchangam.computeAngams()
   Panchangam.assignLunarMonths()
   Panchangam.computeFestivals()
   Panchangam.computeSolarEclipses()
   Panchangam.computeLunarEclipses()
   #Panchangam.computeIcsCalendar()
   #Panchangam.writeIcsCalendar()
   template_file=open('cal_template_compre.tex')
   Panchangam.writeTeX(template_file)
   Panchangam.writeDebugLog()

if  __name__=='__main__':
   main()
else:
   '''Imported as a module'''
   
