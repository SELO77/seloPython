# -*- coding: utf-8 -*-

# Python supports a simple type of multiple inheritance which allows the creation of Mixins. Mixins are a sort of class that is used to "mix in" extra properties and methods into a class. This allows you to create classes in a compositional style.

# Mixins are a really great concept but I often find that people use them incorrectly which can lead to some bugs. I often see Mixins used like the following:

class Mixin1(object):
    def test(self):
        print "Mixin1"


class Mixin2(object):
    def test(self):
        print "Mixin2"


class BaseClass():
    pass

# in Python the class hierarchy is defined right to left,
class MyClass(BaseClass, Mixin1, Mixin2):
    pass


MyClass().test()


class FixedMyClass(Mixin2, Mixin1, BaseClass):
    pass

FixedMyClass().test()