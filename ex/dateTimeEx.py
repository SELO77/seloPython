import datetime
from time import gmtime, strftime

nowDate = datetime.datetime.now()

print(nowDate)

testDate = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

print(testDate)


testStrfTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(testStrfTime)