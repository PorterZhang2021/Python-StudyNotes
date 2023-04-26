import requests
import logging
import pymongo

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


# 常量
# 索引url
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
# 内容url
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
# limit
LIMIT = 10
# 总页数
TOTAL_PAGE = 10
# 代理
PROXIES = {
    # 此部分在v2rayN代理中找到系统代理部分找到对应端口
	'http': '127.0.0.1:10809',
	'https': '127.0.0.1:10809'
}
# mongo连接
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
# mongo数据库
MONGO_DB_NAME = 'spiders'
# mongo集合
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

def scrape_api(url):
    logging.info('scraping %s ...', url)
    try:
        # 请求要爬取的页面
        response = requests.get(url, proxies=PROXIES)
        # 如果状态码为200 
        if response.status_code == 200:
            # 返回json格式数据
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occured while scraping %s', url, exc_info=True)

def scrape_index(page):
    # 获取链接
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

def save_data(data):
    collection.update_one(
        {'name': data.get('name')},
        {'$set': data},
        upsert=True
    )

def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)
            logging.info('data saved successfully')

if __name__ == '__main__':
    main()