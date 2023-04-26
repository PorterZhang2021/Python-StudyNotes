import requests

# get请求数据
r = requests.get('https://scrape.center/favicon.ico')
with open(r'.\爬虫\Python3网络爬虫开发实战\2.基本库使用\res\favicon.ico', 'wb') as f:
    # 写入二进制数据 这里直接使用content属性 因为其是二进制格式
    f.write(r.content)