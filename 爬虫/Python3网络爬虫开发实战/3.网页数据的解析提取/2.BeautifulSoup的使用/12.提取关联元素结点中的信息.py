html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href=
                    "http://example.com/lacie" class="sister" id="link2">Lacie</a>
        </P>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')

# 这里是查看类型
print(type(soup.a.next_sibling))
# 获取同级节点的下一个结点
print(soup.a.next_sibling)
# 获取同级节点的下一个结点的文本
print(soup.a.next_sibling.string)
# 父节点
print('Parent:')
# a结点的所有父节点
print(type(soup.a.parents))
# a结点的父节点的第一个
print(list(soup.a.parents)[0])
# a结点的父节点的第一个中的class属性值
print(list(soup.a.parents)[0].attrs['class'])


