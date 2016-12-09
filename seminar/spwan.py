# asyncio Sample for MyMusicTaste
# SELO77
# 2016-07-24
import asyncio
import time

class SpawnClass():


    def __init__(self):
        pass


    @asyncio.coroutine
    def execute(self, request_class_list):
        response = []
        if request_class_list:

            @asyncio.coroutine
            def run(request_class):
                result = yield from request_class.execute()
                response.append(result)

            tasks_list = []
            for each_class in request_class_list:
                tasks_list.append(
                    asyncio.Task(run(each_class))
                )

            yield from asyncio.gather(*tasks_list)

        return response


class RequestClass1():


    def __init__(self):
        print('RequestClass1.__init()__')


    @asyncio.coroutine
    def execute(self):
        yield from asyncio.sleep(4.0)
        return "class1_response"


class RequestClass2():


    def __init__(self):
        print('RequestClass2.__init()__')


    @asyncio.coroutine
    def execute(self):
        yield from asyncio.sleep(2.0)
        return "class2_response"


@asyncio.coroutine
def main():
    request_class_list = [RequestClass1(), RequestClass2()]
    spawnClass = SpawnClass()
    st = time.time()
    final_result = yield from spawnClass.execute(request_class_list)
    print("runtime:%s, final_result:%s"% (time.time() - st, final_result))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())