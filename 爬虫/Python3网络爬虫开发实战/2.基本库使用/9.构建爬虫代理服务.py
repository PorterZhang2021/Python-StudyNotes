from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 为什么会遭到拒绝呢？

# 本地搭建http代理
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
})
# 利用代理构建opener
opener = build_opener(proxy_handler)

# 异常捕获
try:
    # 利用代理身份登入百度 - 此代理身份会遭到目标计算机的拒绝而无法连接
    response = opener.open('https://www.baidu.com')
    # 输出响应请求
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)