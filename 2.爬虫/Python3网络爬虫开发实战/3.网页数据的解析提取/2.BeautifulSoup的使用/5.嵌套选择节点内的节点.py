html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
# 解析后的head节点中title节点
print(soup.head.title)
# 查看相关的类型
print(type(soup.head.title))
# 查看文本内容
print(soup.head.title.string)