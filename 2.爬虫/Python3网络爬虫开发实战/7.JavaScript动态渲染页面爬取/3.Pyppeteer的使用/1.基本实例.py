import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    # 启动
    browser = await launch()
    print(type(browser))
    # 开启浏览器页面
    page = await browser.newPage()
    print(type(page))
    # 进入页面
    await page.goto('https://spa2.scrape.center/')
    # 找到对应元素
    await page.waitForSelector('.item .name')
    # 进行内容解析
    doc = pq(await page.content())
    # 查看内容
    names = [item.text() for item in doc('.item .name').items()]
    # 输出名字
    print('Names:', names)
    # 浏览器关闭
    await browser.close()
# 进行执行
asyncio.get_event_loop().run_until_complete(main())
