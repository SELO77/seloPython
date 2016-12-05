flag = True
for v in xrange(10):
    print v
    try:
        if v == 2:
            raise AttributeError
    except Exception:
        print "Exception"
        flag = False
        break
    except AttributeError:
        print "AttributeError"
        flag = False
        break

print flag



