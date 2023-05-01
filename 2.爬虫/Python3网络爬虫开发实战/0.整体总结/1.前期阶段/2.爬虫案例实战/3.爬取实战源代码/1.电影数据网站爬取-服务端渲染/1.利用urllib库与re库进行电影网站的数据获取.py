import urllib
import urllib.error
from os import makedirs
from os.path import exists
from urllib.request import urlopen
from urllib.parse import urljoin


import re
import logging


# logging用于进行日志输出
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
# 基本URL
BASE_URL = 'https://ssr1.scrape.center'
# 需要请求的总页数
TOTAL_PAGE = 10
# 文件夹
RESULTS_DIR = 'RESULTS'
# 索引
index = 0

# 存放OS文件
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# 完成对网页内容的爬取

# 构建一个基本的函数用于网页的爬取
def scarpe_page(url):
    # 进行爬取网页链接的输出
    logging.info('scraping %s ...', url)
    # 异常捕获操作
    try:
        # 尝试打开网页内容
        response = urlopen(url)
        # 如果页面返回代码为200
        if response.status == 200:
            # 输出网页的内容
            return response.read().decode('utf-8')
        # 日志请求
        logging.error('get invalid status code %s while scraping %s',
                      response.status, url)
    except urllib.error.HTTPError as e:
        # 输出错误
        logging.error('error ocurred while scraping %s', url, exc_info=True)

# 构建一个函数用于爬取列表页
def scrape_index(page):
    # 列表页的索引
    index_url = f'{BASE_URL}/page/{page}'
    # 调用爬取页面
    return scarpe_page(url=index_url)

# 构建一个函数用于爬取详情页
def scrape_detail(url):
    return scarpe_page(url=url)

# 完成对网页内容的解析

# 解析列表页网页
def parse_index(html):
    # 正则表达式
    # 构建正则表达式
    pattern = re.compile('a.*?href="(.*?)" class="name"')
    # 查找所有满足正则表达式的字符串
    items = re.findall(pattern, html)
    # 如果为空就返回一个空列表
    if not items:
        return []
    # 获取详情页
    for item in items:
        # 进行详情页的url拼接
        detail_url = urljoin(BASE_URL, item)
        # 输出生成的链接信息
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url

# 解析详情页网页
def parse_detail(html):
    global index

    # 构建正则表达式
    # 电影标题
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    # 电影图片url
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    # 电影上映时间
    published_at = re.compile('(\d{4}-\d{2}-\d{2}) 上映')
    # 电影分类
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    # 电影评分
    score_pattern = re.compile('score.*?>(.*?)</p>', re.S)
    # 电影剧情简介
    drama_pattern = re.compile('drama.*?<p.*?>(.*?)</p></div>', re.S)

    # 获取需要的解析数据
    name = re.search(name_pattern, html).group(1) if re.search(name_pattern, html) \
            else None
    cover = re.search(cover_pattern, html).group(1) if re.search(cover_pattern, html) \
            else None
    published = re.search(published_at, html).group(1) if re.search(published_at, html) \
            else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) \
            else []
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) \
            else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) \
            else None
    
    # 以字典形式输出解析数据
    return {
        # 索引
        'index': index,
        # 电影标题
        'name': name,
        # 图片地址
        'cover': cover,
        # 出版日期
        'published': published,
        # 分类
        'categories': categories,
        # 剧情简介
        'drama': drama,
        # 分数
        'score': score
    }


# 完成对网页内容的存储
# 本次存储使用txt进行文件内容的存储
def save_data(data):
    data_path = '{0}/movies.txt'.format(RESULTS_DIR)
    

    # 创建一个文件
    with open(data_path, 'a+', encoding='utf-8') as file:
        # 内部直接进行索引的自增并不会做到文件的自增
        file.write('索引:{0}\n'.format(data.get('index')))
        file.write('名称:{0}\n'.format(data.get('name')))
        file.write('类别:{0}\n'.format(data.get('categories')))
        file.write('图片地址:{0}\n'.format(data.get('cover')))
        file.write('出版日期:{0}\n'.format(data.get('published')))
        file.write('剧情简介:{0}\n'.format(data.get('drama')))
        file.write('评分:{0}\n'.format(data.get('score')))
        file.write(f'{"=" * 50}\n')
        


def main():
    global index

    # 对网页进行测试
    for page_index in range(1, TOTAL_PAGE + 1):
        page = scrape_index(page=page_index)
        # 获取url解析
        detail_urls = parse_index(page)
        for detail_url in detail_urls:
            index += 1
            # 获取页面内容
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info('get detail data %s', data)
            save_data(data=data)

if __name__ == '__main__':
    main()
