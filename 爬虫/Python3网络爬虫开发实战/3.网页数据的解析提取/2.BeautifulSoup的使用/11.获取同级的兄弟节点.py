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
# 同级兄弟节点下一个
print('Next Sibling', soup.a.next_sibling)
# 同级兄弟节点的上一个
print('Prev Sibling', soup.a.previous_sibling)
# 同级兄弟结点的下面所有兄弟结点
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
# 同级兄弟结点的上面所有兄弟结点
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))