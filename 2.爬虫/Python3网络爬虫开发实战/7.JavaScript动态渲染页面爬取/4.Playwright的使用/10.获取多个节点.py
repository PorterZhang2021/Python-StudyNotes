from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # 访问并加载网页
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    # 获取网页请求
    elements = page.query_selector_all('a.name')
    for element in elements:
        print(element.get_attribute('href'))
        print(element.text_content())
    browser.close()