import requests

# 代理
proxies = {'https':'http://user:password@代理地址',}
# 利用代理进行请求
requests.get('https://www.httpbin.org/get', proxies=proxies)