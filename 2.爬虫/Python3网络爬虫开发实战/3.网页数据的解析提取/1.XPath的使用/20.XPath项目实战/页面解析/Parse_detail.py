from lxml import etree

html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/20.XPath项目实战/页面解析/detail_movie.html',
                   etree.HTMLParser())

# 图片的地址
cover = html.xpath('//img[@class="cover"]/@src')
print(cover)
# 电影的名称
name = html.xpath('//a/h2/text()')[0]
print(name)
# 分类
categories = html.xpath('//div[@class="categories"]//span/text()')
print(categories)
# 上映时间 - 此部分明显re方便
published_at = None
# 电影简介
drama = html.xpath('//div[@class="drama"]/p/text()')[0].strip()
print(drama)
# 评分
score = html.xpath('//p[contains(@class, "score")]/text()')[0].strip()
print(score)