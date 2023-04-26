from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_element(by=By.CSS_SELECTOR, value='ul.service-bd li')
print(lis)
browser.close()