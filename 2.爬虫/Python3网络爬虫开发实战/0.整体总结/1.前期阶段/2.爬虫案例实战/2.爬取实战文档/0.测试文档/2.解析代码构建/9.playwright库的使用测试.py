from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://ssr1.scrape.center/detail/1')
    page.wait_for_load_state('networkidle')
    
    # 标题
    name_tag = page.query_selector('h2.m-b-sm')
    print(name_tag.text_content())
    # 图片
    cover_tag = page.query_selector('img.cover')
    print(cover_tag.get_attribute('src'))
    # 分类
    categories = []
    category_tags = page.query_selector_all('div.categories > button> span')
    if category_tags:
        categories = [category.text_content() for category in category_tags]
    print(categories)
    # 剧情简介
    drama_tag = page.query_selector('div.drama > p')
    print(drama_tag.text_content().strip())
    # 评分
    score_tag = page.query_selector('p.score')
    print(score_tag.text_content().strip())
    browser.close()