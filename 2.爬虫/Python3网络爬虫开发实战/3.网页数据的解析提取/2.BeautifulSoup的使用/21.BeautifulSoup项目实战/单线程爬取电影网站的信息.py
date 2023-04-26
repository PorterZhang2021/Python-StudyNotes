import re
import json
import logging
import requests
import multiprocessing

from os import makedirs
from os.path import exists
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 用于进行日志输出
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# Python中通过大写作为常量
# 基本的URL
BASE_URL = 'https://ssr1.scrape.center'
# 需要请求的总页数
TOTAL_PAGE = 10
# 保存文件夹
RESULTS_DIR = 'results'
# 存在就直接使用不存在就构建
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def scrape_page(url):
    # 进行页面内容的爬取

    # 输出日志
    logging.info('scarping %s ...', url)
    # 进行异常捕获
    try:
        # 获取响应的请求
        response = requests.get(url, verify=False)
        # 如果状态码正确
        if response.status_code == 200:
            # 输出抓取到的页面
            return response.text
        # 错误情况下对日志输出
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    # 异常情况处理
    except requests.RequestException:
        # 错误日志
        logging.error('error ocurred while scraping %s', url,
                      exc_info=True)

def scrape_index(page):
    # 获取列表页
    # 索引链接构建
    index_url = f'{BASE_URL}/page/{page}'
    # 调用爬取页面方法
    return scrape_page(index_url)

def scrape_detail(url):
    # 获取详情页
    return scrape_page(url)

def parse_index(html):
    # 进行列表页的解析
    soup = BeautifulSoup(html, 'html.parser')
    # 获取链接元素列表
    movie_items = soup.find_all(class_="name")
    # 如果这个列表为空那么就返回一个空列表
    if not movie_items:
        return []
    # 进行链接的输出与拼接
    for item in movie_items:
        # 获取href的属性
        href = item['href']
        # 进行详情页的url的拼接
        detail_url = urljoin(BASE_URL, href)
        # 输出获取的链接
        logging.info('get detail url %s', detail_url)
        # 生成器的函数
        yield detail_url

def parse_detail(html):
    
    # 找到上映电影的信息正则表达式
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    soup = BeautifulSoup(html, 'html.parser')
    # 获取图片的地址
    cover = soup.find(class_="cover")['src'] if soup.find(class_="cover")['src'] else None
    # 获取电影的名称
    name_ele = soup.find(name="h2")
    name = name_ele.string if name_ele.string else None
    # 获取分类
    categorie = soup.find(class_='categories')
    spans = categorie.find_all(name="span")
    categories = [ span.string for span in spans ]
    # 获取上映时间
    # 获取到匹配到的日期
    published_at = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    # 获取电影简介
    drama_ele = soup.find(class_="drama") 
    drama = drama_ele.p.string.strip() if drama_ele.p.string.strip() else None
    # 获取评分
    score_ele = soup.find(class_='score')
    score = score_ele.string.strip() if score_ele.string.strip() else None
    
    # 返回获取到的内容
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }

def save_data(data):
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




