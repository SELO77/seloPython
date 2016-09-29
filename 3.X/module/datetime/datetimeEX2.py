import datetime


now = datetime.datetime.now()
print now # 2016-09-04 16:33:11.164451

now_date = now.date()
print now_date # 2016-09-04
print type(now_date) # <type 'datetime.date'>

now = now.replace(year=2000)
print now # 2000-09-04 16:35:03.646963

d = datetime.date(1987, 04, 13)
t = datetime.time(01, 01, 59)

dt = datetime.datetime.combine(d, t)
print dt

dt_tuple = dt.timetuple()
for i in dt_tuple:
  print i
  # 1987
  # 4
  # 13
  # 1
  # 1
  # 59
  # 0
  # 103
  # -1
