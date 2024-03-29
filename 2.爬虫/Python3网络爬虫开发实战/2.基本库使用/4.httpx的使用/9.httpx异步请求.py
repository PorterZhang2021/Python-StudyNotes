import httpx
import asyncio

url = 'https://www.httpbin.org/get'

# 设置异步函数
async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        # 请求响应 
        response = await client.get(url)
        print(response.text)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch(url))