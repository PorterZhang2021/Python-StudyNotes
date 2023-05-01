import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    # 无头模式
    browser = await launch(headless=False)
    # 访问网页
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    # 获取网页内容
    print('HTML:', await page.content())
    # 获取cookies
    print('Cookies:', await page.cookies())
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())