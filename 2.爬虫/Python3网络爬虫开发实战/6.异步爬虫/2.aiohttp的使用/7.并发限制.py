import asyncio
import aiohttp

# 最大爬取并发量
CONCURRENCY = 5
URL = 'https://www.baidu.com'
# 信号量对象
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

async def scrape_api():
    # 此部分内容用于控制并发
    async with semaphore:
        print('scraping', URL)
        # 获取网页响应
        async with session.get(URL) as response:
            # 这里是每次开启并发时休眠1秒
            await asyncio.sleep(1)
            return await response.text()

async def main():
    global session
    session = aiohttp.ClientSession()
    # 构建10000个task任务
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    # 运行任务
    await asyncio.gather(*scrape_index_tasks)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())