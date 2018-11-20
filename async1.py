
#通过async关键字定义Coroutine对象，但是调用函数时，函数没有执行，只是打印出coroutine对象的地址
async def  test1():
    print("1")
    print("2")



async def  test2():
    print("3")
    print("4")



print(test1())
print(test2())