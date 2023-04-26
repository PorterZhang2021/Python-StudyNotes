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
# 初始化文件对象
doc = pq(html)
# 获取li节点
li = doc('.item-0.active')
# 输出li节点
print(li)
# 移除active类
li.remove_class('active')
# 输出li节点
print(li)
# 增加active类
li.add_class('active')
# 输出li节点
print(li)