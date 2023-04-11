from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
# html文本解析
html = etree.HTML(text)
# 获取多属性值匹配后的节点
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# 输出节点值
print(result)