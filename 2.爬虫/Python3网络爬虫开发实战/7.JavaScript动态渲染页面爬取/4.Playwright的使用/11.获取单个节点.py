from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 无头模式关闭
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    # 获取所有节点
    element = page.query_selector('a.name')
    # 获取链接
    print(element.get_attribute('href'))
    # 获取内容
    print(element.text_content())
    browser.close()