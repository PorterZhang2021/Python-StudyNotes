import aiohttp
import asyncio

# 每个异步爬取方式都需要加async来修饰
async def fetch(session, url):
    # 上下文管理器 帮助我们自动分配和释放资源
    async with session.get(url) as response:
        # 返回协程对象，需要增加await 状态码为数值则不需要
        return await response.text(), response.status
    
async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'html:{html[:100]}...')
        print(f'status:{status}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())