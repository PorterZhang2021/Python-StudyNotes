import socket
import urllib.request
import urllib.error

# 异常捕获操作
try:
    # 响应请求 timeout 超时响应 这里是0.1秒后没有响应发出超时响应
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    # 这里是比对两个错误信息是否为超时
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')