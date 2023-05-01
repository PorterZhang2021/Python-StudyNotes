from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 无头模式
    browser = p.chromium.launch(headless=False)
    # 进入网页
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    # 获取网页请求
    page.wait_for_load_state('networkidle')
    # 获取属性内容
    href = page.get_attribute('a.name', 'href')
    print(href)
    browser.close()