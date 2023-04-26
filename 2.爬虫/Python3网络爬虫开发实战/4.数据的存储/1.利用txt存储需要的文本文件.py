import requests
from pyquery import PyQuery as pq
import re

proxies = {
    # 此部分在v2rayN代理中找到系统代理部分找到对应端口
	'http': '127.0.0.1:10809',
	'https': '127.0.0.1:10809'
}

url = 'https://ssr1.scrape.center/'
html = requests.get(url=url, proxies=proxies).text
doc = pq(html)
items = doc('.el-card').items()

# 这里是创建了一个文件，然后将文件以UTF-8的形式写入
file = open('movies.text', 'w', encoding='utf-8')

for item in items:
    # 电影名称
    # 使用了CSS选择器
    name = item.find('a > h2').text()
    # 向文件内写入信息
    file.write(f'名称: {name}\n')
    # 类别
    # 利用了生成器进行快速迭代生成
    categories = [item.text() for item in item.find('.categories button span').items()]
    # 信息写入
    file.write(f'类别: {categories}\n')
    # 上映时间 这里利用了伪类选择器，找到信息中包含 '上映'两个字的对象后输出文本
    published_at = item.find('.info:contains(上映)').text()
    # 将上映时间获取后进行写入 这里对获取的文本利用正则表达式
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
    if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    file.write(f'上映时间：{published_at}\n')
    # 获取评分后写入
    score = item.find('p.score').text()
    file.write(f'评分: {score}\n')
    # 这里用于分割
    file.write(f'{"=" * 50}\n')

# 写入后关闭文件
file.close()