html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie </a>;
and they lived at the bottom of a well.</p>
<p class="story">...</P>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
# 获取直接子节点
print(soup.p.children)
# 输出子节点的信息
for i, child in enumerate(soup.p.children):
    print(i, child)