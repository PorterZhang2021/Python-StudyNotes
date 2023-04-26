import aiohttp
import asyncio

async def main():
    data = {'name': 'germy', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.httpbin.org/post', data=data) as response:
            print(await response.text())

async def main_json():
    data = {'name': 'germy', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.httpbin.org/post', json=data) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().run_until_complete(main_json())