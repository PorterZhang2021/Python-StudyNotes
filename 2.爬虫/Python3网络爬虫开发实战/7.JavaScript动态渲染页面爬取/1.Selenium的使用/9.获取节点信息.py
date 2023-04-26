from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://spa2.scrape.center/'
# 打开地址网页
browser.get(url)
# 查找到需要的节点
logo = browser.find_element(By.CLASS_NAME, 'logo-image')
# 输出
print(logo)
# 输出获取到的属性
print(logo.get_attribute('src'))
# 获取文本信息
input = browser.find_element(By.CLASS_NAME, 'logo-title')
print(input.text)
# 获取id
print(input.id)
# 获取location
print(input.location)
# 获取标签名
print(input.tag_name)
# 获取大小
print(input.size)