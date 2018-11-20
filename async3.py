#使用send时，程序先执行了test1协程函数，当test1执行完毕后报了StopIteration异常
#这是协程函数执行完返回的一个异常。我们可以用try except来捕捉，来判断coroutine函数是否执行完毕

async def  test1():
    print("1")
    print("2")



async def  test2():
    print("3")
    print("4")



a = test1()
b = test2()

# a.send(None)
# b.send(None)


try:
    a.send(None)
except StopIteration as e:
    print(e.value)
    pass


try:
    b.send(None)
except StopIteration as e:
    print(e.value)
    pass