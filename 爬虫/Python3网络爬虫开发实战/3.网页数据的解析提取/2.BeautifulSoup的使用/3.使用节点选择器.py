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

# 利用lxml进行html文本的解析
soup = BeautifulSoup(html, 'lxml')
# 输出解析后的标题
print(soup.title)
# 查看解析后标题的对象类型
print(type(soup.title))
# 输出解析后标题的字符串
print(soup.title.string)
# 输出head标签的内容
print(soup.head)
# 输出p标签的内容
print(soup.p)