import asyncio
import traceback


class SpwanClass():
  def __init__(self):
    print("SpwanClass.__init()__")

  @asyncio.coroutine
  def execute(self, request_class_list):
    print("SpwanClass.execute()")
    response = []

    if request_class_list:
      @asyncio.coroutine
      def run(self, request_class):
        try:
          result = yield from request_class.execute()
          response.append(result)
        except:
          print(traceback.format_exc())

      try:
        tasks_list = []
        for each_class in request_class_list:
          print(each_class)
          tasks_list.append(
            asyncio.Task(run(each_class))
          )

        gather_result = yield from asyncio.gather(tasks_list)
        print("gather_result:\n%s"%gather_result)

      except:
        print(traceback.format_exc())

    return response


class RequestClass1():
  def __init__(self):
    print('RequestClass1.__init()__')

  @asyncio.coroutine
  def execute(self):
    print("RequestClass1.execute()")


class RequestClass2():
  def __init__(self):
    print('RequestClass2.__init()__')

  @asyncio.coroutine
  def execute(self):
    print("RequestClass2.execute()")

@asyncio.coroutine
def main():
  try:
    request_class_list = [RequestClass1(), RequestClass2()]
    # RequestClass1()
    # RequestClass2()

    spwanClass = SpwanClass()
    final_result = yield from spwanClass.execute(request_class_list)
    print(final_result)
  except:
    print(traceback.format_exc())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

