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
from parsel import Selector
# 初始化一个Selector对象
selector = Selector(text=html)

# css选择器
items = selector.css('.item-0')
print(len(items), type(items), items)
# Xpath选择器
items2 = selector.xpath('//li[contains(@class, "item-0")]')
print(len(items2), type(items2), items2)