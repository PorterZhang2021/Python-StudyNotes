from lxml import etree
# text文本
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
# HTML文件解析
html = etree.HTML(text)
# 利用XPath获取解析文本
result = html.xpath('//li[@class="li"]/a/text()')
# 输出获取到的结果
print(result)