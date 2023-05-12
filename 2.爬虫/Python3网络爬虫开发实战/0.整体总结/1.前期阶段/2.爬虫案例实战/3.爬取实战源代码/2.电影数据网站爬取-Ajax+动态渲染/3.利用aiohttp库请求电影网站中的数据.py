import asyncio
import aiohttp
import aiofiles
import logging
import json

from os import makedirs
from os.path import exists

# 日志信息设置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
# 索引网页
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
# 详情页网页
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
# 总页数
TOTAL_PAGE = 10
# 文件夹
RESULT_DIR = 'results'
# 通信量
CONCURRENCY = 5

exists(RESULT_DIR) or makedirs(RESULT_DIR)

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

# 数据抓取
# api数据抓取
async def scrape_api(url: str) -> dict:
    """
    传入参数：传入url链接
    任务目标：获取到请求的数据
    逻辑步骤：
    1. 构建异步请求的session
    2. 通过session来进行网页的请求访问
    3. 判断访问的的代码是不是200
        如果是200就返回json数据
    4. 不是的话就直接结束
    返回结果：最终返回结果最好为一个dict格式的对象
    """
    # 日志消息
    logging.info('scraping %s ...', url)
    # 异常捕获操作
    try:
        # 进行请求操作
        async with session.get(url=url) as response:
            # 查看请求后的状态
            if response.status == 200:
                # 返回dict对象
                return await response.json()
        # 返回错误消息
        logging.error('get an error of status code is %s while scraping %s ...',
                      response.status, url)
    except aiohttp.ClientError as e:
        logging.error('scraping %s ... has an error', url, exc_info=True)


# 索引页数据抓取
async def scrape_index(page: int) -> dict:
    """
    传入参数：page
    任务目标：获取索引页中的数据
    执行逻辑：
    1. 分析索引页的逻辑，构造url后传入抓取函数中
    这里分析结果limit不变为10，offset为(page-1) * 10满足条件
    2. 因此这里可以知道传入参数可以设置为page
    返回结果：最终结果应该为一个字典对象
    """
    # 索引链接
    index_url = INDEX_URL.format(limit=10, offset=(page - 1) * 10)
    # 返回响应后获取的数据
    return await scrape_api(url=index_url)

# 数据处理

# 解析索引页内的内容
def handle_index(response_results: list) -> list:
    """
    传入参数：list格式的响应请求
    任务目标：获取到我们所需要的id，并构成列表
    逻辑步骤：
    1. 分析一个dict格式响应请求后发现由count与results两部分
        我们需要的就是results部分中的id内容，results本身
        为一个列表，嵌套了一堆字典数据
    2. 利用循环获取列表中的字典数据
    3. 将字典数据中的id获取并存放在我们构建的ids列表中
    返回结果：返回一个名叫ids的列表
    """
    # 创建一个ids的列表
    ids = []
    for response_result in response_results:
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

# 数据存储
# 这次以txt格式的方式进行存储 并且实现异步写入
async def save_data(data: dict) -> None:
    """
    传入参数：字典数据
    任务目标：将获取到的数据以txt文本的方式写入
    逻辑步骤：
    1. 构建要存放的地址
    2. 进行数据的写入，这里要注意的是提取的数据格式可能
    需要进行转换 None，float，list都需要变成文本
    返回结果：无
    """
    # 文件地址
    data_path = '{0}/movies.txt'.format(RESULT_DIR)
    # 文件写入
    async with aiofiles.open(data_path, 'a+', encoding='utf-8') as file:
        # 标题
        name = data.get('name', '')
        # 图片
        cover = data.get('cover', '')
        # 上映时间
        published_at = data.get('published_at', '')
        # 电影分类内容
        categories = str(data.get('categories', []))
        # 电影评分内容
        score = str(data.get('score', ''))
        # 电影剧情简介
        drama = data.get('drama', '')

        # 内容写入
        await file.write('标题:' + name + '\n' + \
                        '图片:' + cover + '\n' + \
                        '上映时间:' + published_at + '\n' + \
                        '电影分类:' + categories + '\n' + \
                        '电影评分:' + score + '\n' + \
                        '电影剧情简介:' + drama + '\n' + \
                        '=' * 50 + '\n')


# 详情页数据抓取
async def scrape_detail(id: int) -> dict:
    """
    传入参数: id
    任务目标：获取详情页中的数据
    执行逻辑：
    1. 传入id数据构建需要的url
    2. 利用抓取函数进行抓取
    返回结果：返回结果应该为一个字典对象
    """
    # 详情链接
    detail_url = DETAIL_URL.format(id=id)
    # 返回响应后获取的数据
    data =  await scrape_api(url=detail_url)
    # 异步写入
    await save_data(data=data)

# 主函数执行
async def main():
    # 获取session
    global session
    # 对session进行操作
    session = aiohttp.ClientSession()
    
    # 抓取索引页
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page=page)) for page in range(1, TOTAL_PAGE + 1)]
    # 获取抓取到的结果
    index_response_result = await asyncio.gather(*scrape_index_tasks)
    # 输出结果信息
    logging.info('response results %s', json.dumps(index_response_result, ensure_ascii=False, indent=2))
    # 进行数据处理
    ids = handle_index(response_results=index_response_result)

    # 抓取详情页
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id=id)) for id in ids]
    # 执行任务
    await asyncio.wait(scrape_detail_tasks)
    # 关闭session
    await session.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())