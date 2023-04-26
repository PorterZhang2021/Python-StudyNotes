import requests

r = requests.get('https://www.baidu.com/')
# get方法请求
print(type(r))
# 状态码
print(r.status_code)
# 文本类型
print(type(r.text))
# 输出文本
print(r.text[:100])
# 输出cookies
print(r.cookies)