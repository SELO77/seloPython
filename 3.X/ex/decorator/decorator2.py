# -*- coding: utf-8 -*-

class DecoratorClass:
    def __init__(self, original_fnc):
        self.original_fnc = original_fnc

    def __call__(self, *args, **kwargs):
        print '{}'.format(self.original_fnc.__name__)
        return self.original_fnc(*args, **kwargs)

@DecoratorClass
def display():
    print 'display function run.'

@DecoratorClass
def display_info(name, age):
    print '{}, {}'.format(name, age)

display()
print
display_info('SELO', 30)
