html = '''
<ul class="list">
    <li class="item-0 active"><a href="link3.html"><span class="blod">third item</span></a></li>
</ul>
'''

from pyquery import PyQuery as pq

doc = pq(html)
# 找到对应的li节点
li = doc('.item-0.active') 
# 输出li
print(li)
# 增加一个name属性
li.attr('name', 'link')
# 输出li
print(li)
# 添加文本内容
li.text('changed item')
# 输出li
print(li)
# 添加html内容
li.html('<span>changed item</span>')
# 输出li
print(li)