import dis
import time


def do_work(start, end, result):
    sum = 0
    for i in range(start, end):
        sum += i
    result['sum'] = sum


if __name__ == '__main__':
    START, END = 0, 100000000
    result = {}
    st = time.time()
    do_work(START, END, result)
    print('== sum:{} running time {:.4f}s'.format(result['sum'],
                                                  time.time() - st))
    # 7.9923s