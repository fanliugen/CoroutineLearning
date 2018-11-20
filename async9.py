#通过绑定回调函数获取返回值。回调函数的最后一个参数是future对象，通过该对象可以获取coroutine反回值

import asyncio

async def test1():
    print("1")
    await test2()
    print("2")
    return "stop"

async def test2():
    print("3")
    print("4")


def callback(future):
    print('Callback:' , future.result())

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(test1())
task.add_done_callback(callback)
loop.run_until_complete(task)
