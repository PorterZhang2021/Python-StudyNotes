from lxml import etree

# 获取text的结点
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
# html文件解析
html = etree.HTML(text)
# 属性的多值匹配
result = html.xpath('//li[contains(@class, "li")]/a/text()')
# 获取最终的结果
print(result)