# 导入requests模块
import requests

# 进行Get请求
r = requests.get('https://api.github.com/events')
# 进行Post请求
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# put请求
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
# delete请求
r = requests.delete('https://httpbin.org/delete')
# head请求
r = requests.head('https://httpbin.org/get')
# options请求
r = requests.options('https://httpbin.org/get')

# 携带请求参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

# 假装自己是浏览器
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

# 获取服务器响应文本内容
r = requests.get('https://api.github.com/events')
print(r.text)
print(r.encoding)

# 获取字节响应内容
print(r.content)

# 获取响应码
r = requests.get('https://httpbin.org/get')
print(r.status_code)

# 获取响应头
print(r.headers)

# 获取JSON响应内容
r = requests.get('https://api.github.com/events')
print(r.json())

# 获取socket流响应内容
r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)

print(r.raw.read(10))

# POST的请求 当你想要一个键里面添加多个值的时候
# 元组形式
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
# 字典形式
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)

print(r1.text)
print(r1.text == r2.text)

# 利用JSON作为参数
url = 'https://api.github.com/some/endpoint'
payload = {'some':' data'}
r = requests.post(url, json=payload)


# 文件上传
url = 'https://httpbin.org/post'
files = {'file': open('reports.xls', 'rb')}
r = requests.post(url, files=files)
print(r.text)

# 获取cookie信息
url = 'https://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies['example_cookie_name'])

# 发送cookie信息
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are = 'working')
r = requests.get(url, cookies=cookies)
print(r.text)

# 设置超时
requests.get('https://github.com/', timeout=0.001)
