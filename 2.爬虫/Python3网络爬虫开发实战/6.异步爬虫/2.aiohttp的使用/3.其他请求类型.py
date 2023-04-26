import aiohttp
import asyncio

async def main_post():
    url = 'https://www.httpbin.org/post'
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=data) as response:
            print(await response.text())

async def main_put():
    url = 'https://www.httpbin.org/put'
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.put(url=url, data=data) as response:
            print(await response.text())

async def main_delete():
    url = 'https://www.httpbin.org/delete'
    async with aiohttp.ClientSession() as session:
        async with session.delete(url=url) as response:
            print(await response.text())

async def main_head():
    url = 'https://www.httpbin.org/get'
    async with aiohttp.ClientSession() as session:
        async with session.head(url=url) as response:
            print(await response.text())

async def main_options():
    url = 'https://www.httpbin.org/get'
    async with aiohttp.ClientSession() as session:
        async with session.options(url=url) as response:
            print(await response.text())

async def main_patch():
    url = 'https://www.httpbin.org/patch'
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.patch(url=url, data=data) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main_post())
    asyncio.get_event_loop().run_until_complete(main_put())
    asyncio.get_event_loop().run_until_complete(main_delete())
    asyncio.get_event_loop().run_until_complete(main_head())
    asyncio.get_event_loop().run_until_complete(main_options())
    asyncio.get_event_loop().run_until_complete(main_patch())
