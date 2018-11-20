#使用aiohttp实现异步爬虫

import asyncio
import aiohttp

async def run(url):
    print("start spider",url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.url)

url_list = [
    "https://thief.one",
    "https://home.nmask.cn",
    "https://movie.nmask.cn",
]

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(run(url)) for url in url_list]
loop.run_until_complete(asyncio.wait(tasks))


