import httpx

url = 'https://www.httpbin.org/get'
# 设置请求头信息 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# 设置请求响应
response = httpx.get(url=url, headers=headers)
# 访问结果
print(response.text)