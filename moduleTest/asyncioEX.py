import asyncio

# loop = asyncio.get_event_loop()
#
# @asyncio.coroutine
# def hi():
#   print("hi")
#
# @asyncio.coroutine
# def execute():
#   print(type(hi()))
#   yield from hi()
#   print("hello")
#
# loop.run_until_complete(execute())

# def test():
#   task = asyncio.Task(hi())
#   yield from asyncio.gather(*task)
#
# asyncio.get_event_loop().run_until_complete(test())
class scope_test():
  dddddd = 0
  def __init__(self):
    pass

  def hello(self):
    self.dddddd += 1
    print("hello")
    if self.dddddd > 3:
      return 0
    return self.hello()


st = scope_test()
st.hello()