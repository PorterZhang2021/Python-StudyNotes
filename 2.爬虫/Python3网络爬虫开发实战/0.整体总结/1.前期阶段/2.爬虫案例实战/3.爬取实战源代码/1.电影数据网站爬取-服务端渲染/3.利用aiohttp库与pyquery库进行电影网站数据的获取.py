import re
import aiohttp
import asyncio
import logging

from os import makedirs
from os.path import exists
from pyquery import PyQuery as pq
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
BASE_URL = 'https://ssr1.scrape.center/'
TOTAL_PAGE = 10

# 通信量
CONCURRENCY = 5

# 建立异步通信量
sempahore = asyncio.Semaphore(CONCURRENCY)
session = None

# 进行网页数据的抓取

# 设计网页的抓取函数
async def scrape_page(url):
    try:
        logging.info('scraping %s ...', url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                if response.status == 200:
                    return await response.text()
                logging.error('get invalid status code %s while scraping %s',
                            response.status, url)        
    except  aiohttp.ClientResponseError:
        logging.error('error occured while scraping %s', url, exc_info=True)

# 设计列表页的抓取
async def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return await scrape_page(index_url)

# 设计详情页的抓取
async def scrape_detail(url):
    return await scrape_page(url=url)

# 进行网页数据的解析

# 进行列表页的数据解析
async def parse_index(html, results):
    # 创建解析对象
    doc = pq(html)
    # 获取所有的标签节点
    name_of_a = doc('a.name')
    # 如果没有值那么就返回空
    if not name_of_a:
        return
    
    # 将标签节点的url组合
    for item in name_of_a.items():
        detail_url = urljoin(BASE_URL, item)
        # 输出信息
        logging.info('get detail url %s', detail_url)
        # 生成器输出
        await results.append(detail_url)

# 异步数据存储
# 异步存储在文件夹中
async def save_data(data):
    logging.info('saving data %s', data)
    await with open('')

# 进行详情页的数据解析
async def parse_detail(html):
    doc = pq(html)
    # 标题内容获取
    name = doc('h2.m-b-sm').text() if doc('h2.m-b-sm') else None
    # 图片url获取
    cover = doc('img.cover').attr.src if doc('img.cover') else None
    # 分类获取
    categories = []
    items = doc('button.category').children()
    for item in items.items():
        categories.append(item.text())
    # 上映时间获取
    published_at = re.compile('(\d{4}-\d{2}-\d{2}) 上映')
    published = re.search(published_at, html).group(1) if re.search(published_at, html) \
                else None
    # 评分获取
    score = doc('p.score').text() if doc('p.score') else None
    # 剧情简介获取
    drama = doc('div.drama').find('p').text() if doc('div.drama').find('p') \
            else None
    
    return {
        'name': name,
        'cover': cover,
        'categories': categories,
        'published': published,
        'score': score,
        'drama': drama
    }


# 异步主函数
async def main():
    global session
    # 获取session
    session = aiohttp.ClientSession()
    # 构建页面抓取任务
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, TOTAL_PAGE + 1)]
    # 获取异步抓取后的URL信息
    html_result = await asyncio.gather(*scrape_index_tasks)
    index_html_results = []
    for index_html in html_result:
        if not index_html: 
            continue
        else:
            index_html_results.append(index_html)