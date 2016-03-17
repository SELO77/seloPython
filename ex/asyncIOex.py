
# def custom_range(end):
#     i = 0
#     z = "How generator works!!??"
#     while i < end:
#         yield i #coroutine : 진입점이 여러개인 함수
#         print('custom_range.i :%s'%i)
#         i += 1
#         yield z

# gen = custom_range(5)
# for i in gen:
#     print(i, end=',')

# list(gen)
# print(next(gen))


# def sendme():
#   while  1:
#     something = yield
#     if something is None:
#       raise StopIteration()
#     print(something)

# gen = sendme()
# next(gen)
# gen.send('a')
# gen.send('b')
# gen.send(None)


# import timeit
# from urllib.request import urlopen
#
# urls = ['http://naver.com', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']
# start = timeit.default_timer()
#
# for url in urls:
#   print('Start', url)
#   urlopen(url)
#   print('Done', url)
#
# duration = timeit.default_timer() - start
# print(duration)

# Start http://naver.com
# Done http://naver.com
# Start https://google.com
# Done https://google.com
# Start https://apple.com
# Done https://apple.com
# Start https://ubit.info
# Done https://ubit.info
# Start https://github.com/ssut
# Done https://github.com/ssut
# 3.2820995340007357

# 위 코드의 문제점은 다음과 같습니다:
# 한 번에 한 URL밖에 받아오지 못합니다.
# 따라서 한 작업이 끝나기 전까지 다음 작업을 할 수 없습니다.
# URL이 늘어나면 늘어날수록 위 코드는 매우 비효율적입니다.
# IO 작업이 끝나기 전까지 나머지 모든 코드는 블록됩니다.
# ==========================================


# import timeit
# from concurrent.futures import ThreadPoolExecutor
# from urllib.request import urlopen
#
# urls = ['http://naver.com', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']
#
# def fetch(url):
#   print('Start', url)
#   urlopen(url)
#   print('Done', url)
#
# start = timeit.default_timer()
# with ThreadPoolExecutor(max_workers=5) as executor:
#   for url in urls:
#     executor.submit(fetch, url)
#
# duration = timeit.default_timer() - start
# print(duration)

# Start http://naver.com
# Start https://google.com
# Start https://apple.com
# Start https://ubit.info
# Start https://github.com/ssut
# Done http://naver.com
# Done https://ubit.info
# Done https://google.com
# Done https://apple.com
# Done https://github.com/ssut
# 1.3564843910025957

# 스레드 갯수는 OS에 의해 한정되어 있습니다.
# 공유 메모리 문제가 있습니다. 락(Mutex)을 사용해야 하죠.
# 그런데 파이썬에는 GIL이라는 괴상한 놈이 있습니다.
# 파이썬 스레드를 스레드답게 쓰지 못하게(?) 해주는 놈인데요. 뭐 자세한 설명은 구글링을.. (이 글에서는 aio에 대해서만 다룹니다. ㅠㅠ)
# ==========================================



# import timeit
# from concurrent.futures import ProcessPoolExecutor
# from urllib.request import urlopen
#
# urls = ['http://naver.com', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']
#
# def fetch(url):
#   print('Start', url)
#   urlopen(url)
#   print('Done', url)
#
# start = timeit.default_timer()
# with ProcessPoolExecutor(max_workers=5) as executor:
#   for url in urls:
#     executor.submit(fetch, url)
#
# duration = timeit.default_timer() - start
# print(duration)

# Start https://google.com
# Start http://naver.com
# Start https://apple.com
# Start https://ubit.info
# Start https://github.com/ssut
# Done https://ubit.info
# Done http://naver.com
# Done https://google.com
# Done https://apple.com
# Done https://github.com/ssut
# 1.5680245689982257

# 프로세스는 스레드와 비슷하지만 직접적으로 메모리를 공유하지 않습니다. (물론 일부 상황을 제외하고고 가능합니다)
# GIL도 없습니다: CPU-bound 작업에 유리합니다.
# 단 프로세스는 높은 cost를 요구합니다. 즉, 오버헤드가 큽니다. 시간을 잴 때 보면 알겠지만 프로세스 풀이 생성되고 작업이 끝나기 까지의 시간을 쟀습니다.
# 위에서 언급한 GIL을 조금 찾아보시면 아시겠지만 CPU-bound 작업에는 프로세스를 스폰하는 방법이 무조건 유리합니다. (AsyncIO도 동일합니다.)
# ==========================================

import aiohttp
import asyncio
import timeit

@asyncio.coroutine
def fetch(url):
  print('Start', url)
  req = yield from aiohttp.request('GET', url)
  print('Done', url)

@asyncio.coroutine
def fetch_all(urls):
  fetches = [asyncio.Task(fetch(url)) for url in urls]
  yield from asyncio.gather(*fetches)

urls = ['http://naver.com', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']

start = timeit.default_timer()
asyncio.get_event_loop().run_until_complete(fetch_all(urls))
duration = timeit.default_timer() - start
print(duration)

#1.4278107339996495
# asyncio에서 이벤트 루프를 끄집어오고 fetch_all 함수를 실행합니다. (코루틴 함수를 실행합니다.)
# fetch_all 함수 내에서 fetch(url) 가 실행된 결과(제너레이터)를 asyncio.Task로 래핑해줍니다. 결과, asyncio에서는 위 이미지에 보이는 이벤트 루프 큐에 이 함수 제너레이터를 삽입하고 자동으로 스케쥴링을 합니다.
# asyncio.gather 함수는 넘겨진 모든 코루틴 Task가 종료될 때까지 기다렸다가 종료되면 모든 결과를 모아서 리턴해줍니다.
