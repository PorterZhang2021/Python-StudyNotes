from lxml import etree

html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/20.XPath项目实战/页面解析/Scrape_Movie.html',
                   etree.HTMLParser())
# 获取单个电影块 获取超链接a
movie_card = html.xpath('//div[contains(@class, "el-card")]//a[@class="name"]/@href')
print(movie_card)
