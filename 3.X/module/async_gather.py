# asyncio Sample for MyMusicTaste
# SELO77
# 2016-07-24
import asyncio
import traceback


class SpawnClass():


  def __init__(self):
    pass


  @asyncio.coroutine
  def execute(self, request_class_list):
    response = []
    try:
      if request_class_list:
        @asyncio.coroutine
        def run(request_class):
          try:
            result = yield from request_class.execute()
            response.append(result)
          except:
            print(traceback.format_exc())
        tasks_list = []
        for each_class in request_class_list:
          tasks_list.append(
            asyncio.Task(run(each_class))
          )
        yield from asyncio.gather(*tasks_list)
    except:
      print(traceback.format_exc())
    return response


class RequestClass1():

  def __init__(self):
    print('RequestClass1.__init()__')

  @asyncio.coroutine
  def execute(self):
    return "class1_response"


class RequestClass2():

  def __init__(self):
    print('RequestClass2.__init()__')

  @asyncio.coroutine
  def execute(self):
    return "class2_response"


@asyncio.coroutine
def main():
  try:
    request_class_list = [RequestClass1(), RequestClass2()]
    spawnClass = SpawnClass()
    final_result = yield from spawnClass.execute(request_class_list)
    print("final_result:%s"%final_result)
  except:
    print(traceback.format_exc())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())