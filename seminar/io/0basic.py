import time
from urllib.request import urlopen

urls = ['http://www.naver.com',
       'https://www.google.com',
       'https://www.apple.com',
       'http://www.bing.com/'] * 10


def fetch(url):
    print('Start with', url)
    urlopen(url)
    print('End', url)


st = time.time()
for url in urls:
    fetch(url)


print("duration(s):{:.4f}".format(time.time() - st))
# duration(s):6.5380