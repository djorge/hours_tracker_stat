#! python2
#HoursTrackerStat (Main)
#WeekTracker week
import csv
import appex
import codecs

csv.register_dialect('HoursTtracker-csv', delimiter=',', quoting=csv.QUOTE_ALL)
from WeekTracker import WeekTracker
file_to_open='CSVExport.csv'
if appex.is_running_extension():
  file_paths = appex.get_file_paths()
  for i, file in enumerate(file_paths):
    print('from appex:',file)
    if file.endswith('/CSVExport-SIBS.csv'):	
    	file_to_open=file
        
print(file_to_open)
#for ios
csv_file = codecs.open(file_to_open,'r','utf-8')
#for windows
#csv_file = open(file_to_open)
#print(csv_file.read())
csv_reader = csv.reader(csv_file,'HoursTtracker-csv')

week = WeekTracker()
for line, row in enumerate(csv_reader):
    '''
        "Job","Clocked In","Clocked Out","Duration","Comment","Tags","Breaks","Adjustments","TotalTimeAdjustment","TotalEarningsAdjustment"
        "SIBS","21/02/17 12:51","21/02/17 17:12","4,35","Mastercard pin offline autorizacoes  Recibo Bits","ARCTIC - Construction - Suporte interno/externo sem SW","","","",""
    '''
    if line >1:
        print("line {} ".format(line))
        job = row[0]
        clockedIn = row[1]
        clockedOut = row[2]
        duration = str(row[3])
        comments = row[4]     
        tags     = row[5]
        print ('job:{} clockedIn:{}, clockedOut:{} , duration:{} , comments:{} , tags:{}clockedIn '.format(job, clockedIn, clockedOut, duration, comments, tags))
        week.add(job, clockedIn, clockedOut, duration, comments, tags)
    else:
        print(row)
        
#print final objects
print("================================")
for day in (0,1,2,3,4):
    week.weekDays[day].closeForHours()
week.print_data()
#week.weekDays[4].addTime("0.75")    
#week.print_data()

#week.weekDays[0].addTime("0.75")
#week.print_data() 

#week.weekDays[0].addTime("-0.75")
#week.print_data() 

    
#week.weekDays[4].calcCheckoutHour("", 6, 0.25*60)
#45 minutes lunch
#target worktime = "9:15"

week.weekDays[4].calcForXHourMinute("09:30", 0, 45, 7, 15)
#week.weekDays[5].calcForXHourMinute("09:25", 0, 45, 8, 15)
week.print_data()
print("=======================================")
#weektest40 = WeekTracker()
#weektest40.calcFor40Hours("09:15", "09:20", "09:50", "09:20", "09:55", 0, 45)
#weektest40.print_data()
