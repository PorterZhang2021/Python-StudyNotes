import requests


# r = requests.get('https://ssr3.scrape.center/, auth=HTTPBasicAuth('admin', 'admin'))
# 更简便的身份认证响应请求方式
r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# 输出状态码
print(r.status_code)