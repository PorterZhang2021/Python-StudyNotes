from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/404')
    # 捕获HTTPError的错误
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
    # 捕获URLError的错误
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
    