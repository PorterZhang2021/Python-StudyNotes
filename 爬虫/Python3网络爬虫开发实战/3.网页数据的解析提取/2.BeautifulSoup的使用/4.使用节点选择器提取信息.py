html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie </a>;
and they lived at the bottom of a well.</p>
<p class="story">...</P>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
# 获取节点名称
print(soup.title.name)
# 获取节点属性名称
print(soup.p.attrs)
print(soup.p.attrs['name'])
# 获取节点属性
print(soup.p['name'])
print(soup.p['class'])
# 获取节点内的文本内容
print(soup.p.string)