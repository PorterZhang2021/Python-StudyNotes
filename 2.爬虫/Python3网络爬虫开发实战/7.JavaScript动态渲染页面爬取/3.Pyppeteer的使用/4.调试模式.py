import asyncio
from pyppeteer import launch

async def main():
    # 开启开发者工具，此时无头模式会关闭
    browser = await launch(devtools=True)
    # 建立一个新页面
    page = await browser.newPage()
    # 输入要访问的网站
    await page.goto('https://www.baidu.com')
    # 进行等待
    await asyncio.sleep(100)
# 注册并执行
asyncio.get_event_loop().run_until_complete(main())