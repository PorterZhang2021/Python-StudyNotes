from lxml import etree

# 对html进行解析
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html',
                   etree.HTMLParser())
# 获取ul下的所有子孙结点a
result = html.xpath('//ul//a')
# 输出结果
print(result)