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

# 字符串对象初始化
doc = pq(html)
# 获取a标签
a = doc('a')
# 查看获取得a标签对象的类型
print(a, type(a))
# 获取a标签的属性
print(a.attr('href'))
# 获取a标签的属性
print(a.attr.href)

a = doc('a')
# 遍历获取所有a标签的属性
for item in a.items():
    print(item.attr('href'))