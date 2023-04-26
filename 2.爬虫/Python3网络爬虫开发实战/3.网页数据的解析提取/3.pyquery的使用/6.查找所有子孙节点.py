html = '''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

from pyquery import PyQuery as pq
# 初始化html
doc = pq(html)
# css选择器获取list
items = doc('.list')
# 查看对象
print(type(items))
# 输出结果
print(items)
# 对象内查找所有子孙节点-所有
lis = items.find('li')
# 查看子节点的类型
print(type(lis))
# 输出子节点
print(lis)