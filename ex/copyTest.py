import copy

testList = list(range(5))
copyList = testList.copy()

result = testList is copyList
print(testList)
print(testList[-1])
print(result)

# print(id(testList)) # 메모리 주소가 다르다. 하지만!!!
# print(id(copyList))
#
# print(id(testList[0])) # 리스트가 갖는 요소들의 값은 같은 메모리 주소
# print(id(copyList[0]))

# 그래서 완전한 복사 객체를 만들려면
deepcopyList = copy.deepcopy(testList)
print(result)

print(id(testList)) #
print(id(deepcopyList))
print()

print(id(testList[0])) #
print(id(deepcopyList))