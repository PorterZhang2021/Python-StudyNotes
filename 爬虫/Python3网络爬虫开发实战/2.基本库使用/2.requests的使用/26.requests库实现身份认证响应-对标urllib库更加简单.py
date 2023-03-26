import requests
from requests.auth import HTTPBasicAuth

# 此响应方式对标urllib库的响应方式更加简答
# urllib库进行这种响应方式如下
"""
# 构建基本身份认证
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
"""

# 进行身份认证的请求响应
r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# 输出请求响应后的状态码
print(r.status_code)