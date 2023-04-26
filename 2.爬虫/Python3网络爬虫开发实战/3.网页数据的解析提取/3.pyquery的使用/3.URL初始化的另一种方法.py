from pyquery import PyQuery as pq
import requests

# 利用request获取响应对象的text后初始化为pyQuery对象
doc = pq(requests.get('https://cuiqingcai.com').text)
# css选择器找到title
print(doc('title'))