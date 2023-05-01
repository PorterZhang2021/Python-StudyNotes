from selenium import webdriver

browser = webdriver.Chrome()
# 打开url
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
# 添加cookie
browser.add_cookie(
    {
        'name': 'name',
        'domain': 'www.zhihu.com',
        'value': 'germey'
    }
)
# 输出cookies
print(browser.get_cookies())
# 删除所有cookie
browser.delete_all_cookies()
# 输出cookies
print(browser.get_cookies())