import requests

# 请求爬取的url
url = 'https://spa16.scrape.center'
# 设置请求头信息 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# 进行请求 http2协议 强迫关闭了这个现有的请求 设置请求头后结果一致
req = requests.get(url)
# 输出请求结果
print(req.text)