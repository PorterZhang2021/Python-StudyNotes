import os
from pyquery import PyQuery as pq

html_file = './2.爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/3.pyquery的使用/23.pyquery项目实战/页面解析/Scrape_Movie.html'

def read_files_as_str(filepath):
    # 判断路径文件存在
    if not os.path.exists(filepath):
        raise TypeError(filepath + 'does not exist')
    # 以
    with open(filepath, encoding='utf-8') as f:
        return f.read()

html_str = read_files_as_str(html_file)

doc = pq(html_str)

movie_a = doc('a.name')

for a in movie_a.items():
    print(a.attr('href'))
    

