
#requests库实现协程爬虫

import asyncio
import requests

async  def run(url):
    print("start ",url)
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,requests.get,url)
    print(response.url)


url_list = ["https://thief.one","https://home.nmask.cn","https://movie.nmask.cn"]

tasks = [asyncio.ensure_future(run(url)) for url in url_list]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))