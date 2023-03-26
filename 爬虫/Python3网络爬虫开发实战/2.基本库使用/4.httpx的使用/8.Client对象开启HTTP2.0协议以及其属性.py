import httpx

# 请求链接
url = 'https://www.httpbin.org/get'
# 开启http2协议的Client对象
client = httpx.Client(http2=True)
# 进行get请求
response = client.get(url)
# 查看请求后的文本
print(response.text)
# 查看请求后的版本
print(response.http_version)