import time
import math
timer = None

def tStart():
    global timer
    timer = time.time()
    return True

def tStop():
    global timer
    return time.time() - timer

def sec2date(sec, string = True):
    year = 31556952 #one year is NOT 365 days NOR 365.25 days, according to the gregorian calendar, one year is 365.2425 days
    month = year / 12 #can't be bothered to deal with the hell of detecting what month it is
    week = 604800
    day = 86400
    hour = 3600
    minute = 60
    second = 1
    nanosecond = 0.000000001
    
    date = ["years", "months", "weeks", "days", "hours", "minutes", "seconds", "nanoseconds"]
    
    date[0] = math.floor(sec / year)
    date[1] = math.floor((sec - year * date[0]) / month)
    date[2] = math.floor(((sec - year * date[0]) - month * date[1]) / week)
    date[3] = math.floor((((sec - year * date[0]) - month * date[1]) - week * date[2]) / day)
    date[4] = math.floor(((((sec - year * date[0]) - month * date[1]) - week * date[2]) - day * date[3]) / hour)
    date[5] = math.floor((((((sec - year * date[0]) - month * date[1]) - week * date[2]) - day * date[3]) - hour * date[4]) / minute)
    date[6] = math.floor(((((((sec - year * date[0]) - month * date[1]) - week * date[2]) - day * date[3]) - hour * date[4]) - minute * date[5]) / second)
    date[7] = math.floor((((((((sec - year * date[0]) - month * date[1]) - week * date[2]) - day * date[3]) - hour * date[4]) - minute * date[5]) - second * date[6]) / nanosecond)

    if string == True:
        return f"years: {date[0]}\nmonths: {date[1]}\nweeks: {date[2]}\ndays: {date[3]}\nhours: {date[4]}\nminutes: {date[5]}\nseconds: {date[6]}\nnanoseconds: {date[7]}"
    elif string == False:
        return date
    
def date2sec(date):
    year = 31556952
    month = year / 12
    week = 604800
    day = 86400
    hour = 3600
    minute = 60
    second = 1
    nanosecond = 0.000000001
    
    sec = date[0] * year
    sec += date[1] * month
    sec += date[2] * week
    sec += date[3] * day
    sec += date[4] * hour
    sec += date[5] * minute
    sec += date[6] * second
    sec += date[7] * nanosecond

    return sec
