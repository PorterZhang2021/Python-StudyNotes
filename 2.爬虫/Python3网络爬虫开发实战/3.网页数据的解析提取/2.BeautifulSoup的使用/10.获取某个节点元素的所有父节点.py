html = """
<html>
    <body>
        <p class="story">
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
    </body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
# 找到a节点的父节点
print(type(soup.a.parents))
# 找到a节点的所有父节点
print(list(enumerate(soup.a.parents)))