import traceback

data = [3,1,2,5,6,7]

try:
  result = filter(lambda x, y: y <x ,data)
  print(type(result))
  print(result)

  for i in result:
    print(i)

  testResult = filter(lambda x:x < 5, data)

  for i in testResult:
    print(i)

except:
  print(traceback.format_exc())