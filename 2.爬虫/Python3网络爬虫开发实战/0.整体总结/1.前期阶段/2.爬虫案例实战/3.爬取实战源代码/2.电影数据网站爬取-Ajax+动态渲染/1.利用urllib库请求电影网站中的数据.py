import json
import logging
import urllib.error
from os import makedirs
from os.path import exists
from urllib.request import urlopen

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量与规律
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
LIMIT = 10
TOTAL_PAGE = 10
# offset = (page - 1) * 10
RESULT_DIR = 'results'

# 存在放前面 
exists(RESULT_DIR) or makedirs(RESULT_DIR)

# 进行数据的获取
# 获取api中的数据
def scrape_api(url):
    # 网页抓取
    logging.info('scraping %s ...', url)
    # 异常捕获
    try:
        # 响应
        response = urlopen(url)
        # 响应状态
        if response.status == 200:
            # 获取请求结果
            response_text = response.read()
            # json格式转字典
            response_result = json.loads(response_text)
            # 返回响应结果
            return response_result
        
        logging.error('get invalid status code %s while scraping %s',
                      response.status, url)
    except urllib.error.HTTPError as e:
        logging.error('error occured while scraping %s', url, exc_info=True)

# 获取列表页面中的数据
def scrape_index(page):
    index_url = INDEX_URL.format(limit=LIMIT, offset=(page - 1)*LIMIT)
    return scrape_api(index_url)

# 获取详情页面中的数据
def scrape_detail(id):
    detail_url = DETAIL_URL.format(id=id)
    # 获取详情页中的数据
    return scrape_api(detail_url)

# 进行数据处理
def handle_index(result):
    # 获取到响应请求数据
    response_result = result['results']
    ids = []
    for movie in response_result:
        # 这里判断是否具有id值
        if movie.__contains__('id'):
            ids.append(movie['id'])
    return ids

def handle_detail(result):
    # 获取到响应请求数据
    # 标题
    name = result.get('name', '')
    # 图片
    cover = result.get('cover', '')
    # 分类
    categories = result.get('categories', '')
    # 分数
    score = result.get('score', '')
    # 上映时间
    published_at = result.get('published_at', '')
    # 简介
    drama = result.get('drama', '')

    # 返回字典信息
    return {
        # 标题
        'name': name,
        # 图片
        'cover': cover,
        # 分类
        'categories': categories,
        # 分数
        'score': score,
        # 上映时间
        'published_at': published_at,
        # 简介
        'drama': drama
    }

# 进行数据的存储 - txt格式
def save_data(data):
    # 存放地址
    data_path = '{0}/movies.txt'.format(RESULT_DIR)
    # 进行存放
    with open(data_path, 'a+', encoding='utf-8') as file:
        file.write('电影名称:' + str(data['name']) + '\n')
        file.write('电影图片:' + str(data['cover']) + '\n')
        file.write('剧情分类:' + str(data['categories']) + '\n')
        file.write('分数:' + str(data['score']) + '\n')
        file.write('上映时间:' + str(data['published_at']) + '\n')
        file.write('剧情简介:' + str(data['drama'])+ '\n')
        file.write('=' * 50 + '\n')

def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_response_result = scrape_index(page)
        ids = handle_index(index_response_result)
        for id in ids:
            detail_response_result = scrape_detail(id)
            data = handle_detail(detail_response_result)
            logging.info('get data: %s', data)
            save_data(data)


if __name__ == '__main__':
    main()