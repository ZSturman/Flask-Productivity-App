import os
from os import listdir
from datetime import *
from dateutil.tz import tzlocal, tzutc, tz
from calendar import *
from flask import request, url_for
from flask_login import current_user
from random import randint
from colour import Color
import random
from math import floor

def dt_module_stuff():
    microsecond = timedelta(microseconds=1)
    millisecond = timedelta(milliseconds=1)
    second = timedelta(seconds=1)
    minute = timedelta(minutes=1)
    hour = timedelta(hours=1)
    day = timedelta(days=1)
    week = timedelta(weeks=1)

    #print("microsecond", microsecond)
    #print("millisecond", millisecond)
    #print("second", second)
    #print("minute", minute)
    #print("hour", hour)
    #print("day", day)
    #print("week", week)
    
    return week, day, hour, minute, second, millisecond, microsecond

def get_hh_mm_ss(td_str):
    # split string into individual component
    x = td_str.split(':')
    hours = x[0]
    minutes = x[1]
    seconds = x[2]
    return hours, minutes, seconds

def dt_module_conversion(secs):  
    td = timedelta(seconds=secs)
    td_str = str(timedelta(seconds=secs))

    hh, mm, ss = get_hh_mm_ss(td_str)
    string_format = f"{hh}hrs, {mm}min, {ss}sec"

    return string_format


def redirect_url(default='main.home'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

def convert_time(secs):
    if secs == None:
        pass
    else:
        secs = int(secs)
        mins = 0
        hrs = 0
        if secs == 0 or secs == None or secs == "":
            pass
        elif secs <=59:
            return int(secs), int(mins), int(hrs)
        elif secs >=60:
            mins = floor(secs/60)
            if mins >= 60:
                hrs = floor(mins/60)
                mins = floor(mins - (hrs*60))
                secs = floor(secs - ((mins*60)+((hrs*60)*60)))
                return int(secs), int(mins), int(hrs)
            else:
                secs = floor(secs - (mins*60))
                return int(secs), int(mins), int(hrs)

def add_padding(hours, minutes, seconds):
    if hours and minutes and seconds == None:
        pass
    else:
        hours = f'{int(hours):02}'
        minutes = f'{int(minutes):02}'
        seconds = f'{int(seconds):02}'
        return hours, minutes, seconds
        
def today():
    today = datetime.utcnow().date()
    return today
    
def getRandomColor():
    r = lambda: random.randint(0,255)
    randColor = '#%02X%02X%02X' % (r(),r(),r())
    randColorHex = Color(randColor)
    randColorHex.saturation = .4
    randColorHex.luminance = .8
    return randColorHex

def get_icons():
    folder_dir="mapps/static/Icon_Library/sets/all"
    icons = []
    for images in os.listdir(folder_dir):
        if (images.endswith(".svg")):
            icons.append(images)
    return icons

def get_icon_list():
    os.chdir("./mapps")
    #os.chdir("/Users/zacharysturman/Library/Mobile Documents/com~apple~CloudDocs/miniapps/mapps")
    with open("icon_list.txt", "r") as f:
        icon_list = f.readlines()
        icon_list = [line.rstrip() for line in icon_list]
        os.chdir("..")
        return icon_list
    


def check_status(today, due_date, total_seconds=None):
    due_date = convert_for_model(due_date)
    due_date = convert_to_utc(due_date)
    due_date = due_date.astimezone(tz.tzlocal())
    today = today.astimezone(tz.tzlocal())
    upcoming = 0
    late = 0
    status = None
    x = round((due_date - today).total_seconds())
    if due_date == 0:
        late = 0
        upcoming = 0
        status = "none"
    else:
        if x < 0:
            late = 1
            upcoming = 0
            status = "danger"
        elif 0 < x <= 350000:
            late = 0
            upcoming = 1
            status = "danger"
        elif 350000 < x <= 900000:
            upcoming = 2
            late = 0
            status = "warning"
        elif x >= 900001:
            upcoming = 3
            late = 0
            status = "success"
    if total_seconds != None:
        string = dt_module_conversion(x)
        return x, string
    return late, upcoming, status

def convert_to_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = input_date.replace(tzinfo=from_zone)
    local_dt = utc.astimezone(to_zone)
    return local_dt

def convert_to_utc(input_date):
    to_zone = tz.tzutc()
    from_zone = tz.tzlocal()
    utc = input_date.replace(tzinfo=from_zone)
    local_dt = utc.astimezone(to_zone)
    return local_dt

def convert_for_model(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
            """ print(type(input_date_int)) """
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S')
            """ print(type(input_date_int)) """
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
            """ print(type(input_date_int)) """
        except ValueError as e:
            #print("3333",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
            """ print(type(input_date_int)) """
        except ValueError as e:
            #print("444",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        date_utc = input_date_dt.replace(tzinfo=from_zone)
        return date_utc











def readable_datetime(dt, format):
    #use the convert to local fucntion then parse it out into other stuff
    pass

def yyyy_mm_dd_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("111",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("222",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("333",e) """
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        converted_date_time = local_dt.strftime('%Y %m %d')
        return converted_date_time

def yyyy_mm_dd(input_date):
    input_date_int = input_date
    if input_date == "" or input_date == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("111",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("222",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("333",e) """
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day)
        return input_date_dt

def yyyy_mm_dd_hh_mm_ss_zz_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("111",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("222",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("333",e) """
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        converted_date_time = local_dt.strftime('%x %X')
        return converted_date_time

def yyyy_mm_dd_hh_mm_ss_zz(input_date):
    input_date_int = input_date
    if input_date == "" or input_date == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("111",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("222",e) """
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
            """ print(type(input_date_int)) """
        except ValueError as e:
            """ print("333",e) """
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        converted_date_time = input_date_dt.strftime('%x %X')
        return converted_date_time

def wkd_mon_dd_hh_mm_ss_yyyy_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        short_w_nums = local_dt.strftime('%c')
        return short_w_nums

def weekday_month_dd_yyyy(input_date):
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        """ today_utc_tz = datetime.now(tzutc()).tzname()
        today_utc = datetime.now(tzutc())
        today_local_tz = datetime.now(tzlocal()).tzname()
        today_local = datetime.now(tzlocal()) """
        """ date_weekday_mname_dd_yyy_hh_mm_ss_f = input_date_dt.strftime('%A %B %d, %Y') """
        #return input_date_dt
        date_weekday_mname_dd_yyy_hh_mm_ss_f = input_date_dt.strftime('%A %B %d, %Y')
        return date_weekday_mname_dd_yyy_hh_mm_ss_f

def weekday_month_dd_yyy_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        """ today_utc_tz = datetime.now(tzutc()).tzname()
        today_utc = datetime.now(tzutc())
        today_local_tz = datetime.now(tzlocal()).tzname()
        today_local = datetime.now(tzlocal()) """
        """ date_weekday_mname_dd_yyy_hh_mm_ss_f = input_date_dt.strftime('%A %B %d, %Y') """
        #return input_date_dt
        date_weekday_mname_dd_yyy_hh_mm_ss_f = local_dt.strftime('%A %B %d, %Y')
        return date_weekday_mname_dd_yyy_hh_mm_ss_f

def hh_mm_ss_am_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        """ today_utc_tz = datetime.now(tzutc()).tzname()
        today_utc = datetime.now(tzutc())
        today_local_tz = datetime.now(tzlocal()).tzname()
        today_local = datetime.now(tzlocal())
        date_weekday_mname_dd_yyy_hh_mm_ss_f = input_date_dt.strftime('%A %B %d, %Y %H:%M:%S:%f %z') """
        """ time = input_date_dt.strftime('%-I:%M:%S %p') """
        """ m = input_date_dt.strftime('%M')
        s = input_date_dt.strftime('%S')
        ampm = input_date_dt.strftime('%p') """
        time = local_dt.strftime('%-I:%M:%S %p')
        return time

def wkd_mon_dd_hh_mm_ss_yyy_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        print("Input Date = ' ' ")
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        converted_date_time = local_dt.strftime('%c')
        return converted_date_time

def wkd_mon_dd_yyy_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        converted_date_time = local_dt.strftime('%a %b %d, %Y')
        return converted_date_time

def weekday_month_dd_yyy_local(input_date):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        utc = input_date_dt.replace(tzinfo=from_zone)
        local_dt = utc.astimezone(to_zone)
        converted_date_time = local_dt.strftime('%A %B %d, %Y')
        return converted_date_time

def hh_mm_ss_am(input_date):
    input_date_int = input_date
    if input_date == "" or input_date_int == None:
        """ print("Input Date = ' ' ") """
    else:
        input_date_str = str(input_date)
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f%z')
        except ValueError as e:
            #print("111",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            #print("222",e)
            pass
        try:
            input_date_int = datetime.strptime(input_date_str, '%Y-%m-%d')
        except ValueError as e:
            #print("333",e)
            pass
        input_date_year = int(datetime.strftime(input_date_int, '%Y'))
        input_date_month = int(datetime.strftime(input_date_int, '%m'))
        input_date_day = int(datetime.strftime(input_date_int, '%d'))
        input_date_hour = int(datetime.strftime(input_date_int, '%H'))
        input_date_minute = int(datetime.strftime(input_date_int, '%M'))
        input_date_second = int(datetime.strftime(input_date_int, '%S'))
        input_date_microsecond = int(datetime.strftime(input_date_int, '%f'))
        input_date_int = (input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        input_date_dt = datetime(input_date_year,input_date_month,input_date_day,input_date_hour,input_date_minute,input_date_second,input_date_microsecond)
        time = input_date_dt.strftime('%-I:%M:%S %p')
        
        return time