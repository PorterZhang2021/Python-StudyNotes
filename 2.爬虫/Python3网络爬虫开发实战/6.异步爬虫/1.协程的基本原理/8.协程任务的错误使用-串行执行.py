import asyncio
import requests
import time

start = time.time()
# 构建一个请求操作
async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = requests.get(url)
    print('Get response from', url, 'response', response)
# 构建10个任务
tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# 构建一个执行循环
loop = asyncio.get_event_loop()
# 对任务进行操作
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
# 发现用时没有变化，主要原因是因为其利用的是串行执行
print('Cost time:', end - start)