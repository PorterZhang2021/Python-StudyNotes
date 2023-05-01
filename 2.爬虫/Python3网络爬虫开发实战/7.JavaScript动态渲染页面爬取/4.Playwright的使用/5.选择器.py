from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # 打开新页面
    page = context.new_page()

    # 访问 https://www.baidu.com
    page.go('https://www.baidu.com/')

    # 文本选择
    page.click("text=Log in")

    # css选择器
    page.click("button")
    page.click("#nav-bar .contact-us-item")

    # 特定的节点属性筛选
    page.click("[data-test=login-button]")
    page.click("[aria-label='Sign in']")

    # CSS选择器+文本值
    page.click("article:has-text('Playwright')")
    page.click("#nav-bar: text('Contact us')")

    # CSS选择器+节点关系
    page.click(".item-description:has(.item-promo-banner)")
    page.click("input:right-of(:text('Username'))")

    # XPath
    page.click("xpath=//button")
