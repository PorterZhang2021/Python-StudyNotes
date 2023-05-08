import asyncio
import logging

from pyppeteer import launch

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 基础页面
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10

# 抓取网站
async def scrape_page(page, url):
    logging.info('scraping %s ...', url)
    try:
        await page.goto(url)
        await page.waitForSelector('div#app')
    except:
        logging.error('error occured while scraping %s', url, exc_info=True)

async def scrape_index(page, page_index):
    index_url = f'{BASE_URL}/page/{page_index}'
    return await scrape_page(page, index_url)

async def scrape_detail(page, url):
    return await scrape_page(page, url)


# 解析网站的数据内容


# 存储网站内容


# 输出最终的内容
def main():
    pass

if __name__ == '__main__':
    main()