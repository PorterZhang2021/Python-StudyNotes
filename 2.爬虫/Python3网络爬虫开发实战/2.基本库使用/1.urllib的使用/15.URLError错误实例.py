from urllib import request, error

# 异常捕获
try:
    # 请求一个不存在的页面
    response = request.urlopen('https://cuiqingcai.com/404')
except error.URLError as e:
    # 返回错误信息 
    print(e.reason)