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
# 获取卡片对象
items = doc('.el-card').items()

with open('movies.txt', 'w', encoding='utf-8') as file:
    for item in items:
        # 电影名称
        name = item.find('a > h2').text()
        # 类别
        categories = [item.text() for item in item.find('.categories button span').items()]
        # 上映时间
        published_at = item.find('.info:contains(上映)').text()
        # 表达式获取
        published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
        # 评分
        score = item.find('p.score').text()

        # 进行写入
        file.write(f'名称: {name}\n')
        file.write(f'类别:{categories}\n')
        file.write(f'上映时间:{published_at}\n')
        file.write(f'评分: {score}\n')
        # 用于分割
        file.write(f'{"=" * 50}\n')

