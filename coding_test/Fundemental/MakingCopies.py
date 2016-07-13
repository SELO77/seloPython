import copy

def copy_list(l):
  if l is None:
    raise Exception
  else:
    return copy.deepcopy(l)

# print(copy_list(None))

def copy_list_best_answer(l):
  return list(l)

# print(copy_list_best_answer(None))

# What is difference between deepcopy and list

some_list = list(range(0,5))
print(some_list)
print(id(some_list))

list1 = list(some_list)
list2 = copy.deepcopy(some_list)

print(id(list1))
print(id(list2))

# those do the same work



