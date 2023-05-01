from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browse = webdriver.Chrome()
browse.get('https://antispider3.scrape.center/')
WebDriverWait(browse, 10) \
    .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = browse.page_source
doc = pq(html)
name = doc('.item .name')
for name in name.items():
    print(name.text())
browse.close()