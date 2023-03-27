import requests
import logging
import re
from urllib.parse import urljoin

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


# 爬取详情页
"""
详情页中要获取的内容：
1. 封面：是一个img节点，其属性为cover
2. 名称：是一个h2节点，其内容是电影名称
3. 类别：是span节点，其中内容是电影类别 span的节点外侧是button节点，再外侧是class为categories的div节点
4. 上映时间：是span节点，其内容包含上映时间，外侧是class为info的div节点，提取出时间即可
5. 评分：是一个p节点，其内容为电影评分，p节点的class属性为score
6. 剧情简介：是一个p节点，其内容为剧情简介，外侧是class为drama的div节点
"""

def scrape_detail(url):
    """
    抓取我所需要的详情页，
    最终返回的是一个html的string类型的变量
    """
    return scrape_page(url)

def parse_detail(html):
    """
    用于处理详情页中的内容信息
    html: 传入一个string类型的html页面
    return dict: 按我所需的部分直接写入字典
    """

    # 构建正则表达式
    # 构建图片的正则表达式
    img_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    # 构建名称的正则表达式
    title_pattern = re.compile('<h2.*?>(.*?)</h2>')
    # 构建类别的正则表达式
    categories_pattern = re.compile('category.*?<span>(.*?)</span>', re.S)
    # 构架上映时间的正则表达式
    time_pattern = re.compile('<span.*?>(\d{4}-\d{2}-\d{2}) 上映</span>')
    # 构建评分的正则表达式
    score_pattern = re.compile('<p.*?class="score.*?">(.*?)</p>', re.S)
    # 构建剧情简介表达式
    description_pattern = re.compile('class="drama".*?<p.*?>(.*?)</p>', re.S)

    # 搜索所需要的内容
    # 进行解析获取验证
    # 验证图片是否能够解析获取到
    img_match = re.search(pattern=img_pattern, string=html)
    # 获取到图片的url
    img= img_match.group(1)
    # 验证名称是否能够获取到
    title_match = re.search(pattern=title_pattern, string=html)
    # 获取所需要的标题
    title = title_match.group(1)   
    # 验证所需要的类别是否能够获取到
    categories_match = re.findall(pattern=categories_pattern, string=html)
    categories_list = categories_match
    # 验证上映时间是否能够获取到
    time_match = re.search(pattern=time_pattern, string=html)
    # 如果没有上映时间 则没有
    if time_match:
        time = time_match.group(1)
    else:
        time = '暂无'
    # 验证评分表达式是否能够获取
    score_match = re.search(pattern=score_pattern, string=html)
    score = float(score_match.group(1))
    # 验证剧情简介的表达式
    description_match = re.search(pattern=description_pattern, string=html)
    # 获取字符串后对字符串进行处理
    need_handle_description = description_match.group(1)
    # 这里的操作是截掉左边会出现的空格
    description = need_handle_description.strip()

    # 将获取到的内容返回
    detail_dict = {
        'img': img,
        'title': title,
        'categories': categories_list,
        'time': time,
        'score': score,
        'description': description
    }

    return detail_dict



def main():
    # 进行页面的循环
    for page in range(1, TOTAL_PAGE + 1):
        # 抓取列表页
        index_html = scrape_index(page)
        # 解析获取url
        detail_urls = parse_index(index_html)
        # # 输出获取的url信息
        # logging.info('detail urls %s', list(detail_urls))
        for detail_url in detail_urls:
            # 抓取详情页
            detail_html = scrape_detail(detail_url)
            # 解析获取数据
            detail_data_list = parse_detail(detail_html)
            print(detail_data_list)
            

        
    


if __name__ == '__main__':
    main()



