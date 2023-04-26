import aiohttp
import asyncio

async def main():
    # 这里进行了超时设定
    timeout = aiohttp.ClientTimeout(total=5)
    # 传入超时情况
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # 如果超时这里会直接报错
        async with session.get('https://www.httpbin.org/get') as response:
            print('status', response.status)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())