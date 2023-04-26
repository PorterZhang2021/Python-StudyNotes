import httpx
# url超链接
url = 'https://www.httpbin.org/get'
# 构建一个client对象
client = httpx.Client()
# 这里是异常捕获 
try:
    response = client.get(url)
finally:
    client.close()

# 此方法可以等价于
with httpx.Client as client:
    # 响应
    response = client.get(url)
    # 响应请求
    print(response)