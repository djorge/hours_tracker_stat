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
        self.lastDayProcessed = -1
        
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
            
        '''if self.lastDayProcessed == -1:
            self.lastDayProcessed = dayOfTheWeek
        if self.lastDayProcessed != -1 and self.lastDayProcessed != dayOfTheWeek:
            self.weekDays[self.lastDayProcessed].closeForHours()
            self.lastDayProcessed = dayOfTheWeek
        '''
            
    def weekTotals(self):
        weekDuration = 40
        weekTotalDuration = 0
        weekTotalRemaining = 0
        for idx, day in self.weekDays.iteritems():
            if idx not in (5, 6):
                 weekTotalDuration += day.dayTotalTimeRounded
                 weekTotalRemaining += day.remainingHours                 
        print("Week Totals\n TotalDuration: {} TotalRemaining:{} ".format(weekTotalDuration, weekTotalRemaining))        
        
    def print_data(self):   
        #for idx, day in enumerate(self.weekDays):
         #   print "%d, %f" %(idx, day.dayTotalTime)
        print (self.weekTotalTime)
        for idx, day in self.weekDays.iteritems():
            if idx not in (5, 6):
                print("idx: {} total time:{} remaining {} ".format(idx,day.dayTotalTime, day.remainingHours))
                if self.weekDays[idx].clokOutChanged == True:                    
                    print("with offset {} new clockOut {}".format(self.weekDays[idx].deltaAdded,self.weekDays[idx].lastDateTimeOut + self.weekDays[idx].deltaAdded))
                    print("with offset {} new clockOut {}".format(self.weekDays[idx].deltaAdded,self.weekDays[idx].calcCheckOut))
                    
        self.weekTotals()

    def calcFor40Hours(self):
        #if day < 8 hors, calc day to get 8 hour
        pass
        
