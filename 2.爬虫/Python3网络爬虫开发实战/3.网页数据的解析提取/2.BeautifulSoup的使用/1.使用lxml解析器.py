# 使用BeautifulSoup
from bs4 import BeautifulSoup

# 使用lxml解析器
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# 输出p节点的文本值
print(soup.p.string)
