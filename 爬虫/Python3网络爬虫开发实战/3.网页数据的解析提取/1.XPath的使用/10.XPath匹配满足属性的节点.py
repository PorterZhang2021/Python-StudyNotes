from lxml import etree

# html文件解析
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html',
                   etree.HTMLParser())
# 获取节点并满足属性item-0
result = html.xpath('//li[@class="item-0"]')
# 输出结果
print(result)