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
    if file.endswith('/CSVExport.csv'):
    	print(file)
    	file_to_open=file
print(file_to_open)
csv_file = codecs.open(file_to_open,'r','utf-8')
#print(csv_file.read())
csv_reader = csv.reader(csv_file,'HoursTtracker-csv')

week = WeekTracker()
for line, row in enumerate(csv_reader):
    '''
        "Job","Clocked In","Clocked Out","Duration","Comment","Tags","Breaks","Adjustments","TotalTimeAdjustment","TotalEarningsAdjustment"
        "SIBS","21/02/17 12:51","21/02/17 17:12","4,35","Mastercard pin offline autorizacoes  Recibo Bits","ARCTIC - Construction - Suporte interno/externo sem SW","","","",""
    '''
    if line >2:
        print("line %d".format(line))
        job = row[0]
        clockedIn = row[1]
        clockedOut = row[2]
        duration = str(row[3])
        comments = row[4]     
        tags     = row[5]
        print ('job:{} clockedIn:{}, clockedOut:{} , duration:{} , comments:{} , tags:{}clockedIn '.format(job, clockedIn, clockedOut, duration, comments, tags))
        week.add(job, clockedIn, clockedOut, duration, comments, tags)
        
#print final objects
print("================================")
week.print_data()         
