

result = []

test_dict = {
  "A": {
    "Aa": {
      "Aaa": "",
      "Aab": "",
    },
    "Ab": "",
  },
  "B": {
    "Ba": ""
  },
  "C": ""
}


def recursive_get_keys(dict_keys):

  # if not isinstance(dict_keys, dict):
  #   raise Exception
  if len(dict_keys.keys()) == 0:
    return
  for v in dict_keys.keys():
    result.append(v)
    if len(test_dict[v].keys()):
      recursive_get_keys(v)

recursive_get_keys(test_dict)

print(result)

