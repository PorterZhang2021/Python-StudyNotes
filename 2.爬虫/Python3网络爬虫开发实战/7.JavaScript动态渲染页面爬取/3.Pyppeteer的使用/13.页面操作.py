import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://cuiqingcai.com/')
    await page.goto('https://spa2.scrape.center/')
    # 后退操作
    await page.goBack()
    # 前进操作
    await page.goForward()
    # 刷新操作
    await page.reload()
    # 保存 PDF操作
    # await page.pdf()
    # 截图操作
    await page.screenshot()
    # 设置页面HTML
    await page.setContent('<h2>Hello World</h2>')
    # 设置User-Agent
    await page.setUserAgent('Python')
    # 设置Headers
    await page.setExtraHTTPHeaders(headers={})
    # 关闭
    await page.close()
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())