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
# 对象初始化
doc = pq(html)
# 获取所有li节点对象，并以生成器的形式返回
lis = doc('li').items()
# 输出lis的类型 
print(type(lis))
# 输出所有的li节点
for li in lis:
    print(li, type(li))