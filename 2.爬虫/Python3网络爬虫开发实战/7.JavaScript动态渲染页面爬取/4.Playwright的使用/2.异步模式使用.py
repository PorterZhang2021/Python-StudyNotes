import asyncio
from playwright.async_api import async_playwright

# 异步执行
async def main():
    # 上下文管理器
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            # 浏览器的启动
            browser = await browser_type.launch()
            # 新页面
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            # 截图
            await page.screenshot(path=f'screenshot-{browser_type.name}.png')
            # 获取页面标题
            print(await page.title())
            await browser.close()

asyncio.run(main())
