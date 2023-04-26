import asyncio
import requests
# 构建一个request()方法
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status
# 构建5个任务
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
# 输出查看
print('Tasks:', tasks)
# 进行循环执行
loop = asyncio.get_event_loop()
# 注册协程任务
loop.run_until_complete(asyncio.wait(tasks))
# 输出执行结果
for task in tasks:
    print('Task Result:', task.result())