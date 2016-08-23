# Generators are used to create iterators,
# but with a different approach.
# Generators are simple functions which return an iterable set of items, one at a time, in a special way.

def generatorSimple():
  for i in range(4):
    yield i

g = generatorSimple()
print(g.__next__()) # 0
print(g.__next__()) # 1
print(g.__next__()) # 2
print(g.__next__())