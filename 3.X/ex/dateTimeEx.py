from datetime import *
from time import gmtime, strftime

nowDate = datetime.now()

print(nowDate)

testDate = nowDate.strftime('%Y-%m-%d %H:%M:%S')

print(testDate)
print type(testDate)


testStrfTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(testStrfTime)

print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')