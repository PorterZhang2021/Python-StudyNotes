import asyncio
import requests
import time

start = time.time()

async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    # 这里的等待操作是错误的
    response = await requests.get(url)
    # 这里错误的原因是因为 await对象
    # await后面对象有如下要求：
    # 1.一个原生协程对象
    # 2.一个由types.coroutine修饰的生成器，这个生成器可以返回协程对象
    # 3.由一个包含__await__方法的对象返回的一个迭代器
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)