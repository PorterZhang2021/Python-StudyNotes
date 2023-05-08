import requests
from pyquery import PyQuery as pq

response = requests.get('https://ssr1.scrape.center/detail/1')
html_str = response.text

doc = pq(html_str)

# 标题
name = doc('h2.m-b-sm')
print(name.text())
# 图片
cover = doc('img.cover')
print(cover.attr.src)
# 分类
categories = []
items = doc('button.category').children()
for item in items.items():
    categories.append(item.text())
print(categories)
# 上映时间 - 使用re模块
published = None
# 评分
score = doc('p.score')
print(score.text())
# 剧情简介
drama = doc('div.drama').find('p')
print(drama.text())


