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
# 查找ul元素结点
for ul in soup.select('ul'):
    # 查找li元素结点
    print(ul.select('li'))