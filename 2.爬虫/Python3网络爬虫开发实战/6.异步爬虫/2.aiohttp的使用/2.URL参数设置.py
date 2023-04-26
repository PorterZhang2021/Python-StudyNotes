import aiohttp
import asyncio

async def main():
    # 参数
    params = {'name': 'germey', 'age': 25}
    # 异步获取
    async with aiohttp.ClientSession() as session:
        # 异步获取
        async with session.get('https://www.httpbin.org/get', params=params) as response:
            # 获取需要的结果
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())