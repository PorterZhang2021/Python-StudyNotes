import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    # 浏览器关闭
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())