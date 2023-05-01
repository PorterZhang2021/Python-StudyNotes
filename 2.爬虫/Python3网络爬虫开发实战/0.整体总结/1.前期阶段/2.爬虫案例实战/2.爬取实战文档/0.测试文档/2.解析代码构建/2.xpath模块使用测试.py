import lxml
import requests
from lxml.html import etree

response = requests.get('https://ssr1.scrape.center/detail/1')

html_str = response.text

html = etree.HTML(html_str)

name = html.xpath('//h2[@class="m-b-sm"]/text()')
print(name)
cover = html.xpath('//img[@class="cover"]/@src')
print(cover)
# 此定位不如使用re模块定位方便
# publish_at_text = html.xpath('')
# 电影分类
categories = html.xpath('//button[contains(@class, "category")]/span/text()')
print(categories)
# 电影剧情简介
drama = html.xpath('//div[contains(@class, "drama")]/p/text()')
print(drama)
# 电影评分
score = html.xpath('//p[contains(@class, "score")]/text()')
print(score)