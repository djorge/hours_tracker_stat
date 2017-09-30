import datetime
import calendar
from DayTracker import DayTracker
from WeekTracker import WeekTracker
from math import ceil

'''a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day
'''

def get_month_range(start_date = None):
    if start_date is None:
        start_date = date.today()
    start_date.replace(day = 1)        
    days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return  (start_date,end_date )

class MonthTracker:
    
    def __init__(self, clockedIn):
        #clockedIn format: "21/02/17 12:51"
        
        self.weekJob = None
        #semana 1 a semana 4/5                
        self.dt = datetime.datetime.strptime(clockedIn, '%d/%m/%y %H:%M')
        self.monthNumber = self.dt.month
        
        #get number of weeks for given month 4/5        
        endWeek = self.week_of_month(self.dt.replace(day=calendar.monthrange(self.dt.year,self.dt.month)[1]))
        if endWeek == 4:
            self.weekNumber = {0 : WeekTracker(),
                1 : WeekTracker(),
                2 : WeekTracker(),
                3 : WeekTracker(),
                }
        elif endWeek == 5:
            self.weekNumber = {0 : WeekTracker(),
                1 : WeekTracker(),
                2 : WeekTracker(),
                3 : WeekTracker(),
                4 : WeekTracker()
                }
        elif endWeek == 6:
            self.weekNumber = {0 : WeekTracker(),
                1 : WeekTracker(),
                2 : WeekTracker(),
                3 : WeekTracker(),
                4 : WeekTracker(),
                5 : WeekTracker()                
                }
        print("num weeek:",len(self.weekNumber))
        
    def numWeeks(self):
      return len(self.weekNumber)
        
    def week_of_month(self, dt):
        """ Returns the week of the month for the specified date.
        """
        first_day = dt.replace(day=1)
        dom = dt.day
        adjusted_dom = dom + first_day.weekday()
        return int(ceil(adjusted_dom/7.0))
    
    def add(self, job, clockedIn, clockedOut, duration, comments, tags):
        ''' 
        "Job","Clocked In","Clocked Out","Duration","Comment","Tags","Breaks","Adjustments","TotalTimeAdjustment","TotalEarningsAdjustment"
        "SIBS","21/02/17 12:51","21/02/17 17:12","4,35","Mastercard pin offline autorizacoes  Recibo Bits","ARCTIC - Construction - Suporte interno/externo sem SW","","","",""
        '''
        datetimeIn = datetime.datetime.strptime(clockedIn, '%d/%m/%y %H:%M')
        print("Adding {} to week number {}".format(datetimeIn, self.week_of_month(datetimeIn)))
        self.weekNumber[self.week_of_month(datetimeIn)-1].add(job, clockedIn, clockedOut, duration, comments, tags)
        pass
        
    def getHoursOfDay(self, dt):
        if dt.weekday() in[5,6]:
            return 0
        
        week = self.week_of_month(dt)
        #print ('dt:{} dt.weekday:{}'.format(dt, dt.weekday()))
        return self.weekNumber[week-1].weekDays[dt.weekday()].dayTotalTimeRounded
    
    def getDayTracker(self, dt):
        if dt.weekday() in[5,6]:
            return None
        
        week = self.week_of_month(dt)
        #print ('dt:{} dt.weekday:{}'.format(dt, dt.weekday()))
        return self.weekNumber[week-1].weekDays[dt.weekday()]
    
    def calcHours(self):
        for idx, week in enumerate(self.weekNumber):
            for day in (0,1,2,3,4):
                self.weekNumber[idx].weekDays[day].closeForHours()