# -*- coding: utf-8 -*-
from functools import wraps
import datetime
import time


def my_logger(original_fnc):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_fnc.__name__), level=logging.NOTSET)

    @wraps(original_fnc)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] 실행결과 args = {}, kwargs = {}'.format(timestamp, args, kwargs))
        return original_fnc(*args, **kwargs)
    return wrapper


def my_timer(original_fnc):
    import time

    @wraps(original_fnc)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_fnc(*args, **kwargs)
        t2 = time.time() - t1
        print '{} 함수가 실행된 총 시간: {}초'.format(original_fnc.__name__, t2)
        return result

    return wrapper

@my_timer
@my_logger
def display_info(name, age):
    time.sleep(2)
    print 'display_info({}, {}) function run.'.format(name, age)


display_info('David', 33)
