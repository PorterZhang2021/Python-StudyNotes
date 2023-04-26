from bs4 import BeautifulSoup
import os

html_file = './爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/2.BeautifulSoup的使用/21.BeautifulSoup项目实战/页面解析/Scrape_Movie.html'

def read_files_as_str(filepath):
    # 判断路径文件存在
    if not os.path.exists(filepath):
        raise TypeError(filepath + 'does not exist')
    # 以
    with open(filepath, encoding='utf-8') as f:
        return f.read()

html_str = read_files_as_str(html_file)
# 进行解析
soup = BeautifulSoup(html_str, 'lxml')
# 获取元素
print(soup.find_all(class_="name"))
href_a_list = soup.find_all(class_="name")

for (i, value) in enumerate(href_a_list):
    print(i, value['href'])