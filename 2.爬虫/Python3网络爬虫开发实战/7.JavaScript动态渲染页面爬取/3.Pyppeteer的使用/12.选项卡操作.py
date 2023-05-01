import asyncio
from pyppeteer import launch

async def main():
    # 关闭无头模式
    browser = await launch(headless=False)
    # 新建页面并访问
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    # 新建页面并访问
    page = await browser.newPage()
    await page.goto('https://www.bing.com')
    # 获取所有页面的选项卡
    pages = await browser.pages()
    print('Pages:', pages)
    # 对页面选项卡进行操作
    page1 = pages[1]
    await page1.bringToFront()
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())
