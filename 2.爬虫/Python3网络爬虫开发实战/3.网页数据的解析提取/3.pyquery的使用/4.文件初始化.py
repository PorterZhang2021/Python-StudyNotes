from pyquery import PyQuery as pq
# 初始化文档
doc = pq(filename='demo.html')
# css选择器li
print(doc('li'))