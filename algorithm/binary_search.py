import random
import time
import sys
sys.getrecursionlimit() # 1000
#sys.setrecursionlimit()

#def binary_search(data, val):
#    if len(data) < 2:
#        return -1
#    length = len(data)
#    for idx, i in enumerate(data[:length/2]):
#        if i == val:
#            return idx
#    return binary_search(data[length/2:], val)

def binary_search(data, val):
    if not data:
        return -1
    mid = len(data)/2
    for idx, i in data[:mid]:
        if i == val:
            return idx, mid
    return binary_search(data[mid:], val)

if __name__ == "__main__":
    sample_data = []
    for v in range(1000000):
        sample_data.append(random.randrange(1, 1000000))
    val = random.randrange(1, 999999)
    start = time.time()
    print binary_search(sample_data, val)
    print time.time() - start
