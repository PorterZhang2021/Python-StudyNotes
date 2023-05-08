import re
import requests
import logging
import csv

from os import makedirs
from os.path import exists
from bs4 import BeautifulSoup
from urllib.parse import urljoin


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULT_DIR = 'results'

exists(RESULT_DIR) or makedirs(RESULT_DIR)


# 对网页进行爬取
def scrape_page(url):
    logging.info('scraping url: %s ...', url)
    try:
        # 进行请求
        response = requests.get(url=url)
        # 请求结果判断
        if response.status_code == 200:
            # 输出文本内容
            return response.text
        # 错误情况输出
        logging.error('get invaild status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        # 输出错误情况
        logging.error('error occured while scraping %s', url, exc_info=True)

def scrape_index(page):
    # 索引页面
    index_url = f'{BASE_URL}/page/{page}'
    # 进行抓取
    return scrape_page(index_url)

def scrape_detail(url):
    # 抓取页面内容
    return scrape_page(url)

# 对网页数据进行解析
def parse_index(html):
    soup = BeautifulSoup(html, 'lxml')
    # 获取url
    items = soup.find_all(class_='name')
    
    # 如果没有值
    if not items:
        return []
    
    # 存在值
    for item in items:
        # 对链接进行拼接
        detail_url = urljoin(BASE_URL, item['href'])
        # 输出生成的链接
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url

# 对详情网页进行解析
def parse_detail(html):
    soup = BeautifulSoup(html, 'lxml')

    # 标题
    name = soup.find(name="h2").string if soup.find(name="h2") else None
    # 图片
    cover = soup.find(class_='cover')['src'] if soup.find(class_='cover') \
            else None
    # 分类
    categories = []
    # 获取分类
    categories_ele = soup.find(class_='categories')
    # 如果存在
    if categories_ele != -1:
        # 查找内部节点
        for category in categories_ele:
            if category.find('span') != -1:
                category = category.find('span').string
                categories.append(category)
    # 简介
    drama = soup.select('div.drama p')[0].string.strip() if soup.select('div.drama p') \
            else None
    # 上映时间
    published_at = re.compile('(\d{4}-\d{2}-\d{2}) 上映')
    published = re.search(published_at, html).group(1) if re.search(published_at, html) \
                else None
    # 评分
    score = soup.find(class_='score').string.strip() if soup.find(class_='score') \
            else None
    
    return {
        'name': name,
        'cover': cover,
        'published': published,
        'categories': categories,
        'score': score,
        'drama': drama
    }

# 对获取的内容进行存储
# 本次存储使用csv
def save_data(data_path ,data):
    # 初始化字典写入对象
    with open(data_path, 'a+', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'cover', 'published', 'categories', 'score', 'drama']  
        # 初始化一个字典写入对象
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)

# 主函数
def main():
    # 数据存放地址
    data_path = '{0}/movies.csv'.format(RESULT_DIR)
     # 初始化一个写入对象
    with open(data_path, 'w', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'cover', 'published', 'categories', 'score', 'drama']  
        # 初始化一个字典写入对象
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    
    for page_index in range(1, TOTAL_PAGE + 1):
        # 获取列表页
        page_html = scrape_index(page=page_index)
        # 获取详情页的urls
        detail_urls = parse_index(page_html)        
        for detail_url in detail_urls:
            # 抓取详情页内容
            detail_html = scrape_detail(detail_url)
            # 获取数据
            data = parse_detail(detail_html)
            # 获取信息
            logging.info('get detail data %s', data)
            save_data(data=data, data_path=data_path)
            

if __name__ == '__main__':
    main()