from datetime import *
from time import gmtime, strftime

nowDate = datetime.now()

print(nowDate)

testDate = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

print(testDate)


testStrfTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(testStrfTime)