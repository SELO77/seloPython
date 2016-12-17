import os
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

urls = ['http://www.naver.com',
       'https://www.google.com',
       'https://www.apple.com',
       'http://www.bing.com/'] * 10
NUM_WORKERS = 5

def fetch(url):
    # print(os.getpid())
    print('Start with', url)
    urlopen(url)
    print('End', url)


st = time.time()

with ThreadPoolExecutor(max_workers=NUM_WORKERS) as th:
    for url in urls:
        th.submit(fetch, url)


print("duration(s):{:.4f}, NUM_WORKERS:{}".format((time.time() - st), NUM_WORKERS))
# duration(s):1.6250, NUM_WORKERS:5
# duration(s):1.8724, NUM_WORKERS:4
