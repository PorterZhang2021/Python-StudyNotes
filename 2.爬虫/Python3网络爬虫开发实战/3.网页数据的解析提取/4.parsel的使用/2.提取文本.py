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
# selector选择器对象
selector = Selector(text=html)
# 获取css选择器对象
items = selector.css('.item-0')
# 查找list
for item in items:
    # 利用text()方法获取文本内容
    text = item.xpath('.//text()').get()
    # 输出文本
    print(text)
# 选取所有class包含item-0的li节点的文本内容
result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
# 输出文本结果
print(result)
# 提取所有对应的li节点的文本内容
result = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
# 输出文本结果
print(result)
# 改写使用css方法
result = selector.css('.item-0 *::text').getall()
# 输出文本结果
print(result)