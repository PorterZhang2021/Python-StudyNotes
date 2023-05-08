import logging

from os import makedirs
from os.path import exists
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

#
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULT_DIR = 'results'

exists(RESULT_DIR) or makedirs(RESULT_DIR)

# 抓取网页内容
def scrape_page(page, url):
    logging.info('scraping %s ...', url)
    try:
        page.goto(url)
        page.wait_for_load_state('networkidle')
    except:
        logging.error('error occured while scraping %s', url, exc_info=True)


def scrape_index(page, page_index):
    index_url = f'{BASE_URL}/page/{page_index}'
    return scrape_page(page, index_url)


def scrape_detail(page, url):
    return scrape_page(page, url)

# 获取解析内容
def parse_index(page):
    # 获取网页内容请求
    elements = page.query_selector_all('a.name')
    # 获取元素信息
    for element in elements:
        part_of_url = element.get_attribute('href')
        detail_url = urljoin(BASE_URL, part_of_url)
        logging.info('get url: %s', detail_url)
        yield detail_url


def parse_detail(page):
    # 获取标题
    name = None
    name_tag = page.query_selector('h2.m-b-sm')
    if name_tag:
        name = name_tag.text_content()

    # 获取图片
    cover = None
    cover_tag = page.query_selector('img.cover')
    if cover_tag:
        cover = cover_tag.get_attribute('src')

    # 获取分类
    categories = []
    category_tags = page.query_selector_all('div.categories > button > span')
    if category_tags:
        categories = [category.text_content() for category in category_tags]

    # 获取评分
    score = None
    score_tag = page.query_selector('p.score')
    if score_tag:
        score = score_tag.text_content().strip()

    # 剧情简介
    drama = None
    drama_tag = page.query_selector('div.drama > p')
    if drama_tag:
        drama = drama_tag.text_content().strip()

    return {
        # 标题
        'name': name,
        # 图片
        'cover': cover,
        # 分类
        'categories': categories,
        # 简介
        'drama': drama,
        # 评分
        'score': score
    }

# 数据内容存储
def save_data(data):
    # 文件存放地址
    data_path = '{0}/movies.txt'.format(RESULT_DIR)
    # 进行文件写入
    with open(data_path, 'a+', encoding='utf-8') as file:
        name = data.get('name', None)
        cover = data.get('cover', None)
        categories = data.get('categories', None)
        drama = data.get('drama', None)
        score = data.get('score', None)

        file.write('name:'+name+'\n')
        file.write('cover:'+cover+'\n')
        file.write('categories:'+str(categories)+'\n')
        file.write('drama:'+drama+'\n')
        file.write('score:'+score+'\n')
        file.write('='*50 + '\n')


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        for page_index in range(1, TOTAL_PAGE + 1):
            scrape_index(page, page_index)
            detail_urls = list(parse_index(page))
            for detail_url in detail_urls:
                scrape_detail(page, detail_url)
                data = parse_detail(page)
                logging.info('get data: %s', data)
                save_data(data)
            
    browser.close()

if __name__ == '__main__':
    main()
