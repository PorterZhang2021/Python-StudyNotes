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
# 初始化对象
doc = pq(html)
# 获取li节点对象
li = doc('li')
# 输出html()方法的情况
print(li.html())
# 输出text()方法的情况
print(li.text())
# 查看text()方法下的类型
print(type(li.text()))
# 可以发现 text()会输出多个节点下的text
# 但是html方法只输出第一个节点的html文本