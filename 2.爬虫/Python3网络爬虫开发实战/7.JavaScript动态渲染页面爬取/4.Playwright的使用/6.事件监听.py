from playwright.sync_api import sync_playwright

def on_response(response):
    # 事件响应
    print(f'Statue {response.status}: {response.url}')

with sync_playwright() as p:
    # 无头模式关闭
    browser = p.chromium.launch(headless=False)
    # 打开并访问一个页面
    page = browser.new_page()
    # 获取事件的监听 这里监听的其实是network面板中的所有请求与响应
    page.on('response', on_response)
    page.goto('https://spa6.scrape.center/')
    # 这里应该是等待网页的响应状态
    page.wait_for_load_state('networkidle')
    browser.close()