import asyncio
import time
from urllib.request import urlopen


import aiohttp


urls = ['http://www.naver.com',
       'https://www.google.com',
       'https://www.apple.com',
       'http://www.bing.com/'] * 10


@asyncio.coroutine
def fetch(url):
    print('Start with', url)
    res = yield from aiohttp.request('GET', url)
    res.close()
    print('End', url)


st = time.time()
def fetch_all(urls):
    loop = asyncio.get_event_loop()
    fetchs = [fetch(url) for url in urls]
    wait_coro = asyncio.wait(fetchs)
    loop.run_until_complete(wait_coro)
    loop.close()


fetch_all(urls)
print("duration(s):{:.4f}".format(time.time() - st))
# duration(s):1.0372