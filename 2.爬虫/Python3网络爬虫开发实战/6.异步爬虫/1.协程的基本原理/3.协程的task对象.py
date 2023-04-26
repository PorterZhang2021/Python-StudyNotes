import asyncio

# 构架一个execute方法
async def execute(x):
    print('Number:', x)
    return x

# 直接调用 发现没有执行
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

# 构建一个事件循环
loop = asyncio.get_event_loop()
# 直接创建一个task
task = loop.create_task(coroutine)
print('Task:', task)
# 注册调用task
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')