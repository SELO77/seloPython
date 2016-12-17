import time
import os
from threading import Thread

def do_work(start, end, result):
    print(os.getpid())
    sum = 0
    for i in range(start, end):
        sum += i
    result.append(sum)
    return


if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    st = time.time()
    th1 = Thread(target=do_work, args=(START, int(END/2), result))
    th2 = Thread(target=do_work, args=(int(END/2), END, result))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('==sum:{}, running time {:.4f}s'.format(sum(result),
                                                  time.time() - st))  # 8.6576s
