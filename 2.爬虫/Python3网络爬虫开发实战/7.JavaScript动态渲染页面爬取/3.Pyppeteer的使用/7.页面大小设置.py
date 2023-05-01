import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    # 浏览器设置
    browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
    # 访问页面
    page = await browser.newPage()
    # 设置窗口大小
    await page.setViewport({'width': width, 'height': height})
    # 防止检测
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get:()=>undefined})')
    await page.goto('https://antispider1.scrape.center/')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())