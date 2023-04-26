import socket
import urllib.request
import urllib.error

try:
    # 超时响应请求
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    # 输出错误原因对象
    print(type(e.reason))
    # 是否是超时对象
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
        