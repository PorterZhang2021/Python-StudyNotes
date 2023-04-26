import asyncio
import requests

# 构建一个request的方法
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url) 
    return status
# 任务回调函数
def callback(task):
    print('Status:', task.result())
# 协程对象
coroutine = request()
# 任务
task = asyncio.ensure_future(coroutine)
# 绑定回调
task.add_done_callback(callback)
# 输出任务
print('Task:', task)
# 获取循环
loop = asyncio.get_event_loop()
# 注册事件
loop.run_until_complete(task)
print('Task:', task)