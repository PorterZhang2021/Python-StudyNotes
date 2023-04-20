from pyquery import PyQuery as pq

# 将URL对象进行初始化
doc = pq(url='https://cuiqingcai.com')
# 输出title结果
print(doc('title'))
