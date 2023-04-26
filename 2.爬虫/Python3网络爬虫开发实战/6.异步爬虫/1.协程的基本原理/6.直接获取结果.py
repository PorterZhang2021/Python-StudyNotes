import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

coroutine = request()
# 构架task对象
task = asyncio.ensure_future(coroutine)
print('Task:', task)
# 构建一个循环
loop = asyncio.get_event_loop()
# 注册task任务
loop.run_until_complete(task)
# 输出情况
print('Task:', task)
# 输出结果
print('Task Result:', task.result())