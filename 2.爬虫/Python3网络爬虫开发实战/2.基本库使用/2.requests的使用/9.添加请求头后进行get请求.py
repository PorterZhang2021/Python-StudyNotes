import requests

# 设置请求头信息 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# 进行get请求
r = requests.get('https://ssr1.scrape.center/', headers=headers)
# 获取抓取内的信息
print(r.text)