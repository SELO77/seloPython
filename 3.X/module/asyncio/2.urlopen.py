import timeit
from urllib.request import urlopen


urls = ['https://selo77.github.io/2016/07/05/Python-Asyncio/',
        'https://google.com',
        'https://apple.com',
        'http://www.naver.com',
        'https://github.com/ssut']
start_time = timeit.default_timer()
for url in urls:
  print('start', url)
  urlopen(url)
  print('done', url)

duration = timeit.default_timer() - start_time
print(duration)

# start https://selo77.github.io/2016/07/05/Python-Asyncio/
# done https://selo77.github.io/2016/07/05/Python-Asyncio/
# start https://google.com
# done https://google.com
# start https://apple.com
# done https://apple.com
# start http://www.naver.com
# done http://www.naver.com
# start https://github.com/ssut
# done https://github.com/ssut
# 3.3478158349989826