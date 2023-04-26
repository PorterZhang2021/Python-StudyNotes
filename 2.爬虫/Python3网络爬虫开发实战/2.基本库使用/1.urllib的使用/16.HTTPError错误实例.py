from urllib import request, error

try:
    # 响应请求
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    # 错误代码
    print(e.reason, e.code, e.headers, sep='\n')
