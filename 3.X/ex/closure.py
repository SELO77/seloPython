# -*- coding: utf-8 -*-

def outer_func(tag):
    tag = tag

    def inner_func(txt):
        text = txt
        print '<{0}>{1}<{0}>'.format(tag, text)

    return inner_func

h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func('it\'s in h1 tag')
p_func('it\' in p tag')
