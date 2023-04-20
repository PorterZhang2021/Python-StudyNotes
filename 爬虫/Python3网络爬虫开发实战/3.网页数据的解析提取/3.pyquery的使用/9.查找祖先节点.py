html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''

from pyquery import PyQuery as pq

# pyquery对象初始化
doc = pq(html)
# 获取list对象
items = doc('.list')
# 获取其所有祖先节点
parents = items.parents()
# 查看祖先节点的类型
print(type(parents))
# 获取所有祖先节点
print(parents)