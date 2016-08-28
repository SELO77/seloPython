x = 126
y = 90
r = None
while True:
    print x, y, r
    r = x % y
    if r == 0:
        print y
        break
    x = y
    y = r
