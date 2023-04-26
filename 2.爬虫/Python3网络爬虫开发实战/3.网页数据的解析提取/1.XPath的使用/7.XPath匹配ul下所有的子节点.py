from lxml import etree

# html解析式
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html',
                   etree.HTMLParser())
# 获取ul下所有的子结点a 这个获取不到因为没有
result = html.xpath('//ul/a')
# 输出获取的结果
print(result)