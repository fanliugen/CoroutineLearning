#遇到异常停止coroutine，需先cancel协程对象，再停止loop

import asyncio

async def test1():
    print("1")
    await asyncio.sleep(3)
    print("2")
    return "stop"

tasks = [
    asyncio.ensure_future(test1()),
    asyncio.ensure_future(test1()),
    asyncio.ensure_future(test1()),
]

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(asyncio.wait(tasks))

except KeyboardInterrupt as e:
    for task in asyncio.Task.all_tasks():
        task.cancel()
    loop.stop()
    loop.run_forever()
finally:
    loop.close()