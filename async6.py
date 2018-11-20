#通过send函数调用coroutine函数时，test1阻塞，执行test2函数，但是执行完test2后，没法反回执行test1
#我们这里使用asynio自带的方法循环执行coroutine函数


import asyncio

async def test1():
    print("1")
    await test2()
    print("2")


async def  test2():
    print("3")
    print("4")


loop = asyncio.get_event_loop()
loop.run_until_complete(test1())