import json
import logging
import pymongo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 日志设置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
# 常量
# 网址相关
# 索引页网址
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
# 详情页网址
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
# 总页数
TOTAL_PAGE = 10

# mongodb相关
# mongodb地址
MONGODB_CONNECT_STRING = 'mongodb://localhost:27017'
# mongodb数据库
MONGODB_DB = 'spiders'
# mongodb集合
MONGODB_COLLECTION = 'movies'

# 自动化设定
# 超时时间
TIME_OUT = 10

# api信息抓取
# api信息抓取函数
def scrape_api(browser, wait, url, condition, locator):
    """
    任务目标: 获取api当中的数据
    传入参数: 浏览器要访问的url, 情况condition，加载信息locator
    逻辑分析:
    1. 判断返回之后的状态 如果状态正确则获取我们所需要的数据
    返回结果: 无 这里直接是一个自动化网页
    """
    # 日志显示抓取的网页
    logging.info('scraping %s ...', url)
    # 异常捕获操作
    try:
        # 尝试进入网页
        # 设置浏览器地址
        browser.get(url=url)
        # 等待操作
        wait.until(condition(locator))
    # 没有进入成功就返回超时操作
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)
# 索引页面api信息抓取
def scrape_index(browser, wait, page):
    """
    任务目标：获取索引页面的api数据
    传入参数：页面page
    逻辑分析：
    1. 获取url链接
    2. 进行数据的抓取
    返回结果：无
    """
    # 页面网址
    index_url = INDEX_URL.format(limit=10, offset=(page-1)*10)
    return scrape_api(browser=browser, wait=wait, 
                      url=index_url, condition=EC.visibility_of_all_elements_located,
                      locator=(By.CSS_SELECTOR, 'body'))
# 详情页面api信息抓取
def scrape_detail(browser, wait, id):
    """
    任务目标：获取详情页面的api数据
    传入参数：详情页id
    逻辑分析：
    1. 获取url链接
    2. 进行数据的抓取
    返回结果：无
    """
    # 页面网址
    detail_url = DETAIL_URL.format(id=id)
    return scrape_api(browser=browser, wait=wait,
                      url=detail_url, condition=EC.visibility_of_all_elements_located,
                      locator=(By.CSS_SELECTOR, 'body'))

# api数据解析
# 获取解析数据
def parse_json(browser) -> dict:
    """
    任务目标：解析访问页面后的json元素
    传入参数：无
    逻辑分析：
    1. 获取json数据存在的标签元素的文本
    2. 将获取的json数据转换成字典格式
    返回结果
    """
    pre = browser.find_element(by=By.TAG_NAME, value='pre').text
    # 转换数据
    pre_dict = json.loads(pre)
    return pre_dict

# 解析索引页内的内容
def handle_index(response_result: dict) -> list:
    """
    传入参数：dict格式的响应请求
    任务目标：获取到我们所需要的id，并构成列表
    逻辑步骤：
    1. 分析dict格式响应请求后发现由count与results两部分
        我们需要的就是results部分中的id内容，results本身
        为一个列表，嵌套了一堆字典数据
    2. 利用循环获取列表中的字典数据
    3. 将字典数据中的id获取并存放在我们构建的ids列表中
    返回结果：返回一个名叫ids的列表
    """
    # 创建一个ids的列表
    ids = []
    # 获取results部分
    movie_results = response_result['results']
    # 进行id的提取
    for movie in movie_results:
        # 判断字典中是否由id这个键
        if movie.__contains__('id'):
            # 存放id值
            ids.append(movie['id'])
    # 返回ids列表数据
    return ids


def handle_detail(response_result: dict) -> dict:
    """
    传入参数：传入响应请求的dict内容
    任务目标：获取到我们所需要抓取的内容
    1. 电影标题 name 
    2. 电影图片url cover
    3. 电影上映时间 published_at
    4. 电影分类 categories
    5. 电影评分 score
    6. 剧情简介 drama
    详细步骤：
    1. 分析响应返回请求发现字典可以直接提取我们所需要的内容，
        因此这里对字典当中的内容做好风险判断即可
    返回结果：
    返回一个存放我们所需要的值的字典
    """
    # 电影标题获取
    name = response_result.get('name', None)
    # 电影图片url获取
    cover = response_result.get('cover', None)
    # 电影上映时间获取
    published_at = response_result.get('published_at', None)
    # 电影分类内容获取
    categories = response_result.get('categories', [])
    # 电影评分获取
    score = response_result.get('score', None)
    # 电影剧情简介
    drama = response_result.get('drama', None)
    
    # 返回获取到的值
    return {
        # 电影标题
        'name': name,
        # 电影图片url
        'cover': cover,
        # 电影上映时间
        'published_at': published_at,
        # 电影分类内容
        'categories': categories,
        # 电影评分内容
        'score': score,
        # 电影剧情简介
        'drama': drama
    }

# 数据获取存储
# 利用mongoDB存储我们所需要的内容
def save_data(collection, data):
    collection.insert_one(data)

# 主函数
def main():
    # 无头模式
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # 设定使用的浏览器
    browser = webdriver.Chrome(options=options)
    # 浏览器等待
    wait = WebDriverWait(browser, TIME_OUT)


    # 数据库连接
    mongdb_client = pymongo.MongoClient(MONGODB_CONNECT_STRING)
    mongdb_db = mongdb_client[MONGODB_DB]
    mongdb_collection = mongdb_db[MONGODB_COLLECTION]

    # 进行网站内容的爬取
    for page in range(1, TOTAL_PAGE + 1):
        # 抓取api当中的数据
        scrape_index(browser=browser, wait=wait, page=page)
        index_response_results = parse_json(browser=browser)
        # 解析api中的数据
        ids = handle_index(response_result=index_response_results)
        # 进行详情页内容的获取与抓取
        for id in ids:
            # 抓取detail_api中的数据
            scrape_detail(browser=browser, wait=wait, id=id)
            detail_response_results = parse_json(browser=browser)
            # 解析数据并输出查看
            data = handle_detail(response_result=detail_response_results)
            logging.info('get data %s', data)
            # 数据保存
            save_data(collection=mongdb_collection, data=data)

# 主函数的数据获取
if __name__ == '__main__':
    main()