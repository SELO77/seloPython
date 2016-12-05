import types
from collections import abc


class Fibonacci:


    def __iter__(self):
        return FibonacciGenerator()


class FibonacciGenerator:


    def __init__(self):
        self.a = 0
        self.b = 1


    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self


fg = FibonacciGenerator()
f = Fibonacci()
print(isinstance(fg, types.GeneratorType))
print(isinstance(fg, abc.Generator))
print()
print(isinstance(f, types.GeneratorType))
print(isinstance(f, abc.Generator))

limit = 10
index = 0
for v in f:
    print(v)
    index += 1
    if index > limit:
        break


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print()
count = 0
def recursive_fibonacci(a, b):
    print(a)
    global count
    count += 1
    if count > 10:
        return
    return recursive_fibonacci(b, a + b)

rf = recursive_fibonacci(0, 1)
# print(rf)
# print(next(rf))
# print(next(rf))
# print(next(rf))

