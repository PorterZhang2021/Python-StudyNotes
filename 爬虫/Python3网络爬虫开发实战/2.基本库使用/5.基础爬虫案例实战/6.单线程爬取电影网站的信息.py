import requests
import logging
import re
import json

from urllib.parse import urljoin
from os import makedirs
from os.path import exists

# logging用于进行日志输出
# 这里定义了日志输出级别和输出格式
# 这里的输出格式 因为多加了一个% 导致出现了错误
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# python当中大写通常作为常量
# 基本的URL
BASE_URL = 'https://ssr1.scrape.center'
# 需要请求的总页数
TOTAL_PAGE = 10
# 保存的文件夹
RESULTS_DIR = 'results'
# 存在用不存在就构建
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def scrape_page(url):
    """
    页面爬取方法，因为我们要爬取列表页还要爬取详情页，所以定义了一个比较通用的爬取页面方法
    url: 要爬取的链接
    return string: 返回一个页面信息以字符串的形式返回
    """
    # 这里的是输出信息，输出的是爬取的网页链接
    logging.info('scraping %s...', url)
    # 异常捕获操作
    try:
        # 获取请求响应
        response = requests.get(url)
        # 如果状态码正确
        if response.status_code == 200:
            # 输出响应后的页面即抓取到的页面
            return response.text
        # 这里的请求日志 说明如果输出的是其他情况下的响应 返回一个日志报错
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    # 这里出现请求的异常
    except requests.RequestException:
        # 这里的错误日志 是当请求异常时，返回出请求异常的信息
        logging.error('error ocurred while scraping %s', url,
                      exc_info=True)


def scrape_index(page):
    """
    定义列表页的爬取方法,此方法主要爬取一个页面
    这里内容其实并不多，但是为了减少耦合或者原子化，
    将此单独设置成了一个函数，此函数内主要完成的就是url的拼接
    然后调用爬取页面方法
    page: 相关页面的更换逻辑
    return :这里的返回直接调用了爬取页面的方法
    """
    # 索引链接构建
    index_url = f'{BASE_URL}/page/{page}'
    # 调用爬取页面方法
    return scrape_page(index_url)


def parse_index(html):
    """
    此方法主要分析一页当中的列表中的详情页
    html: 传入html页面的字符串
    return detail_url: 返回要构成的详情页url
    这里生成器函数的好处是我最终会在生成器停顿的地方，自动收集url链接
    它以一种列表的形式返回，这种方式很神奇。
    """
    # 构建一个正则表达式
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    # 查找到所有满足正则表达式的字符串
    items = re.findall(pattern, html)
    # 如果其为空，那么就返回一个空列表
    if not items:
        return []
    # 对获取到的列表进行遍历
    for item in items:
        # 进行详情页的url拼接
        detail_url = urljoin(BASE_URL, item)
        # 输出获取的的详情页url链接
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url


def scrape_detail(url):
    """
    获取详情页的html文档
    """
    return scrape_page(url)


def parse_detail(html):
    # 找到图片的地址的正则表达式
    cover_pattern = re.compile(
        'class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    # 找到电影名的正则表达式
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    # 找到分类的正则表达式
    categories_pattern = re.compile(
        '<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    # 找到上映电影的信息正则表达式
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    # 找到电影简介正则表达式
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    # 找到评分的正则表达式
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)

    # 获取到匹配到的对象
    # 获取到匹配到的图片
    cover = re.search(cover_pattern, html).group(
        1).strip() if re.search(cover_pattern, html) else None
    # 获取到匹配到的电影名
    name = re.search(name_pattern, html).group(
        1).strip() if re.search(name_pattern, html) else None
    # 获取到匹配到的电影分类
    categories = re.findall(categories_pattern, html) if re.findall(
        categories_pattern, html) else []
    # 获取到匹配到的日期
    published_at = re.search(published_at_pattern, html).group(
        1) if re.search(published_at_pattern, html) else None
    # 获取到匹配到的描述信息
    drama = re.search(drama_pattern, html).group(
        1).strip() if re.search(drama_pattern, html) else None
    # 获取到匹配到的分数信息
    score = float(re.search(score_pattern, html).group(1).strip()
                  if re.search(score_pattern, html) else None)

    #  返回获取到的相关内容
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
