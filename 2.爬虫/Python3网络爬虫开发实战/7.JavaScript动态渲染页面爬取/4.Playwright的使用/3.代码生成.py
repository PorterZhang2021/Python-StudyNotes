from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").fill("nba")
    page.locator("#kw").press("Enter")
    page.get_by_role("button", name="百度一下").click()
    page.locator("#kw").click()
    page.locator("#kw").fill("bilibli")
    page.get_by_role("button", name="百度一下").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("heading", name="哔哩哔哩 (゜-゜)つロ 干杯~-bilibili 官方").get_by_role("link", name="哔哩哔哩 (゜-゜)つロ 干杯~-bilibili").click()
    page1 = page1_info.value
    with page1.expect_popup() as page3_info:
        page1.get_by_role("link", name="当你用bug的方式打开星穹铁道！ 哔哩哔哩播放器 12.9万 603 06:21").click()
    page3 = page3_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
