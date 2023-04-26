from lxml import etree
# html文件解析
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html',
                   etree.HTMLParser())
# 获取一个子节点a的父节点
result = html.xpath('//a[@href="link4.html"]/../@class')
# 输出结果
print(result)