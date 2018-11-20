#coroutine对象不能直接运行，在注册事件循环时，其实是run_until_complete方法
# 将coroutine函数包装成了一个（task）对象。所谓task对象，是Future类的子类
#保存了coroutine运行后的状态，用于未来获取coroutine的结果。我们也可以手动将
#coroutine对象定义成task


import asyncio

async def test1():
    print("1")
    await test2()
    print("2")


async def test2():
    print("3")
    print("4")



loop = asyncio.get_event_loop()
task = loop.create_task(test1())
loop.run_until_complete(task)
