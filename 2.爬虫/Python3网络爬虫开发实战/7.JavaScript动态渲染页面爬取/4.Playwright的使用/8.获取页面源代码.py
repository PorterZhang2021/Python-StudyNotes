from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 浏览器无头模式关闭
    browser = p.chromium.launch(headless=False)
    # 访问页面
    page =  browser.new_page()
    page.goto('https://spa6.scrape.center/')
    # 等待网页请求
    page.wait_for_load_state('networkidle')
    # 获取源代码
    html = page.content()
    print(html)
    browser.close()