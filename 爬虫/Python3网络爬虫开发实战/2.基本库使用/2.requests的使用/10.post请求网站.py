import requests

# 传入的data数据
data = {'name': 'germey', 'age': '25'}
# 进行post请求
r = requests.post('https://www.httpbin.org/post', data=data)
# 获取请求后的信息
print(r.text)
