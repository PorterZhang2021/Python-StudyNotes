from lxml import etree

# html文本解析
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html',
                   etree.HTMLParser())
# 获取节点中的属性
result = html.xpath('//li/a/@href')
# 输出
print(result)