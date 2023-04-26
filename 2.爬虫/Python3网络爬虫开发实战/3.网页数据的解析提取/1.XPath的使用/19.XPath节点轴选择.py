from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''

html = etree.HTML(text)
# 调用ancestor轴获取所有祖先节点
result = html.xpath('//li[1]/ancestor::*')
print(result)
# 调用ancestor轴获取所有div祖先节点
result = html.xpath('//li[1]/ancestor::div')
print(result)
# 调用attribute轴获取所有属性值
result = html.xpath('//li[1]/attribute::*')
print(result)
# 调用child轴获取所有直接子节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# 调用descendant轴可以获取所有子孙节点
result = html.xpath('//li[1]/descendant::span')
print(result)
# 调用following轴，获取当前节点之后的所有节点
result = html.xpath('//li[1]/following::*[2]')
print(result)
# 调用following-sibling轴，获取当前节点之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)