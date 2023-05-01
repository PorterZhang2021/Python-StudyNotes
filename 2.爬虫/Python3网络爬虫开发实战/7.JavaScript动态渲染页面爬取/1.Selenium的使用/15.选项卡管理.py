import time
from selenium import webdriver

browser = webdriver.Chrome()
# 百度
browser.get('https://www.baidu.com')
# 开启一个新选项卡
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
# 淘宝
browser.get('https://www.taobao.com')
time.sleep(1)
# 返回之前打开的选项卡
browser.switch_to.window(browser.window_handles[0])
# Python
browser.get('https://python.org')
