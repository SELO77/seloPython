# -*- coding: utf-8 -*-

#def decorator_func(original_func):
#    def wrapper_func():
#        return original_func()
#    return wrapper_func
#
#
#def display():
#    print 'display 함수가 실행되었습니다.'
#
#decorated_display = decorator_func(display)
#
#decorated_display()
#
#print ''
#
#
#def decorator_f(original_f):
#    def wrapper_f():
#        print '{} 함수가 호출되기전 입니다.'.format(original_f.__name__)
#        return original_f()
#    return wrapper_f
#
#def display_1():
#    print 'display_1 fnc is runed'
#
#def display_2():
#    print 'display_2 fnc is runed'
#
#d_display_1 = decorator_f(display_1)
#d_display_2 = decorator_f(display_2)
#
#d_display_1()
#print
#d_display_2()

#def decorator_fnc(original_fnc):
#    def wrapper_fnc():
#        print '{} function is not called yet'.format(original_fnc.__name__)
#        return original_fnc()
#    return wrapper_fnc
#
#@decorator_fnc
#def display_1():
#    print 'display_1 function run.'
#
#@decorator_fnc
#def display_2():
#    print 'display_2 function run.'
#
#display_1()
#print
#display_2()

def decorator_fnc(original_fnc):
    def wrapper_fnc(*args, **kwargs):
        print '{} function is not called yet.'.format(original_fnc.__name__)
        return original_fnc(*args, **kwargs)
    return wrapper_fnc

@decorator_fnc
def display():
    print 'display function run.'

@decorator_fnc
def display_info(name, age):
    print '{}, {}'.format(name, age)

display()
print
display_info('SELO', 30)

