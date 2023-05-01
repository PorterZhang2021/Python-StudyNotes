import json
import re
import requests
import logging

from os import makedirs
from os.path import exists
from lxml import etree
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULT_DIR = 'results'

exists(RESULT_DIR) or makedirs(RESULT_DIR)


# 网页内容的爬取

# 网页爬取
def scrape_page(url):
    logging.info('scraping url: %s', url)
    # 进行异常操作
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occured while scraping %s', url, exc_info=True)

# 爬取列表页
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


# 爬取详情页
def scrape_detail(url):
    return scrape_page(url)


# 网页内容的解析

# 解析列表页
def parse_index(html_str):
    html = etree.HTML(html_str)
    # 解析获取需要的内容
    items = html.xpath('//a[@class="name"]/@href')
    if not items:
        return []
    for item in items:
        # 进行链接的拼接
        detail_url = urljoin(BASE_URL, item)
        # 输出生成的链接信息
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url


# 解析详情页
def parse_detail(html_str, index):
    html = etree.HTML(html_str)

    # 电影标题
    name = html.xpath('//h2[@class="m-b-sm"]/text()')[0] if html.xpath('//h2[@class="m-b-sm"]/text()') \
            else None
    # 电影图片URL
    cover = html.xpath('//img[@class="cover"]/@src')[0] if html.xpath('//img[@class="cover"]/@src') \
            else None
    # 电影上映时间
    published_at = re.compile('(\d{4}-\d{2}-\d{2}) 上映')
    published = re.search(published_at, html_str).group(1) if re.search(published_at, html_str) \
                else None
    # 电影分类
    categories = html.xpath('//button[contains(@class, "category")]/span/text()') \
                if html.xpath('//button[contains(@class, "category")]/span/text()') \
                else None
    # 电影评分
    score = html.xpath('//p[contains(@class, "score")]/text()')[0] \
            if html.xpath('//p[contains(@class, "score")]/text()') \
            else None
    # 电影剧情简介
    drama = html.xpath('//div[contains(@class, "drama")]/p/text()')[0] \
            if html.xpath('//div[contains(@class, "drama")]/p/text()') \
            else None
    
    # 以字典形式返回所需要的内容
    return {
        'index': index,
        'name': name,
        'cover': cover,
        'published': published,
        'categories': categories,
        'drama': drama.strip(),
        'score': score.strip()
    }

# 存储获取到的数据

# 以json文件的方式进行存储
def save_data(data):
    data_path = '{0}/movies.json'.format(RESULT_DIR)

    # 创建一个进行内容的存放
    with open(data_path, 'a+', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write(',')
        file.write('\n')
        
# 主函数
def main():
    index = 0
    for page_index in range(1, TOTAL_PAGE + 1):
        # 获取列表页
        page_html = scrape_index(page=page_index)
        # 获取详情页
        detail_urls = parse_index(page_html)
        for detail_url in detail_urls:
            index += 1
            # 抓取详情页内容
            detail_html = scrape_detail(detail_url)
            # 获取数据
            data = parse_detail(detail_html, index)
            # 获取信息
            logging.info('get detail data %s', data)
            save_data(data=data)


if __name__ == '__main__':
    main()
