import re
import logging
import requests
import json

from pyquery import PyQuery as pq
from os import makedirs
from os.path import exists
from urllib.parse import urljoin

# 进行日志的输出
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
# 基本网页地址
BASE_URL = 'https://ssr1.scrape.center'
# 网页爬取的总页数
TOTAL_PAGE = 10
# 保存文件夹名
RESULTS_DIR = 'results'

# 如果存在文件夹就不创建，不存在就创建
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

proxies = {
    # 此部分在v2rayN代理中找到系统代理部分找到对应端口
	'http': '127.0.0.1:10809',
	'https': '127.0.0.1:10809'
}

def scrape_page(url):
    # 日志输出
    logging.info('scraping %s ...', url)

    # 爬取页面
    try:
        # 获取响应请求
        res = requests.get(url=url, proxies=proxies)
        # 状态码
        if res.status_code == 200:
            # 返回抓取到的页面
            return res.text
        # 错误情况日志输出
        logging.error('get invalid status code %s while scraping %s',
                      res.status_code, url)
    except requests.RequestException:
        # 错误日志
        logging.error('error occured while scraping %s', url, exc_info=True)

def scrape_index(page):
    # 索引构建
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

def scrape_detail(url):
    # 获取详情页
    return scrape_page(url)

def parse_index(html):
    # 进行列表页的解析
    doc = pq(html)
    # 获取链接元素
    move_items = doc('a.name').items()
    # 如果为空则返回空
    if not move_items:
        return []
    # 输出链接并进行拼接
    for item in move_items:
        # 获取链接属性
        href = item.attr('href')
        # 进行链接的凭借
        detail_url = urljoin(BASE_URL, href)
        # 输出获取的链接
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url

def parse_detail(html):
    # 找到上映电影的信息正则表达式
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    # 获取PyQuery对象
    doc = pq(html)

    # 获取图片的地址
    cover = doc('img.cover').attr('src') if doc('img.cover').attr('src') else None
    # 获取电影名称
    name = doc('h2.m-b-sm').text() if doc('h2.m-b-sm').text() else None
    # 获取分类
    categories_span = doc('div.categories').find('span').items()
    categories = [categorie.text() for categorie in categories_span]
    # 获取到匹配到的日期
    published_at = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    # 获取电影简介
    drama = doc('div.drama').find('p').text() if doc('div.drama').find('p').text() else None
    # 获取评分
    score = doc('p.score').text() if doc('p.score').text() else None

    # 返回获取的内容
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }

def save_data(data):
    # 数据的保存
    # 获取名字
    name = data.get('name')
    name = name.split('-')[0]
    # 数据存放地址
    data_path = '{0}/{1}.json'.format(RESULTS_DIR, name.strip())
    # 以json的格式将数据保存
    json.dump(data, open(data_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)

def main():
    # 进行页面的循环
    for page in range(1, TOTAL_PAGE + 1):
        # 抓取列表页
        index_html = scrape_index(page)
        # 解析构建好的内容详情页的url
        detail_urls = parse_index(index_html)
        # 循环遍历构建好的详情页url
        for detail_url in detail_urls:
            # 爬取详情页的html
            detail_html = scrape_detail(detail_url)
            # 解析详情页中的数据
            data = parse_detail(detail_html)
            # 日志输出
            logging.info('get detail data %s', data)
            # 将文件保存为json
            logging.info('saving data to json file')
            # 保存数据
            save_data(data)
            # 输出保存成功
            logging.info('data saved successfully')


if __name__ == '__main__':
    main()