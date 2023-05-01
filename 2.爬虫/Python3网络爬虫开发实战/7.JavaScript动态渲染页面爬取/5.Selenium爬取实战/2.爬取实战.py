from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urljoin
from os import makedirs
from os.path import exists

import logging
import json


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 常量
INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10
RESULTS_DIR = 'results'

# 构建文件夹
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# 设定使用浏览器
# 无头模式开启
options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)

# 浏览器页面等待
wait = WebDriverWait(browser, TIME_OUT)


# 页面抓取
def scrape_page(url, condition, locator):
    # 抓取页面信息
    logging.info('scraping %s', url)
    try:
        # 设置浏览地址
        browser.get(url)
        # 等待操作,直到完成内部的条件判断操作完成
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 抓取列表页
def scrape_index(page):
    # 设置要访问的url
    url = INDEX_URL.format(page=page)
    # 进行页面的抓取
    scrape_page(url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, '#index .item'))

# 抓取详情页
def scrape_detail(url):
    # 页面详情页的抓取
    scrape_page(url, condition=EC.visibility_of_all_elements_located,
                locator=(By.TAG_NAME, 'h2'))

# 列表页内容解析
def parse_index():
    # 进行列表页的内容解析
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item a.name')
    # 将内容页的元素获取
    for element in elements:
        href = element.get_attribute('href')
        # url 链接
        yield urljoin(INDEX_URL, href)

# 页面详情内容解析
def parse_detail():
    # 获取浏览器的链接
    url = browser.current_url
    # 获取电影名称
    name = browser.find_element(By.TAG_NAME, 'h2').text
    # 获取电影分类
    categories = [element.text for element in browser.find_elements(By.CSS_SELECTOR, '.categories button span')]
    # 获取图片
    cover = browser.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')
    # 获取评分
    score = browser.find_element(By.CLASS_NAME, 'score').text
    # 获取剧情简介
    drama = browser.find_element(By.CSS_SELECTOR, '.drama p').text

    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }

# 数据存储
def save_data(data):
    # 获取数据名称
    name = data.get('name')
    # 数据地址
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


# 主函数
def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            # 页面抓取
            scrape_index(page)
            # 获取url
            detail_urls = parse_index()
            # logging.info('details urls %s', list(detail_urls))
            # 获取页面详情内容
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)
                # 内容抓取
                scrape_detail(detail_url)
                # 获取数据
                detail_data = parse_detail()
                logging.info('detail data %s', detail_data)
                # 数据保存
                save_data(detail_data)
    finally:
        browser.close()

if __name__ == '__main__':
    main()