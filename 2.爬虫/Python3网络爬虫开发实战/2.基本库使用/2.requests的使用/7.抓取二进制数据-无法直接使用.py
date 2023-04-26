import requests

# get请求
r = requests.get('https://scrape.center/favicon.ico')
# 返回响应头、IP
print(r.text)
# b bytes类型数据
print(r.content)