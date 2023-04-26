import requests
# 用于忽略证书警告
from requests.packages import urllib3

# 忽略证书警告
urllib3.disable_warnings()
# 取消证书验证
response = requests.get('https://ssr2.scrape.center/', verify=False)
# 输出状态码
print(response.status_code)