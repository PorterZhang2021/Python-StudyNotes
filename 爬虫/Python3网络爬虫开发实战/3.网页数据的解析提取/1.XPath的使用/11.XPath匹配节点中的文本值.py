from lxml import etree

# html文件解析
html = etree.parse('./爬虫/Python3网络爬虫开发实战/3.网页数据的解析提取/1.XPath的使用/test.html',
                   etree.HTMLParser())
# 获取节点后的文本 - 此情况获取的结果出错
# 此情况下由于有补全,这里先获取了a节点，而a节点有一个补全换行符，所以获取的是补全结果
result = html.xpath('//li[@class="item-0"]/text()')
# 输出结果值
print(result)
# 获取li下的a下的文本节点
result = html.xpath('//li[@class="item-0"]/a/text()')
# 输出结果
print(result)