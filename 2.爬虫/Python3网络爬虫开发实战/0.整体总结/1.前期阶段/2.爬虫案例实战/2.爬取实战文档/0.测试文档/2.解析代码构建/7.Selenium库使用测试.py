from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://ssr1.scrape.center/detail/1')
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#app')))

# 标题
name_tag = browser.find_element(By.CSS_SELECTOR, 'h2.m-b-sm')
print(name_tag.text)
# 图片
cover_tag = browser.find_element(By.CSS_SELECTOR, 'img.cover')
print(cover_tag.get_attribute('src'))
# 分数
score_tag = browser.find_element(By.CSS_SELECTOR, 'p.score')
print(score_tag.text)
# 分类
categories = browser.find_elements(By.CSS_SELECTOR, 'div.categories > button > span')
for categorie in categories:
    print(categorie.text)
# 简介
drama_tag = browser.find_element(By.CSS_SELECTOR, 'div.drama > p')
print(drama_tag.text)

