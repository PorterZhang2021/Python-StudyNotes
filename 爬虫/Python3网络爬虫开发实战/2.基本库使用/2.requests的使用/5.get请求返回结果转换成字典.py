import requests

# get请求
r = requests.get('https://www.httpbin.org/get')
# 查看输出text的类型
print(type(r.text)) # 字符串
# 以字典的形式输出 这里是将str转换成了dict
print(r.json())
# 查看json方法输出后的类型
print(type(r.json()))
