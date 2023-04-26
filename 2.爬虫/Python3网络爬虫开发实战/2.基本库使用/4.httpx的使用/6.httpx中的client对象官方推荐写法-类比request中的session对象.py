import httpx

# 超链接
url = 'https://www.httpbin.org/get'
# Client的对象与Session对象可以类比
# httpx库       requests库
# 官方推荐的使用方式
with httpx.Client as client:
    # 进行get方法的请求
    response = client.get(url)
    # 输出请求后的情况
    print(response)