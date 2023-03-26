import requests
# timeout超时请求 这里的timeout设定是从请求发出到请求结束的时间
r = requests.get('https://www.httpbin.org/get', timeout=1)
# 请求状态码
print(r.status_code)