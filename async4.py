#前面的都没有实现coroutine函数的交替执行，这里我们能过await函数，让test2函数也可以执行



import asyncio

async def  test1():
    print("1")
    await asyncio.sleep(1)
    print("2")

async def test2():
    print("3")
    print("4")


a = test1()
b = test2()

try:
    a.send(None)
except StopIteration:
    pass


try:
    b.send(None)
except StopIteration:
    pass