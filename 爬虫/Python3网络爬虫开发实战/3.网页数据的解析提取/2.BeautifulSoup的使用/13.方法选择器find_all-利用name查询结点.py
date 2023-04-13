html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list=-1">
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
# 查找所有ul标签的结点
print(soup.find_all(name='ul'))
# 获取ul标签结点的类型
print(type(soup.find_all(name='ul')[0]))
# 查询ul标签下的所有li
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
# 获取ul标签下li中的文本内容
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)