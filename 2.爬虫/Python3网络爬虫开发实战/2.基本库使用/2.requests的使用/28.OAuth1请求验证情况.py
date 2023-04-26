import requests
from requests_oauthlib import OAuth1

# 请求认证的链接
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# 这里时OAuth1认证的情况
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# 获取相关的请求
requests.get(url, auth=auth)