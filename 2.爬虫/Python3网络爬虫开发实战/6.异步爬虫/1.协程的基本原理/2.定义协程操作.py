# 引入asyncio包
import asyncio
# 利用async定义execute方法
async def execute(x):
    print('Number:', x)
# 调用execute方法 但并没有执行
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
# 创建事件循环loop
loop = asyncio.get_event_loop()
# 将协程对象注册到事件循环中
loop.run_until_complete(coroutine)
print('After calling loop')