import traceback

test_val = None

try:
  for v in range(0, 5):
    result = test_val.get('result')
    print(v)

except:
  print(traceback.format_exc())