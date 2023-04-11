from lxml import etree

# 获取一个html解析对象
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html', 
                   etree.HTMLParser())
# 将其转化成bytes形式
result = etree.tostring(html)
# 以utf-8的格式输出
print(result.decode('utf-8'))