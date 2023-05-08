import csv
import logging

from os import makedirs
from os.path import exists
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量值
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULT_DIR = 'results'

# 文件夹存在或者创建文件夹
exists(RESULT_DIR) or makedirs(RESULT_DIR)

# 网页内容的抓取
def scrape_page(browser, url):
    logging.info('scraping %s ...', url)
    # 异常捕获操作
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#app')))
    except:
        logging.error('error occured while scraping %s', url, exc_info=True)

# 进行列表页的抓取
def scrape_index(browser, page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(browser, index_url)

# 进行详情页的抓取
def scrape_detail(browser, url):
    return scrape_page(browser, url)

# 进行网页内容的获取
# 解析索引页
def parse_index(browser):
    # 获取所有超链接
    a_tags = browser.find_elements(By.CSS_SELECTOR, 'a.name')
    
    if not a_tags:
        return []
    
    for a_tag in a_tags:
        detail_url = a_tag.get_attribute('href')
        # 输出链接
        logging.info('get detail url %s', detail_url)
        # 生成器函数
        yield detail_url

# 解析详情页
def parse_detail(browser):
    
    # 获取标题
    name = None
    name_tag = browser.find_element(By.CSS_SELECTOR, 'h2.m-b-sm')
    if name_tag:
        name = name_tag.text
    
    # 获取图片
    cover = None
    cover_tag = browser.find_element(By.CSS_SELECTOR, 'img.cover')
    if cover_tag:
        cover = cover_tag.get_attribute('src')
    
    # 获取分类
    categories = []
    category_tags = browser.find_elements(By.CSS_SELECTOR, 'div.categories > button > span')
    if category_tags:
        categories = [category.text for category in category_tags]
    
    # 获取简介
    drama = None
    drama_tag = browser.find_element(By.CSS_SELECTOR, 'div.drama > p')
    if drama_tag:
        drama = drama_tag.text

    # 获取分数
    score = None
    score_tag = browser.find_element(By.CSS_SELECTOR, 'p.score')
    if score_tag:
        score = score_tag.text

    return {
        # 标题
        'name': name,
        # 图片
        'cover': cover,
        # 分数
        'score': score,
        # 分类
        'categories': categories,
        # 剧情简介
        'drama': drama
    }

# 网页内容的存储
def save_data(data_path, data):
    # 利用csv存储
    with open(data_path, 'a+', encoding='utf-8') as csv_file:
        field_name = ['name', 'cover', 'score', 'categories', 'drama']
        csv_writer = csv.DictWriter(csv_file,fieldnames=field_name)
        csv_writer.writerow(data)

# 输出获取的网页内容
def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    data_path = '{0}/movies.csv'.format(RESULT_DIR)
    with open(data_path, 'w', encoding='utf-8') as csv_file:
        field_name = ['name', 'cover', 'score', 'categories', 'drama']
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
        csv_writer.writeheader()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            # 进入列表页
            scrape_index(browser, page)
            # 解析索引页
            detail_urls = list(parse_index(browser))

            for detail_url in detail_urls:
                scrape_detail(browser, detail_url)
                data = parse_detail(browser)
                logging.info('get data %s', data)
                save_data(data_path, data)
    finally:
        browser.close()


if __name__ == '__main__':
    main()