from selenium import webdriver

browser = webdriver.Chrome()
# 获取淘宝信息
browser.get('https://www.taobao.com')
# 输出页面资源
print(browser.page_source)
# 关闭浏览器
browser.close()
