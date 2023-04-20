from bs4 import BeautifulSoup
import os
import re


html_file = './爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/2.BeautifulSoup的使用/21.BeautifulSoup项目实战/页面解析/Scrape_Movie_detail.html'

def read_files_as_str(filepath):
    # 判断路径文件存在
    if not os.path.exists(filepath):
        raise TypeError(filepath + 'does not exist')
    # 以
    with open(filepath, encoding='utf-8') as f:
        return f.read()

html_str = read_files_as_str(html_file)
# 进行html文本解析
soup = BeautifulSoup(html_str, 'lxml')

# 获取图片的地址
cover = soup.find(class_="cover")['src']
# 获取电影的名称
name_ele = soup.find(name="h2")
name = name_ele.string
# 获取分类
categorie = soup.find(class_='categories')
spans = categorie.find_all(name="span")
categories = [ span.string for span in spans ]
# print(categories)
# 获取上映时间
# 获取电影简介
drama_ele = soup.find(class_="drama")
drama = drama_ele.p.string.strip()
# 获取评分
score_ele = soup.find(class_='score')
score = score_ele.string.strip()


