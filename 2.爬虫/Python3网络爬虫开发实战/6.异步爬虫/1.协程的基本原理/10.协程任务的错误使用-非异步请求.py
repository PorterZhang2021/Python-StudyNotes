import asyncio
import requests
import time

start = time.time()

# 这种方式直接破坏了异步请求
# 请求页面方法独立
async def get(url):
    return requests.get(url)

async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    # 执行操作
    response = await get(url)
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)