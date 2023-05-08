import re
import logging
import pymongo

from parsel import Selector
from urllib.request import urlopen
from urllib.parse import urljoin


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10

# MONGO
# 链接地址
MONGO_CLIENT_STRING = 'mongodb://localhost:27017'
# 链接数据库
MONGO_DB = 'spiders'
# 链接集合
MONGO_COLLECTION = 'movies'

# 数据库连接与配置
client = pymongo.MongoClient(MONGO_CLIENT_STRING)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# 进行页面的抓取
# 构建一个抓取页面的函数
def scrape_page(url):
    logging.info('scraping %s ...', url)
    # 异常捕获操作
    try:
        # 进行请求
        response = urlopen(url=url)
        # 判断请求码
        if response.status == 200:
            # 输出网页内容
            return response.read().decode('utf-8')
        # 错误请求
        logging.error('get invaild status code %s while scraping %s',
                      response.status, url)
    except:
        # 错误请求
        logging.error('error occured while scraping %s', url, exc_info=True)

# 获取列表页网页
def scarpe_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

# 获取详情页网页
def scrape_detail(url):
    return scrape_page(url=url)

# 进行页面的解析

# 获取列表页的数据
def parse_index(html):
    selector = Selector(html)
    items = selector.css('a.name::attr(href)').getall()
    
    if not items:
        return []

    for item in items:
        # 对链接进行拼接
        detail_url = urljoin(BASE_URL, item)
        # 输出生成的链接
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url


# 获取详情页的数据
def parse_detail(html):
    selector = Selector(text=html)

    # 标题
    name = selector.xpath('//h2[@class="m-b-sm"]/text()').get() if selector.xpath('//h2[@class="m-b-sm"]/text()').get() else None
    # 图片
    cover = selector.css('img.cover::attr(src)').get() if selector.css('img.cover::attr(src)').get() else None
    # 分类
    categories = selector.xpath('//button[contains(@class,"category")]/span/text()').getall() \
                if selector.xpath('//button[contains(@class,"category")]/span/text()').getall() \
                else None
    # 简介
    drama = selector.xpath('//div[@class="drama"]/p/text()').get().strip() \
            if selector.xpath('//div[@class="drama"]/p/text()').get() \
            else None
    # 出版日期
    published_at = re.compile('(\d{4}-\d{2}-\d{2}) 上映')
    published = re.search(published_at, html).group(1) if re.search(published_at, html) \
                else None
    # 分数
    score = selector.xpath('//p[contains(@class, "score")]/text()').get().strip() \
            if selector.xpath('//p[contains(@class, "score")]/text()').get() \
            else None
    
    return {
        'name': name,
        'cover': cover,
        'categories': categories,
        'drama': drama,
        'published': published,
        'score': score
    }

# 进行数据内容的存储
# 使用MongoDB进行数据存储
def save_data(data):
    collection.update_one(
        {'name': data.get('name')},
        {'$set': data},
        upsert=True
    )

# 主函数
def main():
    for page in range(1, TOTAL_PAGE + 1):
        # 抓取详情页
        index_html = scarpe_index(page)
        # 获取urls
        detail_urls = parse_index(index_html)
        # 抓取每个详情页里面的内容
        for detail_url in detail_urls:
            # 获取详情页内容
            detail_html = scrape_detail(detail_url)
            # 解析详情页内容获取数据
            data = parse_detail(detail_html)
            # 将最终的数据输出
            logging.info('get detail data %s', data)
            # 保存数据
            save_data(data=data)

if __name__ == '__main__':
    main()