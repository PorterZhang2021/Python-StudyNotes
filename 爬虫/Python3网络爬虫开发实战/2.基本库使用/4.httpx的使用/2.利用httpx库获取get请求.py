import httpx

# 进行get请求
response = httpx.get('https://www.httpbin.org/get')
# 类型
print(type(response))
# 请求状态码
print(response.status_code)
# 请求头
print(response.headers)
# 获取请求后的内容
print(response.text)