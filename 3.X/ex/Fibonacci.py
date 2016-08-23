from timeit import timeit
now = timeit()


def fib(n):
    count = 0
    a, b = 0, 1
    while a < n:
        count += 1
        a, b = b, a + b
        print a, b
    print "\n" + str(count)
fib(100000000000000000000000000000000000000000)
end = timeit()
print end - now

# with recursive
