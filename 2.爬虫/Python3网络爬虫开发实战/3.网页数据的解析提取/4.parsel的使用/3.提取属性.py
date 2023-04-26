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

selector = Selector(text=html)
# 利用css的方式获取href的属性内容
result = selector.css('.item-0.active a::attr(href)').get()
print(result)
# 利用xpath的方式获取href属性的内容
result = selector.xpath('//li[contains(@class, "item-0") and contains(@class, "active")]/a/@href').get()
print(result)