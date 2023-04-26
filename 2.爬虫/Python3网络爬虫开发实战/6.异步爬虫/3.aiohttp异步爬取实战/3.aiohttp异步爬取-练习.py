# 本次爬取练习是需要进行大批量的爬取
# 并将爬取之后的数据存放到mongoDB当中
# aiohttp 用于进行异步爬虫执行
# asyncio 用于构建协程函数
# motor 用于进行异步的数据存储
import aiohttp
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import logging
import json

# 打印日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 网页内容分析
# 网页常量
LIMIT = 18
# offset计算公式 LIMIT * (page - 1) 因为是从0开始的
INDEX_URL = 'https://spa5.scrape.center/api/book/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 10

# 通信量
CONCURRENCY = 5

# 数据库引擎常量
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB = 'spiders'
MONGO_COLLECTION = 'books'

# 建立异步通行量
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

# 构建数据库通信连接
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# 获取网页内容
# 抓取api
async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occured while scraping %s', url, exc_info=True)

# 获取列表页信息
async def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)

# 异步存放数据
async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one(
            {'id': data.get('id')},
            {'$set': data},
            upsert = True
        )

# 获取内容详情页信息
async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data=data)

# 执行
async def main():
    global session
    # 获取session
    session = aiohttp.ClientSession()
    # 构建任务
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    # 获取异步结果
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('results %s', json.dumps(results, ensure_ascii=False, indent=2))
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    # 构建获取详细内容
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    # 执行任务
    await asyncio.wait(scrape_detail_tasks)
    await session.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


# 整体执行