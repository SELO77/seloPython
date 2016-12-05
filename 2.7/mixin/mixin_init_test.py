
class Mixin1:
    hello = "mixin1"
    def __init__(self):
        print "Mixin1 init"

class Mixin2:
    hello2 = "mixin2"
    def __init__(self):
        print "Mixin2 init"


class TestClass(Mixin1,Mixin2):
    print "TestClass"

test = TestClass()
print test.hello
print test.hello2
