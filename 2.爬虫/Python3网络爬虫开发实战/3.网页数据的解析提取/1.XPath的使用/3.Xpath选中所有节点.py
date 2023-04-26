from lxml import etree

# 获取一个html解析对象
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html', 
                   etree.HTMLParser())
# 获取所有节点 *匹配所有节点
result = html.xpath('//*')
# 输出结果
print(result)