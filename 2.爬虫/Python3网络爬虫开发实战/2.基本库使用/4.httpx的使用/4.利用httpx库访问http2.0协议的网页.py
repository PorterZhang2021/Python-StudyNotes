import httpx

# http2.0协议，url地址
url = 'https://spa16.scrape.center'
# 用于访问http2.0协议情况下的url
# response = httpx.get(url) 默认情况下httpx不会开启HTTP2.0协议的支持
# 设置一个Client对象，将http2.0协议设置为true
client = httpx.Client(http2=True)
# 进行请求
response = client.get(url)
# 获取请求响应后的页面
print(response.text)