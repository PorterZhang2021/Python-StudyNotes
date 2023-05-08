import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://ssr1.scrape.center/page/1')
    await page.waitForSelector('div#app')

    detail_url = await page.querySelectorAllEval('a.name', 'nodes => nodes.map(node => node.href)')
    print(detail_url)
asyncio.get_event_loop().run_until_complete(main())
