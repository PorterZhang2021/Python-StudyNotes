import requests
from bs4 import BeautifulSoup

response = requests.get('https://ssr1.scrape.center/detail/1')

html = response.text

soup = BeautifulSoup(html, 'lxml')

# 标题
name = soup.find(name="h2")
print(name.string)
# 图片
cover = soup.find(class_='cover')
print(cover['src'])
# 简介
drama = soup.select('div.drama p')[0].string.strip()
# 分类
categories_ele = soup.find(class_='categories')

for category in categories_ele:
    if category.find('span') != -1:
        print(category.find('span').string)

# 上映时间

# 评分
score = soup.find(class_='score').string.strip()
print(score)