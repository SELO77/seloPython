import aioredis
import asyncio


def main():
  loop = asyncio.get_event_loop()

  @asyncio.coroutine
  def go():
    # def create_connection(address, *, db=None, password=None,
    #                   encoding=None, loop=None):
    conn = yield from aioredis.create_connection(('localhost', 6379), encoding='utf-8')
    print("redis connection:",conn)

    ok = yield from conn.execute('set', 'my-key', 'selo')
    assert ok == 'OK', ok

    str_value = yield from conn.execute('get', 'my-key')
    raw_value = yield from conn.execute('get', 'my-key', encoding=None)

    print('str_value:', str_value)
    print('raw_value:', raw_value)

    assert str_value == 'selo'
    assert raw_value == b'selo'

    conn.close()

  loop.run_until_complete(go())

main()







