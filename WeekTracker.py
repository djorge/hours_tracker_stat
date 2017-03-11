import datetime
from DayTracker import DayTracker
class WeekTracker:
    def __init__(self):
        self.weekJob = None    
        #semana 1 a semana 4    
        self.weekNumber = 0       
    
        self.weekDays = {0 : DayTracker(),
                1 : DayTracker(),
                2 : DayTracker(),
                3 : DayTracker(),
                4 : DayTracker(),    
                5 : DayTracker(),                    
                6 : DayTracker(),    
                }
        self.weekTotalTime = 0
        
    #datetime.datetime.strptime('12/03/17 12:51', '%d/%m/%y %H:%M').weekday()
    def add(self, job, clockedIn, clockedOut, duration, comments, tags):
        if self.weekJob is None:
            self.weekJob = job
        if self.weekJob != None and self.weekJob != job:
            return -1
        datetimeIn = datetime.datetime.strptime(clockedIn, '%d/%m/%y %H:%M')
        dayOfTheWeek = datetimeIn.weekday() #0-segunda, 1-terca, 2-quarta, 3-quinta, 4-sexta
        self.weekNumber = datetimeIn.isocalendar()[1]
        
        datetimeOut = datetime.datetime.strptime(clockedOut, '%d/%m/%y %H:%M')
        if dayOfTheWeek >= 0 and dayOfTheWeek < 7:
            self.weekDays[dayOfTheWeek].add(clockedIn, clockedOut, dayOfTheWeek, duration, tags, comments)
            self.weekTotalTime += self.weekDays[dayOfTheWeek].currentDuration
     
    def print_data(self):   
        #for idx, day in enumerate(self.weekDays):
         #   print "%d, %f" %(idx, day.dayTimeDuration)
        print (self.weekTotalTime)
        for idx, day in self.weekDays.iteritems():
            print("idx: {} total time:{}".format(idx,day.dayTimeDuration))
