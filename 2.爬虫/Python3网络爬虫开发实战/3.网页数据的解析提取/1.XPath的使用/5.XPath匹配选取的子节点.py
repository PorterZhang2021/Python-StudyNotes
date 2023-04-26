from lxml import etree

# 解析html页面
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html',
                   etree.HTMLParser())
# 获取li下的所有子节点a
result = html.xpath('//li/a')
# 输出子结点的结果
print(result)