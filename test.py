from datetime import *
from decimal import Decimal

result = datetime.utcnow() + timedelta(hours=9)
print(result)





str_time = "2016-11-17T23:59:59"

datetime_time = datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S")
print(datetime_time)


str_float = "3000.00"

print(Decimal(str_float))
print(type(Decimal(str_float)))

print(0 + 1.34)
print(type(0))
print(type(1.34))