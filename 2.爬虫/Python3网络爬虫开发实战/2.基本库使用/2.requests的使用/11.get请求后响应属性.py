import requests

r = requests.get('https://ssr1.scrape.center/')
# 状态码
print(type(r.status_code), r.status_code)
# 请求头
print(type(r.headers), r.headers)
# 请求链接
print(type(r.url), r.url)
# 请求历史 - 暂时不知道是什么
print(type(r.history), r.history)