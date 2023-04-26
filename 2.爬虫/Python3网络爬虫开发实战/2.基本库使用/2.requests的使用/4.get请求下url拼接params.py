import requests

# 参数
data = {
    'name': 'germey',
    'age': 25
}
# 传入参数的方式可以拼接url为https://www.httpbin.org/get?name=germey&age=25
r = requests.get('https://www.httpbin.org/get', params=data)
# 输出请求头、URL、IP等信息
print(r.text)