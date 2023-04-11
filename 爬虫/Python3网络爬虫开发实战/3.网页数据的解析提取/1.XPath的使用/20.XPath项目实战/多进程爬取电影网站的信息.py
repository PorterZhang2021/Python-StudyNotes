import re
import json
import logging
import requests
import multiprocessing

from os import makedirs
from os.path import exists
from lxml import etree
from urllib.parse import urljoin

# 用于进行日志的输出
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# Python中通过大写作为常量
# 基本的URL
BASE_URL = 'https://ssr1.scrape.center'
# 需要请求的总页数
TOTAL_PAGE = 10
# 保存的文件夹
RESULTS_DIR = 'result'
# 存在就直接用不存在就构建
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def scrape_page(url):
    """
    用于对整个页面进行爬取
    url:爬取的连接
    return string:返回一个以字符串形式的页面信息
    """
    # 这里的是输出信息，输出的是爬取网站的链接 - 日志输出
    logging.info('scarping %s ...', url)
    # 进行异常捕获操作
    try:
        # 获取响应请求
        response = requests.get(url)
        # 如果状态码正确
        if response.status_code == 200:
            # 输出抓取到的页面
            return response.text
        # 错误情况下的日志输出
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    # 异常情况
    except requests.RequestException:
        # 错误日志
        logging.error('error ocurred while scraping %s', url,
                      exc_info=True)

def scrape_index(page):
    """
    用于爬取列表页
    page: 页面的规律
    return: 调用scrape_page方法直接获取页面
    """
    # 索引链接构建
    index_url = f'{BASE_URL}/page/{page}'
    # 调用爬取页面方法
    return scrape_page(index_url)

def scrape_detail(url):
    """
    详情页的信息获取
    url:详情页的url
    return: 调用scrape_page方法直接获取页面
    """
    return scrape_page(url)

def parse_index(html):
    """
    对列表页面进行解析
    html: 传入html页面的字符串
    return detail_url: 返回要构成详情页的url
    """
    # 获取单个页面的所有url
    # 构建html文件对象
    html = etree.HTML(html)
    # 获取所有的链接
    movie_items = html.xpath('//div[contains(@class, "el-card")]//a[@class="name"]/@href')
    # 如果其为空就返回一个空列表
    if not movie_items:
        return []
    # 输出链接
    for item in movie_items:
        # 进行详情页的url拼接
        detail_url = urljoin(BASE_URL, item)
        # 输出获取的链接
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url

def parse_detail(html):
    # text_html
    txt_html = html
    # 构建html文件对象
    html = etree.HTML(html)

    # 找到上映电影的信息正则表达式
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')

    # 图片的地址
    cover = html.xpath('//img[@class="cover"]/@src') if html.xpath('//img[@class="cover"]/@src') else None
    # 电影的名称
    name = html.xpath('//a/h2/text()')[0] if html.xpath('//a/h2/text()') else None
    # 分类
    categories = html.xpath('//div[@class="categories"]//span/text()') if html.xpath('//div[@class="categories"]//span/text()') else []
    # 电影简介
    drama = html.xpath('//div[@class="drama"]/p/text()')[0].strip() if html.xpath('//div[@class="drama"]/p/text()') else None
    # 获取到匹配到的日期
    published_at = re.search(published_at_pattern, txt_html).group(1) if re.search(published_at_pattern, txt_html) else None
    # 评分
    score = html.xpath('//p[contains(@class, "score")]/text()')[0].strip() if html.xpath('//p[contains(@class, "score")]/text()') else None
    
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

def main(page):

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
    # 创建进程池
    pool = multiprocessing.Pool()
    # 遍历的页码
    pages = range(1, TOTAL_PAGE + 1)
    # 开启多进程
    pool.map(main, pages)
    # 关闭进程
    pool.close()
    pool.join()