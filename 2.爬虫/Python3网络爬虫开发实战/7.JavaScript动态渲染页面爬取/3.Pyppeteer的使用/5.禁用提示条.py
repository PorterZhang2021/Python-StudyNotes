import asyncio
from pyppeteer import launch

async def main():
    # 将提示条关闭
    browser = await launch(headless=False, args=['--disable-infobars'])
    # 创建页面并访问
    page = await browser.newPage()
    await page.goto('https://antispider1.scrape.center')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())