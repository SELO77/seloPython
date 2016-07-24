
tree = {
  'A': {
    'Aa': {
      'Ab': {
        'Aba':{}
      }
    }
  },
  'B': {},
  'C': {},
}

print(tree.keys())

result_list = []
def recursive_get_keys(dict):
  if len(dict.keys()) == 0:
    return
  for v in dict.keys():
    result_list.append(v)
    recursive_get_keys(v)



result = recursive_get_keys(tree)
print(result)