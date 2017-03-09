#HoursTrackerStat (Main)
#WeekTracker week
import csv
csv.register_dialect('HoursTtracker-csv', delimiter=',', quoting=csv.QUOTE_ALL)
from WeekTracker import WeekTracker

csv_file = open('CSVExport.csv')
csv_reader = csv.reader(csv_file,'HoursTtracker-csv')

week = WeekTracker()
for  row in csv_reader:
    '''
        "Job","Clocked In","Clocked Out","Duration","Comment","Tags","Breaks","Adjustments","TotalTimeAdjustment","TotalEarningsAdjustment"
        "SIBS","21/02/17 12:51","21/02/17 17:12","4,35","Mastercard pin offline autorizacoes  Recibo Bits","ARCTIC - Construction - Suporte interno/externo sem SW","","","",""
    '''
    if csv_reader.line_num >2:
        print "line %d"%(csv_reader.line_num)
        job = row[0]
        clockedIn = row[1]
        clockedOut = row[2]
        duration = str(row[3])
        comments = row[4]     
        tags     = row[5]
        print "job:%s, clockedIn:%s, clockedOut:%s, duration:%s, comments:%s, tags: %r"%(job, clockedIn, clockedOut, duration, comments, tags)
        week.add(job, clockedIn, clockedOut, duration, comments, tags)
        
#print final objects
print "================================"
week.print_data()        