import os
from pyquery import PyQuery as pq

html_file = './2.爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/3.pyquery的使用/23.pyquery项目实战/页面解析/Scrape_Movie_detail.html'

def read_files_as_str(filepath):
    # 判断路径文件存在
    if not os.path.exists(filepath):
        raise TypeError(filepath + 'does not exist')
    # 以
    with open(filepath, encoding='utf-8') as f:
        return f.read()
    
html_str = read_files_as_str(html_file)

doc = pq(html_str)

# 获取图片的地址
cover_ele = doc('img.cover')
cover_src = cover_ele.attr('src')

# 获取电影的名称
name_ele = doc('h2.m-b-sm')
name = name_ele.text()

# 获取分类
categories_ele = doc('div.categories')
categories_span_items = categories_ele.find('span').items()
categories = [ categorie.text() for categorie in categories_span_items]
print(categories)
# 获取上映时间
# 获取电影的简介
drama_ele = doc('div.drama')
drama = drama_ele.find('p').text()

# 获取评分
score = doc('p.score').text()
