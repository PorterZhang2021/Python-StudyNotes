import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    # 关闭无头模式
    browser = await launch(headless=False)
    # 开启新页面
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    # 查找css
    await page.waitForSelector('.item .name')
    # 点击按钮
    await page.click('.item .name', options={
        # left 左 middle 中 right 右
        'button': 'right',
        # 点击次数
        'clickCount': 1, # 1或2
        'delay': 3000, # 毫秒
    })
    # 关闭
    await browser.close()
   

asyncio.get_event_loop().run_until_complete(main())