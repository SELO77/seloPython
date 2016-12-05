def f():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        yield from do_yield(x)

f1 = f()
print(next(f1))
print(next(f1))
print(next(f1))