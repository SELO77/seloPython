from datetime import *


date_str = "2016-08-30"
result = datetime.strptime('2011-07-07', "%Y-%m-%d")

# print(result)

if result < datetime.strptime("2016-09-01", "%Y-%m-%d"):
  print('innner day')
else:
  print('outter day')