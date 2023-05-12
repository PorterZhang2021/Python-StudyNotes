import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://spa1.scrape.center/api/movie/?limit=10&offset=0'
condition = EC.visibility_of_all_elements_located
locator = (By.CSS_SELECTOR, 'body')

browser = webdriver.Chrome()
# 浏览器页面等待
wait = WebDriverWait(browser, 10)
browser.get(url)
wait.until(condition(locator))

pre = browser.find_element(by=By.TAG_NAME, value='pre').text
data = json.loads(pre)
print(data)