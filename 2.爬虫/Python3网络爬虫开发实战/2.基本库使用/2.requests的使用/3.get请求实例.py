import requests

# get请求
r = requests.get('https://www.httpbin.org/get')
# 输出文本 返回请求头、URL、IP等信息
print(r.text)