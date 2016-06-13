import aioredis
import asyncio

from module.util.bColor import color_console as cc

def main():
  loop = asyncio.get_event_loop()
  redisKey = input("Redis 키를 입력하시오:")

  @asyncio.coroutine
  def go():
    # def create_connection(address, *, db=None, password=None,
    #                   encoding=None, loop=None):
    conn = yield from aioredis.create_connection(('localhost', 6379), encoding='utf-8')
    print("redis connection:",conn)

    str_value = yield from conn.execute('keys', "%s*"%redisKey)

    # str_value = yield from conn.execute('get', redisKey)
    # raw_value = yield from conn.execute('get', 'my-key', encoding=None)

    cc('warning','str_value:%s'%str_value)
    # print('raw_value:', raw_value)

    # assert str_value == 'selo'
    # assert raw_value == b'selo'

    conn.close()

  loop.run_until_complete(go())


main()