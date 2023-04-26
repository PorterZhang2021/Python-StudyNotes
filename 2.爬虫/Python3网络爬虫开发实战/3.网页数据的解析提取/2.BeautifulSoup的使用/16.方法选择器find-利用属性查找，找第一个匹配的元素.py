html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
# 查找ul列表只查找到的第一个
print(soup.find(name='ul'))
# 查看类型
print(type(soup.find(name='ul')))
# 查找class为list的第一个结点
print(soup.find(class_='list'))