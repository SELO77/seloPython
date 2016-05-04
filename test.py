bedTypesInfo = {
        'SGL': 0,
        'DBL': 0,
        'TRP': 0,
        'QUAD': 0
      }

print(bedTypesInfo)
print(bedTypesInfo.keys())
print('')

for value in bedTypesInfo.__iter__():
  print(value)

print('')

for v in bedTypesInfo:
  print(v)

