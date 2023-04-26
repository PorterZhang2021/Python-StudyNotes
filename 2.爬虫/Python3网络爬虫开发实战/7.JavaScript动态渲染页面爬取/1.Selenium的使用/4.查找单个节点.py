from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# 使用id选择
input_first = browser.find_element(by=By.ID, value='q')
# 使用css选择器选择
input_second = browser.find_element(by=By.CSS_SELECTOR, value='#q')
# 使用xpath选择
input_third = browser.find_element(by=By.XPATH, value='//*[@id="q"]')
# 输出结果
print(input_first, input_second, input_third)
browser.close()