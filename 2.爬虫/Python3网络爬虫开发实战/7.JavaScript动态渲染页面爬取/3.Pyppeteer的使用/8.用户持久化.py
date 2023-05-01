import asyncio
from pyppeteer import launch

async def main():
    # 设置浏览器的启动并设置用户存储的数据文件夹
    browser = await launch(headless=False, userDataDir='./userdata', args=['--disable-infobars'])
    # 访问页面
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())                                                                                                                                                       