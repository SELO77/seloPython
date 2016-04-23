# About generator, randint

import random

# def lottery():
#   # returns 6 numbers between 1 and 40
#   for i in range(6):
#       yield random.randint(1, 40)
#
# count = 1
# for random_number in lottery():
#   print("And the next number is... %d: %d!" %(count,random_number))
#   count += 1


#  Upper code has some error. sometime one number can be occur again. How fix it?
def lottery():
  bascket = list(range(1, 46))
  print(",".join(str(v) for v in bascket))

  for i in range(6):
    yield bascket.pop(random.randint(1,len(bascket)))

for random_number in lottery():
  print(random_number)

