import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    # 浏览器启动
    browser = await launch()
    # 设置一个新页面
    page = await browser.newPage()
    # 设置浏览器窗口
    await page.setViewport({'width': width, 'height': height})
    # 跳转地址
    await page.goto('https://spa2.scrape.center/')
    # 选择元素
    await page.waitForSelector('.item .name')
    # 进行睡眠
    await asyncio.sleep(2)
    # 页面截图路径
    await page.screenshot(path='example.png')
    # 返回页面截图
    dimensions = await page.evaluate(''' 
        () => {
            return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
            }
        }
    ''')
    # 输出结果
    print(dimensions)
    # 关闭浏览器扩展
    await browser.close()
# 进行注册
asyncio.get_event_loop().run_until_complete(main())