#-*- coding: utf-8 -*-
import traceback


def e_t():
    # raise Exception
    return 'HELLO'


def main():
    try:
        r = e_t()
        print "!!"
        print r
    except:
        print traceback.format_exc()


if __name__ == '__main__':
    main()