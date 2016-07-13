import timeit
import traceback
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

# concurrent.futures 모듈은 비동기 실행을 위한 high-level interface 입니다.
# [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
# 3가지 대표적인 Executor의 구현을 통해 비동기 실행이 이루어 집니다. 첫번째 ThreadPoolExecutor를 사용하여 실행해 봅시다.

urls = ['https://selo77.github.io/2016/07/05/Python-Asyncio/',
        'https://google.com',
        'https://apple.com',
        'http://www.naver.com',
        'https://github.com/ssut']
start_time = timeit.default_timer()

def fetch(url):
  print('Start', url)
  response = urlopen(url)
  # print(response) # <http.client.HTTPResponse object at 0x10446b3c8>
  # print(response.status) # 200
  if response.status == 200:
    print(response.headers)
  print('End', url)

with ThreadPoolExecutor(max_workers=5) as executor:
  for url in urls:
    executor.submit(fetch, url)

duration = timeit.default_timer() - start_time
print(duration) # 1.1321891870011314

# Start https://selo77.github.io/2016/07/05/Python-Asyncio/
# Start https://google.com
# Start https://apple.com
# Start http://www.naver.com
# Start https://github.com/ssut
# End http://www.naver.com
# End https://selo77.github.io/2016/07/05/Python-Asyncio/
# End https://google.com
# End https://apple.com
# End https://github.com/ssut
# 1.1321891870011314

# print의 출력을 보면 Thread드 스러운 정상작동 결과를 확인할 수 있습니다. 하지만
# Python에서 제공하는 Thread에는 아래와 같은 문제가 있습니다
# 1. 스레드 갯수는 OS에 의해 한정되어 있습니다
# 2. 공유 메모리 문제로 인해 락(Mutex)를 사용해야합니다.


