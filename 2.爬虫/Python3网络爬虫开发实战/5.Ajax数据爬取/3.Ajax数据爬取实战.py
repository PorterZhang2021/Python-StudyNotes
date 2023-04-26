# request库 - 抓取json
import requests
# logging库 - 用于输出日志
import logging
# pymongo - 用于存储数据
import pymongo

# 日志初始化
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
# URL
INDEX_URL = 'https://spa1.scrape.center/api/movie?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'

# 网页
TOTAL_PAGE = 10
LIMIT = 10

# PROXIES
PROXIES = {
    # 此部分在v2rayN代理中找到系统代理部分找到对应端口
	'http': '127.0.0.1:10809',
	'https': '127.0.0.1:10809'
}

# MONGO
MONGO_CLIENT_STRING = 'mongodb://localhost:27017'
MONGO_DB = 'spiders'
MONGO_COLLECTION = 'movies'

# 连接数据库
client = pymongo.MongoClient(MONGO_CLIENT_STRING)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# 页面抓取
def scrape_api(url):
    logging.info('scraping %s ...', url)
    try:
        response = requests.get(url, proxies=PROXIES)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occured while scraping %s', url, exc_info=True)

def scrape_index(page):
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