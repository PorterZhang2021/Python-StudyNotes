import urllib.request

# 请求响应 timeout设置超时时间 超时后没有响应就抛出异常
response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
# 输出请求响应的内容
print(response.read())