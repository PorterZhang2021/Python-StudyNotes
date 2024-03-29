from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import re

def parese_name(name_html):
    has_whole = name_html('.whole')
    if has_whole:
        return name_html.text()
    else:
        # 字符解析
        chars = name_html('.char')
        items = []
        # 字符
        for char in chars.items():
            items.append({
                'text': char.text().strip(),
                'left': int(re.search('(\d+)px', char.attr('style')).group(1))
            })
        # 进行排序
        items = sorted(items, key=lambda x: x['left'], reverse=False)


# 浏览器
browser = webdriver.Chrome()
# 打开网页
browser.get('https://antispider3.scrape.center/')
# 进行页面等待
WebDriverWait(browser, 10) \
            .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
# 浏览器元素
html = browser.page_source
doc = pq(html)
# 获取名字
names = doc('.item .name')
# 对名字解析重构
for name_html in names.items():
    name = parese_name(name_html)
    print(name)
browser.close()