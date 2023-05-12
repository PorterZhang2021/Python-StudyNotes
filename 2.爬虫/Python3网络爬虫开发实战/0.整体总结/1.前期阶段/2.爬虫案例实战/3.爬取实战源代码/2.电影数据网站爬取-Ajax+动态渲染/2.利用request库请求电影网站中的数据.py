import csv
import requests
import logging

from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
# 列表索引网址
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
# offset = (page - 1) * 10
# 详情页内容索引网址
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
# 总页面
TOTAL_PAGE = 10
# 存放地址
RESULT_DIR = 'results'

# 是否存在或者创建
exists(RESULT_DIR) or makedirs(RESULT_DIR) 

def scrape_api(url: str) -> dict:
    """
        抓取api当中的内容并以字典格式进行返回
    """
    # 提示抓取某个网页
    logging.info('scraping %s ...', url)
    # 异常捕获
    try:
        # 响应获取
        response = requests.get(url=url)
        # 判断响应是不是200 ok
        if response.status_code == 200:
            # 返回内容为一个字典，这里是将json格式的内容
            # 转化了
            return response.json()
        # 如果不是返回响应的错误码
        logging.error('get an error for scraping %s, this error of status code is %s', url, response.status_code)
    except requests.RequestException as e:
        # 如果出现错误的响应请求直接返回错误信息
        logging.error('get an error about %s', e, exc_info=True)
    

def scrape_index(page: int) -> dict:
    """
    获取到索引网站接口当中的内容，这里的url可以通过逻辑推断出来
    url中limit是恒定不变的10
    offset是(page - 1) * 10
    因此这里参数传入page即可
    """
    index_url = INDEX_URL.format(limit = 10, offset = (page - 1) * 10)
    return scrape_api(index_url)


def scrape_detail(id: int) -> dict:
    """
    由列表页爬取后可以解析获取到id
    而id是我们所需要的获取ajax数据的内容，因此传入id即可
    这里返回的同样是dict格式
    """
    detail_url = DETAIL_URL.format(id=id)
    return scrape_api(detail_url)

# 对api内的内容进行重新整理

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


# 存放在需要的数据库中
# 选择使用csv进行数据的保存
def save_data(data_path: str, data: dict) -> None:
    """
    传入参数：传入数据存储地址，数据
    任务目标：将数据按行写入
    逻辑步骤：
    1. 打开构建好的文件，直接按行将data值写入即可
    返回结果：无
    """
    # 创建上下文管理器
    with open(data_path, 'a+', encoding='utf-8') as file:
        # 构建一个字典key值对象
        field_name = ['name', 'cover', 'published_at', 'categories', 'score', 'drama']
        # 创建一个csv的字典写入头
        writer = csv.DictWriter(file, fieldnames=field_name)
        # 按行写入数据
        writer.writerow(data)


# 进行整体的爬取操作
def main():
    # 文件头部写入
    # 创建一个文件地址并写入文件头部
    data_path = '{0}/results.csv'.format(RESULT_DIR)
    # 上下文管理器
    with open(data_path, 'w', encoding='utf-8') as file:
        # 构建一个字典key值对象
        field_name = ['name', 'cover', 'published_at', 'categories', 'score', 'drama']
        # 创建一个csv的字典写入头
        writer = csv.DictWriter(file, fieldnames=field_name)
        # 将头写入
        writer.writeheader()

    # 进行网站内容的爬取
    for page in range(1, TOTAL_PAGE + 1):
        # 抓取api当中的数据
        index_response_result = scrape_index(page=page)
        # 解析api中的数据获取到ids
        ids = handle_index(response_result=index_response_result)
        # 进行详情页内容的获取与抓取
        for id in ids:
            # 抓取detail_api中的数据
            detail_response_result = scrape_detail(id=id)
            # 解析数据并输出查看
            data = handle_detail(response_result=detail_response_result)
            logging.info('get data %s', data)
            # 将数据写入
            save_data(data_path=data_path, data=data)

if __name__ == '__main__':
    main()