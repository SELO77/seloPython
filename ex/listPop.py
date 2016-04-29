# list = list(range(7))
#
# for v in list:
#   print(v)
#
# result = list.pop(3)
# print("\n\n", result)
#
# print(list)
#
# result = list.pop(3)
# print("\n\n", result)
#
# print(list)

# strTest = "Stokmarknes, Norway"
# terms = "tokyo"
# print(terms in strTest)

testList = ["H", "E", "L", "S", "o"]

# while testList:
#   print(len(testList), testList[0])
#   testList.pop(0)

for i, v in enumerate(testList):
  print(i, v)
  testList.pop(i)



