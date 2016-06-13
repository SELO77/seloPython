
from datetime import date, timedelta, datetime
from time import gmtime, strftime

# nowDate = datetime.now()
#
# print(nowDate)
#
# testDate = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
#
# print(testDate)
#
#
# testStrfTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
# print(testStrfTime)
#
#
#
# hello = "2016-06-28 00:00:00"
#
# dt1 = datetime.strptime(hello, '%Y-%m-%d %H:%M:%S')
#
# dt2 = datetime.date(dt1)
#
# dt4 = dt1 - timedelta(days=2)
# print(dt1)
# print(dt2)
# print(dt2 - timedelta(days=2)) # 2016-06-26
# print(type(dt2 - timedelta(days=2))) #< class 'datetime.date'>
# print(dt4) # 2016-06-26 00:00:00
#
# ## 유닉스 타임 스탬프
# print(datetime.timestamp(dt1)) # 1463624768
#
# print(datetime.today()) # 2016-05-19 11:24:02.468760
# print(datetime.timestamp(datetime.today())) # 1463624642.468774
#
# # UTC_time
# print(datetime.utcnow()) # 2016-05-19 02:33:09.047241


UTC_DATETIME = datetime.utcnow().strftime("%Y-%m-%d %T")
print(UTC_DATETIME) # 2016-05-19 03:02:05
LOCAL_DATETIME = datetime.today().strftime("%Y-%m-%d %T")
print(LOCAL_DATETIME) # 2016-05-19 12:02:05
print(type(LOCAL_DATETIME)) # str
BETWEEN_HOUR = 0

if UTC_DATETIME == LOCAL_DATETIME:
  BETWEEN_HOUR = 9


print("=======")
NOW_DATETIME = datetime.today() # 2016-05-19 12:00:53.841482
print(NOW_DATETIME)
NOW_TIMESTAMP = int(datetime.timestamp(NOW_DATETIME))# sever 시간 GMT 0
print(NOW_TIMESTAMP) # 1463626853.841482

NOW_HOUR = NOW_DATETIME.hour
print(NOW_HOUR) # 12

TIME_KEY = NOW_DATETIME.strftime("%Y%m%d%H")
print(TIME_KEY) # 2016051919




