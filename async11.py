#coroutine并发


import asyncio

async def test1():
    print("1")
    await asyncio.sleep(1)
    print("2")
    return "stop"

a = test1()
b = test1()
c = test1()

tasks = [
    asyncio.ensure_future(a),
    asyncio.ensure_future(b),
    asyncio.ensure_future(c),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print("task result is ",task.result())