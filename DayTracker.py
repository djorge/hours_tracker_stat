import datetime
from datetime import timedelta

class myutil:
    @staticmethod
    def print_map(d):
        print("{:<8} {:<10}".format('Tag','Tuple Hours'))
        for k, v in d.iteritems():            
            print("{:<8}  {:<10}".format(k, v))
    @staticmethod     
    def DateTimeToFloatRounded(DateTimeIn):
        '''
        Converts a DateTime (04:45) to a float (4.75)
        '''
        print("[DateTimeToFloatRounded] DateTimeIn:{} ".format(DateTimeIn))        
        
        dur_frac =  DateTimeIn.minute/60.0
        dur_int = DateTimeIn.hour
        
        if dur_frac < .25:
            dur_frac = 0
        elif dur_frac < .50:
            dur_frac = .25
        elif dur_frac < .75:
            dur_frac = .50
        elif dur_frac <= .99:
            dur_frac = .0
            
        print("[DateTimeToFloatRounded] dur_int:{} , dur_frac:{}  ".format(dur_int, dur_frac))
        return dur_int + dur_frac
        
            
class DayTracker:       
    def __init__(self):
        self.dayTotalTime = 0
        self.dayTotalTimeRounded = 0
        self.workDay = -1
        self.currentDuration = 0
        
        #{work, holiday, vacation, compensated}    
        self.listItems = []
        self.tags_duration = {}
        
        #tags_time[tag] = [(begin_time, end_time)]
        self.tags_time = {}
        self.comments = {}
        self.remainingHours = 8.00
        self.lastClockOut = 0
        
        self.clokOutChanged = False
        self.calcCheckOut = 0
        self.deltaAdded = 0
        self.newDatetimeIn = 0
        
        #used for calcForXHourMinute
        self.calcXWorkTimeTarget = 0
        self.calcXLunchDuration = 0
        self.calcXCheckin = 0
        self.calcXCheckOut = 0
        
    def roundDuration(self, duration):
        print("........................")
        print(duration)
        ind_d = duration#float(duration.replace(',','.'))
        dur_frac =  round(ind_d%1,2)
        dur_int = int(ind_d)
        
        if dur_frac < .25:
            dur_frac = 0
        elif dur_frac < .50:
            dur_frac = .25
        elif dur_frac < .75:
            dur_frac = .50
        elif dur_frac <= .99:
            dur_frac = .0
            
        print("dur_int:{} , dur_frac:{}  ".format(dur_int, dur_frac))
        return dur_int + dur_frac
        
    def add(self, clockedIn, clockedOut, weekday, duration, tags, comments):
        print("[D] add for weekday {}, duration: {} ".format(weekday, duration))
        #self.currentDuration = self.roundDuration(duration)
        self.dayTotalTime += float(duration.replace(',','.'))
        print ("accumulate duration {} remaining {}".format(self.dayTotalTime,self.remainingHours))
        itemList = (weekday, self.currentDuration, tags, comments)
        print("tags: {} ".format(tags))        
        if len(tags) >0:
            if tags in self.tags_duration.keys():
                self.tags_duration[tags] += int(self.currentDuration)
            else:
                self.tags_duration[tags] = int(self.currentDuration)
        if comments is not None:
            self.comments[tags] = comments
            
        self.listItems.append(itemList)
        print(self.listItems)
        self.workDay = weekday
        datetimeIn = datetime.datetime.strptime(clockedIn, '%d/%m/%y %H:%M')
        datetimeOut = datetime.datetime.strptime(clockedOut, '%d/%m/%y %H:%M')
        if tags not in self.tags_time.keys():            
            self.tags_time[tags] = []            
        self.tags_time[tags].append((datetimeIn.hour,datetimeIn.minute,datetimeOut.hour,datetimeOut.minute))
        self.lastDateTimeOut = datetimeOut
        #myutil.print_map(self.tags_time)
        
    def countItems(self):
        return len(listItems)

    def closeForHours(self):
        self.dayTotalTimeRounded = self.roundDuration(self.dayTotalTime)
        self.remainingHours = 8 - self.dayTotalTimeRounded
        
    def addTime(self, timeDuration):
        self.dayTotalTime += float(timeDuration);
        self.closeForHours()
        
    def subtractTime(self, timeDuration):        
        self.dayTotalTime -= float(timeDuration);
        self.closeForHours()
        
    def calcCheckoutHour(self, checkIn, hoursTarget, minuteTarget):  
        '''
        Calc checkout time wih given checkin and offset
        '''
        # checkOut = delta = checkIn + (hoursTarget, minuteTarget) 
        #clockedOut time
        #print("old checkout {} offset hours {}, minutes {}".format(self.lastDateTimeOut, hoursTarget, minuteTarget))
        self.deltaAdded = timedelta(hours = hoursTarget, minutes = minuteTarget )        
        if checkIn != "":
            self.newDatetimeIn = datetime.datetime.strptime(checkIn, '%H:%M')
            self.calcCheckOut = self.newDatetimeIn + self.deltaAdded
        else:
            self.newDatetimeIn = 0
            self.calcCheckOut = self.lastDateTimeOut + self.deltaAdded
        #self.dayTotalTimeRounded e nao self.dayTotalTime porque ja vem arredondado
        self.dayTotalTimeRounded += hoursTarget +(minuteTarget/60)
        self.remainingHours = 8 - self.dayTotalTimeRounded        
        self.clokOutChanged = True        
        
    def calcForXHourMinute(self, checkinArriveDate, lunchDurationHour,lunchDurationMinutes, hoursTarget, minuteTarget):
        '''
            Calc checkout time with given checkin Arrive Date and lunch duration for X hour and minute target work time
            "Which is my clockOut time if i arrive a '09:30' and lunch time is 45 minutes and i have to do '8:45' of work time?"
        '''
        print("->calcForXHourMinute({},{},{},{},{})".format(checkinArriveDate, lunchDurationHour,lunchDurationMinutes, hoursTarget, minuteTarget ))
        #dayTotalTime must be 0 which means day is totally empty        
        self.calcXWorkTimeTarget = timedelta(hours = hoursTarget, minutes = minuteTarget )
        self.calcXLunchDuration = timedelta(hours = lunchDurationHour, minutes = lunchDurationMinutes )
        self.calcXCheckin = datetime.datetime.strptime(checkinArriveDate, '%H:%M')
        self.calcXCheckOut =  self.calcXCheckin + self.calcXLunchDuration + self.calcXWorkTimeTarget 
        self.calcXCheckOutFloat =  myutil.DateTimeToFloatRounded(self.calcXCheckOut)
        #update dayTotalTime (float datatype)        
        #print("->{}".format(self.dayTotalTimeRounded))
        self.dayTotalTimeRounded += hoursTarget +(minuteTarget/60)
        #print("->{}".format(self.dayTotalTimeRounded))
        self.remainingHours = 8 - self.dayTotalTimeRounded   
        
        
    def __str__(self):
        return "Total time worked: {0}".format(self.dayTotalTime)
        
        
