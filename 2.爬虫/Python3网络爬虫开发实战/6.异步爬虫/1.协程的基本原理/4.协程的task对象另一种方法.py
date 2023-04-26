import asyncio

async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
# 调用ensure_future方法 直接创建了task对象
task = asyncio.ensure_future(coroutine)
print('Task:', task)
# 构建一个事件循环
loop = asyncio.get_event_loop()
# 注册执行task
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')
