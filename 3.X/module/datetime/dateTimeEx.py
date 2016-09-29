import datetime

print type(datetime) # module

from datetime import datetime

mybirthday_datetime = datetime(year=1987, month=04, day=13)
print mybirthday_datetime # 2016-10-23 00:00:00


mybirthday_str = datetime.strftime(mybirthday_datetime, "%Y/%m/%d %H:%M:%S")
print mybirthday_str # 1987/04/13 00:00:00
print type(mybirthday_str) # <type 'str'>


now_str = "2016-09-02 21:31:30"
now_datetime = datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")
print type(now_datetime) # <type 'datetime.datetime'>


print datetime.strftime(now_datetime, "%y %B %A %p %I/ week number of the year: %W")
# 16 September Friday PM 09/ week number of the year: 35


from datetime import datetime, timedelta


today_datetime = datetime.today()
print today_datetime # 2016-09-02 22:38:09.543477
one_weeks = timedelta(weeks=1)
# days=None, seconds=None, microseconds=None, milliseconds=None, minutes=None, hours=None, weeks=None
one_weeks_ago = today_datetime - one_weeks
print one_weeks_ago # 2016-08-26 22:38:09.543477