from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def modify_response(route, request):
        route.fulfill(path="./13-1.custom_response.html")

    page.route('/', modify_response)
    page.goto('https://spa6.scrape.center')
    page.wait_for_load_state('networkidle')