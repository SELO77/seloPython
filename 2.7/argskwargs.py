

class TestClass(object):

    def some_fnc(self, population, *args):
        print args
        print population

    def main(self):
        self.some_fnc("first")

TestClass().main()
