html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
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
# 查找id属性为list-1的结点
print(soup.find_all(attrs={'id': 'list-1'}))
# 查找name属性为elements的结点
print(soup.find_all(attrs={'name': 'elements'}))
# 对于常用属性可以直接传参
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))