from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input= browser.find_element(By.ID, 'q')
input.send_keys('iPhone')
time.sleep(10)
input.clear()
input.send_keys('iPad')
button = browser.find_element(By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')
button.click()
browser.close()