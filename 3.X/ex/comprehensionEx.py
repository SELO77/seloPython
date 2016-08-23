a = range(1, 11)

even_square = [x**2 for x in a if x % 2 == 0]
print(even_square)

study_members = {"name": "selo", "age": "30", "job": "programmer"}

result = {val: key for key, val in study_members.items()}
print(result)
# print(type(tuple(result.keys())))

# for key in result.keys():
#   print(key)

dict_val_len = {len(val) for val in study_members.values() if len(val) > 2}
print(dict_val_len)


