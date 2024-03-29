import asyncio
from pyppeteer import launch

async def main():
    # 关闭无头模式
    await launch(headless=False)
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())