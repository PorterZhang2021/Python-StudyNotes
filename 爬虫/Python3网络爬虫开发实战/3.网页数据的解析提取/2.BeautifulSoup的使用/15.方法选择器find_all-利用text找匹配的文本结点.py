import re
html = """
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
# 传入一个正则表达式对象，返回结果是由所有与正则表达式相匹配的结点文本组成的列表
print(soup.find_all(text=re.compile('link')))