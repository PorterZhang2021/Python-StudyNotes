import logging
import requests

# 捕获警告到日志
logging.captureWarnings(True)
# 不进行证书验证
response = requests.get('https://ssr2.scrape.center/', verify=False)
# 反应状态码
print(response.status_code)