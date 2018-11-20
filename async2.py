#执行coroutine函数
#coroutine对象和yield对象一样，也可以通过使用send函数来使其执行
async def  test1():
    print("1")
    print("2")



async def  test2():
    print("3")
    print("4")



a = test1()
b = test2()

a.send(None)
b.send(None)