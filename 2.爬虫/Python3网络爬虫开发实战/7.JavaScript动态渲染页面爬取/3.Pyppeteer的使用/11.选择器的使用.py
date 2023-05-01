import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    # 启动浏览器
    browser = await launch()
    # 创建页面并访问
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    # 等价方法
    # j用于寻找一个元素
    j_result1 = await page.J('.item .name')
    j_result2 = await page.querySelector('.item .name')
    # jj用于寻找所有元素
    jj_result1 = await page.JJ('.item .name')
    jj_result2 = await page.querySelectorAll('.item .name')
    print('J Result1:', j_result1)
    print('J Result2:', j_result2)
    print('JJ Result1:', jj_result1)
    print('JJ Result2:', jj_result2)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())