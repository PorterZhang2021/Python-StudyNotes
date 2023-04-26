from lxml import etree

# 文本信息
text = '''
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a>
        </ul>
    </div>
'''
# 构造一个Xpath解析对象 lxml.etree_Element 
# 这部分应该是解析html文本并修复html问
html = etree.HTML(text)
print(type(html))
# 将Xpath解析对象转换成 bytes对象
result = etree.tostring(html)
print(type(result))
# 以utf-8的形式输出
print(result.decode('utf-8'))
