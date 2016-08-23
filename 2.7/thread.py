# -*- coding: UTF-8 -*-
# python 2.7.8

import threading
import time

globalResource = 0

def clock_usingGlobalVariable(interval):
    global globalResource
    while True:
        globalResource += 1
        print 'func) this is {0}\n'.format(globalResource)
        time.sleep(interval)


class Clock(threading.Thread):
    def __init__(self, interval):
        super(Clock, self).__init__()
        global globalResource
        self.resource = globalResource
        self.interval = interval


    def run(self):
        while True:
            self.resource += 1
            print 'obj) this is {0}\n'.format(self.resource)
            time.sleep(self.interval)


if __name__ == '__main__':

    # 함수형 쓰레드 구현
    fun_thread = threading.Thread(target=clock_usingGlobalVariable, args=(1,))
    fun_thread.daemon = True
    fun_thread.start()

    # 객체형 구현
    thread = Clock(1)
    thread.demon = True
    thread.start()
