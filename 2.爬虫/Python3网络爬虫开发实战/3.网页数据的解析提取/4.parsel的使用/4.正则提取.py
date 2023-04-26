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
# 获取selector对象
selector = Selector(text=html)
# 利用正则表达式获取结果
result = selector.css('.item-0').re('link.*')
# 输出结果
print(result)
# 利用正则表达式获取文本结果
result = selector.css('.item-0 *::text').re('.*item')
# 输出结果
print(result)
# 提取第一个符合规则的结果
result = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
print(result)