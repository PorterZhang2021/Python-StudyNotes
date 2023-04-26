html='''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
</div>
'''

from pyquery import PyQuery as pq
# 初始化html对象
doc = pq(html)
# 获取wrap类的标签对象
wrap = doc('.wrap')
# 输出器内部的文字内容
print(wrap.text())
# remove方法在标签内包含p时输出p中文本时
# 可以使用此方法进行删除
wrap.find('p').remove()
# 输出文本内容
print(wrap.text())