from lxml import etree

# 获取一个html解析对象
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html', 
                   etree.HTMLParser())
# 匹配获取li节点
result = html.xpath('//li')
# 输出所有的li节点
print(result)
# 输出获取到的第一个li节点
print(result[0])