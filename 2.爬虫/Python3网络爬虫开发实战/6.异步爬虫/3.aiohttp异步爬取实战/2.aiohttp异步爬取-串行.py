import asyncio
import aiohttp
import logging
import json
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

LIMIT = 18
PAGE_SIZE = 18
# 貌似串行时间久了还是会被监测到？
PAGE_NUMBER = 10
CONCURRENCY = 5
INDEX_URL = 'https://spa5.scrape.center/api/book/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'spiders'
MONGO_COLLECTION_NAME = 'books'

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occured while scraping %s', url, exc_info=True)

async def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)

async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one(
            {'id': data.get('id')},
            {'$set': data},
            upsert = True
            )

async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)


async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('results %s', json.dumps(results, ensure_ascii=False, indent=2))
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())