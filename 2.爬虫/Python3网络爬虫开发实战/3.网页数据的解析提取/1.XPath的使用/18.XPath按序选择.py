from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
# 对html文件解析
html = etree.HTML(text)
# 选取第一个li节点
result = html.xpath('//li[1]/a/text()')
print(result)
# 选取最后一个li节点
result = html.xpath('//li[last()]/a/text()')
print(result)
# 选取位置小于3的li节点 即 1和2
result = html.xpath('//li[position()<3]/a/text()')
print(result)
# 选取倒数第三个节点
result = html.xpath('//li[last()-2]/a/text()')
print(result)